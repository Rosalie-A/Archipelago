"""Int subclass instances representing the behaviour of an object shift."""

from .types.classes import ShiftType

SHIFT_TYPE_0X00 = ShiftType(0)
SHIFT_TYPE_SHIFT = ShiftType(2)
SHIFT_TYPE_TRANSFER = ShiftType(4)
SHIFT_TYPE_0X04 = ShiftType(6)
SHIFT_TYPE_0X08 = ShiftType(8)
