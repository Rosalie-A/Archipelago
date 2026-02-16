"""Int subclass instances representing valid directions in which an object can walk or face."""

from .types.direction import Direction

EAST = Direction(0b0)
SOUTHEAST = Direction(0b1)
SOUTH = Direction(0b10)
SOUTHWEST = Direction(0b11)
WEST = Direction(0b100)
NORTHWEST = Direction(0b101)
NORTH = Direction(0b110)
NORTHEAST = Direction(0b111)
