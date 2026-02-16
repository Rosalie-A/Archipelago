"""Static values for item properties"""

import enum

""" class EffectTypeOld(enum.Enum):
    # Enumeration to describe the type of effect an item will have on its target.

    NORMAL = enum.auto()
    ELEMENTAL_IMMUNITY = enum.auto()
    ELEMENTAL_RESISTANCE = enum.auto()
    STATUS_PROTECTION = enum.auto()
    FEW_EFFECTS = enum.auto()
    BUFFS = enum.auto()
 """

class EquipStats(str, enum.Enum):
    """Enumeration for numerical stats that are directly affected by equips."""

    SPEED = "speed"
    ATTACK = "attack"
    DEFENSE = "defense"
    MAGIC_ATTACK = "magic_attack"
    MAGIC_DEFENSE = "magic_defense"

class ItemTypeValue(enum.IntEnum):
    """Enumeration for distinct base classifications for items."""

    WEAPON = 0b00
    ARMOR = 0b01
    ACCESSORY = 0b10
    ITEM = 0b11

class EffectType(enum.IntEnum):
    INFLICTION = 0x02
    PROTECTION = 0x01
    NULLIFICATION = 0x04

class InflictFunction(enum.IntEnum):
    ITEM_MORPH = 0
    REVIVE = 1
    RESTORE_FP = 2
    INCREASE_STATS_ITEM = 3
    RESTORE_HP = 4
    RESTORE_ALL_HP_FP = 5
    RAISE_MAX_FP = 6
    INSTANT_DEATH = 7

class OverworldMenuBehaviour(enum.IntEnum):
    LEAD_TO_HP = 0
    LEAD_TO_FP = 1

class ItemPrefix(enum.IntEnum):
    """Enumeration for item name prefix icons."""

    NONE = 0x00  # No prefix (regular ASCII character)
    EMPTY_SPACE = 0x7F
    HAMMER = 0x22
    WAND = 0x28
    SHELL = 0x23
    GLOVE = 0x21
    GUN = 0x29
    MUSIC = 0x25
    CHOMP = 0x27
    FAN = 0x26
    SHIRT = 0x3C
    RING = 0x3D
    CONSUMABLE = 0x2D
    DOT = 0x2E
    BOMB = 0x3B
    QUESTION = 0x3F
    STAR = 0x40
