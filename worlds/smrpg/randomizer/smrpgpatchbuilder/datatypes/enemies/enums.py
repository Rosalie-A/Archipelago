"""Enums supporting enemy classes and functions."""

from enum import IntEnum

class HitSound(IntEnum):
    """Enum for the default sound an enemy will make when attacking you."""

    BITE = 0
    PIERCE = 1
    CLAW = 2
    JAB = 3
    SLAP = 4
    KNOCK = 5
    SMASH = 6
    DEEP_KNOCK = 7
    PUNCH = 8
    BONK = 9
    FLOPPING = 10
    DEEP_JAB = 11
    BLAST_1 = 12
    BLAST_2 = 13

class FlowerBonusType(IntEnum):
    """Enum for the type of flower bonus the enemy will award you."""

    NONE = 0
    ATTACK_UP = 1
    DEFENSE_UP = 2
    HP_MAX = 3
    ONCE_AGAIN = 4
    LUCKY = 5

class ApproachSound(IntEnum):
    """Enum for the default sound an enemy will make when approaching you."""

    NONE = 0
    STARSLAP_SPIKEY_ENIGMA = 1
    SPARKY_GOOMBA_BIRDY = 2
    AMANITA_TERRAPIN = 3
    GUERRILLA = 4
    PULSAR = 5
    DRY_BONES = 6
    TORTE = 7

class CoinSprite(IntEnum):
    """Enum for the type of coin sprite displayed when enemy is defeated."""

    NONE = 0
    SMALL = 1
    BIG = 2

class EntranceStyle(IntEnum):
    """Enum for the entrance animation style of the enemy."""

    NONE = 0
    SLIDE_IN = 1
    LONG_JUMP = 2
    HOP_3_TIMES = 3
    DROP_FROM_ABOVE = 4
    ZOOM_IN_FROM_RIGHT = 5
    ZOOM_IN_FROM_LEFT = 6
    SPREAD_OUT_FROM_BACK = 7
    HOVER_IN = 8
    READY_TO_ATTACK = 9
    FADE_IN = 10
    SLOW_DROP_FROM_ABOVE = 11
    WAIT_THEN_APPEAR = 12
    SPREAD_FROM_FRONT = 13
    SPREAD_FROM_MIDDLE = 14
    READY_TO_ATTACK_2 = 15
