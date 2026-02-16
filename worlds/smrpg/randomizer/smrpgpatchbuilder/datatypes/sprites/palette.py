"""Palette classes for SMRPG sprite and event palettes.

SMRPG uses 15-bit colors (5 bits each for R, G, B) stored in SNES format.
This module stores colors as 24-bit hex integers (0xRRGGBB) for readability,
and converts to/from SNES format for ROM operations.

Sprite palettes: 819 palettes at 0x253000-0x258FFF (object/NPC palettes)
Event palettes: 273 palettes at 0x37A000-0x37BFFF (event/scene palettes)
"""

from .ids.misc import (
    COLORS_PER_PALETTE,
    EVENT_PALETTE_END,
    EVENT_PALETTE_OFFSET,
    PALETTE_SIZE,
    SPRITE_PALETTE_OFFSET,
    TOTAL_EVENT_PALETTES,
    TOTAL_SPRITE_PALETTES,
)

# Special palette offsets used for specific game locations
CLASSIC_PALETTE_OFFSET = 0x2567E6
MINECART_PALETTE_OFFSET = 0x256DFE
MAP_PALETTE_OFFSET = 0x3E99C1
HOTSPRING_PALETTE_OFFSET = 0x37B0A4


def snes_bytes_to_color(byte1: int, byte2: int) -> int:
    """Convert SNES 15-bit color (2 bytes) to 24-bit hex color.

    SNES format: byte1 = gggrrrrr, byte2 = 0bbbbbgg
    Returns: 0xRRGGBB
    """
    r5 = byte1 & 0x1F
    g5 = ((byte1 >> 5) & 0x07) | ((byte2 & 0x03) << 3)
    b5 = (byte2 >> 2) & 0x1F

    # Scale from 5-bit (0-31) to 8-bit (0-255)
    r8 = (r5 << 3) | (r5 >> 2)
    g8 = (g5 << 3) | (g5 >> 2)
    b8 = (b5 << 3) | (b5 >> 2)

    return (r8 << 16) | (g8 << 8) | b8


def color_to_snes_bytes(color: int) -> list[int]:
    """Convert 24-bit hex color to SNES 15-bit color (2 bytes).

    Input: 0xRRGGBB
    Returns: [byte1, byte2] where byte1 = gggrrrrr, byte2 = 0bbbbbgg
    """
    r8 = (color >> 16) & 0xFF
    g8 = (color >> 8) & 0xFF
    b8 = color & 0xFF

    # Scale from 8-bit to 5-bit (keep top 5 bits)
    r5 = r8 >> 3
    g5 = g8 >> 3
    b5 = b8 >> 3

    byte1 = (r5 & 0x1F) | ((g5 & 0x07) << 5)
    byte2 = ((g5 >> 3) & 0x03) | ((b5 & 0x1F) << 2)

    return [byte1, byte2]


def color_str_to_snes_bytes(color: str) -> list[int]:
    """Convert hex color string to SNES 15-bit color (2 bytes).

    Input: "RRGGBB" or "RGB" hex string (e.g., "FF0000" for red)
    Returns: [byte1, byte2] where byte1 = gggrrrrr, byte2 = 0bbbbbgg

    This uses the original SMRPG conversion algorithm for compatibility.
    """
    color_int = int(color, 16)
    r = color_int >> 19
    g = (color_int >> 10) & 0x3E
    b = (color_int >> 1) & 0x7C

    byte_1 = r + ((g << 4) & 0xF0)
    byte_2 = b + (g >> 4)
    return [byte_1, byte_2]


def palette_str_to_bytes(colors: list[str]) -> list[int]:
    """Convert list of hex color strings to SNES palette bytes.

    Args:
        colors: List of hex color strings (e.g., ["FF0000", "00FF00", ...])

    Returns:
        List of bytes representing the palette in SNES format.
    """
    ret = []
    for color in colors:
        ret += color_str_to_snes_bytes(color)
    return ret


def parse_color(color: int | str) -> int:
    """Parse a color value to integer format.

    Args:
        color: Either an integer (0xRRGGBB) or hex string ("RRGGBB")

    Returns:
        Integer color value (0xRRGGBB)
    """
    if isinstance(color, str):
        return int(color, 16)
    return color


class _BasePalette:
    """Base class for palette types."""

    _index: int
    _colors: list[int]
    _rom_offset: int  # To be set by subclasses

    @property
    def index(self) -> int:
        """The palette index."""
        return self._index

    def set_index(self, index: int) -> None:
        """Set the palette index."""
        self._index = index

    @property
    def colors(self) -> list[int]:
        """The 15 colors in this palette as 24-bit hex integers."""
        return self._colors

    def set_colors(self, colors: list[int]) -> None:
        """Set the palette colors.

        Args:
            colors: List of 15 colors as 24-bit hex integers (0xRRGGBB).
        """
        if len(colors) != COLORS_PER_PALETTE:
            raise ValueError(f"Palette must have exactly {COLORS_PER_PALETTE} colors")
        self._colors = list(colors)

    def get_color(self, index: int) -> int:
        """Get a single color by index (0-14)."""
        return self._colors[index]

    def set_color(self, index: int, color: int) -> None:
        """Set a single color by index (0-14)."""
        self._colors[index] = color

    @property
    def rom_address(self) -> int:
        """The ROM address where this palette is stored."""
        return self._rom_offset + self._index * PALETTE_SIZE

    def to_bytes(self) -> bytearray:
        """Convert palette to ROM bytes (30 bytes)."""
        result = bytearray()
        for color in self._colors:
            result.extend(color_to_snes_bytes(color))
        return result

    def special_palette(
        self, color_indices: list[int | None], address: int
    ) -> dict[int, bytearray]:
        """Write specific colors from this palette to an address using index mapping.

        This allows writing a subset of colors to a different location,
        useful for special palette locations like dolls, minecart, etc.

        Args:
            color_indices: List of color indices to write. Use None to skip a slot.
                          e.g., [0, 1, None, 3] writes colors 0, 1, skips slot 2, writes color 3
            address: The ROM address to write to.

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        patch: dict[int, bytearray] = {}
        for j, i in enumerate(color_indices):
            if i is not None:
                color = self._colors[i]
                patch[address + j * 2] = bytearray(color_to_snes_bytes(color))
        return patch

    def palette_override(
        self, colors: list[int | str], address: int
    ) -> dict[int, bytearray]:
        """Write a list of colors to a specific ROM address.

        Args:
            colors: List of colors (as integers 0xRRGGBB or hex strings "RRGGBB")
            address: The ROM address to write to.

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        patch: dict[int, bytearray] = {}
        for j, color in enumerate(colors):
            color_int = parse_color(color)
            patch[address + j * 2] = bytearray(color_to_snes_bytes(color_int))
        return patch

    def write_to_address(self, address: int) -> dict[int, bytearray]:
        """Write this entire palette to a specific ROM address.

        Args:
            address: The ROM address to write to.

        Returns:
            Dictionary mapping ROM address to byte data.
        """
        return {address: self.to_bytes()}

    def write_colors_to_address(
        self, address: int, start_index: int = 0, count: int | None = None
    ) -> dict[int, bytearray]:
        """Write a range of colors from this palette to an address.

        Args:
            address: The ROM address to write to.
            start_index: Index of first color to write (default 0).
            count: Number of colors to write (default all remaining).

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        if count is None:
            count = COLORS_PER_PALETTE - start_index

        result = bytearray()
        for i in range(start_index, start_index + count):
            result.extend(color_to_snes_bytes(self._colors[i]))
        return {address: result}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._index}, [{', '.join(f'0x{c:06X}' for c in self._colors)}])"


class SpritePalette(_BasePalette):
    """A single SMRPG sprite palette containing 15 colors.

    Sprite palettes are used for object/NPC graphics.
    Colors are stored as 24-bit hex integers (0xRRGGBB format).
    """

    _rom_offset = SPRITE_PALETTE_OFFSET

    @classmethod
    def from_bytes(cls, index: int, data: bytes | bytearray) -> "SpritePalette":
        """Create a SpritePalette from ROM bytes.

        Args:
            index: The palette index.
            data: 30 bytes of palette data.
        """
        if len(data) != PALETTE_SIZE:
            raise ValueError(f"Palette data must be exactly {PALETTE_SIZE} bytes")

        colors = []
        for i in range(COLORS_PER_PALETTE):
            byte1 = data[i * 2]
            byte2 = data[i * 2 + 1]
            colors.append(snes_bytes_to_color(byte1, byte2))

        palette = cls(index, colors)
        return palette

    @classmethod
    def from_color_strings(cls, index: int, colors: list[str]) -> "SpritePalette":
        """Create a SpritePalette from hex color strings.

        Args:
            index: The palette index.
            colors: List of 15 hex color strings (e.g., ["FF0000", "00FF00", ...])
        """
        color_ints = [int(c, 16) for c in colors]
        return cls(index, color_ints)

    def __init__(self, index: int, colors: list[int] | None = None) -> None:
        """Create a new SpritePalette.

        Args:
            index: The palette index (0-818).
            colors: Optional list of 15 colors as 24-bit hex integers.
                   If not provided, initializes to all black (0x000000).
        """
        self.set_index(index)
        if colors is None:
            colors = [0x000000] * COLORS_PER_PALETTE
        self.set_colors(colors)


class EventPalette(_BasePalette):
    """A single SMRPG event palette containing 15 colors.

    Event palettes are used for event/scene graphics.
    Colors are stored as 24-bit hex integers (0xRRGGBB format).
    """

    _rom_offset = EVENT_PALETTE_OFFSET

    @classmethod
    def from_bytes(cls, index: int, data: bytes | bytearray) -> "EventPalette":
        """Create an EventPalette from ROM bytes.

        Args:
            index: The palette index.
            data: 30 bytes of palette data.
        """
        if len(data) != PALETTE_SIZE:
            raise ValueError(f"Palette data must be exactly {PALETTE_SIZE} bytes")

        colors = []
        for i in range(COLORS_PER_PALETTE):
            byte1 = data[i * 2]
            byte2 = data[i * 2 + 1]
            colors.append(snes_bytes_to_color(byte1, byte2))

        palette = cls(index, colors)
        return palette

    @classmethod
    def from_color_strings(cls, index: int, colors: list[str]) -> "EventPalette":
        """Create an EventPalette from hex color strings.

        Args:
            index: The palette index.
            colors: List of 15 hex color strings (e.g., ["FF0000", "00FF00", ...])
        """
        color_ints = [int(c, 16) for c in colors]
        return cls(index, color_ints)

    def __init__(self, index: int, colors: list[int] | None = None) -> None:
        """Create a new EventPalette.

        Args:
            index: The palette index (0-272).
            colors: Optional list of 15 colors as 24-bit hex integers.
                   If not provided, initializes to all black (0x000000).
        """
        self.set_index(index)
        if colors is None:
            colors = [0x000000] * COLORS_PER_PALETTE
        self.set_colors(colors)


class SpritePaletteCollection(list[SpritePalette]):
    """Collection of all 819 SMRPG sprite palettes.

    Provides methods to load palettes from ROM and render them back.
    """

    def render(self) -> dict[int, bytearray]:
        """Convert all palettes to ROM patch format.

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        # Collect all palette bytes into a single block
        all_bytes = bytearray()
        for palette in self:
            all_bytes.extend(palette.to_bytes())

        return {SPRITE_PALETTE_OFFSET: all_bytes}

    def get_palette(self, index: int) -> SpritePalette:
        """Get a palette by index."""
        return self[index]

    def set_palette(self, index: int, palette: SpritePalette) -> None:
        """Set a palette by index."""
        self[index] = palette

    @classmethod
    def from_rom(cls, rom_data: bytes | bytearray) -> "SpritePaletteCollection":
        """Create a SpritePaletteCollection by reading from ROM data.

        Args:
            rom_data: The full ROM data.
        """
        collection = cls()

        for i in range(TOTAL_SPRITE_PALETTES):
            offset = SPRITE_PALETTE_OFFSET + i * PALETTE_SIZE
            palette_bytes = rom_data[offset:offset + PALETTE_SIZE]
            palette = SpritePalette.from_bytes(i, palette_bytes)
            collection.append(palette)

        return collection

    @classmethod
    def empty(cls) -> "SpritePaletteCollection":
        """Create an empty SpritePaletteCollection with 819 black palettes."""
        collection = cls()
        for i in range(TOTAL_SPRITE_PALETTES):
            collection.append(SpritePalette(i))
        return collection

    def __init__(self, palettes: list[SpritePalette] | None = None) -> None:
        """Create a new SpritePaletteCollection.

        Args:
            palettes: Optional list of palettes. If not provided, creates empty collection.
        """
        if palettes is None:
            palettes = []
        super().__init__(palettes)


class EventPaletteCollection(list[EventPalette]):
    """Collection of all 273 SMRPG event palettes.

    Provides methods to load palettes from ROM and render them back.
    """

    def render(self) -> dict[int, bytearray]:
        """Convert all palettes to ROM patch format.

        Returns:
            Dictionary mapping ROM addresses to byte data.
            Includes padding to fill the entire event palette space.
        """
        # Collect all palette bytes into a single block
        all_bytes = bytearray()
        for palette in self:
            all_bytes.extend(palette.to_bytes())

        # Pad to fill the entire space (10 leftover bytes)
        total_space = EVENT_PALETTE_END - EVENT_PALETTE_OFFSET
        if len(all_bytes) < total_space:
            all_bytes.extend(bytearray(total_space - len(all_bytes)))

        return {EVENT_PALETTE_OFFSET: all_bytes}

    def get_palette(self, index: int) -> EventPalette:
        """Get a palette by index."""
        return self[index]

    def set_palette(self, index: int, palette: EventPalette) -> None:
        """Set a palette by index."""
        self[index] = palette

    @classmethod
    def from_rom(cls, rom_data: bytes | bytearray) -> "EventPaletteCollection":
        """Create an EventPaletteCollection by reading from ROM data.

        Args:
            rom_data: The full ROM data.
        """
        collection = cls()

        for i in range(TOTAL_EVENT_PALETTES):
            offset = EVENT_PALETTE_OFFSET + i * PALETTE_SIZE
            palette_bytes = rom_data[offset:offset + PALETTE_SIZE]
            palette = EventPalette.from_bytes(i, palette_bytes)
            collection.append(palette)

        return collection

    @classmethod
    def empty(cls) -> "EventPaletteCollection":
        """Create an empty EventPaletteCollection with 273 black palettes."""
        collection = cls()
        for i in range(TOTAL_EVENT_PALETTES):
            collection.append(EventPalette(i))
        return collection

    def __init__(self, palettes: list[EventPalette] | None = None) -> None:
        """Create a new EventPaletteCollection.

        Args:
            palettes: Optional list of palettes. If not provided, creates empty collection.
        """
        if palettes is None:
            palettes = []
        super().__init__(palettes)


# Legacy aliases for backwards compatibility
Palette = SpritePalette
PaletteCollection = SpritePaletteCollection

# Legacy function aliases (from randomizer/data/allies/palettes/types.py)
color_to_bytes = color_str_to_snes_bytes
palette_to_bytes = palette_str_to_bytes

# Re-export offset constants with legacy names
classic_palette_offset = CLASSIC_PALETTE_OFFSET
minecart_palette_offset = MINECART_PALETTE_OFFSET
map_palette_offset = MAP_PALETTE_OFFSET
hotspring_palette_offset = HOTSPRING_PALETTE_OFFSET


def address_to_sprite_palette_index(address: int) -> int | None:
    """Convert a ROM address to sprite palette index.

    Args:
        address: ROM address that should be within sprite palette range.

    Returns:
        Palette index (0-818) if address is in sprite palette range,
        None if address is outside the range.
    """
    if address < SPRITE_PALETTE_OFFSET or address >= SPRITE_PALETTE_OFFSET + TOTAL_SPRITE_PALETTES * PALETTE_SIZE:
        return None
    offset = address - SPRITE_PALETTE_OFFSET
    if offset % PALETTE_SIZE != 0:
        # Address doesn't align to palette boundary
        return None
    return offset // PALETTE_SIZE


def address_to_event_palette_index(address: int) -> int | None:
    """Convert a ROM address to event palette index.

    Args:
        address: ROM address that should be within event palette range.

    Returns:
        Palette index (0-9556) if address is in event palette range,
        None if address is outside the range.
    """
    if address < EVENT_PALETTE_OFFSET or address >= EVENT_PALETTE_END:
        return None
    offset = address - EVENT_PALETTE_OFFSET
    if offset % PALETTE_SIZE != 0:
        # Address doesn't align to palette boundary
        return None
    return offset // PALETTE_SIZE


def sprite_palette_index_to_address(index: int) -> int:
    """Convert a sprite palette index to ROM address."""
    return SPRITE_PALETTE_OFFSET + index * PALETTE_SIZE


def event_palette_index_to_address(index: int) -> int:
    """Convert an event palette index to ROM address."""
    return EVENT_PALETTE_OFFSET + index * PALETTE_SIZE
