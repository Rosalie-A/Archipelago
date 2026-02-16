"""Base classes for sprite development."""

from enum import IntEnum
from typing import Generic, TypeVar

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt4, UInt8

from .exceptions import (
    InvalidSpriteConstructionException,
)

class GridplaneFormats(IntEnum):
    """Enum for the various legal sizes of flat gridplane sprites."""

    THREE_WIDE_THREE_HIGH = 0
    THREE_WIDE_FOUR_HIGH = 1
    FOUR_WIDE_THREE_HIGH = 2
    FOUR_WIDE_FOUR_HIGH = 3

class Tile:
    """A grouping of subtiles, the building blocks of a mold."""

    _mirror: bool = False
    _invert: bool = False
    _format: int = 0
    _subtiles: list[bytearray | None] = []

    @property
    def mirror(self) -> bool:
        """If true, display horizontally flipped from default."""
        return self._mirror

    def set_mirror(self, mirror: bool) -> None:
        """If true, display horizontally flipped from default."""
        self._mirror = mirror

    @property
    def invert(self) -> bool:
        """If true, display vertically flipped from default."""
        return self._invert

    def set_invert(self, invert: bool) -> None:
        """If true, display vertically flipped from default."""
        self._invert = invert

    @property
    def format(self) -> int:
        """Determines special rules about the sprite contents."""
        return self._format

    def set_format(self, fmt: int) -> None:
        """Determines special rules about the sprite contents."""
        self._format = fmt

    @property
    def subtiles(self) -> list[bytearray | None]:
        """A list of 32-byte bytearrays representing graphical data."""
        return self._subtiles

    def set_subtiles(self, subtiles: list[bytearray | None]) -> None:
        """A list of 32-byte bytearrays representing graphical data."""
        for subtile in subtiles:
            if subtile is not None:
                assert len(subtile) == 32
        self._subtiles = subtiles

    def __init__(
        self,
        mirror: bool,
        invert: bool,
        fmt: int,
        subtiles: list[bytearray | None],
    ) -> None:
        self.set_mirror(mirror)
        self.set_invert(invert)
        self.set_format(fmt)
        self.set_subtiles(subtiles)

class GridplaneArrangement(Tile):
    """A tile that can be used in a gridplane sprite.\n
    Gridplane sprites are exactly one tile, where all subtiles
    are arranged in a grid with certain dimensions."""

    _is_16bit: bool = False
    _y_plus: bool = False
    _y_minus: bool = False

    @property
    def is_16bit(self) -> bool:
        """16-bit sprites can reference tiles up to 511 positions
        away from the graphics pointer, but are larger in the ROM."""
        return self._is_16bit

    def set_is_16bit(self, is_16bit: bool) -> None:
        """16-bit sprites can reference tiles up to 511 positions
        away from the graphics pointer, but are larger in the ROM."""
        self._is_16bit = is_16bit

    @property
    def y_plus(self) -> bool:
        """If true, sprite will be shifted 1 pixel up when rendered in-game."""
        return self._y_plus

    def set_y_plus(self, y_plus: bool) -> None:
        """If true, sprite will be shifted 1 pixel up when rendered in-game."""
        self._y_plus = y_plus

    @property
    def y_minus(self) -> bool:
        """If true, sprite will be shifted 1 pixel down when rendered in-game."""
        return self._y_minus

    def set_y_minus(self, y_minus: bool) -> None:
        """If true, sprite will be shifted 1 pixel down when rendered in-game."""
        self._y_minus = y_minus

    @property
    def format(self) -> GridplaneFormats:
        """The layout of the grid for this single-tile sprite."""
        return GridplaneFormats(self._format)

    def set_format(self, fmt: GridplaneFormats) -> None:
        """Set the layout of the grid for this single-tile sprite."""
        if fmt in [GridplaneFormats.THREE_WIDE_THREE_HIGH]:
            assert len(self.subtiles) == 9
        elif fmt in [
            GridplaneFormats.FOUR_WIDE_THREE_HIGH,
            GridplaneFormats.THREE_WIDE_FOUR_HIGH,
        ]:
            assert len(self.subtiles) == 12
        elif fmt in [GridplaneFormats.FOUR_WIDE_FOUR_HIGH]:
            assert len(self.subtiles) == 16
        else:
            raise InvalidSpriteConstructionException(
                f"illegal format for subtile count {len(self.subtiles)}"
            )
        super().set_format(fmt)

    def set_subtiles(
        self,
        subtiles: list[bytearray | None],
        fmt: GridplaneFormats | None = None,
    ) -> None:
        if fmt is None:
            if self.format in [GridplaneFormats.THREE_WIDE_THREE_HIGH]:
                assert len(subtiles) == 9
            elif self.format in [
                GridplaneFormats.FOUR_WIDE_THREE_HIGH,
                GridplaneFormats.THREE_WIDE_FOUR_HIGH,
            ]:
                assert len(subtiles) == 12
            elif self.format in [GridplaneFormats.FOUR_WIDE_FOUR_HIGH]:
                assert len(subtiles) == 16
            else:
                raise InvalidSpriteConstructionException(
                    f"illegal subtile count (format is {self.format})"
                )
        else:
            if fmt in [GridplaneFormats.THREE_WIDE_THREE_HIGH]:
                assert len(subtiles) == 9
            elif fmt in [
                GridplaneFormats.FOUR_WIDE_THREE_HIGH,
                GridplaneFormats.THREE_WIDE_FOUR_HIGH,
            ]:
                assert len(subtiles) == 12
            elif fmt in [GridplaneFormats.FOUR_WIDE_FOUR_HIGH]:
                assert len(subtiles) == 16
            else:
                raise InvalidSpriteConstructionException(
                    f"illegal subtile count (format is {fmt})"
                )
            self.set_format(fmt)
        super().set_subtiles(subtiles)

    # pylint: disable=W0231
    def __init__(
        self,
        fmt: GridplaneFormats,
        subtiles: list[bytearray | None],
        mirror: bool = False,
        invert: bool = False,
        y_plus: bool = False,
        y_minus: bool = False,
    ) -> None:
        super().set_mirror(mirror)
        super().set_invert(invert)
        self.set_subtiles(subtiles, fmt)
        self.set_y_plus(y_plus)
        self.set_y_minus(y_minus)

    @property
    def length(self):
        """The number of bytes this sprite is expected to occupy"""
        return 1 + len(self.subtiles) + (2 * self.is_16bit)

class NonGridplaneArrangement(Tile):
    """A tile that can be used in a gridplane sprite.\n
    Non-gridplane sprites can consist of any number of arbitrarily arranged
    tiles, where each tile is itself an arrangement of four subtiles in a square."""

    _x: UInt16 = UInt16(0)
    _y: UInt16 = UInt16(0)

    @property
    def x(self) -> UInt16:
        """The x offset of the tile."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the x offset of the tile."""
        self._x = UInt16(x)

    @property
    def y(self) -> UInt16:
        """The y offset of the tile."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the y offset of the tile."""
        self._y = UInt16(y)

    # pylint: disable=W0231
    def __init__(
        self,
        fmt: int,
        subtiles: list[bytearray | None],
        x: int,
        y: int,
        mirror: bool = False,
        invert: bool = False,
    ) -> None:
        super().set_mirror(mirror)
        super().set_invert(invert)
        super().set_format(fmt)
        self.set_subtiles(subtiles)
        self.set_x(x)
        self.set_y(y)

    @property
    def length(self):
        """The number of bytes this sprite is expected to occupy"""
        return 3 + len([s for s in self.subtiles if s is not None])

TileT = TypeVar("TileT", bound=Tile)

class Mold(Generic[TileT]):
    """A mold is a single frame of a sprite, which consists of one or more tiles."""

    _gridplane: bool
    _offset: UInt8
    _tiles: list[TileT]

    @property
    def gridplane(self) -> bool:
        """If true, the mold is a gridplane mold."""
        return self._gridplane

    @property
    def offset(self) -> UInt8:
        """(don't remember what this does)"""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """(don't remember what this does)"""
        self._offset = UInt8(offset)

    @property
    def tiles(self) -> list[TileT]:
        """The list of all the tiles in the mold."""
        return self._tiles

    def set_tiles(self, tiles: list[TileT]) -> None:
        """Overwrite the list of all the tiles in the mold."""
        self._tiles = tiles

    def __init__(
        self,
        tiles: list[TileT],
    ) -> None:
        self.set_tiles(tiles)

    def __str__(self):
        tiles = ("\n  ".join([t.__str__() for t in self.tiles]),)
        return f"<gridplane={self.gridplane} tiles=[\n  {tiles}\n]>"

class GridplaneMold(Mold[GridplaneArrangement]):
    """A single frame of a sprite that consists of exactly one gridplane tile."""

    _gridplane: bool = True

    @property
    def tile(self) -> GridplaneArrangement:
        """The gridplane tile used for this sprite."""
        return self.tiles[0]

    def set_tile(self, tile: GridplaneArrangement) -> None:
        """Replace the gridplane tile used for this sprite."""
        self._tiles = [tile]

    def __init__(
        self,
        tile: GridplaneArrangement,
    ) -> None:
        super().__init__([tile])

class NonGridplaneMold(Mold[NonGridplaneArrangement]):
    """A single frame of a sprite that consists of any number of non-gridplane tiles."""

    _gridplane: bool = False

    @property
    def tiles(self) -> list[NonGridplaneArrangement]:
        return super().tiles

    def set_tiles(self, tiles: list[NonGridplaneArrangement]) -> None:
        super().set_tiles(tiles)

    def __init__(
        self,
        tiles: list[NonGridplaneArrangement],
    ) -> None:
        super().__init__(tiles)

class SpriteSequenceFrame:
    """A single frame in an animation sequence for the sprite.\n
    Consists of a mold reference and a duration."""

    _duration: UInt8 = UInt8(0)
    _mold_id: UInt8 = UInt8(0)

    @property
    def duration(self) -> UInt8:
        """The duration of this mold's presence in frames."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration of this mold's presence in frames."""
        self._duration = UInt8(duration)

    @property
    def mold_id(self) -> UInt8:
        """The ID of the mold to use, relative to the sprite encasing both the mold
        and this sequence."""
        return self._mold_id

    def set_mold_id(self, mold_id: int) -> None:
        """Set the ID of the mold to use, relative to the sprite encasing both the mold
        and this sequence."""
        assert 0 <= mold_id < 32
        self._mold_id = UInt8(mold_id)

    def __init__(self, duration: int, mold_id: int) -> None:
        self.set_duration(duration)
        self.set_mold_id(mold_id)

class SpriteSequence:
    """An animation sequence belonging to a sprite, that uses the sprite's molds."""

    _frames: list[SpriteSequenceFrame] = []

    @property
    def frames(self) -> list[SpriteSequenceFrame]:
        """The list of frame data for this animation sequence."""
        return self._frames

    def set_frames(self, frames: list[SpriteSequenceFrame]) -> None:
        """Overwrite the list of frame data for this animation sequence."""
        self._frames = frames

    def __init__(self, frames: list[SpriteSequenceFrame]) -> None:
        self.set_frames(frames)

class AnimationData:
    """A container for mold, animation, and vram properties of the sprite."""

    _molds: list[GridplaneMold | NonGridplaneMold]
    _sequences: list[SpriteSequence]
    _vram_size: int
    _unknown: UInt4 = UInt4(0)

    @property
    def molds(self) -> list[GridplaneMold | NonGridplaneMold]:
        """The molds belonging to this sprite."""
        return self._molds

    def set_molds(self, molds: list[GridplaneMold | NonGridplaneMold]) -> None:
        """Overwrite the molds belonging to this sprite."""
        assert len(molds) <= 32
        self._molds = molds

    @property
    def sequences(self) -> list[SpriteSequence]:
        """The animation sequences belonging to this sprite."""
        return self._sequences

    def set_sequences(self, sequences: list[SpriteSequence]) -> None:
        """Overwrite the animation sequences belonging to this sprite."""
        assert len(sequences) <= 16
        self._sequences = sequences

    @property
    def vram_size(self) -> int:
        """The expected size this sprite should occupy in vram."""
        return self._vram_size

    def set_vram_size(self, vram_size: int) -> None:
        """The expected size this sprite should occupy in vram.\n
        Must be 2048, 4096, 6144, or 8192."""
        assert vram_size in [2048, 4096, 6144, 8192]
        self._vram_size = vram_size

    @property
    def unknown(self) -> UInt4:
        """(unknown)"""
        return self._unknown

    def set_unknown(self, unknown: int) -> None:
        """(unknown)"""
        self._unknown = UInt4(unknown)

    def __init__(
        self,
        molds: list[GridplaneMold | NonGridplaneMold],
        sequences: list[SpriteSequence],
        vram_size: int,
        unknown: int,
    ) -> None:
        self.set_molds(molds)
        self.set_sequences(sequences)
        self.set_vram_size(vram_size)
        self.set_unknown(unknown)

class SpriteContainer:
    """An entire sprite with all associated data."""

    _palette_id: UInt16 = UInt16(0)
    _palette_offset: UInt4 = UInt4(0)
    _unknown: UInt4 = UInt4(0)
    _animation_data: AnimationData

    @property
    def palette_id(self) -> UInt16:
        """The ID of the palette to use."""
        return self._palette_id

    def set_palette_id(self, palette_id: int) -> None:
        """Set the ID of the palette to use."""
        self._palette_id = UInt16(palette_id)

    @property
    def palette_offset(self) -> UInt4:
        """The offset of the palette to use."""
        return self._palette_offset

    def set_palette_offset(self, palette_offset: int) -> None:
        """Set the offset of the palette to use."""
        self._palette_offset = UInt4(palette_offset)

    @property
    def unknown(self) -> UInt4:
        """(unknown)"""
        return self._unknown

    def set_unknown(self, unknown: int) -> None:
        """(unknown)"""
        self._unknown = UInt4(unknown)

    @property
    def animation_data(self) -> AnimationData:
        """The collection of mold, sequence, and vram properties."""
        return self._animation_data

    def set_animation_data(self, animation_data: AnimationData) -> None:
        """Set the collection of mold, sequence, and vram properties."""
        self._animation_data = animation_data

    def __init__(
        self,
        palette_id: int,
        palette_offset: int,
        unknown: int,
        animation_data: AnimationData,
    ) -> None:
        self.set_palette_id(palette_id)
        self.set_palette_offset(palette_offset)
        self.set_unknown(unknown)
        self.set_animation_data(animation_data)
