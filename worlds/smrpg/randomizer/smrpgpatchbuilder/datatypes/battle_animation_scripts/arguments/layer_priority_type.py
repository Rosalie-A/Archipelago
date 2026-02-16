"""Int subclass instances meaningfully representing layer priority in battle animations."""

from .types.classes import LayerPriorityType

TRANSPARENCY_OFF = LayerPriorityType(0)
OVERLAP_ALL = LayerPriorityType(1)
OVERLAP_NONE = LayerPriorityType(2)
OVERLAP_ALL_EXCEPT_ALLIES = LayerPriorityType(3)
