"""Int subclass instances representing special effects that can be applied to a palette."""

from .types.palette_type import PaletteType

NOTHING = PaletteType(0x00)
GLOW = PaletteType(0x06)
SET_TO = PaletteType(0x0C)
FADE_TO = PaletteType(0x0E)
