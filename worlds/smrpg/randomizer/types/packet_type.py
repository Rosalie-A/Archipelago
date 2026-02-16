from enum import Enum, auto


class PacketType(Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    FALLING = auto()
    STATIC = auto()
    CHEST = auto()
