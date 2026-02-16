from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.levels.classes import *
from smrpgpatchbuilder.utils.disassembler_common import (
    shortify,
    writeline,
    bit_bool_from_num,
)
import shutil, os
from .input_file_parser import load_arrays_from_input_files

# Build lookup dictionaries from the imported name modules

start = 0x148400
end = 0x14FFFF
ptrstart = 0x148000
ptrend = 0x1483FF

roomevent_start = 0x20E400
roomevent_end = 0x20FFFF  # might be 0x20fdc7
roomevent_ptrstart = 0x20E000
roomevent_ptrend = 0x20E3FF

roomexit_start = 0x1D3166
roomexit_end = 0x1D4904
roomexit_ptrstart = 0x1D2D64
roomexit_ptrend = 0x1D3165

partitionstart = 0x1DDE00
partitionend = 0x1DDFFF  # bumped up from 0x1ddfdf

npctable_start = 0x1DB800
npctable_end_standard = 0x1DDDFF
npctable_end_extended = 0x1DDFFF

directions = [
    "EAST",
    "SOUTHEAST",
    "SOUTH",
    "SOUTHWEST",
    "WEST",
    "NORTHWEST",
    "NORTH",
    "NORTHEAST",
]

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

        parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer",
        )

        parser.add_argument(
            "--large-partition-table",
            dest="large_partition_table",
            action="store_true",
            help="If true, will read 512 partitions from 0x1DEBE0 instead of 120 partitions from 0x1DDE00. Only use this if you've changed your ROM to use this range already.",
        )

    def _write_npcs_file(self, dest: str, npc_classes: list[NPC], npc_variable_names: dict[int, str], sprite_names_array: list[str]):
        """Write all NPCs to a single file with proper variable names."""
        import os
        os.makedirs(dest, exist_ok=True)

        file = open(f"{dest}/npcs.py", "w", encoding="utf-8")
        writeline(file, "from smrpgpatchbuilder.datatypes.levels.classes import NPC, ShadowSize, VramStore")
        writeline(file, "from ..variables.sprite_names import *")
        writeline(file, "")

        for npc_index, npc in enumerate(npc_classes):
            var_name = npc_variable_names[npc_index]
            writeline(file, f"{var_name} = NPC(")
            # Use sprite name from array, falling back to numeric ID if not found
            sprite_name = sprite_names_array[npc.sprite_id] if npc.sprite_id < len(sprite_names_array) and sprite_names_array[npc.sprite_id] else str(npc.sprite_id)
            writeline(file, f"    sprite_id={sprite_name},")
            writeline(file, f"    shadow_size=ShadowSize.{npc.shadow_size.name},")
            writeline(file, f"    acute_axis={npc.acute_axis},")
            writeline(file, f"    obtuse_axis={npc.obtuse_axis},")
            writeline(file, f"    height={npc.height},")
            writeline(file, f"    y_shift={npc.y_shift},")
            writeline(file, f"    show_shadow={npc.show_shadow!r},")
            writeline(file, f"    directions=VramStore.{npc.directions.name},")
            writeline(file, f"    min_vram_size={npc.min_vram_size},")
            writeline(file, f"    priority_0={npc.priority_0!r},")
            writeline(file, f"    priority_1={npc.priority_1!r},")
            writeline(file, f"    priority_2={npc.priority_2!r},")
            writeline(file, f"    cannot_clone={npc.cannot_clone!r},")
            writeline(file, f"    byte2_bit0={npc.byte2_bit0!r},")
            writeline(file, f"    byte2_bit1={npc.byte2_bit1!r},")
            writeline(file, f"    byte2_bit2={npc.byte2_bit2!r},")
            writeline(file, f"    byte2_bit3={npc.byte2_bit3!r},")
            writeline(file, f"    byte2_bit4={npc.byte2_bit4!r},")
            writeline(file, f"    byte5_bit6={npc.byte5_bit6!r},")
            writeline(file, f"    byte5_bit7={npc.byte5_bit7!r},")
            writeline(file, f"    byte6_bit2={npc.byte6_bit2!r},")
            writeline(file, ")")
            writeline(file, "")

        file.close()
        self.stdout.write(self.style.SUCCESS(f"Successfully wrote {len(npc_classes)} NPCs to {dest}/npcs.py"))

    def handle(self, *args, **options):
        debug = options["debug"]
        large_partition_table = options["large_partition_table"]

        # Load all name arrays from input files
        varnames = load_arrays_from_input_files()
        sprite_names_array = varnames.get("sprites", [])
        room_names_array = varnames.get("rooms", [])
        music_names_array = varnames.get("music", [])
        event_script_names_array = varnames.get("event_scripts", [])
        action_script_names_array = varnames.get("action_scripts", [])
        area_names_array = varnames.get("areas", [])

        # Build lookup dictionaries from arrays (id -> name)
        def build_id_to_name(arr):
            return {i: name for i, name in enumerate(arr) if name}

        room_id_to_name = build_id_to_name(room_names_array)
        music_id_to_name = build_id_to_name(music_names_array)
        event_script_id_to_name = build_id_to_name(event_script_names_array)
        action_script_id_to_name = build_id_to_name(action_script_names_array)
        location_id_to_name = build_id_to_name(area_names_array)

        # Create output directory
        dest = "./src/disassembler_output/rooms"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        open(f"{dest}/__init__.py", "w").close()

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        rooms_raw_data = []
        roomevent_raw_data = []
        roomexit_raw_data = []
        partitions = []

        ptrs = []
        roomevent_ptrs = []
        roomexit_ptrs = []

        # First pass: scan all rooms to find which NPC IDs are actually used
        used_npc_indices = set()

        # Scan room objects to find used NPCs
        for room_idx in range(512):
            ptr_offset = ptrstart + (room_idx * 2)
            room_ptr = shortify(rom, ptr_offset)
            room_offset = start + room_ptr

            if room_offset >= end:
                continue

            # Skip partition byte
            cursor = room_offset + 1

            # Process room objects
            while cursor < end:
                if rom[cursor] == 0xFF:  # End marker
                    break

                obj_type = rom[cursor] >> 4
                if obj_type == 0xFF:
                    break

                # Check if it's a parent object (12 bytes) or clone (4 bytes)
                if cursor + 12 <= end and (rom[cursor] & 0x0F) >= 0:
                    # Parent object - extract NPC index
                    base_assigned_npc = ((rom[cursor + 4] & 0x0F) << 6) + (rom[cursor + 3] >> 2)
                    npc_offset_in_byte8 = rom[cursor + 8] & 0x07

                    if obj_type == 0:  # Regular NPC
                        assigned_npc = base_assigned_npc + npc_offset_in_byte8
                    else:  # Chest or Battle
                        assigned_npc = base_assigned_npc

                    used_npc_indices.add(assigned_npc)

                    # Process clones if any
                    extra_length = rom[cursor] & 0x0F
                    cursor += 12

                    for _ in range(extra_length):
                        if cursor + 4 <= end:
                            clone_offset = rom[cursor] & 0x07
                            clone_npc = base_assigned_npc + clone_offset
                            used_npc_indices.add(clone_npc)
                            cursor += 4
                        else:
                            break
                else:
                    break

        # Determine NPC table end based on partition table size
        npctable_end = npctable_end_extended if large_partition_table else npctable_end_standard

        npc_classes: list[NPC] = []
        npc_variable_names: dict[int, str] = {}  # Maps NPC index to variable name
        sprite_usage_count: dict[int, int] = {}  # Tracks how many NPCs use each sprite

        i = 0
        for offset in range(npctable_start, npctable_end + 1, 7):
            if offset + 7 > npctable_end:
                break

            npc_index = (offset - npctable_start) // 7
            raw_data = rom[offset : (offset + 7)]

            # Skip NPCs that are all 0xFF unless they're used in a room
            if raw_data == bytearray([0xFF] * 7):
                if npc_index not in used_npc_indices:
                    continue
            sprite_val = ((raw_data[1] << 8) | raw_data[0]) & 0x03FF
            vram_store_val = (raw_data[1] >> 2) & 0x07
            vram_size = raw_data[1] >> 5
            priority0 = (raw_data[2] & 0x20) == 0x20  # bit 5
            priority1 = (raw_data[2] & 0x40) == 0x40  # bit 6
            priority2 = (raw_data[2] & 0x80) == 0x80  # bit 7
            byte2_bit0 = (raw_data[2] & 0x01) == 0x01  # bit 0
            byte2_bit1 = (raw_data[2] & 0x02) == 0x02  # bit 1
            byte2_bit2 = (raw_data[2] & 0x04) == 0x04  # bit 2
            byte2_bit3 = (raw_data[2] & 0x08) == 0x08  # bit 3
            byte2_bit4 = (raw_data[2] & 0x10) == 0x10  # bit 4
            y_pixel_shift = raw_data[3] & 0x0F
            shift_16_px_down = (raw_data[3] & 0x10) == 0x10  # bit 4
            shadow_val = (raw_data[3] & 0x60) >> 5
            cannot_clone = (raw_data[3] & 0x80) == 0x80  # bit 7
            acute_axis = raw_data[4] & 0x0F
            obtuse_axis = (raw_data[4] & 0xF0) >> 4

            height = raw_data[5] & 0x1F
            show_shadow = (raw_data[5] & 0x20) == 0x20  # bit 5
            byte5_bit6 = (raw_data[5] & 0x40) == 0x40  # bit 6
            byte5_bit7 = (raw_data[5] & 0x80) == 0x80  # bit 7

            byte6_bit2 = (raw_data[6] & 0x04) == 0x04  # bit 2

            y_pixel_shift = y_pixel_shift + (-16 if shift_16_px_down else 0)

            i += 1

            npc = NPC(
                sprite_val,
                ShadowSize(shadow_val),
                acute_axis,
                obtuse_axis,
                height,
                y_pixel_shift,
                show_shadow,
                VramStore(vram_store_val),
                vram_size,
                priority0,
                priority1,
                priority2,
                cannot_clone,
                byte2_bit0,
                byte2_bit1,
                byte2_bit2,
                byte2_bit3,
                byte2_bit4,
                byte5_bit6,
                byte5_bit7,
                byte6_bit2,
            )

            # Generate variable name based on sprite name from input files
            sprite_name_full = sprite_names_array[sprite_val]
            # Remove the SPRxxxx_ prefix to get the descriptive name
            sprite_name = sprite_name_full.split('_', 1)[1] if '_' in sprite_name_full else sprite_name_full

            # Track usage count for this sprite
            sprite_usage_count[sprite_val] = sprite_usage_count.get(sprite_val, 0) + 1
            usage_count = sprite_usage_count[sprite_val]

            # Generate variable name: SpriteName_NPC or SpriteName_NPC_2, SpriteName_NPC_3, etc.
            if usage_count == 1:
                var_name = f"{sprite_name}_NPC"
            else:
                var_name = f"{sprite_name}_NPC_{usage_count}"

            npc_index = len(npc_classes)
            npc_variable_names[npc_index] = var_name
            npc_classes.append(npc)

        # Use larger partition table if flag is set
        actual_partition_start = 0x1DEBE0 if large_partition_table else partitionstart
        actual_partition_end = 0x1DF3DF if large_partition_table else partitionend
        for i in range(actual_partition_start, actual_partition_end, 4):
            partition_data = rom[i : i + 4]
            allow_extra_sprite_buffer = partition_data[0] & 0x10 == 0x10
            full_palette_buffer = partition_data[0] & 0x80 == 0x80
            ally_sprite_buffer_size = (partition_data[0] & 0x60) >> 5
            extra_sprite_buffer_size = partition_data[0] & 0x0F
            clone_buffer_a_type = partition_data[1] & 0x07
            clone_buffer_a_space = (partition_data[1] & 0x70) >> 4
            clone_buffer_a_index_in_main = partition_data[1] & 0x80 == 0x80
            clone_buffer_b_type = partition_data[2] & 0x07
            clone_buffer_b_space = (partition_data[2] & 0x70) >> 4
            clone_buffer_b_index_in_main = partition_data[2] & 0x80 == 0x80
            clone_buffer_c_type = partition_data[3] & 0x07
            clone_buffer_c_space = (partition_data[3] & 0x70) >> 4
            clone_buffer_c_index_in_main = partition_data[3] & 0x80 == 0x80
            partitions.append(
                Partition(
                    ally_sprite_buffer_size,
                    allow_extra_sprite_buffer,
                    extra_sprite_buffer_size,
                    [
                        Buffer(
                            BufferType(clone_buffer_a_type),
                            BufferSpace(clone_buffer_a_space),
                            clone_buffer_a_index_in_main,
                        ),
                        Buffer(
                            BufferType(clone_buffer_b_type),
                            BufferSpace(clone_buffer_b_space),
                            clone_buffer_b_index_in_main,
                        ),
                        Buffer(
                            BufferType(clone_buffer_c_type),
                            BufferSpace(clone_buffer_c_space),
                            clone_buffer_c_index_in_main,
                        ),
                    ],
                    full_palette_buffer,
                )
            )

        for i in range(ptrstart, ptrend, 2):
            ptrs.append((0x14 << 16) | (shortify(rom, i)))
        for i in range(roomevent_ptrstart, roomevent_ptrend, 2):
            roomevent_ptrs.append((0x20 << 16) | (shortify(rom, i)))
        for i in range(roomexit_ptrstart, roomexit_ptrend, 2):
            roomexit_ptrs.append((0x1D << 16) | (shortify(rom, i)))
        lengths = []
        roomevent_lengths = []
        roomexit_lengths = []

        # get raw data per room
        for i in range(len(ptrs)):
            if i < len(ptrs) - 1:
                lengths.append(ptrs[i + 1] - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : ptrs[i + 1]])
            else:
                lengths.append(end - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : end])
        for i in range(len(roomevent_ptrs)):
            if i < len(roomevent_ptrs) - 1:
                roomevent_lengths.append(roomevent_ptrs[i + 1] - roomevent_ptrs[i])
                roomevent_raw_data.append(
                    rom[roomevent_ptrs[i] : roomevent_ptrs[i + 1]]
                )
            else:
                roomevent_lengths.append(roomevent_ptrend - roomevent_ptrs[i])
                roomevent_raw_data.append(rom[roomevent_ptrs[i] : roomevent_ptrend])
        for i in range(len(roomexit_ptrs)):
            if i < len(roomexit_ptrs) - 1:
                roomexit_lengths.append(roomexit_ptrs[i + 1] - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_ptrs[i + 1]])
            else:
                roomexit_lengths.append(roomexit_end - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_end])

        if len(rooms_raw_data) < 511:
            raise Exception(
                "npc pointer table had %i entries (needs at least 511)"
                % len(rooms_raw_data)
            )
        if len(roomevent_raw_data) < 511:
            raise Exception(
                "event tile pointer table had %i entries (needs at least 511)"
                % len(roomevent_raw_data)
            )
        if len(roomexit_raw_data) < 511:
            raise Exception(
                "exit field pointer table had %i entries (needs at least 511)"
                % len(roomexit_raw_data)
            )

        # Write NPCs file before processing rooms
        self._write_npcs_file(dest, npc_classes, npc_variable_names, sprite_names_array)

        for i in range(len(rooms_raw_data)):
            d = rooms_raw_data[i]
            r = roomevent_raw_data[i]
            e = roomexit_raw_data[i]
            if i > 511:
                break
            if i > 509:
                d = []
                e = []

            file = open("%s/room_%i.py" % (dest, i), "w")

            # Write room name as comment at the top
            room_name = room_id_to_name.get(i, f"R{i:03d}_UNKNOWN")
            writeline(file, "# %s" % room_name)
            writeline(file, "# pyright: reportWildcardImportFromLibrary=false")

            writeline(
                file,
                "from smrpgpatchbuilder.datatypes.levels.classes import ObjectType, EventInitiator, PostBattleBehaviour, Direction, EdgeDirection, ExitType, BufferType, BufferSpace, VramStore, ShadowSize",
            )
            writeline(
                file,
                "from smrpgpatchbuilder.datatypes.levels.classes import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room",
            )
            writeline(
                file,
                "from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *",
            )
            # Import all NPCs from the npcs.py file in the same directory
            writeline(file, "from . import npcs")
            writeline(
                file,
                "from ..variables.room_names import *",
            )
            writeline(
                file,
                "from ..variables.overworld_area_names import *",
            )
            writeline(
                file,
                "from ..variables.music_names import *",
            )
            writeline(
                file,
                "from ..variables.event_script_names import *",
            )
            writeline(
                file,
                "from ..variables.action_script_names import *",
            )

            if len(d) == 0 and len(r) == 0 and len(e) == 0:
                writeline(file, "room = None")
                file.close()
                continue
            writeline(file, "room = Room(")

            # partition

            if len(d) == 0:
                partition = Partition()
            else:
                partition = partitions[d[0]]
            writeline(file, "    partition=Partition(")
            writeline(
                file,
                "        ally_sprite_buffer_size=%i,"
                % partition.ally_sprite_buffer_size,
            )
            writeline(
                file,
                "        allow_extra_sprite_buffer=%r,"
                % partition.allow_extra_sprite_buffer,
            )
            writeline(
                file,
                "        extra_sprite_buffer_size=%i,"
                % partition.extra_sprite_buffer_size,
            )
            writeline(file, "        buffers = [")
            writeline(file, "            Buffer(")
            buffer_type = BufferType(partition.buffers[0].buffer_type)
            writeline(file, "                buffer_type=BufferType.%s," % buffer_type.name)
            main_buffer_space = BufferSpace(partition.buffers[0].main_buffer_space)
            writeline(file, "                main_buffer_space=BufferSpace.%s," % main_buffer_space.name)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[0].index_in_main_buffer,
            )
            writeline(file, "            ),")
            writeline(file, "            Buffer(")
            buffer_type = BufferType(partition.buffers[1].buffer_type)
            writeline(file, "                buffer_type=BufferType.%s," % buffer_type.name)
            main_buffer_space = BufferSpace(partition.buffers[1].main_buffer_space)
            writeline(file, "                main_buffer_space=BufferSpace.%s," % main_buffer_space.name)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[1].index_in_main_buffer,
            )
            writeline(file, "            ),")
            writeline(file, "            Buffer(")
            buffer_type = BufferType(partition.buffers[2].buffer_type)
            writeline(file, "                buffer_type=BufferType.%s," % buffer_type.name)
            main_buffer_space = BufferSpace(partition.buffers[2].main_buffer_space)
            writeline(file, "                main_buffer_space=BufferSpace.%s," % main_buffer_space.name)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[2].index_in_main_buffer,
            )
            writeline(file, "            )")
            writeline(file, "        ],")
            writeline(
                file, "        full_palette_buffer=%r" % partition.full_palette_buffer
            )
            writeline(file, "    ),")

            # events

            if len(r) > 0:
                music_id = r[0]
                music_name = music_id_to_name.get(music_id)
                writeline(file, "    music=%s," % music_name)
                loading_event = (r[2] << 8) + r[1]
                event_name = event_script_id_to_name.get(loading_event, None)
                writeline(file, "    entrance_event=%s," % event_name)
                
                j = 3
                event_triggers = []
                while j < len(r):
                    length_determinant = r[j + 1] & 0x80 == 0x80
                    if length_determinant == 0:
                        trigger_data = r[j : j + 5]
                        length = 1
                        f_bit = 0
                        byte_8_bit_4 = 0
                        j += 5
                    else:
                        trigger_data = r[j : j + 6]
                        length = 1 + (trigger_data[5] & 0x0F)
                        f_bit = (trigger_data[5] & 0x80) >> 7
                        byte_8_bit_4 = (trigger_data[5] & 0x10) >> 4
                        j += 6
                    # Read event as a short (2 bytes little-endian) and mask with 0x0FFF (12 bits)
                    event_value = (trigger_data[0] | (trigger_data[1] << 8)) & 0x0FFF
                    event_triggers.append(
                        Event(
                            event=event_value,
                            x=trigger_data[2] & 0x7F,
                            y=trigger_data[3] & 0x7F,
                            z=trigger_data[4] & 0x1F,
                            f=EdgeDirection(f_bit),
                            length=length,
                            height=(trigger_data[4] & 0xF0) >> 5,
                            nw_se_edge_active=trigger_data[2] & 0x80 == 0x80,
                            ne_sw_edge_active=trigger_data[3] & 0x80 == 0x80,
                            byte_8_bit_4=byte_8_bit_4 == 1,
                        )
                    )
                if len(event_triggers) > 0:
                    writeline(file, "    events=[")
                    for event in event_triggers:
                        writeline(file, "        Event(")
                        event_name = event_script_id_to_name.get(event.event, None)
                        if event_name:
                            writeline(file, "            event=%s," % event_name)
                        else:
                            writeline(file, "            event=%i," % event.event)
                        writeline(file, "            x=%i," % event.x)
                        writeline(file, "            y=%i," % event.y)
                        writeline(file, "            z=%i," % event.z)
                        f_edge = EdgeDirection(event.f)
                        writeline(file, "            f=EdgeDirection.%s," % f_edge.name)
                        writeline(file, "            height=%i," % event.height)
                        writeline(file, "            length=%i," % event.length)
                        writeline(
                            file,
                            "            nw_se_edge_active=%r,"
                            % event.nw_se_edge_active,
                        )
                        writeline(
                            file,
                            "            ne_sw_edge_active=%r,"
                            % event.ne_sw_edge_active,
                        )
                        writeline(
                            file, "            byte_8_bit_4=%r," % event.byte_8_bit_4
                        )
                        writeline(file, "        ),")
                    writeline(file, "    ],")

            # exits

            if len(e) > 0:
                exit_fields = []
                j = 0
                while j < len(e):
                    offset = 0
                    field_data = e[j:]
                    exit_type = (field_data[1] & 0x60) >> 6
                    byte_2_bit_0 = field_data[1] & 0x01
                    byte_2_bit_1 = (field_data[1] & 0x02) >> 1
                    byte_2_bit_2 = (field_data[1] & 0x04) >> 2

                    length_determinant = field_data[1] & 0x80 == 0x80
                    dst = ((field_data[1] << 8) + field_data[0]) & 0x1FF

                    offset += 5
                    if exit_type == 0:  # room
                        offset += 3
                    if length_determinant == 0:
                        length = 1
                        f_bit = 0
                    else:
                        length = 1 + (field_data[offset] & 0x0F)
                        f_bit = (field_data[offset] & 0x80) >> 7
                        offset += 1
                    if exit_type == 0:  # room
                        dst_f_val = (field_data[7] & 0xF0) >> 5
                        exit_fields.append(
                            RoomExit(
                                x=field_data[2] & 0x7F,
                                y=field_data[3] & 0x7F,
                                z=field_data[4] & 0x1F,
                                f=EdgeDirection(f_bit),
                                length=length,
                                height=(field_data[4] & 0xF0) >> 5,
                                nw_se_edge_active=field_data[2] & 0x80 == 0x80,
                                ne_sw_edge_active=field_data[3] & 0x80 == 0x80,
                                byte_2_bit_2=byte_2_bit_2 == 1,
                                destination=dst,
                                show_message=(field_data[1] & 0x08) == 0x08,
                                dst_x=field_data[5] & 0x7F,
                                dst_y=field_data[6] & 0x7F,
                                dst_z=field_data[7] & 0x1F,
                                dst_z_half=(field_data[6] & 0x80) == 0x80,
                                dst_f=Direction(dst_f_val),
                                x_bit_7=(field_data[5] & 0x80) == 0x80,
                            )
                        )
                    else:  # world map location
                        dst &= 0xFF
                        exit_fields.append(
                            MapExit(
                                x=field_data[2] & 0x7F,
                                y=field_data[3] & 0x7F,
                                z=field_data[4] & 0x1F,
                                f=EdgeDirection(f_bit),
                                length=length,
                                height=(field_data[4] & 0xF0) >> 5,
                                nw_se_edge_active=field_data[2] & 0x80 == 0x80,
                                ne_sw_edge_active=field_data[3] & 0x80 == 0x80,
                                byte_2_bit_2=byte_2_bit_2 == 1,
                                destination=dst,
                                show_message=(field_data[1] & 0x08) == 0x08,
                                byte_2_bit_1=byte_2_bit_1 == 1,
                                byte_2_bit_0=byte_2_bit_0 == 1,
                            )
                        )
                    j += offset

                if len(exit_fields) > 0:
                    writeline(file, "    exits=[")
                    for ex in exit_fields:
                        if ex.destination_type == ExitType.ROOM:
                            writeline(file, "        RoomExit(")
                        else:
                            writeline(file, "        MapExit(")
                        writeline(file, "            x=%i," % ex.x)
                        writeline(file, "            y=%i," % ex.y)
                        writeline(file, "            z=%i," % ex.z)
                        f_edge = EdgeDirection(ex.f)
                        writeline(file, "            f=EdgeDirection.%s," % f_edge.name)
                        writeline(file, "            length=%i," % ex.length)
                        writeline(file, "            height=%i," % ex.height)
                        writeline(
                            file,
                            "            nw_se_edge_active=%r," % ex.nw_se_edge_active,
                        )
                        writeline(
                            file,
                            "            ne_sw_edge_active=%r," % ex.ne_sw_edge_active,
                        )
                        writeline(
                            file, "            byte_2_bit_2=%r," % ex.byte_2_bit_2
                        )
                        if ex.destination_type == ExitType.ROOM:
                            dst_name = room_id_to_name.get(ex.destination, f"R{ex.destination:03d}_UNKNOWN")
                            writeline(file, "            destination=%s," % dst_name)
                        else:
                            dst_name = location_id_to_name.get(ex.destination, f"OW{ex.destination:02d}_UNKNOWN")
                            writeline(file, "            destination=%s," % dst_name)
                        writeline(
                            file, "            show_message=%r," % ex.show_message
                        )
                        if ex.destination_type == ExitType.ROOM:
                            writeline(
                                file, "            dst_x=%i," % ex.destination_props.x
                            )
                            writeline(
                                file, "            dst_y=%i," % ex.destination_props.y
                            )
                            writeline(
                                file, "            dst_z=%i," % ex.destination_props.z
                            )
                            writeline(
                                file,
                                "            dst_z_half=%r,"
                                % ex.destination_props.z_half,
                            )
                            dst_f_direction = Direction(ex.destination_props.f)
                            writeline(file, "            dst_f=%s," % directions[dst_f_direction])
                            writeline(
                                file,
                                "            x_bit_7=%r,"
                                % ex.destination_props.x_bit_7,
                            )
                        else:
                            writeline(
                                file, "            byte_2_bit_1=%r," % ex.byte_2_bit_1
                            )
                            writeline(
                                file, "            byte_2_bit_0=%r," % ex.byte_2_bit_0
                            )

                        writeline(file, "        ),")
                    writeline(file, "    ],")

            if len(d) > 0:
                room_objects = []
                offset = 1
                n = 0
                event, upper_70a7, lower_70a7, after_battle, pack, base_event, base_pack = 0,0,0,0,0,0,0
                while offset < len(d):
                    l = 12
                    otype = d[offset] >> 4
                    speed = d[offset + 1] & 0x07
                    base_assigned_npc = ((d[offset + 4] & 0x0F) << 6) + (
                        d[offset + 3] >> 2
                    )
                    base_action_script = ((d[offset + 5] & 0x3F) << 4) + (
                        (d[offset + 4] & 0xFF) >> 4
                    )
                    initiator = d[offset + 7] >> 4
                    if otype == 0:  # regular
                        base_event = ((d[offset + 7] & 0x0F) << 8) + d[offset + 6]
                        # Extract offsets from byte 8 for parent objects
                        npc_offset = d[offset + 8] & 0x07
                        action_offset = (d[offset + 8] >> 3) & 0x03
                        event_offset = d[offset + 8] >> 5
                        event = base_event + event_offset
                        assigned_npc = base_assigned_npc + npc_offset
                        action_script = base_action_script + action_offset
                    elif otype == 1:  # chest
                        base_event = ((d[offset + 7] & 0x0F) << 8) + d[offset + 6]
                        event = base_event
                        assigned_npc = base_assigned_npc
                        action_script = base_action_script
                        upper_70a7 = d[offset + 8] >> 4
                        lower_70a7 = d[offset + 8] & 0x0F
                    else:  # battle
                        assigned_npc = base_assigned_npc
                        after_battle = (d[offset + 7] >> 1) & 0x07
                        base_pack = d[offset + 6]
                        # Extract offsets from byte 8 for parent objects
                        pack_offset = d[offset + 8] >> 4
                        action_offset = d[offset + 8] & 0x0F
                        pack = base_pack + pack_offset
                        action_script = base_action_script + action_offset
                    visible = bit_bool_from_num(d[offset + 9], 7)
                    x = d[offset + 9] & 0x7F
                    y = d[offset + 10] & 0x7F
                    z = d[offset + 11] & 0x1F
                    z_half = bit_bool_from_num(d[offset + 10], 7)
                    direction = d[offset + 11] >> 5
                    face_on_trigger = bit_bool_from_num(d[offset + 1], 3)
                    cant_enter_doors = bit_bool_from_num(d[offset + 1], 4)
                    byte2_bit5 = bit_bool_from_num(d[offset + 1], 5)
                    set_sequence_playback = bit_bool_from_num(d[offset + 1], 6)
                    cant_float = bit_bool_from_num(d[offset + 1], 7)
                    cant_walk_up_stairs = bit_bool_from_num(d[offset + 2], 0)
                    cant_walk_under = bit_bool_from_num(d[offset + 2], 1)
                    cant_pass_walls = bit_bool_from_num(d[offset + 2], 2)
                    cant_jump_through = bit_bool_from_num(d[offset + 2], 3)
                    cant_pass_npcs = bit_bool_from_num(d[offset + 2], 4)
                    byte3_bit5 = bit_bool_from_num(d[offset + 2], 5)
                    cant_walk_through = bit_bool_from_num(d[offset + 2], 6)
                    byte3_bit7 = bit_bool_from_num(d[offset + 2], 7)
                    slidable_along_walls = bit_bool_from_num(d[offset + 3], 0)
                    cant_move_if_in_air = bit_bool_from_num(d[offset + 3], 1)
                    byte7_upper2 = d[offset + 5] >> 6

                    npc_from_table = npc_classes[assigned_npc]

                    ending_args = [
                        speed,
                        visible,
                        x,
                        y,
                        z,
                        z_half,
                        Direction(direction),
                        face_on_trigger,
                        cant_enter_doors,
                        byte2_bit5,
                        set_sequence_playback,
                        cant_float,
                        cant_walk_up_stairs,
                        cant_walk_under,
                        cant_pass_walls,
                        cant_jump_through,
                        cant_pass_npcs,
                        byte3_bit5,
                        cant_walk_through,
                        byte3_bit7,
                        slidable_along_walls,
                        cant_move_if_in_air,
                        byte7_upper2,
                    ]
                    
                    # start comparing properties of npc_from_table vs npc_class
                    if otype == 0:  # regular
                        npcType = RegularNPC
                        args = [
                            npc_from_table,
                            EventInitiator(initiator),
                            event,
                            action_script,
                        ] + ending_args
                    elif otype == 1:  # chest
                        npcType = ChestNPC
                        args = [
                            npc_from_table,
                            EventInitiator(initiator),
                            event,
                            action_script,
                            upper_70a7,
                            lower_70a7,
                        ] + ending_args
                    else:  # battle
                        npcType = BattlePackNPC
                        args = [
                            npc_from_table,
                            EventInitiator(initiator),
                            PostBattleBehaviour(after_battle),
                            pack,
                            action_script,
                        ] + ending_args
                    thisNPC = npcType(*args)

                    room_objects.append(thisNPC)

                    n += 1

                    extra_length = d[offset] & 0x0F
                    if extra_length > 0:
                        l += extra_length * 4
                        for o in range(offset + 12, offset + l - 1, 4):

                            if otype == 0:  # regular
                                npcType = RegularClone
                                assigned_npc = base_assigned_npc + (d[o] & 0x07)
                                event = base_event + (d[o] >> 5)
                                action_script = base_action_script + (
                                    (d[o] & 0x1F) >> 3
                                )
                            elif otype == 1:  # chest
                                npcType = ChestClone
                                upper_70a7 = d[o] >> 4
                                lower_70a7 = d[o] & 0x0F
                            else:  # battle
                                npcType = BattlePackClone
                                action_script = base_action_script + (d[o] & 0x0F)
                                pack = base_pack + (d[o] >> 4)

                            npc_from_table = npc_classes[assigned_npc]

                            # print(npc_from_table.cannot_clone)

                            ending_args = [
                                bit_bool_from_num(d[o + 1], 7),
                                (d[o + 1] & 0x7F),
                                (d[o + 2] & 0x7F),
                                (d[o + 3] & 0x1F),
                                bit_bool_from_num(d[o + 2], 7),
                                Direction((d[o + 3] >> 5)),
                            ]

                            if otype == 0:  # regular
                                args = [npc_from_table, event, action_script] + ending_args
                            elif otype == 1:  # chest
                                args = [npc_from_table, lower_70a7, upper_70a7] + ending_args
                            else:  # battle
                                args = [npc_from_table, pack, action_script] + ending_args
                            thisNPC = npcType(*args)

                            # No validation needed here - parent and clones can have any values
                            # as long as they're all within 0-15 of their shared base value.
                            # The base is determined during assembly as the minimum value.

                            room_objects.append(thisNPC)
                    offset += l

                writeline(file, "    objects=[")
                for index, obj in enumerate(room_objects):
                    if isinstance(obj, BattlePackNPC):
                        writeline(file, "        BattlePackNPC( # %i" % index)
                    elif isinstance(obj, RegularNPC):
                        writeline(file, "        RegularNPC( # %i" % index)
                    elif isinstance(obj, ChestNPC):
                        writeline(file, "        ChestNPC( # %i" % index)
                    elif isinstance(obj, BattlePackClone):
                        writeline(file, "        BattlePackClone( # %i" % index)
                    elif isinstance(obj, RegularClone):
                        writeline(file, "        RegularClone( # %i" % index)
                    elif isinstance(obj, ChestClone):
                        writeline(file, "        ChestClone( # %i" % index)
                    else:
                        raise Exception("unknown class")
                    # Use the variable name from npc_variable_names instead of class name
                    writeline(
                        file,
                        "            npc=npcs.%s," % npc_variable_names[npc_classes.index(obj._npc)],
                    )
                    if (
                        isinstance(obj, BattlePackNPC)
                        or isinstance(obj, RegularNPC)
                        or isinstance(obj, ChestNPC)
                    ):
                        obj_initiator = EventInitiator(obj.initiator)
                        writeline(file, "            initiator=EventInitiator.%s," % obj_initiator.name)
                    if isinstance(obj, BattlePackNPC):
                        obj_postbattle = PostBattleBehaviour(obj.after_battle)
                        writeline(file, "            after_battle=PostBattleBehaviour.%s," % obj_postbattle.name)
                    if isinstance(obj, BattlePackNPC) or isinstance(
                        obj, BattlePackClone
                    ):
                        writeline(file, "            battle_pack=%i," % obj.battle_pack)
                    if (
                        isinstance(obj, RegularNPC)
                        or isinstance(obj, RegularClone)
                        or isinstance(obj, ChestNPC)
                    ):
                        event_name = event_script_id_to_name.get(obj.event_script)
                        writeline(
                            file, "            event_script=%s," % event_name
                        )
                    if (
                        isinstance(obj, RegularNPC)
                        or isinstance(obj, BattlePackNPC)
                        or isinstance(obj, ChestNPC)
                        or isinstance(obj, RegularClone)
                        or isinstance(obj, BattlePackClone)
                    ):
                        action_name = action_script_id_to_name.get(obj.action_script, None)
                        if action_name:
                            writeline(
                                file, "            action_script=%s," % action_name
                            )
                        else:
                            writeline(
                                file, "            action_script=%i," % obj.action_script
                            )
                    if isinstance(obj, ChestNPC) or isinstance(
                        obj, ChestClone
                    ):
                        writeline(file, "            lower_70a7=%i," % obj.lower_70a7)
                        writeline(file, "            upper_70a7=%i," % obj.upper_70a7)
                    if (
                        isinstance(obj, BattlePackNPC)
                        or isinstance(obj, RegularNPC)
                        or isinstance(obj, ChestNPC)
                    ):
                        if obj.speed != 0:
                            writeline(file, "            speed=%i," % obj.speed)
                    writeline(file, "            visible=%r," % obj.visible)
                    writeline(file, "            x=%i," % obj.x)
                    writeline(file, "            y=%i," % obj.y)
                    writeline(file, "            z=%i," % obj.z)
                    writeline(file, "            z_half=%r," % obj.z_half)
                    obj_direction = Direction(obj.direction)
                    writeline(file, "            direction=%s," % directions[obj_direction])
                    if (
                        isinstance(obj, BattlePackNPC)
                        or isinstance(obj, RegularNPC)
                        or isinstance(obj, ChestNPC)
                    ):
                        writeline(
                            file,
                            "            face_on_trigger=%r," % obj.face_on_trigger,
                        )
                        writeline(
                            file,
                            "            cant_enter_doors=%r," % obj.cant_enter_doors,
                        )
                        writeline(file, "            byte2_bit5=%r," % obj.byte2_bit5)
                        writeline(
                            file,
                            "            set_sequence_playback=%r,"
                            % obj.set_sequence_playback,
                        )
                        writeline(file, "            cant_float=%r," % obj.cant_float)
                        writeline(
                            file,
                            "            cant_walk_up_stairs=%r,"
                            % obj.cant_walk_up_stairs,
                        )
                        writeline(
                            file,
                            "            cant_walk_under=%r," % obj.cant_walk_under,
                        )
                        writeline(
                            file,
                            "            cant_pass_walls=%r," % obj.cant_pass_walls,
                        )
                        writeline(
                            file,
                            "            cant_jump_through=%r," % obj.cant_jump_through,
                        )
                        writeline(
                            file, "            cant_pass_npcs=%r," % obj.cant_pass_npcs
                        )
                        writeline(file, "            byte3_bit5=%r," % obj.byte3_bit5)
                        writeline(
                            file,
                            "            cant_walk_through=%r," % obj.cant_walk_through,
                        )
                        writeline(file, "            byte3_bit7=%r," % obj.byte3_bit7)
                        writeline(
                            file,
                            "            slidable_along_walls=%r,"
                            % obj.slidable_along_walls,
                        )
                        writeline(
                            file,
                            "            cant_move_if_in_air=%r,"
                            % obj.cant_move_if_in_air,
                        )
                        writeline(
                            file, "            byte7_upper2=%r," % obj.byte7_upper2
                        )
                    writeline(file, "        ),")

                writeline(file, "    ]")

            writeline(file, ")")
            file.close()

        # Create RoomCollection file
        collection_file = open("%s/rooms.py" % dest, "w", encoding="utf-8")

        # Write imports
        writeline(collection_file, "from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection")
        for i in range(512):
            writeline(
                collection_file,
                "from .room_%i import room as room_%i" % (i, i),
            )

        writeline(collection_file, "")
        writeline(collection_file, "room_collection = RoomCollection(")
        writeline(collection_file, "    rooms=[")

        # Write room array using room_N variables with name comments
        for i in range(512):
            room_name = room_id_to_name.get(i, f"R{i:03d}_UNKNOWN")
            writeline(collection_file, "        room_%i,  # %i: %s" % (i, i, room_name))

        writeline(collection_file, "    ],")
        writeline(collection_file, "    large_partition_table=%r" % large_partition_table)
        writeline(collection_file, ")")
        collection_file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled 512 rooms to ./rooms"
            )
        )
