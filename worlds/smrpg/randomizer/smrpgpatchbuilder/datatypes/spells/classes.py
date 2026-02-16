"""Base classes fors spells."""

from copy import deepcopy
from typing import Generic, TypeVar

from smrpgpatchbuilder.datatypes.numbers.classes import BitMapSet, ByteField, UInt8
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.items.encoding import encode_item_description

from .arguments.types.classes import DamageModifiers, TimingProperties
from .ids.misc import (
    SPELL_BASE_ADDRESS,
    SPELL_BASE_NAME_ADDRESS,
    SPELL_BASE_DESC_POINTER_ADDRESS,
    SPELL_BASE_DESC_DATA_START,
    SPELL_BASE_DESC_DATA_END,
    SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS,
    SPELL_TIMING_MODIFIERS_BASE_ADDRESS,
)
from .enums import (
    EffectType,
    InflictFunction,
    Element,
    Status,
    SpellType,
    TempStatBuff,
)

class Spell:
    """Class representing a magic spell to be randomized."""

    # default per-spell attributes.
    _index: int = 0
    _fp: int = 0
    _power: int = 0
    _hit_rate: int = 0

    _title: str = ""
    _prefix: ItemPrefix | None = None

    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType | None = None
    _inflict: InflictFunction | None = None
    _element = Element.NONE

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _quad9s: bool = False
    _hide_num: bool = False

    _target_others: bool = False
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = False
    _target_not_self: bool = False
    _status_effects: list[Status] = []
    _boosts: list[TempStatBuff] = []

    @property
    def fp(self) -> UInt8:
        """The FP cost of this spell."""
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        """Set the FP cost of this spell."""
        assert 0 <= fp <= 31
        self._fp = fp

    @property
    def power(self) -> UInt8:
        """The base power of this spell."""
        return UInt8(self._power)

    def set_power(self, power: int) -> None:
        """Set the base power of this spell."""
        UInt8(power)
        self._power = power

    @property
    def hit_rate(self) -> UInt8:
        """The likelihood that this spell will hit a target."""
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        """Specify the likelihood that this spell will hit a target."""
        UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def index(self) -> UInt8:
        """The ID of this spell as known to SMRPG."""
        return UInt8(self._index)

    @property
    def title(self) -> str:
        """The name of this spell as it appears in-game."""
        return self._title

    @property
    def prefix(self) -> ItemPrefix | None:
        """The icon prefix that appears before the spell name."""
        return self._prefix

    def set_prefix(self, prefix: ItemPrefix | None) -> None:
        """Set the icon prefix for this spell."""
        self._prefix = prefix

    @property
    def spell_type(self) -> SpellType:
        """Damage vs. heal."""
        return self._spell_type

    def set_spell_type(self, spell_type: SpellType) -> None:
        """Damage vs. heal."""
        self._spell_type = spell_type

    @property
    def effect_type(self) -> EffectType | None:
        """Inflict vs. nullify."""
        return self._effect_type

    def set_effect_type(self, effect_type: EffectType | None) -> None:
        """Inflict vs. nullify."""
        self._effect_type = effect_type

    @property
    def inflict(self) -> InflictFunction | None:
        """A special property of the spell on contact, i.e. jump counter."""
        return self._inflict

    def set_inflict(self, inflict: InflictFunction | None) -> None:
        """A special property of the spell on contact, i.e. jump counter."""
        self._inflict = inflict

    @property
    def element(self) -> Element:
        """The spell's infused element."""
        return self._element

    def set_element(self, element: Element) -> None:
        """Choose the spell's infused element."""
        self._element = element

    @property
    def check_stats(self) -> bool:
        """(unknown)"""
        return self._check_stats

    def set_check_stats(self, check_stats: bool) -> None:
        """(unknown)"""
        self._check_stats = check_stats

    @property
    def ignore_defense(self) -> bool:
        """If true, the target's defense is not factored into output calculation."""
        return self._ignore_defense

    def set_ignore_defense(self, ignore_defense: bool) -> None:
        """If true, the target's defense is not factored into output calculation."""
        self._ignore_defense = ignore_defense

    @property
    def check_ohko(self) -> bool:
        """(unknown)"""
        return self._check_ohko

    def set_check_ohko(self, check_ohko: bool) -> None:
        """(unknown)"""
        self._check_ohko = check_ohko

    @property
    def usable_outside_of_battle(self) -> bool:
        """If true, the spell can be used in the X menu when not in battle."""
        return self._usable_outside_of_battle

    def set_usable_outside_of_battle(self, usable_outside_of_battle: bool) -> None:
        """If true, the spell can be used in the X menu when not in battle."""
        self._usable_outside_of_battle = usable_outside_of_battle

    @property
    def quad9s(self) -> bool:
        """If true, the spell does max damage."""
        return self._quad9s

    def set_quad9s(self, quad9s: bool) -> None:
        """If true, the spell does max damage."""
        self._quad9s = quad9s

    @property
    def hide_num(self) -> bool:
        """If true, the damage output will not be shown."""
        return self._hide_num

    def set_hide_num(self, hide_num: bool) -> None:
        """If true, the damage output will not be shown."""
        self._hide_num = hide_num

    @property
    def target_others(self) -> bool:
        """If true, this spell targets all possible targets instead of just one."""
        return self._target_others

    def set_target_others(self, target_others: bool) -> None:
        """If true, this spell targets all possible targets instead of just one."""
        self._target_others = target_others

    @property
    def target_enemies(self) -> bool:
        """If true, this spell targets opponents."""
        return self._target_enemies

    def set_target_enemies(self, target_enemies: bool) -> None:
        """If true, this spell targets opponents."""
        self._target_enemies = target_enemies

    @property
    def target_party(self) -> bool:
        """If true, this spell targets your own party."""
        return self._target_party

    def set_target_party(self, target_party: bool) -> None:
        """If true, this spell targets your own party."""
        self._target_party = target_party

    @property
    def target_wounded(self) -> bool:
        """If true, this spell targets party members who are KOed."""
        return self._target_wounded

    def set_target_wounded(self, target_wounded: bool) -> None:
        """If true, this spell targets party members who are KOed."""
        self._target_wounded = target_wounded

    @property
    def target_one_party(self) -> bool:
        """(unknown)"""
        return self._target_one_party

    def set_target_one_party(self, target_one_party: bool) -> None:
        """(unknown)"""
        self._target_one_party = target_one_party

    @property
    def target_not_self(self) -> bool:
        """If true, the caster is excluded from targeting."""
        return self._target_not_self

    def set_target_not_self(self, target_not_self: bool) -> None:
        """If true, the caster is excluded from targeting."""
        self._target_not_self = target_not_self

    @property
    def status_effects(self) -> list[Status]:
        """A list of status effects inflicted by this spell."""
        return deepcopy(self._status_effects)

    def set_status_effects(self, status_effects: list[Status]) -> None:
        """Overwrite the list of status effects inflicted by this spell."""
        self._status_effects = deepcopy(status_effects)

    @property
    def boosts(self) -> list[TempStatBuff]:
        """A list of stat boosts applied by this spell."""
        return deepcopy(self._boosts)

    def set_boosts(self, boosts: list[TempStatBuff]) -> None:
        """Overwrite the list of stat boosts applied by this spell."""
        assert len(boosts) == len(set(boosts))
        self._boosts = deepcopy(boosts)

    def __init__(self):
        if len(self._status_effects) == 0:
            self._status_effects = []
        if len(self._boosts) == 0:
            self._boosts = []

    def __str__(self):
        return f"<{self.name}>"

    def __repr__(self):
        return str(self)

    @property
    def name(self) -> str:
        """The class name of this spell."""
        return self.__class__.__name__

    def render(self) -> dict[int, bytearray]:
        """Get data for this spell in `{0x123456: bytearray([0x00])}` format"""
        patch: dict[int, bytearray] = {}

        # Build spell name with prefix
        name_bytes = bytearray()
        if self._prefix is not None and self._prefix != ItemPrefix.NONE:
            name_bytes.append(self._prefix)

        # Add the title
        if self.title:
            name_bytes.extend(self.title.encode('latin-1'))

        # Pad to 15 bytes with spaces
        while len(name_bytes) < 15:
            name_bytes.append(0x20)

        name_addr = SPELL_BASE_NAME_ADDRESS + self.index * 15
        patch[name_addr] = name_bytes

        # fp is byte 3, power is byte 6, hit rate is byte 7.  each spell is 12 bytes.
        base_addr = SPELL_BASE_ADDRESS + (self.index * 12)
        patch[base_addr] = bytearray([
            (self.check_stats * 0x01)
            + (self.ignore_defense * 0x02)
            + (self.check_ohko * 0x20)
            + (self.usable_outside_of_battle * 0x80)
        ])

        spell_type: int = 0
        effect_type: int = 0
        element: int = 0
        inflict_value: int = 0xFF  # Default to 0xFF (no inflict function)

        if self.spell_type is not None:
            spell_type = self.spell_type.value
        if self.effect_type is not None:
            effect_type = self.effect_type.value
        if self.element is not None:
            element = self.element.spell_value
        if self.inflict is not None:
            inflict_value = self.inflict.value  # Use actual value if inflict is set
        patch[base_addr + 1] = bytearray([spell_type + effect_type + (self.quad9s * 0x08)])
        patch[base_addr + 2] = ByteField(self.fp).as_bytes()
        patch[base_addr + 3] = bytearray([
            (self.target_others * 0x02)
            + (self.target_enemies * 0x04)
            + (self.target_party * 0x10)
            + (self.target_wounded * 0x20)
            + (self.target_one_party * 0x40)
            + (self.target_not_self * 0x80)
        ])

        patch[base_addr + 4] = bytearray([element])
        data = ByteField(self.power).as_bytes()
        data += ByteField(self.hit_rate).as_bytes()
        patch[base_addr + 5] = data
        effects = 0
        for index in self.status_effects:
            effects += 2**index.spell_value
        patch[base_addr + 7] = bytearray([effects])
        buffs = 0
        for boost in self.boosts:
            buffs += 2**boost
        patch[base_addr + 8] = bytearray([buffs])
        patch[base_addr + 10] = bytearray([inflict_value])
        patch[base_addr + 11] = bytearray([self.hide_num * 0x04])

        return patch

class CharacterSpell(Spell):
    """Grouping class for character-specific spells."""

    base_title: str = ""
    _prefix = ItemPrefix.STAR
    _description: str = ""

    _timing_modifiers: TimingProperties = TimingProperties(0)
    _damage_modifiers: DamageModifiers = DamageModifiers(0)

    @property
    def timing_modifiers(self) -> TimingProperties:
        """The preset timed hit behaviour of this spell."""
        return self._timing_modifiers

    def set_timing_modifiers(self, timing_modifiers: TimingProperties) -> None:
        """Set the preset timed hit behaviour of this spell."""
        self._timing_modifiers = timing_modifiers

    @property
    def damage_modifiers(self) -> DamageModifiers:
        """(unknown)"""
        return self._damage_modifiers

    def set_damage_modifiers(self, damage_modifiers: DamageModifiers) -> None:
        """(unknown)"""
        self._damage_modifiers = damage_modifiers

    @property
    def description(self) -> str:
        """The description as it appears in the in-game menu"""
        return self._description

    def set_description(self, description: str) -> None:
        """Update the description as it appears in the in-game menu"""
        self._description = description

    def render(self) -> dict[int, bytearray]:
        """Get data for this spell in `{0x123456: bytearray([0x00])}` format"""
        patch = super().render()

        # Only write timing/damage pointers for spells with index < 32
        # Always write these values (even if 0) to match C# LAZYSHELL behavior
        if self.index < 32:
            timing_addr = SPELL_TIMING_MODIFIERS_BASE_ADDRESS + self.index * 2
            damage_addr = SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS + self.index * 2
            patch[timing_addr] = ByteField(
                self.timing_modifiers
            ).as_bytes()
            patch[damage_addr] = ByteField(
                self.damage_modifiers
            ).as_bytes()

        return patch

class EnemySpell(Spell):
    """Grouping class for enemy-specific spells."""
    pass

SpellT = TypeVar("SpellT", bound=Spell)


class SpellCollection(Generic[SpellT]):
    """Collection of spells with rendering support for character spell descriptions."""

    spells: list[SpellT]
    additional_desc_ranges: list[tuple[int, int]]

    def __init__(
        self,
        spells: list[SpellT],
        additional_desc_ranges: list[tuple[int, int]] | None = None
    ):
        """Initialize the collection with a list of spells.

        Args:
            spells: list of Spell objects (can include both CharacterSpell and EnemySpell)
            additional_desc_ranges: optional list of (start, end) address tuples for
                overflow spell descriptions when the default range runs out of room

        Raises:
            ValueError: if there aren't exactly 27 character spells
        """
        self.spells = spells
        self.additional_desc_ranges = additional_desc_ranges or []

        # Count character spells with valid indices (0-26 / 0x1A)
        character_spells = [
            s for s in spells
            if isinstance(s, CharacterSpell) and s.index <= 0x1A
        ]
        if len(character_spells) != 27:
            raise ValueError(
                f"SpellCollection must contain exactly 27 CharacterSpell instances "
                f"with indices 0-26 for descriptions, but {len(character_spells)} were found."
            )

    def render(self) -> dict[int, bytearray]:
        """Render all spells including character spell descriptions and pointer table.

        Returns:
            dictionary mapping ROM addresses to bytearrays
        """
        patch: dict[int, bytearray] = {}

        # First, render each spell individually (stats, names, etc.)
        for spell in self.spells:
            spell_patch = spell.render()
            patch.update(spell_patch)

        # Now handle descriptions for character spells only (index <= 0x1A / 26)
        character_spells = [
            s for s in self.spells
            if isinstance(s, CharacterSpell) and s.index <= 0x1A
        ]

        # Sort by index to ensure correct pointer table ordering
        character_spells.sort(key=lambda s: s.index)

        # Build list of available ranges: default range first, then additional ranges
        available_ranges: list[tuple[int, int]] = [
            (SPELL_BASE_DESC_DATA_START, SPELL_BASE_DESC_DATA_END)
        ]
        available_ranges.extend(self.additional_desc_ranges)

        current_range_index = 0
        current_range_start, current_range_end = available_ranges[current_range_index]
        current_desc_addr = current_range_start

        for spell in character_spells:
            # Get the description
            desc = spell.description if spell.description else ""

            # Encode description using item description character mapping
            desc_bytes = bytearray()
            if desc:
                desc_bytes.extend(encode_item_description(desc))
            # Add terminating 0x00
            desc_bytes.append(0x00)

            # Check if this description fits in the current range
            bytes_remaining_in_range = current_range_end - current_desc_addr + 1
            if len(desc_bytes) > bytes_remaining_in_range:
                # Try to move to the next available range
                current_range_index += 1
                if current_range_index >= len(available_ranges):
                    # Calculate total available space for error message
                    total_available = sum(
                        end - start + 1 for start, end in available_ranges
                    )
                    raise ValueError(
                        f"Spell descriptions exceed all available space. "
                        f"Total available: {total_available} bytes across "
                        f"{len(available_ranges)} range(s). "
                        f"Reduce description lengths or add more ranges."
                    )
                current_range_start, current_range_end = available_ranges[current_range_index]
                current_desc_addr = current_range_start

            # Calculate pointer value (16-bit address within bank)
            pointer_value = current_desc_addr & 0xFFFF

            # Write pointer at the correct position based on spell index
            pointer_addr = SPELL_BASE_DESC_POINTER_ADDRESS + spell.index * 2
            patch[pointer_addr] = bytearray([
                pointer_value & 0xFF,
                (pointer_value >> 8) & 0xFF
            ])

            # Write description to ROM
            patch[current_desc_addr] = desc_bytes

            # Move to next description address
            current_desc_addr += len(desc_bytes)

        return patch
