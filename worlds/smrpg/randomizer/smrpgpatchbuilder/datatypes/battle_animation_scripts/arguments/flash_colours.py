"""Int subclass instances describing screen flash colours in battle animations."""

from .types.classes import FlashColour

NO_COLOUR = FlashColour(0)
RED = FlashColour(1)
GREEN = FlashColour(2)
YELLOW = FlashColour(3)
BLUE = FlashColour(4)
PINK = FlashColour(5)
AQUA = FlashColour(6)
WHITE = FlashColour(7)
FADED = FlashColour(8) # might not work w/o VC adjustments - accessibility feature
