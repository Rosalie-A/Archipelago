"""Enums supporting development surrounding spells."""

from enum import IntEnum, Enum

from smrpgpatchbuilder.datatypes.numbers.classes import UInt4, UInt8

ELEMENT_NAME_NONE = "No Element"
ELEMENT_NAME_FIRE = "Fire"
ELEMENT_NAME_ICE = "Ice"
ELEMENT_NAME_THUNDER = "Thunder"
ELEMENT_NAME_JUMP = "Jump"

STATUS_NAME_MUTE = "Mute"
STATUS_NAME_SLEEP = "Sleep"
STATUS_NAME_POISON = "Poison"
STATUS_NAME_FEAR = "Fear"
STATUS_NAME_BERSERK = "Berserk"
STATUS_NAME_MUSHROOM = "Mushroom"
STATUS_NAME_SCARECROW = "Scarecrow"
STATUS_NAME_INVINCIBLE = "Invincible"

class DescribableAttribute:
    """Base class for attributes like statuses or elements
    that may be assembled differently depending on what
    is using them. Different characters for equips vs.
    Psychopath messages, etc."""

    _name: str
    _stat_value: UInt4
    _spell_value: UInt8
    _stat_char: str
    _dialog_char: str

    @property
    def name(self) -> str:
        """The name of this attribute."""
        return self._name

    @property
    def stat_value(self) -> UInt4:
        """The value or ID of this attribute when used in equipment,
        character, or monster stats."""
        return self._stat_value

    @property
    def spell_value(self) -> UInt8:
        """The value or ID of this attribute when used in spells."""
        return self._spell_value

    @property
    def stat_char(self) -> str:
        """The ascii value of this character when used in equip descriptions."""
        return self._stat_char

    @property
    def dialog_char(self) -> str:
        """The ascii value of this character when used in Psychopath text."""
        return self._dialog_char

    def __init__(
        self,
        name: str,
        stat_value: int,
        spell_value: int,
        stat_char: str,
        dialog_char: str,
    ) -> None:
        self._name = name
        self._stat_value = UInt4(stat_value)
        self._spell_value = UInt8(spell_value)
        self._stat_char = stat_char
        self._dialog_char = dialog_char

class Element(DescribableAttribute, Enum):
    """Enum of elements."""

    NONE = (ELEMENT_NAME_NONE, 0, 0, "", "")
    ICE = (ELEMENT_NAME_ICE, 4, 0x10, "\x81", "\x7D")
    THUNDER = (ELEMENT_NAME_THUNDER, 5, 0x20, "\x82", "\x7F")
    FIRE = (ELEMENT_NAME_FIRE, 6, 0x40, "\x80\x98", "\x7E")
    JUMP = (ELEMENT_NAME_JUMP, 7, 0x80, "", "\x85")

    def __new__(cls, name, stat_value, spell_value, stat_char, dialog_char):
        obj = object.__new__(cls)
        DescribableAttribute.__init__(obj, name, stat_value, spell_value, stat_char, dialog_char)
        return obj

class Status(DescribableAttribute, Enum):
    """Enum of status effects."""
    MUTE = (STATUS_NAME_MUTE, 0, 0, "\x83", "\x82")
    SLEEP = (STATUS_NAME_SLEEP, 1, 1, "\x84", "\x80")
    POISON = (STATUS_NAME_POISON, 2, 2, "\x85", "\x83")
    FEAR = (STATUS_NAME_FEAR, 3, 3, "\x86", "\x81")
    BERSERK = (STATUS_NAME_BERSERK, 4, 4, "\x8A", "")
    MUSHROOM = (STATUS_NAME_MUSHROOM, 5, 5, "\x98\x87", "")
    SCARECROW = (STATUS_NAME_SCARECROW, 6, 6, "\x88", "")
    INVINCIBLE = (STATUS_NAME_INVINCIBLE, 7, 7, "", "")

    def __new__(cls, name, stat_value, spell_value, stat_char, dialog_char):
        obj = object.__new__(cls)
        DescribableAttribute.__init__(obj, name, stat_value, spell_value, stat_char, dialog_char)
        return obj

class SpellType(IntEnum):
    """Enum of damage vs. heal spell types."""

    DAMAGE = 0
    HEAL = 1

class EffectType(IntEnum):
    """Enum of influct vs. nullify spell effect types."""

    INFLICT = 2
    NULLIFY = 4

class InflictFunction(IntEnum):
    """Enum of additional miscellaneous spell effects upon inflict."""

    SCAN = 0
    MISS = 1
    NO_DMG = 2
    REVIVE = 3
    INC_JUMP = 4

class TempStatBuff(IntEnum):
    """Enumeration for in-battle temporary buffs applies to offensive and defensive stats."""

    MAGIC_ATTACK = 3
    ATTACK = 4
    MAGIC_DEFENSE = 5
    DEFENSE = 6
