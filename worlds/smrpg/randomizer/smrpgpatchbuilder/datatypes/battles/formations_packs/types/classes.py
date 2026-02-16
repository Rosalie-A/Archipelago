"""Base class for formations, and battle packs, consisting of 3 formations."""

from random import choices
import statistics

from smrpgpatchbuilder.datatypes.battles.enums import BattleMusic, Battlefields
from smrpgpatchbuilder.datatypes.battles.types.classes import Music
from smrpgpatchbuilder.datatypes.enemies.classes import Enemy
from smrpgpatchbuilder.datatypes.numbers.classes import (
    ByteField,
    BitMapSet,
    UInt16,
    UInt8,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield

from smrpgpatchbuilder.datatypes.battles.ids.misc import (
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_FORMATIONS,
    PACK_BASE_ADDRESS,
)

class FormationMember:
    """Class representing a single enemy in a formation with metadata."""

    _hidden_at_start: bool
    _enemy: type[Enemy]
    _x_pos: UInt8
    _y_pos: UInt8
    _anchor: bool
    _include_in_stat_totaling: bool
    _use: bool

    @property
    def use(self) -> bool:
        """If true, this enemy slot is active in the formation (LazyShell 'Use' checkbox)."""
        return self._use

    def set_use(self, use: bool) -> None:
        """Set whether this enemy slot is active in the formation."""
        self._use = use

    @property
    def hidden_at_start(self) -> bool:
        """If true, this enemy will be hidden when the battle begins."""
        return self._hidden_at_start

    def set_hidden_at_start(self, hidden_at_start: bool) -> None:
        """If true, this enemy will be hidden when the battle begins."""
        self._hidden_at_start = hidden_at_start

    @property
    def enemy(self) -> type[Enemy]:
        """The class of the enemy being included in the formation."""
        return self._enemy

    def set_enemy(self, enemy: type[Enemy]) -> None:
        """Set the class of the enemy being included in the formation."""
        self._enemy = enemy

    @property
    def x_pos(self) -> UInt8:
        """The X coordinate that the enemy will be stationed at."""
        return self._x_pos

    def set_x_pos(self, x_pos: int) -> None:
        """Set the X coordinate that the enemy will be stationed at."""
        self._x_pos = UInt8(x_pos)

    @property
    def y_pos(self) -> UInt8:
        """The Y coordinate that the enemy will be stationed at."""
        return self._y_pos

    def set_y_pos(self, y_pos: int) -> None:
        """Set the Y coordinate that the enemy will be stationed at."""
        self._y_pos = UInt8(y_pos)

    @property
    def anchor(self) -> bool:
        """(deprecated)"""
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        """(deprecated)"""
        self._anchor = anchor

    @property
    def include_in_stat_totaling(self) -> bool:
        """true by default. if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
        return self._include_in_stat_totaling

    def set_include_in_stat_totaling(self, include_in_stat_totaling: bool) -> None:
        """if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
        self._include_in_stat_totaling = include_in_stat_totaling

    def __init__(
        self,
        enemy: type[Enemy],
        x_pos: int,
        y_pos: int,
        hidden_at_start: bool = False,
        anchor: bool = False,
        include_in_stat_totaling: bool = True,
        use: bool = True,
    ) -> None:
        self.set_enemy(enemy)
        self.set_x_pos(x_pos)
        self.set_y_pos(y_pos)
        self.set_hidden_at_start(hidden_at_start)
        self.set_anchor(anchor)
        self.set_include_in_stat_totaling(include_in_stat_totaling)
        self.set_use(use)

class Formation:
    """A subclass that defines an arrangement of enemies in a battle."""

    _formation_id: int | None
    _members: list[FormationMember | None]
    _run_event_at_load: UInt8 | None
    _music: Music | None
    _can_run_away: bool
    _unknown_byte: UInt8
    _unknown_bit: bool
    _battlefield: Battlefield

    @property
    def formation_id(self) -> int | None:
        """The unique ID of this formation (0-511). Used for ROM address calculation."""
        return self._formation_id

    def set_formation_id(self, formation_id: int | None) -> None:
        """Set the unique ID of this formation (0-511)."""
        if formation_id is not None:
            assert 0 <= formation_id < TOTAL_FORMATIONS, \
                f"Formation ID must be 0-{TOTAL_FORMATIONS-1}, got {formation_id}"
        self._formation_id = formation_id

    @property
    def members(self) -> list[FormationMember | None]:
        """A list of containers including info about enemies and their positioning."""
        return self._members

    def set_members(self, members: list[FormationMember | None]) -> None:
        """Overwrite the list of containers including info about enemies and their positioning."""
        self._members = members
        self._members.extend([None] * (8 - len(self._members)))

    @property
    def run_event_at_load(self) -> UInt8 | None:
        """the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        return self._run_event_at_load

    def set_run_event_at_load(self, run_event_at_load: int | None) -> None:
        """set the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        if run_event_at_load is None:
            self._run_event_at_load = run_event_at_load
        else:
            self._run_event_at_load = UInt8(run_event_at_load)

    @property
    def music(self) -> Music | None:
        """The battle music that should accompany this formation."""
        return self._music

    def set_music(self, music: Music | None) -> None:
        """Set the battle music that should accompany this formation."""
        self._music = music

    @property
    def can_run_away(self) -> bool:
        """If false, running away from this formation is impossible."""
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        """If false, running away from this formation is impossible."""
        self._can_run_away = can_run_away

    @property
    def unknown_byte(self) -> UInt8:
        """(unknown)"""
        return self._unknown_byte

    def set_unknown_byte(self, unknown_byte: int) -> None:
        """(unknown)"""
        self._unknown_byte = UInt8(unknown_byte)

    @property
    def unknown_bit(self) -> bool:
        """(unknown)"""
        return self._unknown_bit

    def set_unknown_bit(self, unknown_bit: bool) -> None:
        """(unknown)"""
        self._unknown_bit = unknown_bit

    @property
    def battlefield(self) -> Battlefield:
        """Battlefield to use for this formation"""
        return self._battlefield

    def set_battlefield(
        self, battlefield: Battlefield
    ) -> None:
        """Battlefield to use for this formation"""
        self._battlefield = battlefield
        
    def __init__(
        self,
        members: list[FormationMember | None],
        run_event_at_load: int | None = None,
        music: Music | None = None,
        can_run_away: bool = True,
        unknown_byte: int = 0,
        unknown_bit: bool = False,
        id: int | None = None,
    ) -> None:
        self.set_formation_id(id)
        self.set_members(members)
        self.set_run_event_at_load(run_event_at_load)
        self.set_music(music)
        self.set_can_run_away(can_run_away)
        self.set_unknown_byte(unknown_byte)
        self.set_unknown_bit(unknown_bit)

    def render(self, formation_index: int | None = None) -> dict[int, bytearray]:
        """Get formation data in `{0x123456: bytearray([0x00])}` format.

        Args:
            formation_index: Optional index override. If not provided, uses the
                           internal formation_id. For backward compatibility.
        """
        # Use internal ID if set, otherwise use parameter
        actual_index = formation_index if formation_index is not None else self._formation_id
        if actual_index is None:
            raise ValueError(
                "Formation has no ID set. Either pass formation_index to render() "
                "or set the formation ID via __init__(id=...) or set_formation_id()."
            )
        assert 0 <= actual_index < TOTAL_FORMATIONS
        patch: dict[int, bytearray] = {}
        data = bytearray()

        # monsters present bitmap (Use checkbox in LazyShell).
        monsters_present = [
            7 - index for (index, member) in enumerate(self.members)
            if member is not None and member.use
        ]
        data += BitMapSet(1, monsters_present).as_bytes()

        # monsters hidden bitmap.
        monsters_hidden = [
            7 - index
            for (index, member) in enumerate(self.members)
            if member is not None and member.use and member.hidden_at_start
        ]
        data += BitMapSet(1, monsters_hidden).as_bytes()

        # monster data.
        for index, member in enumerate(self.members):
            if member is not None:
                data += ByteField(member.enemy().monster_id).as_bytes()
                data += ByteField(member.x_pos).as_bytes()
                data += ByteField(member.y_pos).as_bytes()
            else:
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()

        base_addr = BASE_FORMATION_ADDRESS + (actual_index * 26)
        patch[base_addr] = data

        # add formation metadata.
        data = bytearray([self.unknown_byte])
        data += ByteField(
            self.run_event_at_load if self.run_event_at_load is not None else 0xFF
        ).as_bytes()
        music_byte = (
            ((self.music.value if self.music else 0x30) << 2) + ((not self.can_run_away) * 0x02) + self.unknown_bit
        )
        data += ByteField(music_byte).as_bytes()

        base_addr = BASE_FORMATION_META_ADDRESS + actual_index * 3
        patch[base_addr] = data

        return patch

class FormationPack:
    """A pack containing either 1 or 3 Formation instances for battle."""

    _formations: list[Formation]

    @property
    def formations(self) -> list[Formation]:
        """The list of formations in this pack (either 1 or 3 formations)."""
        return self._formations

    def __init__(self, *formations: Formation) -> None:
        """Initialize a FormationPack with either 1 or 3 Formation instances.

        Args:
            *formations: Either 1 Formation (will be used for all 3 slots)
                        or 3 Formations (one for each slot)

        Raises:
            AssertionError: If not exactly 1 or 3 formations are provided
        """
        assert len(formations) in (1, 3), \
            f"FormationPack requires exactly 1 or 3 formations, got {len(formations)}"

        if len(formations) == 1:
            # Store 3 references to the same formation
            self._formations = [formations[0], formations[0], formations[0]]
        else:
            # Store the 3 different formations
            self._formations = list(formations)

    def set_formations(self, *formations: Formation) -> None:
        """Replace the formations in this pack.

        Args:
            *formations: Either 1 Formation (will be used for all 3 slots)
                        or 3 Formations (one for each slot)

        Raises:
            AssertionError: If not exactly 1 or 3 formations are provided
        """
        assert len(formations) in (1, 3), \
            f"FormationPack requires exactly 1 or 3 formations, got {len(formations)}"

        if len(formations) == 1:
            # Store 3 references to the same formation
            self._formations = [formations[0], formations[0], formations[0]]
        else:
            # Store the 3 different formations
            self._formations = list(formations)

class PackCollection:
    """Collection of 256 FormationPacks that renders formations and packs to ROM."""

    _packs: list[FormationPack]

    @property
    def packs(self) -> list[FormationPack]:
        """The list of 256 FormationPacks in this collection."""
        return self._packs

    def __init__(self, packs: list[FormationPack]) -> None:
        """Initialize a PackCollection with exactly 256 FormationPacks.

        Args:
            packs: A list of exactly 256 FormationPack instances

        Raises:
            AssertionError: If not exactly 256 packs are provided
        """
        assert len(packs) == 256, \
            f"PackCollection requires exactly 256 packs, got {len(packs)}"
        self._packs = packs

    def render(self) -> dict[int, bytearray]:
        """Render all packs and formations using their formation IDs.

        This method:
        1. Collects all unique formations from all packs (by object identity)
        2. Renders each formation using its formation_id property
        3. Renders all packs using the formation IDs

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching

        Raises:
            ValueError: If any formation does not have a formation_id set
        """
        patch: dict[int, bytearray] = {}

        # Collect unique formations by object identity (using set of ids)
        seen_formation_ids: set[int] = set()  # Python object ids we've seen
        unique_formations: list[Formation] = []

        for pack in self._packs:
            for formation in pack.formations:
                if id(formation) not in seen_formation_ids:
                    seen_formation_ids.add(id(formation))
                    unique_formations.append(formation)

        # Render all unique formations using their formation_id property
        for formation in unique_formations:
            if formation.formation_id is None:
                raise ValueError(
                    "Formation has no ID set. All formations in a PackCollection "
                    "must have a formation_id. Set it via Formation(id=...) or set_formation_id()."
                )
            formation_patch = formation.render()
            patch.update(formation_patch)

        # Render all packs using the formation IDs
        for pack_index, pack in enumerate(self._packs):
            # Get the formation IDs for this pack
            formation_ids: list[int] = []
            for f in pack.formations:
                if f.formation_id is None:
                    raise ValueError(
                        f"Formation in pack {pack_index} has no ID set. "
                        "All formations must have a formation_id."
                    )
                formation_ids.append(f.formation_id)

            # Render pack data (3 formation IDs + high bank indicator)
            data = bytearray()
            hi_bits = 0

            for i, formation_id in enumerate(formation_ids):
                if formation_id > 255:
                    hi_bits |= (1 << i)
                    data += ByteField(formation_id - 256).as_bytes()
                else:
                    data += ByteField(formation_id).as_bytes()

            # High bank indicator byte
            data += ByteField(hi_bits).as_bytes()

            base_addr = PACK_BASE_ADDRESS + (pack_index * 4)
            patch[base_addr] = data

        return patch
