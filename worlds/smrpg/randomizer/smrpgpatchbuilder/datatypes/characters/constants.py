""""Miscellaeous constants used for playable character classes and functions."""

from .enums import LevelStats

LEVELUP_BASE_ADDRESS: int = 0x3A1AFF

LEVEL_CURVE: list[int] = [
    0,
    16,
    48,
    84,
    130,
    200,
    290,
    402,
    538,
    700,
    890,
    1110,
    1360,
    1640,
    1950,
    2290,
    2660,
    3060,
    3490,
    3950,
    4440,
    4960,
    5510,
    6088,
    6692,
    7320,
    7968,
    8634,
    9315,
    9999,
]

CHARACTER_BASE_ADDRESS: int = 0x3A002C
CHARACTER_BASE_STAT_GROWTH_ADDRESS: int = 0x3A1B39
CHARACTER_BASE_STAT_BONUS_ADDRESS: int = 0x3A1CEC
CHARACTER_BASE_LEARNED_SPELLS_ADDRESS: int = 0x3A42F5

# Stats used during levelups.
CHARACTER_LEVEL_STATS: list[str] = [
    LevelStats.MAX_HP,
    LevelStats.ATTACK,
    LevelStats.DEFENSE,
    LevelStats.MAGIC_ATTACK,
    LevelStats.MAGIC_DEFENSE,
]
ENDING_PALETTES: list[tuple[int, int]] = [
    (0x37A9D8, 0x37B31A),
    (0x37B086, 0x37B338),
    (0x37B068, 0x37B356),
    (0x37AA14, 0x37B392),
    (0x37A9F6, 0x37B374),
]
