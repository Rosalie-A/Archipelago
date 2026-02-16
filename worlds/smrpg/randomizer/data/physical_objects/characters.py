from ...types.physical_objects import NPC
from ..rooms.npcs import (
    BOWSER_WALKING_DOWN_LEFT_NPC_2,
    GENO_WALKING_DOWN_LEFT_NPC_2_CLONEABLE,
    MALLOW_WALKING_DOWN_LEFT_NPC_2,
    MARIO_CLONE_WALKING_DOWN_LEFT_NPC,
    TOADSTOOL_WALKING_DOWN_LEFT_LOW_VRAM,
)


class MarioCharacterNPC(NPC):
    """Mario character NPC wrapper for recruitment prizes."""

    _base = MARIO_CLONE_WALKING_DOWN_LEFT_NPC


class MallowCharacterNPC(NPC):
    """Mallow character NPC wrapper for recruitment prizes."""

    _base = MALLOW_WALKING_DOWN_LEFT_NPC_2


class GenoCharacterNPC(NPC):
    """Geno character NPC wrapper for recruitment prizes."""

    _base = GENO_WALKING_DOWN_LEFT_NPC_2_CLONEABLE


class BowserCharacterNPC(NPC):
    """Bowser character NPC wrapper for recruitment prizes."""

    _base = BOWSER_WALKING_DOWN_LEFT_NPC_2


class ToadstoolCharacterNPC(NPC):
    """Toadstool character NPC wrapper for recruitment prizes."""

    _base = TOADSTOOL_WALKING_DOWN_LEFT_LOW_VRAM
