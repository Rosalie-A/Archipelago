""" "Miscellaeous constants used for item classes and functions."""

from .enums import EquipStats

# Global item address info.
ITEMS_BASE_ADDRESS: int = 0x3A014D
ITEMS_BASE_PRICE_ADDRESS: int = 0x3A40F2
ITEMS_BASE_DESC_POINTER_ADDRESS: int = 0x3A2F20
ITEMS_DESC_DATA_POINTER_OFFSET: int = 0x3A0000
ITEMS_BASE_DESC_DATA_ADDRESSES = (
    (0x3A3120, 0x3A40F1),
    (0x3A55F0, 0x3A5FFF),
)
ITEMS_BASE_TIMING_ADDRESS: int = 0x3A438A
ITEMS_BASE_NAME_ADDRESS: int = 0x3A46EF

# Total number of items in the data.
NUM_ITEMS: int = 256

# Stats used during equipment randomization.
EQUIP_STATS: list[EquipStats] = [
    EquipStats.SPEED,
    EquipStats.ATTACK,
    EquipStats.DEFENSE,
    EquipStats.MAGIC_ATTACK,
    EquipStats.MAGIC_DEFENSE,
]
