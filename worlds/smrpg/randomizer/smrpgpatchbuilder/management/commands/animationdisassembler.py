from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import (
    shortify,
    shortify_signed,
    byte_signed,
    writeline,
)
import os
import shutil
from copy import deepcopy
from dataclasses import dataclass
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing
import queue
import threading
from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config
from disassembler_output.variables import battle_event_names

ORIGINS = [
    "ABSOLUTE_POSITION",
    "CASTER_INITIAL_POSITION",
    "TARGET_CURRENT_POSITION",
    "CASTER_CURRENT_POSITION",
]

FLASH_COLOURS = ["NO_COLOUR", "RED", "GREEN", "YELLOW", "BLUE", "PINK", "AQUA", "WHITE"]

BONUS_MESSAGES = [
    "BM_ATTACK",
    "BM_DEFENSE",
    "BM_UP",
    "BM_HPMAX",
    "BM_ONCE",
    "BM_AGAIN",
    "BM_LUCKY",
]

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_05",
    "UNKNOWN_06",
    "UNKNOWN_07",
    "UNKNOWN_08",
    "UNKNOWN_09",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "CHARACTER_IN_SLOT_1",
    "CHARACTER_IN_SLOT_2",
    "CHARACTER_IN_SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_NOT_SELF",
    "RANDOM_ALLY_NOT_SELF",
    "ALL_ALLIES_AND_SELF",
    "RANDOM_ALLY_OR_SELF",
    "UNKNOWN_32",
    "UNKNOWN_33",
    "UNKNOWN_34",
    "ALL_OPPONENTS",
    "AT_LEAST_ONE_OPPONENT",
    "RANDOM_OPPONENT",
    "UNKNOWN_38",
    "AT_LEAST_ONE_ALLY",
    "MONSTER_1_CALL",
    "MONSTER_2_CALL",
    "MONSTER_3_CALL",
    "MONSTER_4_CALL",
    "MONSTER_5_CALL",
    "MONSTER_6_CALL",
    "MONSTER_7_CALL",
    "MONSTER_8_CALL",
]

MASKS = [
    "NO_MASK",
    "INCLINE_1",
    "INCLINE_2",
    "CIRCLE_MASK",
    "DOME_MASK",
    "POLYGON_MASK",
    "WAVY_CIRCLE_MASK",
    "CYLINDER_MASK",
]

searchable_vars = globals()

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] == obj]

# monster behaviours are pretty much just object queues.
# the "sprite behaviour" dropdown is a pointer to an object queue.
# 0x350202 + (enemy index * 2) = at this address you will find the address of the object queue the monster uses
monster_behaviour_oq_offsets = [
    0x35058A,  # no movement for "escape"
    0x350596,  # slide backward when hit
    0x3505A2,  # bowser clone sprite
    0x3505AE,  # mario clone sprite
    0x3505BA,  # no reaction when hit
    0x350898,  # sprite shadow
    0x350985,  # floating, sprite shadow
    0x350991,  # floating
    0x350AD3,  # floating, slide backward when hit
    0x350ADF,  # floating, slide backward when hit
    0x350AEB,  # fade out death, floating
    0x350CF2,  # fade out death
    0x350CFE,  # fade out death
    0x350D0A,  # fade out death, smithy spell cast
    0x350D16,  # fade out death, no "escape" movement
    0x350E60,  # fade out death, no "escape" transition
    0x350E6C,  # (normal)
    0x350E78,  # no reaction when hit
]

# Extract monster behaviour names from the comments above
monster_behaviour_names = [
    "no_movement_for_escape",
    "slide_backward_when_hit",
    "bowser_clone_sprite",
    "mario_clone_sprite",
    "no_reaction_when_hit",
    "sprite_shadow",
    "floating_sprite_shadow",
    "floating",
    "floating_slide_backward_when_hit",
    "floating_slide_backward_when_hit_2",
    "fade_out_death_floating",
    "fade_out_death",
    "fade_out_death_2",
    "fade_out_death_smithy_spell_cast",
    "fade_out_death_no_escape_movement",
    "fade_out_death_no_escape_transition",
    "normal",
    "no_reaction_when_hit_2",
]

monster_entrance_offsets = [
    0x352148, 0x352149, 0x352169, 0x352194, 0x3521DA, 0x352207, 0x352227, 0x352247, 0x35227D, 0x3522E1, 0x3522EB, 0x352317, 0x352336, 0x352373, 0x35238F, 0x3523AC
]

@dataclass
class StaticPointer:
    """Defines a pointer that must remain at a fixed address in the ROM.

    These are the entry points for battle animation scripts. Each entry generates
    one script file with expected_beginning set to this address.
    """
    address: int
    is_oq: bool  # True if this is an object queue (pointer table), False if standalone script
    max_length: int | None = None  # Max script size (None = computed from next address)
    name: str | None = None  # Descriptive name for the script file
    oq_ptr_count: int | None = None  # Number of pointers in OQ (for determining OQ size)

    @property
    def bank(self) -> str:
        """Return the bank ID (02, 35, or 3A) for this pointer."""
        return f"{(self.address >> 16):02X}"

# POINTER_MUST_REMAIN_STATIC defines all script entry points
# Each entry becomes a separate script file in the disassembler output
# Script sizes are bounded by the next address in the same bank
# oq_ptr_count values are calculated as len(range(ptr_table_start, ptr_table_end, 2)) from original banks dict
POINTER_MUST_REMAIN_STATIC: list[StaticPointer] = [
    # Bank 0x02
    # flower_bonus: range(0x02F455, 0x02F460, 2) = 6 pointers
    StaticPointer(0x02F455, True, None, "flower_bonus_oq", 6),
    StaticPointer(0x02F4BF, False, None, "toad_tutorial"),

    # Bank 0x35 - Ally and Monster behaviours
    StaticPointer(0x350000, True, 0x202, "ally_behaviour_root_oq", 1),  # 1 ptr to 6-ptr OQ, traced scripts extend to 0x350202
    StaticPointer(0x350202, True, None, "monster_behaviour_ptrs", 256),  # 256 ptrs, each to 6-ptr behaviour OQ
    # monster_spells: range(0x351026, 0x35107F, 2) = 45 pointers
    StaticPointer(0x351026, True, None, "monster_spell_ptrs", 45),
    # monster_attacks: range(0x351493, 0x351594, 2) = 129 pointers
    StaticPointer(0x351493, True, None, "monster_attack_ptrs", 129),
    # monster_entrances: range(0x352128, 0x352147, 2) = 16 pointers
    StaticPointer(0x352128, True, None, "monster_entrance_oq", 16),
    # weapon_misses: range(0x35816D, 0x3581B6, 2) = 37 pointers
    StaticPointer(0x35816D, True, None, "weapon_miss_oq", 37),
    # weapon_sounds: range(0x358271, 0x3582BA, 2) = 37 pointers
    StaticPointer(0x358271, True, None, "weapon_sound_oq", 37),
    StaticPointer(0x358916, False, None, "weapon_wrapper_mario"),
    StaticPointer(0x3589D5, False, None, "weapon_wrapper_toadstool"),
    StaticPointer(0x358AC6, False, None, "weapon_wrapper_bowser"),
    StaticPointer(0x358B57, False, None, "weapon_wrapper_geno"),
    StaticPointer(0x358BEC, False, None, "weapon_wrapper_mallow"),
    # items: range(0x35C761, 0x35C802, 2) = 81 pointers
    StaticPointer(0x35C761, True, None, "item_oq", 81),
    # ally_spells: range(0x35C992, 0x35C9C7, 2) = 27 pointers
    StaticPointer(0x35C992, True, None, "ally_spell_oq", 27),
    # weapons: range(0x35ECA2, 0x35ECE9, 2) = 36 pointers
    StaticPointer(0x35ECA2, True, None, "weapon_animation_oq", 36),

    # Bank 0x3A
    StaticPointer(0x3A6000, True, None, "battle_events_root_oq"),  # Variable-length, determines own size
]

def compute_script_boundaries() -> dict[int, int | None]:
    """Return dict mapping address to max_length for each script.

    For entries with explicit max_length, use that value.
    For others, compute the distance to the next address in the same bank.
    Cross-bank or last entries get None (determined by tracing).
    """
    sorted_ptrs = sorted(POINTER_MUST_REMAIN_STATIC, key=lambda p: p.address)
    boundaries: dict[int, int | None] = {}
    for i, ptr in enumerate(sorted_ptrs):
        if ptr.max_length is not None:
            boundaries[ptr.address] = ptr.max_length
        elif i + 1 < len(sorted_ptrs):
            next_addr = sorted_ptrs[i + 1].address
            if (next_addr >> 16) == (ptr.address >> 16):  # Same bank
                boundaries[ptr.address] = next_addr - ptr.address
            else:
                boundaries[ptr.address] = None  # Cross-bank
        else:
            boundaries[ptr.address] = None  # Last entry
    return boundaries

def get_static_pointer_addresses() -> list[int]:
    """Return list of all addresses in POINTER_MUST_REMAIN_STATIC.

    Used for block boundary detection (replaces force_contiguous_block_start).
    """
    return [p.address for p in POINTER_MUST_REMAIN_STATIC]

def get_static_pointer_by_address(address: int) -> StaticPointer | None:
    """Look up a StaticPointer by its address."""
    for p in POINTER_MUST_REMAIN_STATIC:
        if p.address == address:
            return p
    return None

# Known unused gaps that should be included in script sizes when merging blocks
# These are ranges of bytes that are unused but should be included in the script file
KNOWN_UNUSED_GAPS = [
    (0x350452, 0x350462),  # 16 bytes of unused code in ally/monster behaviours
]

def is_in_known_gap(addr: int) -> bool:
    """Check if an address is within a known unused gap."""
    for start, end in KNOWN_UNUSED_GAPS:
        if start <= addr < end:
            return True
    return False

BATTLE_EVENT_INDEXES_START_AT = 0x3A6004
UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT = 0x3AECF7

command_lens = [
    9,
    8,
    1,
    6,
    4,
    1,
    6,
    1,
    8,
    3,
    1,
    8,
    6,
    1,
    1,
    1,  # 0x00
    3,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    2,
    2,
    2,
    1,
    2,
    2,  # 0x10
    4,
    4,
    4,
    4,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    4,
    4,
    4,
    4,  # 0x20
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    5,
    5,
    1,
    1,
    3,
    1,
    1,
    6,  # 0x30
    3,
    3,
    8,
    2,
    2,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0x40
    3,
    3,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    5,
    1,
    1,  # 0x50
    1,
    1,
    1,
    2,
    3,
    1,
    1,
    1,
    4,
    1,
    3,
    4,
    1,
    1,
    1,
    1,  # 0x60
    1,
    1,
    3,
    1,
    3,
    3,
    1,
    2,
    2,
    5,
    3,
    1,
    1,
    1,
    2,
    1,  # 0x70
    4,
    1,
    1,
    2,
    3,
    3,
    7,
    1,
    1,
    1,
    2,
    5,
    1,
    1,
    3,
    2,  # 0x80
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    5,
    9,
    2,
    3,
    1,  # 0x90
    1,
    1,
    5,
    2,
    1,
    1,
    1,
    3,
    3,
    1,
    1,
    2,
    1,
    1,
    2,
    1,  # 0xa0
    2,
    4,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    1,
    0,
    2,
    3,
    3,
    3,
    2,  # 0xb0
    5,
    1,
    1,
    2,
    1,
    1,
    0,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    8,
    6,  # 0xc0
    4,
    1,
    2,
    4,
    6,
    4,
    1,
    1,
    3,
    1,
    1,
    2,
    1,
    6,
    1,
    1,  # 0xd0
    1,
    4,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xe0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xf0
]

# command_lens = [
#   9, 8, 1, 6, 4, 1, 6, 1, 8, 3, 1, 8, 6, 1, 1, 1, # 0x00
#   3, 1, 2, 1, 1, 1, 1, 1, 3, 1, 2, 2, 2, 1, 2, 2, # 0x10
#   4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, # 0x20
#   2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 1, 1, 3, 1, 1, 6, # 0x30
#   3, 3, 8, 2, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, # 0x40
#   3, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 5, 1, 1, # 0x50
#   1, 1, 1, 2, 3, 1, 1, 1, 4, 1, 3, 4, 1, 1, 1, 1, # 0x60
#   1, 1, 3, 1, 3, 3, 1, 2, 2, 5, 3, 1, 1, 1, 2, 1, # 0x70
#   4, 1, 1, 2, 3, 3, 7, 1, 1, 1, 2, 5, 1, 1, 3, 2, # 0x80
#   1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 9, 2, 3, 1, # 0x90
#   1, 1, 5, 2, 1, 1, 1, 3, 3, 1, 1, 2, 1, 1, 2, 1, # 0xa0
#   2, 4, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 3, 3, 3, 2, # 0xb0
#   5, 1, 1, 2, 1, 1,10, 2, 2, 2, 1, 2, 1, 1, 8, 6, # 0xc0
#   4, 1, 2, 4, 6, 4, 1, 1, 3, 1, 1, 2, 1, 6, 1, 1, # 0xd0
#   1, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, # 0xe0
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  # 0xf0
# ]

rom_coverage = [None] * 0x400000
addresses_to_track = []

class AMEM(list):
    """Base class representing a battlefield layout as a list of 16 lists of ints."""

    def __new__(cls, data):
        # validate the outer list length
        if not isinstance(data, list) or len(data) != 16:
            raise ValueError("AMEM must be a list of 16 lists.")

        # validate each inner list
        for i, inner in enumerate(data):
            if not isinstance(inner, list):
                raise TypeError(f"Element at index {i} is not a list.")
            if not all(isinstance(x, int) for x in inner):
                raise TypeError(f"Element at index {i} contains non-integer values.")

        # create the list instance (empty; contents set in __init__)
        return super().__new__(cls)

    def __init__(self, data):
        # initialize list contents
        super().__init__(data)

    def __reduce_ex__(self, protocol):
        # tell pickle/deepcopy how to reconstruct us: call amem(list(self))
        return (self.__class__, (list(self),))

@dataclass
class OQRef:
    addr: int
    amem: AMEM
    relevant_indexes: list[int]
    label: str
    length: int
    pointers: list[int]

    def __init__(self, addr: int, amem: AMEM, relevant_indexes: list[int], label: str = ""):
        self.addr = addr
        self.amem = deepcopy(amem)
        self.relevant_indexes = deepcopy (relevant_indexes)
        self.label = label

    def __repr__(self) -> str:
        return f"OQRef(addr=0x{self.addr:06X}, label={self.label}, length={self.length if hasattr(self, 'length') else None}, pointers={[f'0x{p:06X}' for p in self.pointers] if hasattr(self, 'pointers') else None}, relevant_indexes={self.relevant_indexes}, amem={self.amem})"

def tok(rom: bytearray, start: int, end: int, oq_starts: list[OQRef], oq_idx_starts: list[OQRef]) -> list[tuple[bytearray, int, bool]]:
    dex = start
    script: list[tuple[bytearray, int, bool]] = []
    combo_oq = oq_starts + oq_idx_starts
    while dex < end:
        if dex in [s.addr for s in combo_oq]:
            oq = next((s for s in combo_oq if s.addr == dex), None)
            if oq is None:
                raise Exception("how did you get here?")
            script.append((rom[dex : dex + oq.length], dex, True))
            dex += oq.length
        else:
            cmd = rom[dex]
            l = command_lens[cmd]
            if cmd == 0x02 or cmd == 0x47:
                #print("warning: encountered 0x02 or 0x47 command at 0x%06x" % dex)
                pass
            if cmd == 0xC6 and l == 0:
                l = 2 + rom[dex + 1]
            elif cmd == 0xBA and l == 0:
                l = 2 + rom[dex + 1] * 2
            script.append((rom[dex : dex + l], dex, False))
            dex += l
    return script

jmp_cmds = [
    0x09,
    0x10,
    0x24,
    0x25,
    0x26,
    0x27,
    0x28,
    0x29,
    0x2A,
    0x2B,
    0x38,
    0x39,
    0x47, # experimental
    0x50,
    0x51,
    0x5D,
    0x64,
    0x68,
    0xA7,
    0xCE,
    0xCF,
    0xD0,
    0xD8,
]

jmp_cmds_1 = [0x68]

TERMINATING_OPCODES = [0x09, 0x11, 0x07, 0x5E,
                       0x02 # experimental
                       ]

SPECIAL_CASE_BREAKS = [
    0x356076,
    0x356087,
    0x3560A9,
    0x3560CD,
    0x3560FE,
    0x356131,
    0x356152,
    0x35617A,
    0x3561AD,
    0x3561E0,
    0x356213,
    0x35624B,
    0x3A8A68,
    0x3A8AC0,
    0x3A8C8A,
]

@dataclass
class Addr:
    offset: int
    amem: AMEM
    ref_label: str
    _referenced_by: list[str]

    @property
    def referenced_by(self) -> list[str]:
        return [r for r in self._referenced_by if r != ""]

    def __init__(self, offset: int, amem: AMEM, ref_label: str, refs: list[str] | None = None):
        self.offset = offset
        self.amem = amem
        self.ref_label = ref_label
        self._referenced_by = deepcopy(refs) if refs is not None else []

    def __str__(self) -> str:
        return (
            f"Addr(offset=0x{self.offset:06X}, amem={self.amem}, "
            f"ref_label={self.ref_label}, referenced_by={self.referenced_by})"
        )

@dataclass
class ObjectQueue:
    offset: int
    destination_offsets: list[int]

    def __init__(self, offset: int, destination_offsets: list[int]):
        self.offset = offset
        self.destination_offsets = destination_offsets

@dataclass
class ObjectQueueWithIndex:
    offset: int
    destination_offsets: list[list[int]]

    def __init__(self, offset: int, destination_offsets: list[list[int]]):
        self.offset = offset
        self.destination_offsets = destination_offsets

@dataclass
class ProtoCommand:
    id: str 
    addr: int
    raw_data: bytearray
    parsed_data: list[int | str]
    length: int | None
    oq: bool

    def __init__(
        self,
        id: str,
        addr: int,
        data: bytearray,
        oq: bool = False,
        length: int | None = None
    ):
        self.id = id
        self.addr = addr
        self.raw_data = data
        self.oq = oq
        self.length = length
        self.parsed_data = []

    def __repr__(self) -> str:
        return (
            f"ProtoCommand(id={self.id!r}, addr=0x{self.addr:06X}, "
            f"raw_data=[{" ".join([f'0x{b:02X}' for b in self.raw_data])}], parsed_data=[{" ".join([str(d) for d in self.parsed_data])}], oq={self.oq}, length={self.length})"
        )

@dataclass
class ContiguousBlock:
    start: int
    contents: bytearray

    @property
    def size(self):
        return len(self.contents)
    
    @property
    def end(self):
        return self.start + self.size
    
    def __init__(self, start: int, contents: bytearray):
        self.start = start
        self.contents = contents

    def __str__(self) -> str:
        return f"ContiguousBlock(start=0x{self.start:06X}, size={self.size}, end=0x{self.end:06X})"

def string_byte(word):
    if type(word) == str:
        return '''"%s"''' % word
    else:
        return "0x%02x" % word

INIT_AMEM: AMEM = AMEM([[0]] * 16)

BATTLE_EVENTS_WITH_QUEUE_POINTER_TABLE = [22]
BATTLE_EVENTS_WITH_DOUBLE_QUEUE_POINTER_TABLE = [70, 85]

BATTLE_EVENTS_ROOT_LABEL = "battle_events_root"

def hash_amem_for_dedup(amem: AMEM, important_indexes: list[int]) -> tuple:
    """Create a hashable representation of AMEM state for duplicate detection."""
    result = []
    for idx in important_indexes:
        # Cap values at 65535 and convert to frozenset for hashing
        capped = frozenset(min(65535, val) for val in amem[idx])
        result.append(capped)
    return tuple(result)

# Maximum number of distinct values to track per AMEM slot before widening
# This prevents state explosion while maintaining correctness
MAX_AMEM_VALUES = 100

def widen_amem_slot(values: list[int]) -> list[int]:
    """
    Widen an AMEM slot that has too many values to prevent state explosion.

    Uses sampling strategy: keep min, max, and representative intermediate values.
    This maintains correctness (conservative approximation) while preventing
    the 60,000+ branch explosions.
    """
    if len(values) <= MAX_AMEM_VALUES:
        return values

    # Sort and get boundaries
    sorted_vals = sorted(set(values))
    min_val = sorted_vals[0]
    max_val = sorted_vals[-1]

    # Sample strategy: keep min, max, and evenly distributed samples
    num_samples = MAX_AMEM_VALUES - 2  # Reserve 2 for min/max
    step = len(sorted_vals) // num_samples

    result = [min_val]
    for i in range(1, num_samples + 1):
        idx = min(i * step, len(sorted_vals) - 1)
        result.append(sorted_vals[idx])
    result.append(max_val)

    return sorted(set(result))

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):
        output_path = "./src/disassembler_output/battle_animation"

        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w")

        # Create variables directory for battle_event_names
        variables_path = "./src/disassembler_output/variables"
        os.makedirs(variables_path, exist_ok=True)
        if not os.path.exists(f"{variables_path}/__init__.py"):
            open(f"{variables_path}/__init__.py", "w")

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        jump_pointers = []

        oq_starts: list[OQRef] = []
        oq_idx_starts: list[OQRef] = []

        known_addresses_covered = {
            "02": [False] * 0x10000,
            "35": [False] * 0x10000,
            "3A": [False] * 0x10000,
        }
        

        collective_data: dict[str, list[list[ProtoCommand]]] = {"35": [], "3A": [], "02": []}

        references: dict[int, list[str]] = {}

        # Cache static pointer addresses for performance (avoid recomputing in loops)
        static_pointer_addresses_cache = set(get_static_pointer_addresses())

        # Load data from config input files
        loaded_arrays = load_arrays_from_input_files()
        loaded_class_names = load_class_names_from_config()

        def convert_event_script_command(command, valid_identifiers):
            cmd = command.raw_data
            # Force identifier output for commands at monster_behaviour_oq_offsets
            is_monster_behaviour = command.addr in monster_behaviour_oq_offsets
            use_identifier: bool = (
                command.id in valid_identifiers or "queuestart" in command.id or is_monster_behaviour
            )
            # use_identifier: bool = false
            args = {}
            cls = None
            include_argnames = True

            # Skip filler commands for unused gaps (they're only for size calculation)
            if command.id.startswith("unused_gap_"):
                return None, {}, False, False

            if command.oq:
                args["destinations"] = '[%s]' %  ", ".join(f"\"{a}\"" for a in command.parsed_data)
                return "DefineObjectQueue", args, True, False

            opcode = cmd[0]

            if opcode == 0x00:
                cls = "NewSpriteAtCoords"
                args["sprite_id"] = loaded_arrays["sprites"][shortify(cmd, 3) & 0x3FF]
                args["sequence"] = str(cmd[5] & 0x0F)
                args["priority"] = str((cmd[6] & 0x30) >> 4)
                args["vram_address"] = f"0x{shortify(cmd, 7):04X}"
                args["palette_row"] = str(cmd[6] & 0x0F)
                if (cmd[1] & 0x01) == 0x01:
                    args["overwrite_vram"] = "True"
                if (cmd[2] & 0x08) == 0x08:
                    args["looping"] = "True"
                if (cmd[2] & 0x10) == 0x10:
                    args["param_2_and_0x10"] = "True"
                if (cmd[2] & 0x20) == 0x20:
                    args["overwrite_palette"] = "True"
                if (cmd[6] & 0x40) == 0x40:
                    args["mirror_sprite"] = "True"
                if (cmd[6] & 0x80) == 0x80:
                    args["invert_sprite"] = "True"
                if (cmd[1] & 0x40) == 0x40:
                    args["behind_all_sprites"] = "True"
                if (cmd[1] & 0x80) == 0x80:
                    args["overlap_all_sprites"] = "True"
            elif opcode == 0x01 or opcode == 0x0B:
                if opcode == 0x01:
                    cls = "SetAMEM32ToXYZCoords"
                elif opcode == 0x0B:
                    cls = "SetAMEM40ToXYZCoords"
                args["origin"] = ORIGINS[((cmd[1] >> 4) & 0b11)]
                args["x"] = str(shortify_signed(cmd, 2))
                args["y"] = str(shortify_signed(cmd, 4))
                args["z"] = str(shortify_signed(cmd, 6))
                if (cmd[1] & 0x01) == 0x01:
                    args["set_x"] = "True"
                if (cmd[1] & 0x02) == 0x02:
                    args["set_y"] = "True"
                if (cmd[1] & 0x04) == 0x04:
                    args["set_z"] = "True"
            elif opcode == 0x02:
                cls = "ActorExitBattleEXPERIMENTAL"
            elif opcode == 0x03:
                cls = "DrawSpriteAtAMEM32Coords"
                args["sprite_id"] = loaded_arrays["sprites"][shortify(cmd, 3) & 0x3FF]
                args["sequence"] = cmd[5] & 0x0F
                if (cmd[1] & 0x01) == 0x01:
                    args["store_to_vram"] = "True"
                if (cmd[2] & 0x08) == 0x08:
                    args["looping"] = "True"
                if (cmd[2] & 0x20) == 0x20:
                    args["store_palette"] = "True"
                if (cmd[1] & 0x40) == 0x40:
                    args["behind_all_sprites"] = "True"
                if (cmd[1] & 0x80) == 0x80:
                    args["overlap_all_sprites"] = "True"
                if (cmd[2] & 0x10) == 0x10:
                    args["bit_4"] = "True"
                if (cmd[5] & 0x80) == 0x80:
                    args["bit_7"] = "True"
            elif opcode == 0x04:
                cls = "PauseScriptUntil"
                if cmd[1] == 6:
                    args["condition"] = "SPRITE_SHIFT_COMPLETE"
                elif cmd[1] == 8:
                    args["condition"] = "BUTTON_PRESSED"
                elif cmd[1] == 0x10:
                    args["condition"] = "FRAMES_ELAPSED"
                    args["frames"] = str(shortify(cmd, 2))
                elif cmd[1] in [1, 2, 4, 7]:
                    args["condition"] = f"UNKNOWN_PAUSE_{cmd[1]}"
                else:
                    args["condition"] = f"0x{cmd[1]:02X}"
            elif opcode == 0x05:
                cls = "RemoveObject"
            elif opcode == 0x07:
                cls = "ReturnObjectQueue"
            elif opcode == 0x08:
                cls = "MoveObject"
                args["speed"] = str(shortify_signed(cmd, 6))
                args["start_position"] = str(shortify_signed(cmd, 2))
                args["end_position"] = str(shortify_signed(cmd, 4))
                if (cmd[1] & 0x04) == 0x04:
                    args["apply_to_x"] = "True"
                if (cmd[1] & 0x02) == 0x02:
                    args["apply_to_y"] = "True"
                if (cmd[1] & 0x01) == 0x01:
                    args["apply_to_z"] = "True"
                if (cmd[1] & 0x20) == 0x20:
                    args["should_set_start_position"] = "True"
                if (cmd[1] & 0x40) == 0x40:
                    args["should_set_end_position"] = "True"
                if (cmd[1] & 0x80) == 0x80:
                    args["should_set_speed"] = "True"
            elif opcode == 0x09:
                cls = "Jmp"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0x0A:
                cls = "Pause1Frame"
            elif opcode == 0x0C:
                cls = "MoveSpriteToCoords"
                if cmd[1] & 0x0E == 0:
                    args["shift_type"] = "SHIFT_TYPE_0X00"
                elif cmd[1] & 0x0E == 2:
                    args["shift_type"] = "SHIFT_TYPE_SHIFT"
                elif cmd[1] & 0x0E == 4:
                    args["shift_type"] = "SHIFT_TYPE_TRANSFER"
                elif cmd[1] & 0x0E == 6:
                    args["shift_type"] = "SHIFT_TYPE_0X04"
                elif cmd[1] & 0x0E == 8:
                    args["shift_type"] = "SHIFT_TYPE_0X08"
                else:
                    raise Exception("invalid shift type: %r" % command)
                args["speed"] = str(shortify_signed(cmd, 2))
                args["arch_height"] = str(shortify_signed(cmd, 4))
            elif opcode == 0x0E:
                cls = "ResetTargetMappingMemory"
            elif opcode == 0x0F:
                cls = "ResetObjectMappingMemory"
            elif opcode == 0x10:
                cls = "RunSubroutine"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0x11:
                cls = "ReturnSubroutine"
            elif opcode == 0x1A:
                cls = "VisibilityOn"
                args["unknown_byte"] = f"0x{cmd[1]:02X}"
            elif opcode == 0x1B:
                cls = "VisibilityOff"
                args["unknown_byte"] = f"0x{cmd[1]:02X}"
            elif (
                opcode
                in [
                    0x20,
                    0x21,
                    0x24,
                    0x25,
                    0x26,
                    0x27,
                    0x28,
                    0x29,
                    0x2A,
                    0x2B,
                    0x2C,
                    0x2D,
                    0x2E,
                    0x2F,
                ]
                and cmd[1] & 0xF0 <= 0xB0
            ) or (opcode in [0x22, 0x23] and 0x10 <= cmd[1] & 0xF0 <= 0x60):
                byte2 = cmd[1] & 0xF0
                include_argnames = False
                if opcode == 0x20:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "SetAMEM8BitToConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "SetAMEM8BitTo7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "SetAMEM8BitTo7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "SetAMEM8BitToAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "SetAMEM8BitToOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "SetAMEM8BitTo7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "SetAMEM8BitToOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "SetAMEM8BitToUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                elif opcode == 0x21:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "SetAMEM16BitToConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "SetAMEM16BitTo7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "SetAMEM16BitTo7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "SetAMEM16BitToAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "SetAMEM16BitToOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "SetAMEM16BitTo7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "SetAMEM16BitToOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "SetAMEM16BitToUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                elif opcode == 0x22:
                    if byte2 == 0x10:
                        cls = "Set7E1xToAMEM8Bit"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "Set7FToAMEM8Bit"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "SetAMEMToAMEM8Bit"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["dest_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "SetOMEMCurrentToAMEM8Bit"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "Set7E5xToAMEM8Bit"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "SetOMEMMainToAMEM8Bit"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "SetUnknownShortToAMEM8Bit"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                elif opcode == 0x23:
                    if byte2 == 0x10:
                        cls = "Set7E1xToAMEM16Bit"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "Set7FToAMEM16Bit"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "SetAMEMToAMEM16Bit"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["dest_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "SetOMEMCurrentToAMEM16Bit"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "Set7E5xToAMEM16Bit"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "SetOMEMMainToAMEM16Bit"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "SetUnknownShortToAMEM16Bit"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                elif opcode == 0x24:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM8BitEqualsConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM8BitEquals7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM8BitEquals7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM8BitEqualsAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM8BitEqualsOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM8BitEquals7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM8BitEqualsOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    else:
                        cls = "JmpIfAMEM8BitEqualsUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x25:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM16BitEqualsConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM16BitEquals7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM16BitEquals7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM16BitEqualsAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM16BitEqualsOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM16BitEquals7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM16BitEqualsOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM16BitEqualsUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x26:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM8BitNotEqualsConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM8BitNotEquals7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM8BitNotEquals7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM8BitNotEqualsAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM8BitNotEqualsOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM8BitNotEquals7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM8BitNotEqualsOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM8BitNotEqualsUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x27:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM16BitNotEqualsConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM16BitNotEquals7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM16BitNotEquals7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM16BitNotEqualsAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM16BitNotEqualsOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM16BitNotEquals7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM16BitNotEq16BitualsOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM16BitNotEqualsUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x28:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM8BitLessThanConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM8BitLessThan7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM8BitLessThan7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM8BitLessThanAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM8BitLessThanOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM8BitLessThan7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM8BitLessThanOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM8BitLessThanUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x29:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM16BitLessThanConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM16BitLessThan7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM16BitLessThan7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM16BitLessThanAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM16BitLessThanOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM16BitLessThan7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM16BitLessThanOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM16BitLessThanUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x2A:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThanConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThan7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThan7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThanAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThan7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM8BitGreaterOrEqualThanUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x2B:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThanConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThan7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThan7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThanAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThan7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "JmpIfAMEM16BitGreaterOrEqualThanUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                elif opcode == 0x2C:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "IncAMEM8BitByConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "IncAMEM8BitBy7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "IncAMEM8BitBy7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "IncAMEM8BitByAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "IncAMEM8BitByOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "IncAMEM8BitBy7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "IncAMEM8BitByOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "IncAMEM8BitByUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                elif opcode == 0x2D:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "IncAMEM16BitByConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "IncAMEM16BitBy7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "IncAMEM16BitBy7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "IncAMEM16BitByAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "IncAMEM16BitByOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "IncAMEM16BitBy7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "IncAMEM16BitByOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "IncAMEM16BitByUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                elif opcode == 0x2E:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "DecAMEM8BitByConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "DecAMEM8BitBy7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "DecAMEM8BitBy7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "DecAMEM8BitByAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "DecAMEM8BitByOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "DecAMEM8BitBy7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "DecAMEM8BitByOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "DecAMEM8BitByUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
                elif opcode == 0x2F:
                    args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                    if byte2 == 0:
                        cls = "DecAMEM16BitByConst"
                        args["value"] = str(shortify(cmd, 2))
                    elif byte2 == 0x10:
                        cls = "DecAMEM16BitBy7E1x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x20:
                        cls = "DecAMEM16BitBy7F"
                        args["address"] = f"0x7F{shortify(cmd, 2):04X}"
                    elif byte2 == 0x30:
                        cls = "DecAMEM16BitByAMEM"
                        src = cmd[2] & 0x0F
                        upper = cmd[2] & 0xF0
                        args["source_amem"] = f"0x{(src + 0x60):02X}"
                        args["upper"] = f"0x{(upper):02X}"
                        include_argnames = True
                    elif byte2 == 0x40:
                        cls = "DecAMEM16BitByOMEMCurrent"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 == 0x50:
                        cls = "DecAMEM16BitBy7E5x"
                        args["address"] = f"0x7E{shortify(cmd, 2):04X}"
                    elif byte2 == 0x60:
                        cls = "DecAMEM16BitByOMEMMain"
                        args["omem"] = f"0x{cmd[2]:02X}"
                        include_argnames = True
                    elif byte2 <= 0xB0:
                        cls = "DecAMEM16BitByUnknownShort"
                        args["type"] = f"0x{(byte2 >> 4):01X}"
                        args["value"] = f"0x{shortify(cmd, 2):04X}"
                        include_argnames = True
                    else:
                        raise Exception("invalid amem shift type: %r" % command)
            elif opcode in [0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B]:
                cls = "UnknownJmp%02X" % opcode
                args["byte_1"] = str(cmd[1])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode in [0x30, 0x31, 0x32, 0x33, 0x34, 0x35]:
                if opcode == 0x30:
                    cls = "IncAMEM8Bit"
                elif opcode == 0x31:
                    cls = "IncAMEM16Bit"
                elif opcode == 0x32:
                    cls = "DecAMEM8Bit"
                elif opcode == 0x33:
                    cls = "DecAMEM16Bit"
                elif opcode == 0x34:
                    cls = "ClearAMEM8Bit"
                elif opcode == 0x35:
                    cls = "ClearAMEM16Bit"
                args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                include_argnames = False
            elif opcode in [0x36, 0x37, 0x38, 0x39, 0x40, 0x41]:
                if opcode == 0x36:
                    cls = "SetAMEMBits"
                elif opcode == 0x37:
                    cls = "ClearAMEMBits"
                elif opcode == 0x38:
                    cls = "JmpIfAMEMBitsSet"
                elif opcode == 0x39:
                    cls = "JmpIfAMEMBitsClear"
                elif opcode == 0x40:
                    cls = "PauseScriptUntilAMEMBitsSet"
                elif opcode == 0x41:
                    cls = "PauseScriptUntilAMEMBitsClear"
                args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                bits = []
                for b in range(0, 8):
                    if cmd[2] & (1 << b) != 0:
                        bits.append(b)
                args["bits"] = "%r" % bits
                if opcode in [0x38, 0x39]:
                    args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0x3A:
                cls = "AttackTimerBegins"
            elif opcode == 0x43:
                cls = "SpriteSequence"
                args["sequence"] = str(cmd[1] & 0x0F)
                if cmd[1] & 0x10 == 0x10:
                    args["looping_on"] = "True"
                if cmd[1] & 0x20 == 0x20:
                    args["looping_off"] = "True"
                if cmd[1] & 0x40 == 0x40:
                    args["bit_6"] = "True"
                if cmd[1] & 0x80 == 0x80:
                    args["mirror"] = "True"
            elif opcode == 0x45:
                cls = "SetAMEM60ToCurrentTarget"
            elif opcode == 0x46:
                cls = "GameOverIfNoAlliesStanding"
            elif opcode == 0x47:
                cls = "SpriteQueueReferenceEXPERIMENTAL"
                args["unknown_byte"] = str(cmd[1])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0x4E:
                cls = "PauseScriptUntilSpriteSequenceDone"
            elif opcode == 0x50:
                cls = "JmpIfTargetDisabled"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0x51:
                cls = "JmpIfTargetEnabled"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0x5D:
                cls = "UseSpriteQueue"
                args["field_object"] = str(cmd[2])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                if cmd[1] & 0x01 == 0x01:
                    args["bit_0"] = "True"
                if cmd[1] & 0x02 == 0x02:
                    args["bit_1"] = "True"
                if cmd[1] & 0x04 == 0x04:
                    args["bit_2"] = "True"
                if cmd[1] & 0x08 == 0x08:
                    args["character_slot"] = "True"
                if cmd[1] & 0x10 == 0x10:
                    args["bit_4"] = "True"
                if cmd[1] & 0x20 == 0x20:
                    args["bit_5"] = "True"
                if cmd[1] & 0x40 == 0x40:
                    args["current_target"] = "True"
                if cmd[1] & 0x80 == 0x80:
                    args["bit_7"] = "True"
            elif opcode == 0x5E:
                cls = "ReturnSpriteQueue"
            elif opcode == 0x63 and 0 <= cmd[1] <= 2:
                cls = "DisplayMessageAtOMEM60As"
                if cmd[1] == 0:
                    args["type"] = "ATTACK_NAME"
                elif cmd[1] == 1:
                    args["type"] = "SPELL_NAME"
                elif cmd[1] == 2:
                    args["type"] = "ITEM_NAME"
                elif cmd[1] == 3:
                    args["type"] = "UNKNOWN_MESSAGE_TYPE_3"
                elif cmd[1] == 4:
                    args["type"] = "UNKNOWN_MESSAGE_TYPE_4"
                elif cmd[1] == 5:
                    args["type"] = "UNKNOWN_MESSAGE_TYPE_5"
                include_argnames = False
            elif opcode == 0x64:
                cls = "UseObjectQueueAtOffsetWithAMEM60Index"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0x68:
                cls = "UseObjectQueueAtOffsetWithAMEM60PointerOffset"
                args["index"] = str(cmd[1])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0x69:
                cls = "SetOMEM60To072C"
            elif opcode == 0x6A:
                cls = "SetAMEMToRandomByte"
                args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                args["upper_bound"] = str(cmd[2])
            elif opcode == 0x6B:
                cls = "SetAMEMToRandomShort"
                args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
                args["upper_bound"] = str(shortify(cmd, 2))
            elif opcode == 0x70:
                cls = "EnableSpritesOnSubscreen"
            elif opcode == 0x71:
                cls = "DisableSpritesOnSubscreen"
            elif opcode == 0x72:
                cls = "NewEffectObject"
                args["effect"] = loaded_arrays["effects"][cmd[2]]
                if cmd[1] & 0x01 == 0x01:
                    args["looping_on"] = "True"
                if cmd[1] & 0x02 == 0x02:
                    args["playback_off"] = "True"
                if cmd[1] & 0x04 == 0x04:
                    args["looping_off"] = "True"
                if cmd[1] & 0x08 == 0x08:
                    args["bit_3"] = "True"
            elif opcode == 0x73:
                cls = "Pause2Frames"
            elif opcode == 0x74 and cmd[1:] in [
                [0x04, 0x00],
                [0x08, 0x00],
                [0x00, 0x02],
                [0x00, 0x04],
                [0x00, 0x08],
            ]:
                cls = "PauseScriptUntil"
                if cmd[1:] == [0x04, 0x00]:
                    args["condition"] = "SEQ_4BPP_COMPLETE"
                elif cmd[1:] == [0x08, 0x00]:
                    args["condition"] = "SEQ_2BPP_COMPLETE"
                elif cmd[1:] == [0x00, 0x02]:
                    args["condition"] = "FADE_IN_COMPLETE"
                elif cmd[1:] == [0x00, 0x04]:
                    args["condition"] = "FADE_4BPP_COMPLETE"
                elif cmd[1:] == [0x00, 0x08]:
                    args["condition"] = "FADE_2BPP_COMPLETE"
            elif opcode == 0x75:
                cls = "PauseScriptUntilBitsClear"
                args["bits"] = f"0x{shortify(cmd, 1):04X}"
                include_argnames = False
            elif opcode == 0x76:
                cls = "ClearEffectIndex"
            elif opcode in [0x77, 0x78]:
                if opcode == 0x77:
                    cls = "Layer3On"
                else:
                    cls = "Layer3Off"
                if cmd[1] & 0xF0 == 0:
                    args["property"] = "TRANSPARENCY_OFF"
                elif cmd[1] & 0xF0 == 0x10:
                    args["property"] = "OVERLAP_ALL"
                elif cmd[1] & 0xF0 == 0x20:
                    args["property"] = "OVERLAP_NONE"
                elif cmd[1] & 0xF0 == 0x30:
                    args["property"] = "OVERLAP_ALL_EXCEPT_ALLIES"
                else:
                    raise Exception("invalid property type at %r" % command)
                if cmd[1] & 0x01 == 0x01:
                    args["bit_0"] = "True"
                if cmd[1] & 0x02 == 0x02:
                    args["bpp4"] = "True"
                if cmd[1] & 0x04 == 0x04:
                    args["bpp2"] = "True"
                if cmd[1] & 0x08 == 0x08:
                    args["invisible"] = "True"
            elif opcode == 0x7A and 0 <= cmd[1] <= 2:
                cls = "DisplayMessage"
                if cmd[1] == 0:
                    args["type"] = "ATTACK_NAME"
                elif cmd[1] == 1:
                    args["type"] = "SPELL_NAME"
                elif cmd[1] == 2:
                    args["type"] = "ITEM_NAME"
                args["dialog_id"] = str(cmd[2])
                include_argnames = False
            elif opcode == 0x7B:
                cls = "PauseScriptUntilDialogClosed"
            elif opcode == 0x7E:
                cls = "FadeOutObject"
                args["duration"] = str(cmd[1])
            elif opcode == 0x7F:
                cls = "ResetSpriteSequence"
            elif opcode == 0x80:
                cls = "ShineEffect"
                args["colour_count"] = str(cmd[2] & 0x0F)
                args["starting_colour_index"] = str((cmd[2] & 0xF0) >> 4)
                args["glow_duration"] = str(cmd[3])
                if cmd[1] == 1:
                    args["west"] = "True"
                elif cmd[1] == 0:
                    args["east"] = "True"
                else:
                    raise Exception(command)
            elif opcode == 0x85:
                if cmd[1] == 0:
                    cls = "FadeOutEffect"
                elif cmd[1] == 0x10:
                    cls = "FadeOutSprite"
                elif cmd[1] == 0x20:
                    cls = "FadeOutScreen"
                elif cmd[1] == 2:
                    cls = "FadeInEffect"
                elif cmd[1] == 0x12:
                    cls = "FadeInSprite"
                elif cmd[1] == 0x22:
                    cls = "FadeInScreen"
                args["duration"] = cmd[2]
            elif opcode == 0x86 and cmd[1] in [1, 2, 4]:
                if cmd[1] == 1:
                    cls = "ShakeScreen"
                elif cmd[1] == 2:
                    cls = "ShakeSprites"
                elif cmd[1] == 4:
                    cls = "ShakeScreenAndSprites"
                args["amount"] = str(cmd[4])
                args["speed"] = str(shortify(cmd, 5))
            elif opcode == 0x87:
                cls = "StopShakingObject"
            elif opcode == 0x9C:
                cls = "WaveEffect"
                param1 = cmd[2]
                if param1 & 0x01 == 0x01:
                    args["layer"] = "WAVE_LAYER_BATTLEFIELD"
                elif param1 & 0x02 == 0x02:
                    args["layer"] = "WAVE_LAYER_4BPP"
                elif param1 & 0x04 == 0x04:
                    args["layer"] = "WAVE_LAYER_2BPP"
                if param1 & 0x40 == 0x40:
                    args["direction"] = "WAVE_LAYER_HORIZONTAL"
                elif param1 & 0x80 == 0x80:
                    args["direction"] = "WAVE_LAYER_VERTICAL"
                args["depth"] = str(shortify(cmd, 3))
                args["intensity"] = str(shortify(cmd, 5))
                args["speed"] = str(shortify(cmd, 7))
                if param1 & 0x08 == 0x08:
                    args["bit_3"] = "True"
                if param1 & 0x10 == 0x10:
                    args["bit_4"] = "True"
                if param1 & 0x20 == 0x20:
                    args["bit_5"] = "True"
                if cmd[1] != 0:
                    args["byte_1"] = f"0x{cmd[1]:02X}"
            elif opcode == 0x9D:
                cls = "StopWaveEffect"
                if cmd[1] & 0x80 == 0x80:
                    args["bit_7"] = "True"
            elif opcode == 0xA7:
                cls = "JmpIfTimedHitSuccess"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0x8E:
                cls = "ScreenFlashWithDuration"
                args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
                args["duration"] = str(cmd[2])
                if cmd[1] & 0xF8 != 0:
                    args["unknown_upper"] = str(cmd[1] & 0xF8)
                include_argnames = False
            elif opcode == 0x8F:
                cls = "ScreenFlash"
                args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
                if cmd[1] & 0xF8 != 0:
                    args["unknown_upper"] = str(cmd[1] & 0xF8)
                include_argnames = False
            elif opcode == 0x95:
                cls = "InitializeBonusMessageSequence"
            elif opcode == 0x96:
                cls = "DisplayBonusMessage"
                args["message"] = BONUS_MESSAGES[cmd[2]]
                args["x"] = str(byte_signed(cmd[3]))
                args["y"] = str(byte_signed(cmd[4]))
            elif opcode == 0x97:
                cls = "PauseScriptUntilBonusMessageComplete"
            elif opcode == 0xA3:
                cls = "ScreenEffect"
                args["message"] = loaded_arrays["screen_effects"][cmd[1]]
                include_argnames = False
            elif opcode in [0xAB, 0xAE]:
                cls = "PlaySound"
                args["sound"] = loaded_arrays["sounds"][cmd[1]]
                if opcode == 0xAE:
                    args["channel"] = "4"
            elif opcode == 0xB0:
                cls = "PlayMusicAtCurrentVolume"
                args["sound"] = loaded_arrays["music"][cmd[1]]
                include_argnames = False
            elif opcode == 0xB1:
                cls = "PlayMusicAtVolume"
                args["sound"] = loaded_arrays["music"][cmd[1]]
                args["volume"] = str(shortify(cmd, 2))
                include_argnames = False
            elif opcode == 0xB2:
                cls = "StopCurrentSoundEffect"
            elif opcode == 0xB6:
                cls = "FadeCurrentMusicToVolume"
                args["speed"] = str(cmd[1])
                args["volume"] = str(cmd[2])
            elif opcode == 0xBB:
                cls = "SetTarget"
                args["target"] = TARGETS[cmd[1]]
                include_argnames = False
            elif opcode in [0xBC, 0xBD]:
                include_argnames = False
                if cmd[2] == 0:
                    cls = (
                        "AddItemToStandardInventory"
                        if opcode == 0xBC
                        else "AddItemToKeyItemInventory"
                    )
                    args["target"] = loaded_class_names["all_items"][cmd[1]]
                elif cmd[2] == 0xFF:
                    cls = (
                        "RemoveItemFromStandardInventory"
                        if opcode == 0xBC
                        else "RemoveItemFromKeyItemInventory"
                    )
                    args["target"] = loaded_class_names["all_items"][256 - cmd[1]]
                else:
                    raise Exception(command)
            elif opcode == 0xBE:
                cls = "AddCoins"
                args["amount"] = str(shortify(cmd, 1))
                include_argnames = False
            elif opcode == 0xBF:
                cls = "AddYoshiCookiesToInventory"
                args["amount"] = str(cmd[1])
                include_argnames = False
            elif opcode == 0xC3:
                cls = "DoMaskEffect"
                args["effect"] = MASKS[cmd[1] & 0x07]
                if cmd[1] & 0xF8 != 0:
                    args["unknown_upper"] = str(cmd[1] & 0xF8)
                include_argnames = False
            elif opcode == 0xC6:
                cls = "SetMaskCoords"
                point_bytes = byte_signed(cmd[1])
                points = []
                for i in range(2, (point_bytes // 2) * 2 + 2, 2):
                    points.append("(%s, %s)" % (byte_signed(cmd[i]), byte_signed(cmd[i + 1])))
                args["points"] = f'[{",".join(points)}]'
                if point_bytes % 2 != 0:
                    args["extra_byte"] = f"0x{cmd[2 + point_bytes - 1]:02x}"
            elif opcode == 0xCB:
                cls = "SetSequenceSpeed"
                args["speed"] = str(cmd[1])
                include_argnames = False
            elif opcode == 0xCC:
                cls = "StartTrackingAllyButtonInputs"
            elif opcode == 0xCD:
                cls = "EndTrackingAllyButtonInputs"
            elif opcode == 0xCE:
                cls = "TimingForOneTieredButtonPress"
                args["start_accepting_input"] = str(cmd[2])
                args["end_accepting_input"] = str(cmd[1])
                args["partial_start"] = str(cmd[3])
                args["perfect_start"] = str(cmd[4])
                args["perfect_end"] = str(cmd[5])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0xCF:
                cls = "TimingForOneBinaryButtonPress"
                args["start_accepting_input"] = str(cmd[2])
                args["end_accepting_input"] = str(cmd[1])
                args["timed_hit_ends"] = str(cmd[3])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0xD0:
                cls = "TimingForMultipleButtonPresses"
                args["start_accepting_input"] = str(cmd[1])
                args["destinations"] = '["%s"]' % command.parsed_data[0]
            elif opcode == 0xD1:
                cls = "TimingForButtonMashUnknown"
            elif opcode == 0xD2:
                cls = "TimingForButtonMashCount"
                args["max_presses"] = str(cmd[1])
            elif opcode == 0xD3:
                cls = "TimingForRotationCount"
                args["start_accepting_input"] = str(cmd[2])
                args["end_accepting_input"] = str(cmd[1])
                args["max_presses"] = str(cmd[3])
            elif opcode == 0xD4:
                cls = "TimingForChargePress"
                args["charge_level_1_end"] = str(cmd[1])
                args["charge_level_2_end"] = str(cmd[2])
                args["charge_level_3_end"] = str(cmd[3])
                args["charge_level_4_end"] = str(cmd[4])
                args["overcharge_end"] = str(cmd[5])
            elif opcode == 0xD5:
                cls = "SummonMonster"
                args["monster"] = loaded_class_names["enemies"][cmd[2]]
                args["position"] = cmd[3]
                if cmd[1] & 0x01 == 0x01:
                    args["bit_0"] = "True"
                if cmd[1] & 0x02 == 0x02:
                    args["bit_1"] = "True"
                if cmd[1] & 0x04 == 0x04:
                    args["bit_2"] = "True"
                if cmd[1] & 0x08 == 0x08:
                    args["bit_3"] = "True"
                if cmd[1] & 0x10 == 0x10:
                    args["bit_4"] = "True"
                if cmd[1] & 0x20 == 0x20:
                    args["bit_5"] = "True"
                if cmd[1] & 0x40 == 0x40:
                    args["bit_6"] = "True"
                if cmd[1] & 0x80 == 0x80:
                    args["bit_7"] = "True"
            elif opcode == 0xD8:
                cls = "MuteTimingJmp"
                args["destinations"] = '["%s"]' % command.parsed_data[0]
                include_argnames = False
            elif opcode == 0xD9:
                cls = "DisplayCantRunDialog"
            elif opcode == 0xE0:
                cls = "StoreOMEM60ToItemInventory"
            elif opcode == 0xE1:
                cls = "RunBattleEvent"
                args["script_id"] = SCRIPT_NAMES["battle_events"][shortify(cmd, 1)]
                if cmd[3] != 0:
                    args["offset"] = str(cmd[3])
            else:
                cls = "UnknownCommand"
                include_argnames = False
                args["args"] = "%r" % bytearray(cmd)

            return cls, args, use_identifier, include_argnames

        def get_script(script, valid_identifiers):

            new_script = []

            for cmd in script:
                identifier = ""
                cls, args, use_identifier, include_argnames = convert_event_script_command(
                    cmd, valid_identifiers
                )

                if cls is not None:
                    arg_strings = []
                    for key in args:
                        if include_argnames:
                            arg_strings.append("%s=%s" % (key, args[key]))
                        else:
                            arg_strings.append(args[key])
                    try:
                        arg_string = ", ".join(arg_strings)
                    except:
                        raise Exception(cls)

                    if use_identifier:
                        if len(arg_string) > 0:
                            arg_string += ", "
                        identifier = 'identifier="%s"' % cmd.id

                    output = "%s(%s%s)" % (cls, arg_string, identifier)
                    new_script.append(output)

            return new_script

        # Generate battle event names from battle_event_names module
        battle_event_var_names = []
        for attr_name in dir(battle_event_names):
            if attr_name.startswith("BE"):
                battle_event_var_names.append(attr_name)
        # Sort by the numeric value to get them in the right order
        battle_event_var_names.sort(key=lambda x: getattr(battle_event_names, x))

        # Create mapping from battle event command addresses to their names
        battle_event_addr_to_name = {}
        for event_index, event_name in enumerate(battle_event_var_names):
            # Read the pointer at BATTLE_EVENT_INDEXES_START_AT + (event_index * 2)
            pointer_addr = BATTLE_EVENT_INDEXES_START_AT + (event_index * 2)
            if pointer_addr < len(rom):
                # Read the 2-byte pointer (little endian)
                pointer_value = shortify(rom, pointer_addr)
                # Convert to absolute address in bank 0x3A
                command_addr = 0x3A0000 + pointer_value
                # Convert event name to identifier format (e.g., "BE0000_UNUSED" -> "battle_event_0_unused")
                # Remove "BE" prefix and convert to lowercase
                identifier_name = "battle_event_" + event_name[2:].lower()
                battle_event_addr_to_name[command_addr] = identifier_name

        # Helper function to format names with class name and ID
        def format_with_id(class_names, start_id, suffix):
            """Format class names with their IDs: {classname}_{id}_{suffix}"""
            result = []
            for idx, class_name in enumerate(class_names):
                item_id = start_id + idx
                # Remove "Item", "Spell", "Attack" suffixes from class name if present
                base_name = class_name.replace("Item", "").replace("Spell", "").replace("Attack", "")
                result.append(f"{base_name}_{item_id}_{suffix}")
            return result

        # Format names for weapons, items, and spells
        weapon_names = format_with_id(loaded_class_names.get("weapons", []), 0, "weapon")
        item_names = format_with_id(loaded_class_names.get("items", []), 96, "item")
        ally_spell_names = format_with_id(loaded_class_names.get("ally_spells", []), 0, "spell")
        monster_spell_names = format_with_id(loaded_class_names.get("monster_spells", []), 0, "spell")
        monster_attack_names = format_with_id(loaded_class_names.get("monster_attacks", []), 0, "attack")

        SCRIPT_NAMES = {
            "battle_events": battle_event_var_names,
            "ally_spells": ally_spell_names,
            "monster_spells": monster_spell_names,
            "monster_attacks": monster_attack_names,
            "items": item_names,
            "weapons": weapon_names,
            "weapon_misses": weapon_names,
            "weapon_sounds": weapon_names,
            "sprites": loaded_arrays.get("sprites", []),
            "flower_bonus": [
                "(empty flower bonus message)",
                "Attack Up!",
                "Defense Up!",
                "HP Max!",
                "Once Again!",
                "Lucky!",
            ],
            "toad_tutorial": ["toad_tutorial"],
            "weapon_wrapper_mario": ["weapon_wrapper_mario"],
            "weapon_wrapper_toadstool": ["weapon_wrapper_toadstool"],
            "weapon_wrapper_bowser": ["weapon_wrapper_bowser"],
            "weapon_wrapper_geno": ["weapon_wrapper_geno"],
            "weapon_wrapper_mallow": ["weapon_wrapper_mallow"],
            "ally_behaviours": [
                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: Mario/DUMMY A attack',
                'Ally behaviour unindexed: Mario/DUMMY Y attack',
                'Ally behaviour unindexed: Mario/DUMMY X item',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',

                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: Peach A attack',
                'Ally behaviour unindexed: Peach Y attack',
                'Ally behaviour unindexed: Peach X item',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',

                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: Bowser A attack',
                'Ally behaviour unindexed: Bowser Y attack',
                'Ally behaviour unindexed: Bowser X item',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',

                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: Geno A attack',
                'Ally behaviour unindexed: Geno Y attack',
                'Ally behaviour unindexed: Geno X item',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',

                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: Mallow A attack',
                'Ally behaviour unindexed: Mallow Y attack',
                'Ally behaviour unindexed: Mallow X item',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',

                'Ally behaviour unindexed: unknown 0x350462',
                'Ally behaviour 0: flinch animation',
                'Ally behaviour unindexed: unknown 0x350484',
                'Ally behaviour unindexed: unknown 0x350488 (mario/dummy)',
                'Ally behaviour unindexed: unknown 0x3504AB (mario/dummy)',
                'Ally behaviour unindexed: unknown 0x3504CE (mario/dummy)',
                'Ally behaviour unindexed: victory pose',
                'Ally behaviour 1: run away attempt',
            ],
            "monster_behaviours_1": [  # 5
                'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit'
                'Monster behaviour 1: flinch animation of sprite behaviours: no movement for "Escape"',
                'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 8: escape animation of sprite behaviours: no movement for "Escape", no reaction when hit',
                'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
                'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 2: flinch animation of sprite behaviours: slide backward when hit",
                'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
                'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
                'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 3: flinch animation of sprite behaviours: Bowser Clone sprite",
                'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
                'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
                'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 4: flinch animation of sprite behaviours: Mario Clone sprite",
                'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
                'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
                'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                "Monster behaviour 5: flinch animation of sprite behaviours: no reaction when hit",
                'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
                'Monster behaviour 8: escape animation of sprite behaviours: no movement for "Escape", no reaction when hit',
                "Monster behaviour 11: KO animation of sprite behaviours: no reaction when hit",
            ],
            "monster_behaviours_2": [  # 1
                "Monster behaviour 12: entrance animation of sprite behaviours: sprite shadow",
                "Monster behaviour 13: flinch animation of sprite behaviours: sprite shadow",
                "Monster behaviour 14: initiate spell animation of sprite behaviours: sprite shadow",
                "Monster behaviour 15: initiate attack animation of sprite behaviours: sprite shadow",
                "Monster behaviour 16: escape animation of sprite behaviours: sprite shadow",
                "Monster behaviour 17: KO animation of sprite behaviours: sprite shadow",
            ],
            "monster_behaviours_3": [  # 2
                "Monster behaviour 18: entrance animation of sprite behaviours: floating, sprite shadow",
                "Monster behaviour 20: flinch animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 21: initiate spell animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 22: initiate attack animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 23: escape animation of sprite behaviours: floating, sprite shadow",
                "Monster behaviour 25: KO animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 19: entrance animation of sprite behaviours: floating",
                "Monster behaviour 20: flinch animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 21: initiate spell animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 22: initiate attack animation of sprite behaviours: floating, sprite shadow, floating",
                "Monster behaviour 24: escape animation of sprite behaviours: floating",
                "Monster behaviour 25: KO animation of sprite behaviours: floating, sprite shadow, floating",
            ],
            "monster_behaviours_4": [  # 3
                "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 27: flinch animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
                "Monster behaviour 29: initiate spell animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
                "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 32: escape animation of sprite behaviours: floating, slide backward when hit (1)",
                "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 27: flinch animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
                "Monster behaviour 29: initiate spell animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
                "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 33: escape animation of sprite behaviours: floating, slide backward when hit (2)",
                "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 28: flinch animation of sprite behaviours: fade out death, floating",
                "Monster behaviour 30: initiate spell animation of sprite behaviours: fade out death, floating",
                "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
                "Monster behaviour 34: escape animation of sprite behaviours: fade out death, floating",
                "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
            ],
            "monster_behaviours_5": [  # 4
                'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                "Monster behaviour 41: escape animation of sprite behaviours: fade out death (1), fade out death (2)",
                'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                "Monster behaviour 38: initiate spell aanimation of sprite behaviours: fade out death (2)",
                'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                "Monster behaviour 41: escape animation of sprite behaviours: fade out death (1), fade out death (2)",
                'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                "Monster behaviour 42: escape animation of sprite behaviours: fade out death, Smithy spell cast",
                'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
                'Monster behaviour 43: escape animation of sprite behaviours: fade out death, no "Escape" movement',
                'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
            ],
            "monster_behaviours_6": [  # 3
                'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 46: flinch animation of sprite behaviours: fade out death, no "Escape" transition',
                'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 51: escape animation of sprite behaviours: fade out death, no "Escape" transition',
                'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                "Monster behaviour 47: flinch animation of sprite behaviours: (normal)",
                'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                "Monster behaviour 52: escape animation of sprite behaviours: (normal), no reaction when hit",
                'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                "Monster behaviour 48: flinch animation of sprite behaviours: no reaction when hit",
                'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
                "Monster behaviour 52: escape animation of sprite behaviours: (normal), no reaction when hit",
                'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
            ],
            "monster_entrances": [
                "ENT0000_NONE",
                "ENT0001_SLIDE_IN",
                "ENT0002_LONG_JUMP",
                "ENT0003_HOP_3_TIMES",
                "ENT0004_DROP_FROM_ABOVE",
                "ENT0005_ZOOM_IN_FROM_RIGHT",
                "ENT0006_ZOOM_IN_FROM_LEFT",
                "ENT0007_SPREAD_OUT_FROM_BACK",
                "ENT0008_HOVER_IN",
                "ENT0009_READY_TO_ATTACK",
                "ENT0010_FADE_IN",
                "ENT0011_SLOW_DROP_FROM_ABOVE",
                "ENT0012_WAIT_THEN_APPEAR",
                "ENT0013_SPREAD_FROM_FRONT",
                "ENT0014_SPREAD_FROM_MIDDLE",
                "ENT0015_READY_TO_ATTACK",
            ],
        }

        # Map StaticPointer names to SCRIPT_NAMES keys for labeling
        STATIC_POINTER_TO_SCRIPT_NAMES: dict[str, str] = {
            "weapon_miss_oq": "weapon_misses",
            "weapon_sound_oq": "weapon_sounds",
            "item_oq": "items",
            "ally_spell_oq": "ally_spells",
            "weapon_animation_oq": "weapons",
            "monster_spell_ptrs": "monster_spells",
            "monster_attack_ptrs": "monster_attacks",
            "monster_entrance_oq": "monster_entrances",
            "flower_bonus_oq": "flower_bonus",
        }

        # Process all ROM banks using POINTER_MUST_REMAIN_STATIC as the source of truth
        for rom_bank_id in ["02", "35", "3A"]:
            third_byte_as_string = rom_bank_id  # Keep uppercase to match known_addresses_covered keys
            bank_as_upper_byte = int(rom_bank_id, 16) << 16

            # this is the list of every address in the animation code that can be touched, recursively, from a top-level pointer
            branches: list[Addr] = []
            amem: AMEM = deepcopy(INIT_AMEM)

            # Get all static pointers for this bank
            bank_static_pointers = [p for p in POINTER_MUST_REMAIN_STATIC if p.bank.upper() == rom_bank_id.upper()]

            for static_ptr in bank_static_pointers:
                ptr_addr = static_ptr.address
                reference_label = static_ptr.name or f"script_0x{ptr_addr:06X}"

                if static_ptr.is_oq:
                    # Special handling for specific pointer types
                    if static_ptr.name == "ally_behaviour_root_oq":
                        # 0x350000 - ally behaviour root with nested OQs
                        o = OQRef(0x350000, deepcopy(INIT_AMEM), [0])
                        o.length = 2
                        oq_starts.append(deepcopy(o))
                        known_addresses_covered[third_byte_as_string][0] = True
                        known_addresses_covered[third_byte_as_string][1] = True
                        branches.append(Addr(0x350000, deepcopy(INIT_AMEM), "ally_behaviours_root", []))
                        top_level_ally_ptr = shortify(rom, 0x350000) + 0x350000
                        branches.append(Addr(top_level_ally_ptr, deepcopy(INIT_AMEM), "ally_behaviours_subroot", ["ally_behaviours_root"]))
                        o = OQRef(top_level_ally_ptr, deepcopy(INIT_AMEM), [0])
                        o.length = 12
                        oq_starts.append(deepcopy(o))
                        for i in range(0, 12, 2):
                            cursor = top_level_ally_ptr + i
                            known_addresses_covered[third_byte_as_string][cursor & 0xFFFF] = True
                            known_addresses_covered[third_byte_as_string][(cursor & 0xFFFF) + 1] = True
                            a_offset = shortify(rom, cursor) + 0x350000
                            o = OQRef(a_offset, deepcopy(INIT_AMEM), [0])
                            o.length = 16
                            oq_starts.append(deepcopy(o))
                            branches.append(Addr(a_offset, deepcopy(INIT_AMEM), f"ally_behaviour_set_{i}", ["ally_behaviours_root", "ally_behaviours_subroot"]))

                    elif static_ptr.name == "monster_behaviour_ptrs":
                        # 0x350202 - 256 monster behaviour pointers, each to a 6-ptr OQ
                        o = OQRef(ptr_addr, deepcopy(INIT_AMEM), [0])
                        o.length = 512
                        oq_starts.append(deepcopy(o))
                        for i in range(0, 512, 2):
                            mb_offset = shortify(rom, ptr_addr + i) + 0x350000
                            o = OQRef(mb_offset, deepcopy(INIT_AMEM), [0], label=f'monster_{i//2}_sprite_behaviour')
                            o.length = 12
                            oq_starts.append(deepcopy(o))
                            branches.append(Addr(ptr_addr, deepcopy(INIT_AMEM), "monster_behaviour_by_id", []))
                        for i in range(0x0202, 0x0202+512):
                            known_addresses_covered["35"][i] = True

                    elif static_ptr.name == "battle_events_root_oq":
                        # 0x3A6000 - battle events with variable-length pointer table
                        tertiary_cursor = ptr_addr
                        tertiary_cursor_short = tertiary_cursor & 0xFFFF
                        tertiary_end = 0x10000
                        while tertiary_cursor_short < tertiary_end:
                            tertiary_points_to = shortify(rom, tertiary_cursor)
                            known_addresses_covered[third_byte_as_string][tertiary_cursor & 0xFFFF] = True
                            known_addresses_covered[third_byte_as_string][(tertiary_cursor & 0xFFFF) + 1] = True
                            if tertiary_points_to < tertiary_end:
                                tertiary_end = tertiary_points_to
                            tertiary_cursor += 2
                            tertiary_cursor_short = tertiary_cursor & 0xFFFF
                            oq_idx_starts.append(OQRef(bank_as_upper_byte + tertiary_points_to, deepcopy(INIT_AMEM), [0]))
                            branches.append(Addr(bank_as_upper_byte + tertiary_points_to, deepcopy(INIT_AMEM), BATTLE_EVENTS_ROOT_LABEL, []))
                        # force 0x3a6000 to be processed as ptr table
                        o = OQRef(0x3A6000, deepcopy(INIT_AMEM), [0])
                        o.length = 4
                        oq_idx_starts.append(o)

                    else:
                        # Generic OQ pointer table
                        o = OQRef(ptr_addr, deepcopy(amem), [0])
                        if static_ptr.oq_ptr_count:
                            ptr_table_size = static_ptr.oq_ptr_count * 2
                            o.length = ptr_table_size
                            # Mark pointer table bytes as covered
                            for ptr_offset in range(ptr_table_size):
                                known_addresses_covered[third_byte_as_string][(ptr_addr + ptr_offset) & 0xFFFF] = True
                            # Add branches for each pointer
                            script_names_key = STATIC_POINTER_TO_SCRIPT_NAMES.get(static_ptr.name or "", "")
                            for pointer_table_index in range(static_ptr.oq_ptr_count):
                                pointer_addr = ptr_addr + (pointer_table_index * 2)
                                three_byte_pointer = shortify(rom, pointer_addr) + bank_as_upper_byte
                                # Generate label
                                if script_names_key and script_names_key in SCRIPT_NAMES and pointer_table_index < len(SCRIPT_NAMES[script_names_key]):
                                    ref_label = f"{reference_label} {SCRIPT_NAMES[script_names_key][pointer_table_index]}"
                                else:
                                    ref_label = f"{reference_label} {pointer_table_index}"
                                branches.append(Addr(three_byte_pointer, deepcopy(amem), ref_label, []))
                                known_addresses_covered[third_byte_as_string][three_byte_pointer & 0xFFFF] = True
                                known_addresses_covered[third_byte_as_string][(three_byte_pointer & 0xFFFF) + 1] = True
                        oq_starts.append(o)
                else:
                    # Non-OQ entry - just add as a branch
                    branches.append(Addr(ptr_addr, deepcopy(INIT_AMEM), reference_label, []))

            # sprite behaviour OQs need to be included for bank 35
            if rom_bank_id == "35":
                for i, mb_offset in enumerate(monster_behaviour_oq_offsets):
                    label = monster_behaviour_names[i] if i < len(monster_behaviour_names) else f'sprite_behaviour_{i}'
                    oq_starts.append(OQRef(mb_offset, deepcopy(INIT_AMEM), [0], label=label))
                    branches.append(Addr(mb_offset, deepcopy(INIT_AMEM), label, []))
            # now we're going to process every item in the branch array, adding any more branches we find from jumps, object queues, subroutines, etc.
            branch_index: int = 0
            this_branch = branches[branch_index]
            while True:
                #print(f'    tracing branch index {branch_index}/{len(branches)} of {rom_bank_id} (0x{this_branch.offset:06x}): {this_branch}')
                # amem can control where the code branches to.
                amem = deepcopy(this_branch.amem)
                absolute_offset = this_branch.offset 

                # keep a running, recursive list of what top-level scripts ultimately reference this code.
                # this will ultimatley be displayed in the output python file as an annotation.
                cursor = absolute_offset
                if absolute_offset not in references:
                    references[absolute_offset] = []
                references[absolute_offset].extend(this_branch.referenced_by)
                references[absolute_offset] = list(set(references[absolute_offset]))

                # process every command in the script until we find a terminating byte.
                end_found = False
                #print(this_branch)
                while not end_found:
                    #print(f'        current_addr: 0x{cursor:06x}')
                    def validate_addr(offs: int, am: AMEM, lbl: str = "", important_amem_indexes_raw: list[int] | None = None):
                        
                        #print("raw", important_amem_indexes_raw)
                        if important_amem_indexes_raw is None:
                            important_amem_indexes_raw = [0]
                        #print("raw", important_amem_indexes_raw)
                        important_amem_indexes = list(set(important_amem_indexes_raw))
                        #print("important", important_amem_indexes)

                        # ?
                        jump_voided = False

                        # exit if the branch destination is somehow not in this bank
                        if offs & 0xFF0000 != bank_as_upper_byte:
                            raise Exception("illegal addr 0x%06x" % offs)

                        # add this branch's label to the list of references the destination branch will receive
                        dc = deepcopy(this_branch.referenced_by)
                        if (
                            this_branch.ref_label != ""
                            and this_branch.ref_label != BATTLE_EVENTS_ROOT_LABEL
                        ):
                            dc.append(this_branch.ref_label)

                        # separately, maintain an address<->references dict for easier lookup
                        if offs not in references:
                            references[offs] = []
                        references[offs].append(this_branch.ref_label)
                        references[offs] = list(set(references[offs]))

                        destination_branch = Addr(
                            offs, deepcopy(am), lbl, deepcopy(dc)
                        )

                        # if the destination branch already exists, verify that we don't have an exact copy with the same amem
                        for t in [t for t in branches if t.offset == offs]:
                            # debug
                            # Not debug, actually! The trace graph was identical with and without AMEM tracing
                            # which means my method for calculating object queue size is probably correct.
                            jump_voided = True
                            same_amem_count = 0
                            #print(f"0x{offs:06x} comparing amem:")
                            for a in important_amem_indexes:
                                #print(a)
                                capped_amem = list(set([min(65535, b) for b in t.amem[a]]))
                                capped_amem_comp = list(set([min(65535, b) for b in am[a]]))
                                if set(capped_amem) == set(capped_amem_comp):
                                    same_amem_count += 1
                            if same_amem_count == len(important_amem_indexes):
                                jump_voided = True
                                break

                        if not jump_voided:
                            branches.append(destination_branch)

                        return destination_branch

                    def create_object_queue(base_addr: int, label_override: str | None = None) -> int:
                        nonlocal end_found
                        temp_cursor_addr = base_addr
                        length = 0
                        for s in [s for s in oq_starts if s.addr == base_addr]:
                            temp_cursor_addr = base_addr
                            temp_cursor_addr_short = temp_cursor_addr & 0xFFFF
                            i = 0
                            length = 0
                            ptrs: list[int] = []
                            if label_override is not None:
                                label = label_override
                            # check if this is a monster behaviour object queue (should have exactly 6 pointers)
                            is_monster_behaviour = base_addr in monster_behaviour_oq_offsets
                            max_pointers = 6 if is_monster_behaviour else None
                            max_pointers = 256 if (base_addr == 0x350202 or base_addr == 0x350002) else max_pointers
                            max_pointers = s.length // 2 if hasattr(s, 'length') and s.length is not None else max_pointers
                            tbl_ends_at = ((base_addr + (max_pointers * 2)) & 0xFFFF) if max_pointers is not None else 0x10000
                            while temp_cursor_addr_short < tbl_ends_at:
                                #print(f"{base_addr:06x} ends: {tbl_ends_at:06x}, {temp_cursor_addr_short:06x}, {i}")
                                cursor_points_to = shortify(rom, temp_cursor_addr)
                                known_addresses_covered[third_byte_as_string][temp_cursor_addr_short] = True
                                known_addresses_covered[third_byte_as_string][temp_cursor_addr_short + 1] = True
                                if cursor_points_to < tbl_ends_at:
                                    tbl_ends_at = cursor_points_to
                                #print("            reading base_iterator_addr", f"0x{temp_cursor_addr:06x}", "points to", f"0x{bank_as_upper_byte + cursor_points_to:06x}")
                                temp_cursor_addr += 2
                                temp_cursor_addr_short = temp_cursor_addr & 0xFFFF
                                amem = deepcopy(INIT_AMEM)
                                amem[0] = [i]
                                if label_override is None:
                                    label = ""
                                if i in s.relevant_indexes:
                                    amem = s.amem
                                    if label_override is None:
                                        label = s.label
                                ref = bank_as_upper_byte + cursor_points_to
                                validate_addr(ref, amem, label)
                                # if ref == 0x350336:
                                #     raise ValueError(f"found 0x350336 pointer in oq at 0x{s.addr:06x}, index {i}")
                                ptrs.append(ref)
                                i += 1
                                length += 2
                                # for monster behaviours, stop after exactly 6 pointers
                                if (max_pointers is not None and i >= max_pointers) or temp_cursor_addr in static_pointer_addresses_cache:
                                    end_found = True
                                    break
                                if not (temp_cursor_addr_short < tbl_ends_at):
                                    break
                            s.length = length
                            s.pointers = ptrs
                            #print([f"{ptr:06x}" for ptr in ptrs])
                        #print(end_found, length, f"{base_addr:06x}")
                        return length

                    # get the bytes for whatever command begins at current_addr.
                    # check first if this is the start of an oq pointer table. add branches if so, and mark table range as used.
                    #print(f"        cursor at 0x{cursor:06x}")
                    if cursor in [s.addr for s in oq_starts]:
                        s = next((s for s in oq_starts if s.addr == cursor), None)
                        if not s:
                            raise ValueError("how did you get here?")
                        #print("        this is a one-tier oq")
                        length = create_object_queue(s.addr)
                        
                    elif cursor in [s.addr for s in oq_idx_starts]:
                        is_ally_queue = cursor == 0x350002
                        #print("        this is a two-tier oq")
                        complex_oq = next((s for s in oq_idx_starts if s.addr == cursor), None)
                        if not complex_oq:
                            raise ValueError("how did you get here?")
                        tbl_ends_at = 0x10000
                        cursor_short = cursor & 0xFFFF
                        baddr = cursor
                        i = 0
                        if not hasattr(complex_oq, "pointers"):
                            complex_oq.pointers = []
                        #print(cursor_short)
                        length = 0
                        while cursor_short < tbl_ends_at:
                            length += 2
                            #print(f"            coq: reading at 0x{cursor:06x}, ends at {tbl_ends_at:06x}, index {i}")
                            # figure out where every basic oq in the complex oq starts
                            # by iterating through short pointers until we hit the start of a basic oq
                            # complex_oq.relevant_indexes is relevant INDEXES, aka relevant values of amem $60
                            #print(complex_oq.relevant_indexes)
                            if i in complex_oq.relevant_indexes:
                                # relevant indexes are ones that we know are actually referenced by a script
                                # and therefore need to carry possible amem values and a label
                                # other indexes are probably unused but we should know them if they are parts of oqs
                                amem = complex_oq.amem
                                label = complex_oq.label
                            else:
                                amem = deepcopy(INIT_AMEM)
                                amem[0] = [i]
                                label = ""
                            #print(amem)
                            # if this basic oq is a lower pointer than any others, it's probably where the complex oq table ends
                            cursor_points_to = shortify(rom, cursor)
                            if cursor_points_to < tbl_ends_at:
                                tbl_ends_at = cursor_points_to
                            # we know these bytes are used because they point to a basic oq
                            known_addresses_covered[third_byte_as_string][cursor_short] = True
                            known_addresses_covered[third_byte_as_string][cursor_short + 1] = True
                            # add a branch to the branch array for the basic oq
                            # relevant indexes based on the amem being passed in
                            relevant_indexes = list(set([x for sub in amem for x in sub]))
                            pointed_addr = bank_as_upper_byte + cursor_points_to
                            ref = OQRef(pointed_addr, amem, relevant_indexes, label)
                            if is_ally_queue:
                                ref.length = 16
                            oq_starts.append(ref)
                            #print(f"about to validate {pointed_addr:06x} from complex oq at 0x{cursor:06x} with amem", amem, "and relevant indexes", relevant_indexes)
                            validate_addr(pointed_addr, amem, label)
                            complex_oq.pointers.append(pointed_addr)
                            # parse the basic oq to add its branches
                            #print("        reading at 0x%06x: points to 0x%04x" % (cursor, shortify(rom, cursor)))
                            if this_branch.offset == BATTLE_EVENT_INDEXES_START_AT:
                                battle_event_index = (cursor - BATTLE_EVENT_INDEXES_START_AT) // 2
                                label = SCRIPT_NAMES["battle_events"][battle_event_index]
                                create_object_queue(pointed_addr, label_override=label)
                            elif this_branch.offset == UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT:
                                #print(f"cursor: 0x{cursor:06x}, base to: 0x{UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT:06x}")
                                label = f"unknown_battle_event_adjacent"
                                create_object_queue(pointed_addr, label_override=label)
                            else:
                                create_object_queue(pointed_addr)
                            cursor += 2
                            cursor_short = cursor & 0xFFFF
                            i += 1
                        complex_oq.length = length
                        end_found = True
                        #print(f"        complex oq length: {length} bytes")
                    else:

                        #print(f"        now cursor at 0x{cursor:06x}")
                        #print(f"        processing command at 0x{cursor:06x}")

                        opcode = rom[cursor]
                        length = command_lens[opcode]
                        #print(f'            opcode: {opcode:02x}, cursor: 0x{cursor:06x}, length: {length}, data: {" ".join([f"0x{b:02x}" for b in rom[cursor:cursor+length]])}, {this_branch.ref_label} ({this_branch.referenced_by})')
                        if opcode == 0xC6:
                            length = rom[cursor + 1] + 2
                        elif opcode == 0xBA:    
                            length = rom[cursor + 1] * 2 + 2
                        command = rom[cursor : cursor + length]
                        cvr_range = cursor & 0xFFFF

                        if command == bytearray([0,0,0,0,0,0,0,0,0]):
                            end_found = True
                            break
                        # Flag each byte in the command as "used", as in we know some script definitely accesses it
                        for tok_output in range(cvr_range, cvr_range + length):
                            known_addresses_covered[third_byte_as_string][tok_output] = True

                        # if this is a command that changes amem $60-$6f, or could change them, we need to keep track of what its possible values could be in case an amem-based object queue comes up.
                        if opcode in [0x20, 0x21]:  # set amem 8 bit to...
                            if command[1] & 0xF0 == 0x30:  # copy
                                src = command[2] & 0x0F
                                dst = command[1] & 0x0F
                                amem[dst] = amem[src]
                            elif command[1] & 0xF0 == 0x00 and command[1] <= 0x0F:  # const
                                amem[command[1]] = [shortify(command, 2)]
                            # impossible to evaluate other value sources
                        elif (
                            opcode in [0x22, 0x23] and command[1] & 0xF0 == 0x30
                        ):  # copy, other way around
                            dst = command[2] & 0x0F
                            src = command[1] & 0x0F
                            amem[dst] = amem[src]
                        elif opcode in [0x2C, 0x2D]:  # inc
                            if command[1] & 0xF0 == 0x30:  # by amem
                                index1 = command[2] & 0x0F
                                index2 = command[1] & 0x0F
                                consolidated: list[int] = []
                                for x in amem[index2]:
                                    for y in amem[index1]:
                                        consolidated.append(x + y)
                                # Apply widening to prevent state explosion
                                amem[index2] = widen_amem_slot(list(set(consolidated)))
                            elif (
                                command[1] & 0xF0 == 0x00 and command[1] <= 0x0F
                            ):  # by const
                                amem[command[1]] = widen_amem_slot(list(
                                    set(
                                        [
                                            (a + shortify(command, 2))
                                            for a in amem[command[1]]
                                        ]
                                    )
                                ))
                        elif opcode in [0x2E, 0x2F]:  # dec
                            if command[1] & 0xF0 == 0x30:  # by amem
                                index1 = command[2] & 0x0F
                                index2 = command[1] & 0x0F
                                consolidated: list[int] = []
                                for x in amem[index2]:
                                    for y in amem[index1]:
                                        consolidated.append(max(0, x - y))
                                # Apply widening to prevent state explosion
                                amem[index2] = widen_amem_slot(list(set(consolidated)))
                            elif (
                                command[1] & 0xF0 == 0x00 and command[1] <= 0x0F
                            ):  # by const
                                amem[command[1]] = widen_amem_slot(list(
                                    set(
                                        [
                                            max(0, a - shortify(command, 2))
                                            for a in amem[command[1]]
                                        ]
                                    )
                                ))
                        elif opcode in [0x30, 0x31] and command[1] <= 0x0F:
                            amem[command[1]] = list(set([a + 1 for a in amem[command[1]]]))
                        elif opcode in [0x32, 0x33] and command[1] <= 0x0F:
                            amem[command[1]] = list(set([a - 1 for a in amem[command[1]]]))
                        elif opcode in [0x34, 0x35] and command[1] <= 0x0F:
                            amem[command[1]] = [0]
                        elif opcode in [0x6A, 0x6B] and command[1] <= 0x0F:
                            # Critical: this can create large ranges that explode during inc/dec
                            # Apply widening immediately to prevent 60,000+ branch explosions
                            amem[command[1]] = widen_amem_slot(list(range(command[2])))

                        amem_was = deepcopy(amem)

                        # if this command includes a goto, need to add the destinations to the branch array and process them separately
                        if opcode in jmp_cmds or opcode in jmp_cmds_1:
                            if opcode in jmp_cmds_1:
                                address_byte = command[-3:-1]
                            else:
                                address_byte = command[-2:]

                            branch_addr = (
                                bank_as_upper_byte
                                + (address_byte[1] << 8)
                                + address_byte[0]
                            )

                            if branch_addr == 0x35053C:
                                # experimental: reroute jump that goes to partway through command in the original game
                                # and change it to point to another instance of 0x02 instead
                                # which is treated as terminating
                                branch_addr = 0x350532

                            # which of amem $60-$6f are part of the branch condition? ie if amem $64 bit 1 = ... then ...
                            # clean up what the amems can be at the target branch, and then add it to the array.
                            # only really tracking constants and other amem. not really possible to track $7exxxx and $7fxxxx or omem
                            important_amem_indexes = [0]

                            if opcode in [0x24, 0x25]:  # if amem =
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                var_type = (command[1] & 0xF0) >> 4
                                if var_type == 0:
                                    amem[index1] = [shortify(command, 2)]
                                elif var_type == 3:
                                    index2 = command[2] & 0x0F
                                    amem[index1] = amem[index2]
                            elif opcode in [0x26, 0x27]:  # if amem !=
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                var_type = (command[1] & 0xF0) >> 4
                                if var_type == 0:
                                    amem[index1] = [a for a in amem[index1] if a != shortify(command, 2)]
                                elif var_type == 3:
                                    index2 = command[2] & 0x0F
                                    if amem[index1] == amem[index2]:
                                        amem[index1] = []
                            elif opcode in [0x28, 0x29]:  # if amem <
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                var_type = (command[1] & 0xF0) >> 4
                                if var_type == 0:
                                    amem[index1] = [a for a in amem[index1] if a < shortify(command, 2)]
                                elif var_type == 3:
                                    index2 = command[2] & 0x0F
                                    amem[index1] = [a for a in amem[index1] if a < max([0] if not amem[index2] else amem[index2])]
                            elif opcode in [0x2A, 0x2B]:  # if amem >=
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                var_type = (command[1] & 0xF0) >> 4
                                if var_type == 0:
                                    amem[index1] = [a for a in amem[index1] if a >= shortify(command, 2)]
                                elif var_type == 3:
                                    index2 = command[2] & 0x0F
                                    amem[index1] = [a for a in amem[index1] if a >= max([0] if not amem[index2] else amem[index2])]
                            elif opcode == 0x38:  # if amem bits set
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                amem[index1] = [a for a in amem[index1] if a & command[2] == command[2]]
                            elif opcode == 0x39:  # if amem bits clear
                                index1 = command[1] & 0x0F
                                important_amem_indexes.append(index1)
                                amem[index1] = [a for a in amem[index1] if ~a & command[2] == command[2]]
                            elif opcode == 0x64 or opcode == 0x47:  # object queue, command index = amem 60 or experimental
                                oq_starts.append(OQRef(branch_addr, amem, amem[0], this_branch.ref_label))
                            elif (
                                opcode == 0x68
                            ):  # object queue, pointer table index = amem $60, command index is an arg
                                oq_idx_starts.append(OQRef(branch_addr, amem, amem[0], this_branch.ref_label))

                            # if branch_addr == 0x350336:
                            #     raise ValueError(f"found 0x350336 pointer at 0x{cursor:06x}")
                            validate_addr(branch_addr, amem, important_amem_indexes_raw=important_amem_indexes)

                            amem = deepcopy(amem_was)

                        # terminating conditions
                        if opcode in TERMINATING_OPCODES:
                            end_found = True

                    # Battle events region termination
                    if 0x3A0000 <= cursor + length < 0x3A60D0:
                        end_found = True

                    # if not terminated, move on to the next command
                    cursor += length
                    #print(f"        moving cursor to 0x{cursor:06x}, {end_found}")
                    # if cursor == 0x350336:
                    #     raise ValueError(f"found 0x350336 pointer at {this_branch}")
                #print(f"        broken at 0x{cursor:06x}, {end_found}")
                #print("")

                # move on to the next branch
                branch_index += 1
                if branch_index >= len(branches):
                    break
                this_branch = branches[branch_index]

        #print("done tracing branches, collecting data...")
        # collect contiguous known bytes
        used: dict[str, list[ContiguousBlock]] = {
            "02": [],
            "35": [],
            "3A": [],
        }

        for bank_id, bank_contents in known_addresses_covered.items():
            # bank_name: str (02, 35, 3a)
            # bank_contents: list[bool] (0x10000 length)
            started: int | None = None
            upper = (int(bank_id, 16)) << 16
            # upper: 0x020000, 0x350000, 0x3a0000
            for index, value in enumerate(bank_contents):
                # index: 4 digit rom position
                # value: used or not
                absolute_offset = upper + index

                # check if we need to break the block at a static pointer address
                if started is not None and value and absolute_offset in static_pointer_addresses_cache:
                    # end the current block and start a new one
                    used[bank_id].append(ContiguousBlock(started + upper, rom[(upper+started):(upper+index)]))
                    started = index  # Start new block at current position
                elif value and started is None:
                    started = index
                    # started: 4 digit rom position at which current block started
                elif started is not None and not value:
                    used[bank_id].append(ContiguousBlock(started + upper, rom[(upper+started):(upper+index)]))
                    started = None
            if started is not None:
                used[bank_id].append(ContiguousBlock(started + upper, rom[(upper+started):(upper+0x10000)]))

        # turn contiguous blocks into proto-commands
        for bank_id, blocks in used.items():
            data: list[list[ProtoCommand]] = []
            for block in blocks:
                #print(f'block.start, block.end: 0x{block.start:06x}, 0x{block.end:06x} (size {block.size})')
                split_block = tok(
                    rom, block.start, block.end, oq_starts, oq_idx_starts
                )
                offset_within_block = 0
                this_script: list[ProtoCommand] = []
                debug = True if block.start <= 0x350462 < block.end else False
                for tok_output in split_block:
                    #print(tok_output)
                    absolute_offset = block.start + offset_within_block
                    #if debug:
                        #print(f"0x{absolute_offset:06x}: {' '.join([f'0x{b:02x}' for b in tok_output[0]])}")
                    identifier = f"command_0x{absolute_offset:06X}"

                    # Check for special naming cases
                    # 1. Check if this is the ally behaviour pointers table
                    if absolute_offset == 0x350002:
                        identifier = "ally_behaviour_pointers"
                    # 2. Check if this is the monster sprite behaviour pointers table
                    elif absolute_offset == 0x350202:
                        identifier = "monster_sprite_behaviour_pointers"
                    # 3. Check if this is a monster behaviour offset
                    elif absolute_offset in monster_behaviour_oq_offsets:
                        behaviour_index = monster_behaviour_oq_offsets.index(absolute_offset)
                        behaviour_name = monster_behaviour_names[behaviour_index]
                        identifier = f"monster_sprite_behaviour_{behaviour_index}_{behaviour_name}"
                    # 4. Check if this is a battle event command
                    elif absolute_offset in battle_event_addr_to_name:
                        identifier = battle_event_addr_to_name[absolute_offset]
                    # 5. Check for monster entrances
                    elif absolute_offset in monster_entrance_offsets:
                        identifier = f"monster_entrance_{monster_entrance_offsets.index(absolute_offset)}"
                    # 6. Check for branch labels
                    else:
                        possible_rename = [b.ref_label for b in branches if b.offset == absolute_offset and b.ref_label != ""]
                        if len(possible_rename) > 0:
                            identifier = f"{possible_rename[0].lower().replace(" ", "_").replace("-", "_")}_0x{absolute_offset:06X}"
                    named_proto_command = ProtoCommand(identifier, absolute_offset, tok_output[0], tok_output[2], len(tok_output[0]))
                    this_script.append(named_proto_command)
                    #print(f'    parsed command {named_proto_command}')
                    offset_within_block += len(tok_output[0])
                data.append(this_script)
            #print(data)
            collective_data[bank_id].extend(data)

        # associate jump pointers with command ids
        for bank_id, script in collective_data.items():

            third_byte_as_string = bank_id.lower()

            # when reassembling battle scripts: before each script body, need to insert 2 bytes
            # that are a pointer to its own start
            # ie: values in pointer bank @ 3a6004 for script 0: 0xd0 0x60
            # actual value at 3a60d0: 0xd2 0x60
            # actual script 0 begins at 3a60d2

            # replace jump addresses with ids if in the same bank
            for index, commands in enumerate(script):
                for cmd_index, command in enumerate(commands):
                    address_data = None
                    if command.oq:
                        address_data = deepcopy(command.raw_data)
                        #print(f"oq addr data at 0x{command.addr:06X}: ", [f"0x{b:02x}" for b in address_data])
                        del command.raw_data[0:]
                    elif (
                        command.raw_data[0] in jmp_cmds_1
                    ):
                        address_data = command.raw_data[-3:-1]
                        del command.raw_data[-3:-1]
                    elif (
                        command.raw_data[0] in jmp_cmds
                    ):
                        address_data = command.raw_data[-2:]
                        del command.raw_data[-2:]
                        #print(2)
                    #print(address_data)

                    if address_data is None:
                        continue

                    addresses: list[list[int]] = np.array(address_data).reshape(-1, 2)
                    #print("")
                    #print(addresses)
                    for address in addresses:
                        #print(address)
                        dest = (
                            (command.addr & 0xFF0000)
                            + (int(address[1]) << 8)
                            + int(address[0])
                        )

                        found = None
                        # experiment
                        if dest == 0x35053C:
                            address[0] = 0x32
                            address[1] = 0x05
                            dest = 0x350532
                        for search_script in script:
                            for search_command in search_script:
                                #print(f'searching for 0x{dest:06X}, checking command {search_command.id} at 0x{search_command.addr:06X}')
                                if search_command.addr == dest:
                                    found = search_command.id
                                    break
                            if found is not None:
                                break
                        if found is not None:
                            command.parsed_data.append(found)
                            jump_pointers.append(found)
                        else:
                            raise Exception(f"couldn't find jump target 0x{dest:06x} targeted by "f"command {command} {command.id} at 0x{command.addr:06x}")

                        script[index][cmd_index].raw_data = command.raw_data
        
        # Deduplicate scripts by starting address and enforce boundaries
        # based on POINTER_MUST_REMAIN_STATIC
        script_boundaries = compute_script_boundaries()
        static_addresses = static_pointer_addresses_cache  # Use cached set

        for bank_id in collective_data.keys():
            # Deduplicate: keep only the first script for each starting address
            seen_addresses: set[int] = set()
            deduped: list[list[ProtoCommand]] = []
            for script in collective_data[bank_id]:
                if script and script[0].addr not in seen_addresses:
                    seen_addresses.add(script[0].addr)
                    deduped.append(script)
            collective_data[bank_id] = deduped

            # Merge scripts that are separated by known unused gaps
            # Sort scripts by starting address first
            collective_data[bank_id].sort(key=lambda s: s[0].addr if s else 0)
            merged_scripts: list[list[ProtoCommand]] = []
            i = 0
            while i < len(collective_data[bank_id]):
                current_script = collective_data[bank_id][i]
                if not current_script:
                    i += 1
                    continue

                # Check if there's a known gap after this script
                script_end = current_script[-1].addr + (current_script[-1].length or 0)
                gap_found = None
                for gap_start, gap_end in KNOWN_UNUSED_GAPS:
                    if script_end == gap_start:
                        gap_found = (gap_start, gap_end)
                        break

                if gap_found and i + 1 < len(collective_data[bank_id]):
                    next_script = collective_data[bank_id][i + 1]
                    if next_script and next_script[0].addr == gap_found[1]:
                        # Merge: current_script + filler for gap + next_script
                        gap_start, gap_end = gap_found
                        gap_size = gap_end - gap_start
                        filler = ProtoCommand(
                            f"unused_gap_0x{gap_start:06X}",
                            gap_start,
                            rom[gap_start:gap_end],
                            oq=False,
                            length=gap_size
                        )
                        merged = current_script + [filler] + next_script
                        merged_scripts.append(merged)
                        i += 2  # Skip both scripts
                        continue

                merged_scripts.append(current_script)
                i += 1
            collective_data[bank_id] = merged_scripts

            # Enforce script size limits based on boundaries
            for script in collective_data[bank_id]:
                if not script:
                    continue
                script_start = script[0].addr
                # Find the next static pointer in the same bank
                same_bank_addrs = sorted([a for a in static_addresses if (a >> 16) == (script_start >> 16) and a > script_start])
                if same_bank_addrs:
                    max_end = same_bank_addrs[0]
                    # Truncate script if it extends beyond the boundary
                    truncated_script: list[ProtoCommand] = []
                    current_end = script_start
                    for cmd in script:
                        cmd_end = cmd.addr + (cmd.length or 0)
                        if cmd_end <= max_end:
                            truncated_script.append(cmd)
                            current_end = cmd_end
                        else:
                            # Truncate at boundary
                            break
                    script.clear()
                    script.extend(truncated_script)

        for bank_id, blocks in collective_data.items():
            #print(f"exporting {bank_id}...")

            export_dest = f"{output_path}/{bank_id}"
            os.makedirs(export_dest, exist_ok=True)

            open(f"{export_dest}/__init__.py", "w")
            export_file = open("%s/export.py" % export_dest, "w")

            import_body = ""
            export_body = ""

            # when reassembling battle scripts: before each script body, need to insert 2 bytes
            # that are a pointer to its own start
            # ie: values in pointer bank @ 3a6004 for script 0: 0xd0 0x60
            # actual value at 3a60d0: 0xd2 0x60
            # actual script 0 begins at 3a60d2

            # Prepare output directory structure
            dest = f"{output_path}/{bank_id}"
            os.makedirs(f"{dest}/contents", exist_ok=True)
            open(f"{dest}/__init__.py", "w")
            open(f"{dest}/contents/__init__.py", "w")

            # Parallel processing of scripts within this bank
            def write_script_file(script_idx, script):
                script_alias = f"script_0x{script[0].addr:06X}"
                file_path = f"{dest}/contents/{script_alias}.py"

                size = sum([c.length for c in script])

                output = "# pyright: reportWildcardImportFromLibrary=false"
                output += "\nfrom smrpgpatchbuilder.datatypes.battle_animation_scripts import *"

                # Add imports from disassembler_output - variables
                output += "\nfrom ....variables.sprite_names import *"
                output += "\nfrom ....variables.music_names import *"
                output += "\nfrom ....variables.battle_sfx_names import *"
                output += "\nfrom ....variables.battle_effect_names import *"
                output += "\nfrom ....variables.battle_event_names import *"
                output += "\nfrom ....variables.screen_effect_names import *"
                output += "\nfrom ....spells.spells import *"
                output += "\nfrom ....items.items import *"
                output += "\nfrom ....enemies.enemies import *"
                output += "\nfrom ....enemy_attacks.attacks import *"
                output += "\nfrom smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *"

                output += f"\n\nscript = AnimationScriptBlock(expected_size={size}, expected_beginning=0x{script[0].addr:06X}, script=[\n\t"

                contents = get_script(script, jump_pointers)

                output += ",\n\t".join(contents)

                output += "\n])"

                with open(file_path, "w") as file:
                    writeline(file, output)

                # Return data needed for export file
                return (script_idx, script_alias)

            # Execute script writing in parallel
            num_workers = min(multiprocessing.cpu_count(), len(blocks))
            script_results = []
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                futures = [executor.submit(write_script_file, idx, script)
                          for idx, script in enumerate(blocks)]
                for future in as_completed(futures):
                    script_results.append(future.result())

            # Sort results by original index to maintain order
            script_results.sort(key=lambda x: x[0])

            # Build import and export bodies from results
            for _, script_alias in script_results:
                import_body += "\nfrom .contents.%s import script as %s" % (
                    script_alias,
                    script_alias,
                )
                export_body += "\n\t\t%s," % script_alias
            export_output = "from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBank"
            export_output += import_body
            export_output += "\n\nbank = AnimationScriptBank("
            export_output += "\n\tname = \"0x%s\"," % bank_id.upper()
            export_output += "\n\tscripts = ["
            export_output += export_body

            export_output += "\n\t]"
            export_output += "\n)"
            writeline(export_file, export_output)

        # Generate bank usage visualization
        self._write_bank_usage_visualization(output_path, known_addresses_covered)

        self.stdout.write(self.style.SUCCESS("Successfully disassembled battle animation scripts to ./src/disassembler_output/battle_animation/"))

    def _write_bank_usage_visualization(self, output_path: str, known_addresses_covered: dict[str, list[bool]]):
        """Write ASCII visualization of bank usage to a file.

        Args:
            output_path: Base output directory
            known_addresses_covered: Dict mapping bank ID to list of booleans indicating byte usage
        """
        # ANSI color codes for terminal output
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'

        usage_file_path = f"{output_path}/bank_usage.txt"

        with open(usage_file_path, "w", encoding="utf-8") as f:
            f.write("Bank Usage Visualization\n")
            f.write("=" * 80 + "\n")
            f.write("Legend: █ = used (green), █ = unused (red)\n")
            f.write("Each row shows 16 bytes\n\n")

            for bank_id in sorted(known_addresses_covered.keys()):
                bank_contents = known_addresses_covered[bank_id]
                bank_base = int(bank_id, 16) << 16

                # Find the range of used addresses
                first_used = None
                last_used = None
                for i, used in enumerate(bank_contents):
                    if used:
                        if first_used is None:
                            first_used = i
                        last_used = i

                if first_used is None:
                    # No addresses used in this bank
                    f.write(f"Bank 0x{bank_id}: No addresses used\n\n")
                    continue

                # Align to 16-byte boundaries
                start_addr = (first_used // 16) * 16
                end_addr = ((last_used // 16) + 1) * 16

                f.write(f"Bank 0x{bank_id}: 0x{bank_base + first_used:06X} - 0x{bank_base + last_used:06X}\n")
                f.write("-" * 80 + "\n")

                # Generate visualization
                for addr in range(start_addr, end_addr, 16):
                    # Write address
                    f.write(f"0x{bank_base + addr:06X} ")

                    # Write 16 blocks
                    for offset in range(16):
                        byte_addr = addr + offset
                        if byte_addr < len(bank_contents) and bank_contents[byte_addr]:
                            f.write(f"{GREEN}█{RESET}")
                        else:
                            f.write(f"{RED}█{RESET}")

                    # Calculate and show usage percentage for this row
                    used_count = sum(1 for offset in range(16)
                                   if (addr + offset) < len(bank_contents)
                                   and bank_contents[addr + offset])
                    percentage = (used_count / 16) * 100
                    f.write(f" {used_count:2d}/16 ({percentage:5.1f}%)")

                    f.write("\n")

                # Calculate overall usage for this bank
                total_in_range = end_addr - start_addr
                used_in_range = sum(1 for i in range(start_addr, end_addr)
                                  if i < len(bank_contents) and bank_contents[i])
                overall_percentage = (used_in_range / total_in_range) * 100 if total_in_range > 0 else 0

                f.write(f"\nBank 0x{bank_id} overall usage: {used_in_range}/{total_in_range} bytes ({overall_percentage:.1f}%)\n")
                f.write("\n" + "=" * 80 + "\n\n")

        self.stdout.write(f"Bank usage visualization written to {usage_file_path}")

# empty space filler: 0x11

# screen flash none = 2 bytes {0x8f 0x00}
# screen flash none 0 frames = 3 bytes {0x8f 0x00 0x00}

# theoretically, could we have multiple battle events for walking on kc/cd depending on # of party members,
# and battle logic picks which of the 3 to run?
# maybe that's worth disassembling for
# figure out which battle events are unused somehow

# also need to make solo crystal battle events

# also need to da battle text to not deadname birdetta
