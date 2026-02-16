"""Enums supporting character classes and functions."""

from enum import Enum

class LevelStats(str, Enum):
    """An enumerator for the stats that can be incresed upon levelup."""

    MAX_HP = "max_hp"
    ATTACK = "attack"
    DEFENSE = "defense"
    MAGIC_ATTACK = "magic_attack"
    MAGIC_DEFENSE = "magic_defense"
