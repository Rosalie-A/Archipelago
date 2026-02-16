"""Int subclass instances representing valid sprite sequence playback speeds."""

from .types.classes import (
    SequenceSpeed,
)

NORMAL = SequenceSpeed(0)
FAST = SequenceSpeed(1)
FASTER = SequenceSpeed(2)
VERY_FAST = SequenceSpeed(3)
FASTEST = SequenceSpeed(4)
SLOW = SequenceSpeed(5)
VERY_SLOW = SequenceSpeed(6)
