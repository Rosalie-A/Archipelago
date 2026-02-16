"""Int subclass instances representing coordinate axes for commands requiring a coordinate
or coordinate set."""

from .types.coord import Coord

COORD_X = Coord(0x00)
COORD_Y = Coord(0x01)
COORD_Z = Coord(0x02)
COORD_F = Coord(0x05)
