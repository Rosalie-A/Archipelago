"""Int subclass instances representing the origin point that coords should be relative to."""

from .types.classes import Origin

ABSOLUTE_POSITION = Origin(0)
CASTER_INITIAL_POSITION = Origin(1)
TARGET_CURRENT_POSITION = Origin(2)
CASTER_CURRENT_POSITION = Origin(3)
