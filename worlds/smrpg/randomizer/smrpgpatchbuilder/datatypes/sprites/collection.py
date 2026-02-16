"""Base classes for the entire game sprite collection."""

from functools import cmp_to_key
from math import trunc

from random import choices
from copy import deepcopy
from smrpgpatchbuilder.datatypes.dialogs.ids.misc import (
    DIALOG_BANK_22_ENDS,
    DIALOG_BANK_23_ENDS,
)

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt8

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
)

from .disassembler import ImagePack
from .exceptions import (
    InvalidSpriteConstructionException,
)
from .sprite import (
    AnimationData,
    GridplaneArrangement,
    GridplaneFormats,
    GridplaneMold,
    Mold,
    NonGridplaneArrangement,
    NonGridplaneMold,
    SpriteContainer,
    SpriteSequence,
    Tile,
)
from .ids.misc import (
    ALPHABET,
    ANIMATION_PTRS_END,
    ANIMATION_PTRS_START,
    IMAGE_PTRS_END,
    IMAGE_PTRS_START,
    MAX_MOLDS_PER_SPRITE,
    MAX_SEQUENCES_PER_SPRITE,
    PALETTE_OFFSET,
    SPRITE_PTRS_END,
    SPRITE_PTRS_START,
    TOTAL_ANIMATIONS,
    TOTAL_IMAGES,
    UNCOMPRESSED_GFX_END,
    UNCOMPRESSED_GFX_START,
)

# Glossary:
#
# Sprite: graphical assets and animation data for those assets
#   for an NPC in the overworld.
#
# Subtile: 32 bytes of raw pixel data.
#
# Subtile group: A collection of subtiles and what sprites share them.
#
# Tile: A grouping of subtiles, the building blocks of a mold.
#
# Mold: An individual animation frame for a sprite. Can be either a
#   gridplane or a non-gridplane.
#
# Gridplane mold: A mold that consists of exactly one tile,
#   which itself consists of subtiles aligned in a grid.
#   The grid may be 3x3, 4x4, 3x4, or 4x3.
#   These are used as much as possible as they use almost no VRAM.
#
# Non-gridplane mold: A mold that consists of several tiles,
#   where each tile is a 2x2 arrangement of subtiles.
#   Those 2x2 tiles can be arranged freeform and even overlapping.
#   These can be much heavier on VRAM depending on how many tiles are used.
#
# Clone: A clone is a copy of a 2x2 tile (or consecutive series of 2x2 tiles)
#   used elsewhere in the same sprite. It is used to alleviate some of the VRAM being
#   used by the sprite. It can reference any prior mold in the sprite.
#
# Sequence: An animation definition using the molds of a sprite.
#
# Animation data: A container for the rules of how molds and sequences are arranged
#   for a sprite. Multiple sprites can use the same animation data, such as recolours
#   of the same enemy.
#
# Image data: A container for the rules of where specifically in the ROM that a sprite
#   should be reading subtile data from to use with its animation data.
#
# please do not ask me anything about how this works because beyond this i genuinely have no idea.
# i wrote this in like 2021 and am afraid of touching it


class _SpriteRawDataBank:
    """Represents a contiguous block of raw sprite data bytes within a ROM.\n
    Can be either subtile data or animation data.\n
    Should always have the same upper byte, i.e. 0x280000-0x28FFFF."""

    _start: int = 0
    _end: int = 0
    _raw_bytes: bytearray = bytearray()

    @property
    def start(self) -> int:
        """The beginning of this ROM data block."""
        return self._start

    def set_start(self, start: int) -> None:
        """Designate the beginning of this ROM data block."""
        self._start = start

    @property
    def end(self) -> int:
        """The end of this ROM data block."""
        return self._end

    def set_end(self, end: int) -> None:
        """Designate the end of this ROM data block."""
        self._end = end

    @property
    def raw_bytes(self) -> bytearray:
        """The contents of the raw data block."""
        return self._raw_bytes

    def set_raw_bytes(self, raw_bytes: bytearray) -> None:
        """Overwrite the contents of the raw data block."""
        self._raw_bytes = raw_bytes

    def extend_raw_bytes(self, raw_bytes: bytearray) -> None:
        """Add raw data."""
        self._raw_bytes += raw_bytes

    @property
    def remaining_space(self):
        """The current amount of unused bytes in this block."""
        return self.end - self.start - len(self.raw_bytes)

    @property
    def current_offset(self):
        """The absolute ROM address where this raw data block's
        unused space currently begins (not occupied yet)."""
        return self.start + len(self.raw_bytes)

    def __init__(self, start: int, end: int):
        self.set_start(start)
        self.set_end(end)
        self.set_raw_bytes(bytearray())


class _SpriteRawDataBankCollection(list[_SpriteRawDataBank]):
    """Represents the entirety of either subtile data or animation data in the ROM,
    divided up into banks."""

    def place_bytes(self, these_bytes: bytearray):
        """Given a set of raw data bytes, places them into the bank
        that currently has the most empty space.\n
        It is a good idea to use this in a function that places
        raw data in order from longest to shortest."""
        # LAZYSHELL reads 0x4000 bytes for each sprite graphics block.
        # To prevent corruption from cross-bank reads, we must ensure that
        # the entire 0x4000-byte read stays within the same bank.
        # This means we need at least 0x4000 bytes remaining after placement.

        GRAPHICS_READ_SIZE = 0x4000

        # find bank with most space that can accommodate the data + buffer safely
        highest_space = 0
        index = 0
        for bank_index, bank in enumerate(self):
            # Check if this bank can accommodate data + full graphics read buffer
            total_space_needed = len(these_bytes) + GRAPHICS_READ_SIZE

            if bank.remaining_space >= total_space_needed:
                if highest_space < bank.remaining_space:
                    highest_space = bank.remaining_space
                    index = bank_index

        # If no bank can accommodate data + buffer, fall back to largest available bank
        # (this maintains existing behavior if strict buffer requirement can't be met)
        if highest_space == 0:
            for bank_index, bank in enumerate(self):
                if bank.remaining_space >= len(these_bytes):
                    if highest_space < bank.remaining_space:
                        highest_space = bank.remaining_space
                        index = bank_index

        if len(these_bytes) > self[index].remaining_space:
            raise ScriptBankTooLongException(
                "could not place bytes into a bank with space"
            )
        offset = self[index].current_offset
        self[index].extend_raw_bytes(these_bytes)
        return offset


_SUBTILE_BANKS = _SpriteRawDataBankCollection(
    [
        _SpriteRawDataBank(UNCOMPRESSED_GFX_START, 0x290000),
        _SpriteRawDataBank(0x290000, 0x2A0000),
        _SpriteRawDataBank(0x2A0000, 0x2B0000),
        _SpriteRawDataBank(0x2B0000, 0x2C0000),
        _SpriteRawDataBank(0x2C0000, 0x2D0000),
        _SpriteRawDataBank(0x2D0000, 0x2E0000),
        _SpriteRawDataBank(0x2E0000, 0x2F0000),
        _SpriteRawDataBank(0x2F0000, 0x300000),
        _SpriteRawDataBank(0x300000, 0x310000),
        _SpriteRawDataBank(0x310000, 0x320000),
        _SpriteRawDataBank(0x320000, 0x330000),
        # _SpriteRawDataBank(0x330000, UNCOMPRESSED_GFX_END),
        _SpriteRawDataBank(0x360000, 0x370000),
        _SpriteRawDataBank(0x379A00, 0x37A000),
    ]
)

_ANIMATION_DATA_BANKS = [
    _SpriteRawDataBank(0x1A4DA0, 0x1A8000),
    _SpriteRawDataBank(0x1BFC12, 0x1C0000),
    _SpriteRawDataBank(0x1C6505, 0x1C8000),
    _SpriteRawDataBank(DIALOG_BANK_22_ENDS, 0x22FD18),
    _SpriteRawDataBank(DIALOG_BANK_23_ENDS, 0x23F2D5),
    _SpriteRawDataBank(0x24EDE0, 0x250000),
    _SpriteRawDataBank(0x259000, 0x260000),
    _SpriteRawDataBank(0x260000, 0x270000),
    _SpriteRawDataBank(0x270000, UNCOMPRESSED_GFX_START),
    _SpriteRawDataBank(0x384DD0, 0x385000),
    _SpriteRawDataBank(0x385E40, 0x386000),
    _SpriteRawDataBank(0x387220, 0x387400),
    _SpriteRawDataBank(0x3878F0, 0x387A00),
    _SpriteRawDataBank(0x387CC0, 0x388000),
    _SpriteRawDataBank(0x392690, 0x392AA0),
    _SpriteRawDataBank(0x3DB5E0, 0x3DC000),
    _SpriteRawDataBank(0x3DD800, 0x3DF000),
    _SpriteRawDataBank(0x3EF610, 0x3EF700),
]
# classes for managing tile data as it is being collected


class _SubtileTuple(
    tuple[
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
    ]
):
    """Python representation of raw tile data. Tuple of 32 bytes."""

    def __new__(cls, subtile_bytes: bytearray):
        assert len(subtile_bytes) == 0x20
        return tuple.__new__(cls, tuple(subtile_bytes))


class _SubtileSorter(tuple[_SubtileTuple, list[int]]):
    """Used to help sort raw subtile data such that as many NPCs as possible
    using the same subtile set can re-use subtiles, where the relative IDs of those
    subtiles need to be within a certain range of each other."""

    def __new__(cls, subtile_bytes: _SubtileTuple, ids: list[int]):
        return tuple.__new__(cls, (subtile_bytes, ids))


class _SubtileGroup:
    """Used to facilitate grouping of subtiles together by which sprites use them."""

    _used_by: list[int] = []
    _subtiles: list[_SubtileTuple] = []
    _extra: list[_SubtileTuple] = []
    _offset: int = 0

    @property
    def used_by(self) -> list[int]:
        """The IDs of sprites which use at least some of these tiles."""
        return self._used_by

    def set_used_by(self, used_by: list[int]) -> None:
        """Overwrite the ID list of sprites which use at least some of these tiles."""
        self._used_by = used_by

    def add_used_by(self, index: int) -> None:
        """Add to the ID list of sprites which use at least some of these tiles."""
        if index not in self._used_by:
            self._used_by.append(index)

    @property
    def subtiles(self) -> list[_SubtileTuple]:
        """The raw subtile data at least partially used by every sprite in this group."""
        return self._subtiles

    def set_subtiles(self, subtiles: list[bytearray] | list[_SubtileTuple]) -> None:
        """Overwrite the raw tile data at least partially used by every sprite in this group."""
        self._subtiles = [
            _SubtileTuple(t) if isinstance(t, bytearray) else t for t in subtiles
        ]

    def extend_subtiles(self, subtiles: set[bytearray] | set[_SubtileTuple]) -> None:
        """Add to the raw tile data at least partially used by every sprite in this group."""
        incoming = [
            _SubtileTuple(t) if isinstance(t, bytearray) else t
            for t in subtiles
            if t not in self.subtiles
        ]
        self.subtiles.extend(incoming)

    @property
    def offset(self) -> int:
        """The offset in the ROM where this group of subtiles will begin."""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """Set the offset in the ROM where this group of subtiles will begin."""
        self._offset = offset

    @property
    def extra(self) -> list[_SubtileTuple]:
        """Duplicated tiles, populated only when it does not seem possible to
        make sure that every sprite using a subtile group can use the sprites it
        needs within 511 indexes of each other."""
        return self._extra

    def set_extra(self, extra: list[_SubtileTuple]) -> None:
        """Duplicated tiles, populated only when it does not seem possible to
        make sure that every sprite using a subtile group can use the sprites it
        needs within 511 indexes of each other."""
        self._extra = extra

    def __init__(
        self,
        used_by: list[int],
        subtiles: list[bytearray] | list[_SubtileTuple],
        extra: list[_SubtileTuple] | None = None,
    ) -> None:
        if extra is None:
            extra = []
        self.set_used_by(used_by)
        self.set_subtiles(subtiles)


class _TileGroupSet(dict[str, _SubtileGroup]):
    """A managerial class for all by-shared-sprites tile groupings."""

    def get_most_similar_subtileset(
        self, subtileset: set[_SubtileTuple]
    ) -> tuple[str | None, float]:
        """Given tile data of a specific sprite, find the tile group
        that it should most likely be merged into."""
        best = None
        best_similarity = 0
        for key in self:
            similarity = _tileset_similarity(list(subtileset), list(self[key].subtiles))
            if similarity > best_similarity:
                best_similarity = similarity
                best = key
        if best is not None:
            return best, max(
                best_similarity / len(subtileset),
                best_similarity / len(self[best].subtiles),
            )
        return None, 0


# classes for building graphics structures that need to include indexes instead of assets


class _WorkingTile(Tile):
    """Represents a tile in the process of being converted to ROM patch bytes."""

    _subtiles: list[int] = []
    _offset: int = 0

    @property
    def offset(self) -> int:
        """Where this sprite will ultimately sit within the ROM."""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """Where this sprite will ultimately sit within the ROM."""
        self._offset = offset

    @property
    def subtiles(self) -> list[int]:
        return self._subtiles

    def set_subtiles(self, subtiles: list[int]) -> None:
        self._subtiles = subtiles

    # pylint: disable=W0231
    def __init__(
        self,
        mirror: bool,
        invert: bool,
        fmt: int,
    ) -> None:
        super().set_mirror(mirror)
        super().set_invert(invert)
        super().set_format(fmt)
        self.set_subtiles([])


class _WorkingGridplaneArrangement(_WorkingTile, GridplaneArrangement):
    """Represents a gridplane mold in the process of being converted to ROM patch bytes.\n
    Gridplanes are arrangements of tiles that have to follow a grid of a specified size.
    They are very VRAM-efficient."""

    def set_subtiles(
        self,
        subtiles: list[int],
        fmt: GridplaneFormats | None = None,
    ) -> None:
        """Set the order of indexes pointing to raw tile data."""
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
                    "illegal subtile count for given format"
                )
            self.set_format(fmt)
        super().set_subtiles(subtiles)

    # pylint: disable=W0231
    def __init__(self, arrangement: GridplaneArrangement) -> None:
        self.set_mirror(arrangement.mirror)
        self.set_invert(arrangement.invert)
        super().set_format(arrangement.format)
        super().set_y_plus(arrangement.y_plus)
        super().set_y_minus(arrangement.y_minus)


class _WorkingNonGridplaneArrangement(_WorkingTile, NonGridplaneArrangement):
    """Represents a non-gridplane tile grouping in the process of being
    converted to ROM patch bytes.\n
    These are always an arrangement of four raw tiles in a square.\n
    Non-gridplane molds are freeform arrangements of many of these groupings.
    They may be more VRAM-heavy than non-gridplane molds."""

    # pylint: disable=W0231
    def __init__(self, arrangement: NonGridplaneArrangement) -> None:
        super().set_mirror(arrangement.mirror)
        super().set_invert(arrangement.invert)
        super().set_format(arrangement.format)
        super().set_x(arrangement.x)
        super().set_y(arrangement.y)


class _Clone:
    """A clone uses the same raw data as another gridplane
    arrangement (or series of consecutive gridplane arrangements) within the same mold,
    where the clone tile must be placed after the non-clone tile."""

    _offset: UInt8
    _tiles: list[_WorkingNonGridplaneArrangement]
    _x: UInt16 = UInt16(0)
    _y: UInt16 = UInt16(0)
    _mirror: bool = False
    _invert: bool = False

    @property
    def offset(self) -> UInt8:
        """The ROM offset at which this clone will be written."""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """Specify the ROM offset at which this clone will be written."""
        self._offset = UInt8(offset)

    @property
    def tiles(self) -> list[_WorkingNonGridplaneArrangement]:
        """The tile data being referenced by this clone."""
        return self._tiles

    def set_tiles(self, tiles: list[_WorkingNonGridplaneArrangement]) -> None:
        """Overwrite the tile data being referenced by this clone."""
        self._tiles = tiles

    @property
    def x(self) -> UInt16:
        """The X coord of this clone."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coord of this clone."""
        self._x = UInt16(x)

    @property
    def y(self) -> UInt16:
        """The Y coord of this clone."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord of this clone."""
        self._y = UInt16(y)

    @property
    def mirror(self) -> bool:
        """If true, the tile is flipped horizontally compared to its parent."""
        return self._mirror

    def set_mirror(self, mirror: bool) -> None:
        """If true, the tile is flipped horizontally compared to its parent."""
        self._mirror = mirror

    @property
    def invert(self) -> bool:
        """If true, the tile is flipped vertically compared to its parent."""
        return self._invert

    def set_invert(self, invert: bool) -> None:
        """If true, the tile is flipped vertically compared to its parent."""
        self._invert = invert

    def __init__(
        self,
        tiles: list[_WorkingNonGridplaneArrangement],
        x: int,
        y: int,
        mirror: bool,
        invert: bool,
    ) -> None:
        self.set_tiles(tiles)
        self.set_x(x)
        self.set_y(y)
        self.set_mirror(mirror)
        self.set_invert(invert)


class _WorkingMold:
    """A mold in the process of being converted to ROM bytes."""

    _base_mold: Mold
    _offset: int = 0

    @property
    def offset(self) -> int:
        """The ROM offset at which this mold will be written."""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """Specify the ROM offset at which this mold will be written."""
        self._offset = offset

    @property
    def base_mold(self) -> Mold:
        """The mold class to convert to bytes."""
        return self._base_mold

    def set_base_mold(self, base_mold: Mold) -> None:
        """Designate the mold class to convert to bytes."""
        self._base_mold = base_mold

    def __init__(self, base_mold: Mold) -> None:
        self.set_base_mold(base_mold)


class _WorkingGridplaneMold(_WorkingMold):
    """A gridplane mold in the process of being converted to ROM bytes."""

    _tiles: list[_WorkingGridplaneArrangement] = []

    @property
    def tiles(self) -> list[_WorkingGridplaneArrangement]:
        """A list of exactly one working gridplane tile, which will be converted to
        bytes by functions that use this class."""
        return self._tiles

    def set_tiles(self, tiles: list[_WorkingGridplaneArrangement]) -> None:
        """Overwrite the list of exactly one working gridplane tile, which will be converted to
        bytes by functions that use this class."""
        self._tiles = tiles

    # pylint: disable=W0231
    def __init__(self, base_mold: GridplaneMold) -> None:
        super().set_base_mold(base_mold)


class _WorkingNonGridplaneMold(_WorkingMold):
    """A non-gridplane mold in the process of being converted to ROM bytes."""

    _tiles: list[_WorkingNonGridplaneArrangement | _Clone] = []

    @property
    def tiles(self) -> list[_WorkingNonGridplaneArrangement | _Clone]:
        """A list of the mold's working gridplane tiles, which will be converted to
        bytes by functions that use this class."""
        return self._tiles

    def set_tiles(self, tiles: list[_WorkingNonGridplaneArrangement | _Clone]) -> None:
        """Overwrite the list of the mold's working gridplane tiles, which will be converted to
        bytes by functions that use this class."""
        self._tiles = tiles

    # pylint: disable=W0231
    def __init__(self, base_mold: NonGridplaneMold) -> None:
        super().set_base_mold(base_mold)


class _WorkingAnimationData(AnimationData):
    """Animation data in the process of being converted to ROM bytes."""

    _molds: list[_WorkingGridplaneMold | _WorkingNonGridplaneMold]

    @property
    def molds(self) -> list[_WorkingGridplaneMold | _WorkingNonGridplaneMold]:
        """The working molds being converted to ROM bytes."""
        return self._molds

    def set_molds(
        self, molds: list[_WorkingGridplaneMold | _WorkingNonGridplaneMold]
    ) -> None:
        """Set the working molds being converted to ROM bytes."""
        self._molds = molds

    # pylint: disable=W0231
    def __init__(self, data: AnimationData) -> None:
        self.set_molds([])
        self.set_sequences(deepcopy(data.sequences))
        self.set_vram_size(deepcopy(data.vram_size))
        self.set_unknown(deepcopy(data.unknown))


class _WIPSprite:
    """An entire sprite in the process of being converted to ROM bytes."""

    _sprite: SpriteContainer
    _subtiles: list[_SubtileTuple]
    _subtile_group: str
    _relative_offset: int
    _working_animation_data: _WorkingAnimationData | None = None

    @property
    def sprite(self) -> SpriteContainer:
        """The sprite object being converted."""
        return self._sprite

    def set_sprite(self, sprite: SpriteContainer) -> None:
        """Set the sprite object being converted."""
        self._sprite = sprite

    @property
    def subtiles(self) -> list[_SubtileTuple]:
        """The subtiles that this sprite needs to use."""
        return self._subtiles

    def set_subtiles(self, subtiles: list[bytearray] | list[_SubtileTuple]) -> None:
        """Overwrite the list of subtiles that this sprite needs to use."""
        self._subtiles = [
            _SubtileTuple(t) if isinstance(t, bytearray) else t for t in subtiles
        ]

    @property
    def subtile_group_id(self) -> str:
        """The ID of the subtile group used by this sprite."""
        return self._subtile_group

    def set_subtile_group(self, subtile_group: str) -> None:
        """Set the ID of the subtile group used by this sprite."""
        self._subtile_group = subtile_group

    @property
    def relative_offset(self) -> int:
        """The offset at which this sprite should begin reading subtile data,
        relative to the beginning of the subtile group."""
        return self._relative_offset

    def set_relative_offset(self, relative_offset: int) -> None:
        """The offset at which this sprite should begin reading subtile data,
        relative to the beginning of the subtile group."""
        self._relative_offset = relative_offset

    @property
    def working_animation_data(self) -> _WorkingAnimationData | None:
        """The sprite's working animation data being converted to ROM bytes."""
        return self._working_animation_data

    def set_working_animation_data(
        self, working_animation_data: _WorkingAnimationData
    ) -> None:
        """Overwrite the sprite's working animation data being converted to ROM bytes."""
        self._working_animation_data = working_animation_data

    def __init__(
        self,
        sprite: SpriteContainer,
        subtiles: list[bytearray] | list[_SubtileTuple],
        tile_group: str,
        relative_offset: int,
    ) -> None:
        self.set_sprite(sprite)
        self.set_subtiles(subtiles)
        self.set_subtile_group(tile_group)
        self.set_relative_offset(relative_offset)


class _WIPSprites(list[_WIPSprite]):
    """The game's entire collection of sprites being converted to ROM bytes."""

    def rearrange_tiles(self, group: _SubtileGroup) -> None:
        """Reorder all of the subtiles in a group to make sure that subtiles used
        by each sprite are as close together as possible.\n
        This is to make sure that you don't end up with a situation where 4 different
        Mario sprites use a collection of 1000 subtiles, and the first sprite needs to use
        subtile 20 and subtile 800. That would not be allowed."""
        subtile_use: list[_SubtileSorter] = []
        relevant_sprites = group.used_by

        for subtile in group.subtiles:
            sprites_using_this_tile: list[int] = []
            for sprite_id in relevant_sprites:
                if subtile in self[sprite_id].subtiles:
                    sprites_using_this_tile.append(sprite_id)
            subtile_use.append(_SubtileSorter(subtile, sprites_using_this_tile))

        subtile_use.sort(key=cmp_to_key(_WIPSprites.sort_by_used_sprites))

        group.set_subtiles([t[0] for t in subtile_use])

    def get_comparative_similarity(self, key1: int, key2: int) -> float:
        """Get the subtile overlap percentage between two sprites by ID."""
        similarity = _tileset_similarity(
            self[key1].subtiles, self[key2].subtiles
        ) / len([y for y in self[key1].subtiles if _is_significant_tile(y)])
        if similarity == 1:
            return int(similarity)
        return trunc(round(similarity * 10.0)) / 10

    @classmethod
    def sort_by_used_sprites(cls, tup1: _SubtileSorter, tup2: _SubtileSorter) -> int:
        """Sorting logic for sorting subtiles by sprite usage."""
        raw_subtile_1 = tup1[1]
        raw_subtile_2 = tup2[1]
        if len(raw_subtile_1) < len(raw_subtile_2):
            raw_subtile_1 += [0] * (len(raw_subtile_2) - len(raw_subtile_1))
        elif len(raw_subtile_1) > len(raw_subtile_2):
            raw_subtile_2 += [0] * (len(raw_subtile_1) - len(raw_subtile_2))
        used = zip(raw_subtile_1, raw_subtile_2)
        for used_subtile in used:
            if used_subtile[0] < used_subtile[1]:
                return -1
            if used_subtile[0] > used_subtile[1]:
                return 1
        return 0


class AssemblingSpriteContainer(SpriteContainer):
    """A WIP container for a sprite as it is understood by SMRPG: an animation data ID
    and an image data ID."""

    _animation_id: int
    _image_id: int

    @property
    def animation_id(self) -> int:
        """The index of the animation data to be used by this sprite."""
        return self._animation_id

    def set_animation_id(self, animation_id: int) -> None:
        """Set the index of the animation data to be used by this sprite."""
        self._animation_id = animation_id

    @property
    def image_id(self) -> int:
        """The index of the image data to be used by this sprite."""
        return self._image_id

    def set_image_id(self, image_id: int) -> None:
        """Set the index of the image data to be used by this sprite."""
        self._image_id = image_id

    # pylint: disable=W0231
    def __init__(
        self,
        image_id: int,
        animation_id: int,
        palette_offset: int,
        unknown: int,
    ) -> None:
        self.set_image_id(image_id)
        self.set_animation_id(animation_id)
        super().set_palette_offset(palette_offset)
        super().set_unknown(unknown)


class _CloneCandidate:
    """A structure used to assess whether or not a tile is a good candidate for cloning."""

    _mold_id: int
    _start_index: int
    _end_index: int
    _x_offset: int
    _y_offset: int

    @property
    def mold_id(self) -> int:
        """The ID of the mold being referenced."""
        return self._mold_id

    def set_mold_id(self, mold_id: int) -> None:
        """Specify the ID of the mold being referenced."""
        self._mold_id = mold_id

    @property
    def start_index(self) -> int:
        """The first index (within the reference mold) of the tiles to be cloned by this."""
        return self._start_index

    def set_start_index(self, start_index: int) -> None:
        """The first index (within the reference mold) of the tiles to be cloned by this."""
        self._start_index = start_index

    @property
    def end_index(self) -> int:
        """The last index (within the reference mold) of the tiles to be cloned by this."""
        return self._end_index

    def set_end_index(self, end_index: int) -> None:
        """The last index (within the reference mold) of the tiles to be cloned by this."""
        self._end_index = end_index

    @property
    def x_offset(self) -> int:
        """X axis pixels by which each cloned tile should be shifted."""
        return self._x_offset

    def set_x_offset(self, x_offset: int) -> None:
        """X axis pixels by which each cloned tile should be shifted."""
        self._x_offset = x_offset

    @property
    def y_offset(self) -> int:
        """Y axis pixels by which each cloned tile should be shifted."""
        return self._y_offset

    def set_y_offset(self, y_offset: int) -> None:
        """Y axis pixels by which each cloned tile should be shifted."""
        self._y_offset = y_offset

    def __init__(
        self,
        mold_id: int,
        start_index: int,
        end_index: int,
        x_offset: int,
        y_offset: int,
    ) -> None:
        self.set_mold_id(mold_id)
        self.set_start_index(start_index)
        self.set_end_index(end_index)
        self.set_x_offset(x_offset)
        self.set_y_offset(y_offset)


def _random_tile_id() -> str:
    return "".join(choices(ALPHABET, k=8))


# A "significant tile" is a tile that should be a candidate for being reused between sprites.
# Tiles which are mostly empty except for maybe a couple of pixels are not that.
# The importance of this is that tiles deemed significant which are shared between different sprites
# will mean that the assembler will try to group those sprites close together (within 512 indexes)
# such that the same tile can be accessed by both sprites,
# instead of having to write the same tile twice.
def _is_significant_tile(tiledata: _SubtileTuple) -> bool:
    return len([offset for offset in tiledata if offset > 0]) > 4


# Determine how similar two given tilesets are, where similarity is determined by the number of
# tiles between them that are the exact same
def _tileset_similarity(
    tileset1: list[_SubtileTuple], tileset2: list[_SubtileTuple]
) -> int:
    sanitized_tileset_1 = [t for t in tileset1 if _is_significant_tile(t)]
    sanitized_tileset_2 = [t for t in tileset2 if _is_significant_tile(t)]
    tileset_1 = set(sanitized_tileset_1)
    tileset_2 = set(sanitized_tileset_2)
    similarity = len(set(tileset_1).intersection(set(tileset_2)))
    return similarity


# check if two AnimationData classes have the same structure
def _is_same_animation(animation1: AnimationData, animation2: AnimationData) -> bool:
    if animation1.unknown != animation2.unknown:
        return False
    if animation1.vram_size != animation2.vram_size:
        return False
    if len(animation1.molds) != len(animation2.molds):
        return False
    if len(animation1.sequences) != len(animation2.sequences):
        return False
    molds = zip(animation1.molds, animation2.molds)
    for mold in molds:
        if mold[0].gridplane != mold[1].gridplane:
            return False
        if len(mold[0].tiles) != len(mold[1].tiles):
            return False
        for index, _ in enumerate(mold[0].tiles):
            ts1 = mold[0].tiles[index]
            ts2 = mold[1].tiles[index]
            if type(ts1) != type(ts2):
                return False
            if ts1.mirror != ts2.mirror:
                return False
            if ts1.invert != ts2.invert:
                return False
            if isinstance(ts1, NonGridplaneArrangement) and isinstance(
                ts2, NonGridplaneArrangement
            ):
                if ts1.x != ts2.x:
                    return False
                if ts1.y != ts2.y:
                    return False
            elif isinstance(ts1, GridplaneArrangement) and isinstance(
                ts2, GridplaneArrangement
            ):
                if ts1.y_plus != ts2.y_plus:
                    return False
                if ts1.y_minus != ts2.y_minus:
                    return False
            if ts1.subtiles != ts2.subtiles:
                return False

    sequences = zip(animation1.sequences, animation2.sequences)
    for sequence in sequences:
        sequence_1 = sequence[0]
        sequence_2 = sequence[1]
        if len(sequence_1.frames) != len(sequence_2.frames):
            return False
        for index, _ in enumerate(sequence_1.frames):
            as1 = sequence_1.frames[index]
            as2 = sequence_2.frames[index]
            if as1.duration != as2.duration:
                return False
            if as1.mold_id != as2.mold_id:
                return False
    return True


# This method is run multiple times to try and figure out which tile is the beginning
# of a series of consecutive clone tiles.
def _is_clone_start(
    tile: _WorkingNonGridplaneArrangement | _Clone,
    compare_tile: _WorkingNonGridplaneArrangement | _Clone,
) -> tuple[bool, int, int]:
    if isinstance(compare_tile, _Clone) or isinstance(tile, _Clone):
        return False, 0, 0
    if tile.subtiles != compare_tile.subtiles:
        return False, 0, 0
    # Clones might require an x/y offset of at least 1.
    # Unsure
    # Maybe clones can only be within a certain index?
    # Try some of these things if it wont build
    # Definitely cannot be a source tile if x/y is too large - indicates it is also a clone
    if compare_tile.x > 255 or compare_tile.y > 255:
        return False, 0, 0
    if tile.x - compare_tile.x < 0 or tile.y - compare_tile.y < 0:
        return False, 0, 0
    if tile.mirror != compare_tile.mirror or tile.invert != compare_tile.invert:
        return False, 0, 0
    return True, tile.x - compare_tile.x, tile.y - compare_tile.y


# This method is run multiple times to try and figure if a tile is part of a series of
# consecutive clone tiles.
def _is_clone_continuation(
    tile: _WorkingNonGridplaneArrangement | _Clone,
    compare_tile: _WorkingNonGridplaneArrangement | _Clone,
    x_offset: int,
    y_offset: int,
) -> bool:
    if isinstance(tile, _Clone) or isinstance(compare_tile, _Clone):
        return False
    if tile.subtiles != compare_tile.subtiles:
        return False
    if (tile.x - compare_tile.x) != x_offset or (tile.y - compare_tile.y) != y_offset:
        return False
    if tile.mirror != compare_tile.mirror:
        return False
    if tile.invert != compare_tile.invert:
        return False
    return True


# final eligibility check of potential clone, adds if passes
def _finish_candidate(
    mold_id: int,
    tile: _WorkingNonGridplaneArrangement | _Clone,
    compare_tiles: list[_WorkingNonGridplaneArrangement | _Clone],
    end_index: int,
    start_index: int,
    x_offset: int,
    y_offset: int,
) -> _CloneCandidate | None:
    if isinstance(tile, _Clone):
        return None
    cloned = compare_tiles[start_index : end_index + 1]
    if len(cloned) == 0:
        return None
    if x_offset < 0 or y_offset < 0:
        return None
    if len(cloned) == 1:
        if tile.x > 255 or tile.y > 255:
            pass
        elif max(tile.subtiles) > 255:
            pass
        elif len([sb for sb in tile.subtiles if sb != 0]) > 2:
            pass
        else:
            return None
    return _CloneCandidate(mold_id, start_index, end_index + 1, x_offset, y_offset)


# find all possible clones of the tile within the given mold tileset
def _get_clone_ranges(
    mold_id: int,
    tiles: list[_Clone | _WorkingNonGridplaneArrangement],
    tile_index: int,
    compare_tiles: list[_WorkingNonGridplaneArrangement | _Clone],
    mold_index: int = 0,
) -> list[_CloneCandidate]:
    tile = tiles[tile_index]
    clone_candidates: list[_CloneCandidate] = []

    # don't compare to self
    tile_compare_index: int = len(compare_tiles) - 1
    if mold_id == mold_index:
        tile_compare_index = tile_index - 1

    is_candidate: bool = False
    x_offset: int = 0
    y_offset: int = 0
    start: int = tile_compare_index
    end: int = tile_compare_index
    check: int = tile_index

    while tile_compare_index >= 0:
        compare_tile = compare_tiles[tile_compare_index]
        is_ending: bool = False
        # if no active clone check, starts one if it matches
        if not is_candidate:
            is_candidate, x_offset, y_offset = _is_clone_start(tile, compare_tile)
            if is_candidate:
                end = tile_compare_index
        # if active clone check, ends it if it comes across an unmatched tile
        else:
            is_ending = (
                (end - tile_compare_index == 15)
                or (mold_id == mold_index and check == end)
                or not _is_clone_continuation(
                    tiles[check], compare_tile, x_offset, y_offset
                )
            )
        if is_candidate:
            if is_ending or tile_compare_index == 0 or check == 0:
                start = tile_compare_index
                if is_ending:
                    start += 1
                finished_candidate = _finish_candidate(
                    mold_id, tile, compare_tiles, end, start, x_offset, y_offset
                )
                if finished_candidate is not None:
                    clone_candidates.append(finished_candidate)
                is_candidate = False
                x_offset = 0
                y_offset = 0
                check = tile_index
            else:
                check = max(0, check - 1)
        tile_compare_index -= 1

    # need some way to detect internal clones within the same mold
    # most likely want to do this after looking for clones elsewhere

    return clone_candidates


def _find_clones(
    tiles_: list[_WorkingNonGridplaneArrangement],
    molds: list[_WorkingGridplaneMold | _WorkingNonGridplaneMold],
    mold_index: int = 0,
) -> list[_WorkingNonGridplaneArrangement | _Clone]:
    tiles: list[_WorkingNonGridplaneArrangement | _Clone] = list(tiles_)
    output: list[_Clone | _WorkingNonGridplaneArrangement] = []
    tmp_output: list[_Clone | _WorkingNonGridplaneArrangement] = []

    tile_index: int = len(tiles) - 1
    # iterate backwards thru tiles in the mold we're currently forming
    while tile_index >= 0:
        clone_candidates: list[_CloneCandidate] = []
        tile = tiles[tile_index]
        # iterate backwards thru molds to start looking for clones
        mold_index = len(molds) - 1
        while mold_index >= 0:
            mold = molds[mold_index]
            if isinstance(mold, _WorkingNonGridplaneMold):
                # look for any possible point in previous molds that looks like it
                # could be a clone range ending with this tile
                clone_candidates += _get_clone_ranges(
                    mold_index, tiles, tile_index, mold.tiles, mold_index
                )
            mold_index -= 1

        # if eligible ranges found, create clone container for all tiles in range
        if len(clone_candidates) > 0:
            eligible_candidates = [
                c for c in clone_candidates if c.x_offset <= 255 and c.y_offset <= 255
            ]
            ineligible_candidates = [
                c for c in clone_candidates if c not in eligible_candidates
            ]
            # clone detection just doesnt work out sometimes,
            # ie 3 sets of the same tiles that overall are >255 apart
            # in those cases, un-clone them and just treat as normal tiles
            if len(eligible_candidates) == 0:
                candidate = max(
                    ineligible_candidates,
                    key=lambda item: item.end_index - item.start_index,
                )
                decoupled_tiles = deepcopy(
                    molds[candidate.mold_id].tiles[
                        candidate.start_index : candidate.end_index
                    ]
                )
                decoupled_tiles.reverse()
                for c_tile in decoupled_tiles:
                    assert isinstance(c_tile, (_WorkingNonGridplaneArrangement, _Clone))
                    tmp_output.insert(0, c_tile)
            else:
                candidate = max(
                    eligible_candidates,
                    key=lambda item: item.end_index - item.start_index,
                )
                reference_tiles = molds[candidate.mold_id].tiles[
                    candidate.start_index : candidate.end_index
                ]
                final_tiles = [
                    t
                    for t in reference_tiles
                    if isinstance(t, _WorkingNonGridplaneArrangement)
                ]
                assert len(final_tiles) == len(reference_tiles)
                tmp_output.insert(
                    0,
                    _Clone(
                        mirror=False,
                        invert=False,
                        x=candidate.x_offset,
                        y=candidate.y_offset,
                        tiles=final_tiles,
                    ),
                )
            tile_index -= candidate.end_index - candidate.start_index
        # otherwise just append the tile and move onto the next one
        else:
            tmp_output.insert(0, tile)
            tile_index -= 1

    # after scanning previous molds, check for internal clones as well
    tile_index = len(tmp_output) - 1
    ineligible_to_be_clones: list[int] = []
    while tile_index >= 0:
        tile = tmp_output[tile_index]
        if tile_index in ineligible_to_be_clones or isinstance(tile, _Clone):
            output.insert(0, tile)
            tile_index -= 1
            continue

        clone_candidates = _get_clone_ranges(
            len(molds), tmp_output, tile_index, tmp_output, mold_index
        )
        if len(clone_candidates) > 0:
            candidate = max(
                clone_candidates, key=lambda item: item.end_index - item.start_index
            )
            reference_tiles = tmp_output[candidate.start_index : candidate.end_index]
            final_tiles = [
                t
                for t in reference_tiles
                if isinstance(t, _WorkingNonGridplaneArrangement)
            ]
            assert len(final_tiles) == len(reference_tiles)
            output.insert(
                0,
                _Clone(
                    mirror=False,
                    invert=False,
                    x=candidate.x_offset,
                    y=candidate.y_offset,
                    tiles=final_tiles,
                ),
            )
            tile_index -= candidate.end_index - candidate.start_index
            ineligible_to_be_clones.extend(
                list(range(candidate.start_index, candidate.end_index))
            )
        else:
            output.insert(0, tile)
            tile_index -= 1

    return output


def _place_bytes(these_bytes: bytearray) -> int:
    # find bank with most space
    highest_space = 0
    index = 0
    for bank_index, bank in enumerate(_ANIMATION_DATA_BANKS):
        if highest_space < bank.remaining_space:
            highest_space = bank.remaining_space
            index = bank_index
    if len(these_bytes) > _ANIMATION_DATA_BANKS[index].remaining_space:
        raise InvalidSpriteConstructionException(
            "could not place bytes into a bank with space"
        )
    offset = _ANIMATION_DATA_BANKS[index].current_offset
    _ANIMATION_DATA_BANKS[index].raw_bytes.extend(these_bytes)
    return offset


def _create_dummy_sprite() -> _WorkingAnimationData:
    dummy_mold = NonGridplaneMold([])
    dummy_w_mold = _WorkingNonGridplaneMold(dummy_mold)
    dummy_animation_data = AnimationData([dummy_mold], [SpriteSequence([])], 2048, 2)
    dummy_w_animation_data = _WorkingAnimationData(dummy_animation_data)
    dummy_w_animation_data.set_molds([dummy_w_mold])
    return dummy_w_animation_data


class SpriteCollection(list[SpriteContainer]):
    """Managerial class for everything relating to NPC sprites."""

    def render(self) -> dict[int, bytearray]:
        """Get data for all NPC sprite data in `{0x123456: bytearray([0x00])}` format"""
        ### produce rom bytes
        tile_groups = _TileGroupSet()
        wip_sprites: _WIPSprites = _WIPSprites()

        unique_tiles_length: int = 0

        # collect unique subtiles and group sprites by graphic similarity
        for index, wip_sprite in enumerate(self):
            unique_subtiles: list[_SubtileTuple] = []
            for mold in wip_sprite.animation_data.molds:
                for tile in mold.tiles:
                    for subtile in tile.subtiles:
                        if subtile is not None:
                            hashable = _SubtileTuple(subtile)
                            if hashable not in unique_subtiles:
                                unique_subtiles.append(hashable)
            key, similarity = tile_groups.get_most_similar_subtileset(
                set(unique_subtiles)
            )

            if key is None or similarity < 0.075:  # add new tile group
                tile_id: str = _random_tile_id()
                # regen if already taken
                while tile_id in tile_groups:
                    tile_id = _random_tile_id()
                key = tile_id
                tile_groups[key] = _SubtileGroup([index], unique_subtiles)
            else:
                tile_groups[key].add_used_by(index)
                tile_groups[key].extend_subtiles(set(unique_subtiles))
            wip_sprite = _WIPSprite(wip_sprite, unique_subtiles, key, 0)
            wip_sprites.append(wip_sprite)

        # within each tile group, determine which sprites actually use which tiles
        for key in tile_groups:
            tile_group = tile_groups[key]
            # group tiles together by proximity
            has_variance = False
            if len(tile_group.used_by) > 1:
                variance = []
                for key in tile_group.used_by:
                    this_variance = [
                        wip_sprites.get_comparative_similarity(key, x)
                        for x in tile_group.used_by
                    ]
                    variance.append(this_variance)
                for x, variant in enumerate(variance):
                    for y in range(x + 1, len(variance)):
                        if variant[y] != 1 and variance[y][x] != 1:
                            has_variance = True
            if has_variance:
                wip_sprites.rearrange_tiles(tile_group)

        # calculate free space
        free_tiles: int = (
            UNCOMPRESSED_GFX_END - UNCOMPRESSED_GFX_START - (unique_tiles_length * 0x20)
        ) // 0x20

        # reserve 64 tiles for minecart and 8bit
        free_tiles -= 64
        free_tiles = max(free_tiles, 0)

        # find sprites which are going to cause problems because of subtile deltas > 512
        # and duplicate tiles where necessary
        for sprite_index, wip_sprite in enumerate(wip_sprites):
            tile_key: str = wip_sprite.subtile_group_id
            available_tiles = tile_groups[tile_key].subtiles

            lowest_subtile_index: int = 0
            if len(wip_sprite.subtiles) > 0:
                lowest_subtile_index = len(available_tiles)
                highest_subtile_index: int = 0
                all_indexes_for_this_tile: list[int] = []
                for subtile in wip_sprite.subtiles:
                    tilegroup_index_of_this_tile: int = available_tiles.index(subtile)
                    if tilegroup_index_of_this_tile not in all_indexes_for_this_tile:
                        all_indexes_for_this_tile.append(tilegroup_index_of_this_tile)
                    if tilegroup_index_of_this_tile < lowest_subtile_index:
                        lowest_subtile_index = tilegroup_index_of_this_tile
                    if tilegroup_index_of_this_tile > highest_subtile_index:
                        highest_subtile_index = tilegroup_index_of_this_tile
                all_indexes_for_this_tile.sort()

                # try copying some tiles if range is too big
                if highest_subtile_index - lowest_subtile_index > 510:
                    extra_tiles = []
                    smallest_range = highest_subtile_index - lowest_subtile_index
                    cutoff_index = lowest_subtile_index
                    for tg_index, st_index in enumerate(all_indexes_for_this_tile):
                        next_tg_index = tg_index + 1
                        next_st_index = st_index + 1

                        if next_tg_index >= len(all_indexes_for_this_tile):
                            continue

                        tiles_needing_shift = all_indexes_for_this_tile[0:next_tg_index]
                        tentative_clones = [
                            t
                            for t in tiles_needing_shift
                            if available_tiles[t] not in tile_groups[tile_key].extra
                        ]

                        remanining_buffer = available_tiles[next_st_index:]

                        this_range = (
                            len(remanining_buffer)
                            + len(tile_groups[tile_key].extra)
                            + len(tentative_clones)
                        )

                        if this_range < smallest_range:
                            smallest_range = this_range
                            cutoff_index = next_st_index
                    # if still too big, convert into its own tileset?
                    lowest_subtile_index = cutoff_index
                    # add too-low sprite ids to be duped at the end
                    new_tile_pool = (
                        tile_groups[tile_key].subtiles[cutoff_index:]
                        + tile_groups[tile_key].extra
                    )
                    for t_index in all_indexes_for_this_tile:
                        this_tile = available_tiles[t_index]
                        if (
                            this_tile not in extra_tiles
                            and this_tile not in new_tile_pool
                        ):
                            extra_tiles.append(this_tile)
                    tile_groups[tile_key].extra.extend(extra_tiles)

            wip_sprite.set_relative_offset(lowest_subtile_index)

        # start placing tile groups and get offsets for them
        sortable_tile_groups: list[tuple[str, _SubtileGroup]] = []
        for key in tile_groups:
            sortable_tile_groups.append((key, tile_groups[key]))
        sortable_tile_groups.sort(key=lambda tup: len(tup[1].subtiles), reverse=True)
        for tile_key, group in sortable_tile_groups:
            tilebytes = bytearray([])
            for subtile in group.subtiles + group.extra:
                tilebytes += bytearray(subtile)
            group_offset: int = _SUBTILE_BANKS.place_bytes(tilebytes)
            tile_groups[tile_key].set_offset(group_offset)

        # start building stuff
        complete_images: list[ImagePack] = []
        complete_animations: list[_WorkingAnimationData] = []
        complete_sprites: list[AssemblingSpriteContainer] = []

        for sprite_index, wip_sprite in enumerate(wip_sprites):
            # prepare sprite to contain clone arrangement
            wip_sprite.set_working_animation_data(
                _WorkingAnimationData(wip_sprite.sprite.animation_data)
            )
            assert wip_sprite.working_animation_data is not None

            tile_key = wip_sprite.subtile_group_id
            available_tiles = (
                tile_groups[tile_key].subtiles[wip_sprite.relative_offset :]
                + tile_groups[tile_key].extra
            )

            lowest_subtile_index = len(available_tiles)
            highest_subtile_index = 0
            all_indexes_for_this_tile = []
            for tile in wip_sprite.subtiles:
                tilegroup_index_of_this_tile = available_tiles.index(tile)
                if tilegroup_index_of_this_tile < lowest_subtile_index:
                    lowest_subtile_index = tilegroup_index_of_this_tile
                if tilegroup_index_of_this_tile > highest_subtile_index:
                    highest_subtile_index = tilegroup_index_of_this_tile

            subtile_subtract: int = 0

            ### check if this tile group has already been placed
            offset = tile_groups[tile_key].offset + wip_sprite.relative_offset * 0x20
            if len(available_tiles) > 510:
                subtile_subtract = lowest_subtile_index
            # get image pack #, or create new
            offset += (subtile_subtract) * 0x20
            # need to change this to accommodate diff offsets in same tile group
            palette_ptr = PALETTE_OFFSET + wip_sprite.sprite.palette_id * 30
            image_index_to_use = len(complete_images)
            for image_index, image in enumerate(complete_images):
                if (
                    image.graphics_pointer == offset
                    and image.palette_pointer == palette_ptr
                ):
                    image_index_to_use = image_index
            if image_index_to_use == len(complete_images):
                complete_images.append(
                    ImagePack(image_index_to_use, offset, palette_ptr)
                )

            # get animation #, or create new
            animation_id_to_use = len(complete_animations)
            for prev_sprite_index, s in enumerate(wip_sprites[0:sprite_index]):
                if _is_same_animation(
                    wip_sprite.sprite.animation_data, s.sprite.animation_data
                ):
                    animation_id_to_use = complete_sprites[
                        prev_sprite_index
                    ].animation_id
            # if not found, create new
            if animation_id_to_use == len(complete_animations):
                molds: list[_WorkingGridplaneMold | _WorkingNonGridplaneMold] = []
                for mold_index, mold in enumerate(
                    wip_sprite.sprite.animation_data.molds
                ):
                    # build numerical subtile bytes
                    these_tiles: list[
                        _WorkingGridplaneArrangement
                        | _WorkingNonGridplaneArrangement
                        | _Clone
                    ] = []
                    for tile in mold.tiles:
                        subtile_bytes: list[int] = []
                        for subtile in tile.subtiles:
                            if subtile is None:
                                subtile_index = 0
                            else:
                                subtile_index = (
                                    available_tiles.index(_SubtileTuple(subtile))
                                    + 1
                                    - subtile_subtract
                                )
                            subtile_bytes.append(subtile_index)
                        if isinstance(tile, GridplaneArrangement):
                            this_tile = _WorkingGridplaneArrangement(tile)
                        elif isinstance(tile, NonGridplaneArrangement):
                            this_tile = _WorkingNonGridplaneArrangement(tile)
                        else:
                            raise InvalidSpriteConstructionException(
                                "what was the original tile type?"
                            )
                        this_tile.set_subtiles(subtile_bytes)
                        these_tiles.append(this_tile)

                    # create clones and use in mold
                    if isinstance(mold, NonGridplaneMold):
                        this_mold = _WorkingNonGridplaneMold(mold)
                        insertions = [
                            t
                            for t in these_tiles
                            if isinstance(t, _WorkingNonGridplaneArrangement)
                        ]
                        assert len(insertions) == len(these_tiles)
                        include_clones = _find_clones(insertions, molds, mold_index)
                        this_mold.set_tiles(include_clones)
                    else:
                        this_mold = _WorkingGridplaneMold(mold)
                        insertions = [
                            t
                            for t in these_tiles
                            if isinstance(t, _WorkingGridplaneArrangement)
                        ]
                        assert len(insertions) == len(these_tiles)
                        this_mold.set_tiles(insertions)
                    molds.append(this_mold)

                # track this new clone-enabled animation data
                # in case future sprites will need to use it
                wip_sprite.working_animation_data.set_molds(molds)
                complete_animations.append(wip_sprite.working_animation_data)

            # create sprite pack
            complete_sprites.append(
                AssemblingSpriteContainer(
                    image_index_to_use,
                    animation_id_to_use,
                    wip_sprite.sprite.palette_offset,
                    wip_sprite.sprite.unknown,
                )
            )

        output_tile_ranges: list[tuple[int, bytearray]] = []
        final_offset = _SUBTILE_BANKS[0].start
        for bank_index, bank in enumerate(_SUBTILE_BANKS):
            final_offset = bank.start + len(bank.raw_bytes)
            _SUBTILE_BANKS[bank_index].extend_raw_bytes(
                bytearray([0] * (bank.end - bank.start - len(bank.raw_bytes)))
            )
            # Write each bank to its own address
            output_tile_ranges.append(
                (bank.start, _SUBTILE_BANKS[bank_index].raw_bytes)
            )

        if len(complete_images) > TOTAL_IMAGES:
            raise InvalidSpriteConstructionException(
                f"too many images: {len(complete_images)}"
            )
        if len(complete_images) < TOTAL_IMAGES:
            ind = len(complete_images)
            while ind < TOTAL_IMAGES:
                complete_images.append(
                    ImagePack(ind, UNCOMPRESSED_GFX_START + final_offset, 0x250000)
                )
                ind += 1
        if len(complete_animations) < TOTAL_ANIMATIONS:
            ind = len(complete_animations)
            while ind < TOTAL_ANIMATIONS:
                complete_animations.append(_create_dummy_sprite())
                ind += 1

        # secondary function starts here
        sprite_data = bytearray()
        image_data = bytearray()
        animation_pointers = bytearray()
        used_animations: list[int] = []

        for sprite in complete_sprites:
            assert sprite.image_id <= 0x1FF
            assert sprite.palette_offset <= 7
            sprite_data.append(sprite.image_id & 0xFF)
            sprite_data.append(
                ((sprite.image_id >> 8) & 0x01)
                + (sprite.palette_offset << 1)
                + (sprite.unknown << 4)
            )
            assert sprite.animation_id <= 0xFFFF
            sprite_data.append(sprite.animation_id & 0xFF)
            sprite_data.append((sprite.animation_id >> 8) & 0xFF)
            if sprite.animation_id not in used_animations:
                used_animations.append(sprite.animation_id)

        for image in complete_images:
            bank = ((image.graphics_pointer - UNCOMPRESSED_GFX_START) >> 16) & 0x0F
            gfx_short = image.graphics_pointer & 0xFFF0
            assert gfx_short <= 0xFFFF
            image_data.append((gfx_short & 0xF0) + bank)
            image_data.append(gfx_short >> 8)
            palette_ptr = image.palette_pointer - PALETTE_OFFSET + 0x3000
            assert palette_ptr <= 0xFFFF
            image_data.append(palette_ptr & 0xFF)
            image_data.append(palette_ptr >> 8)

        animations_ready_to_place: list[tuple[int, bytearray]] = []
        animation_pointers_wip: list[int | None] = [None] * len(complete_animations)

        for anim_id, animation in enumerate(complete_animations):
            if anim_id not in used_animations:
                animation = _create_dummy_sprite()

            length_bytes = bytearray()
            sequence_offset = bytearray([0x0C, 0x00])
            mold_offset = bytearray()
            num_sequences: int = len(animation.sequences)
            num_molds: int = len(animation.molds)
            assert num_molds <= MAX_MOLDS_PER_SPRITE
            assert num_sequences <= MAX_SEQUENCES_PER_SPRITE
            count_bytes = bytearray([num_sequences, num_molds])
            vram: int = animation.vram_size >> 8
            misc_bytes = bytearray([vram & 0xFF, (vram >> 8) & 0xFF, 0x02, 0x00])
            sequence_ptrs = bytearray()
            sequence_bytes = bytearray()
            mold_ptrs = bytearray()
            mold_bytes = bytearray()

            for sequence in animation.sequences:
                this_sequence_offset: int = (
                    0x0C + (len(animation.sequences) + 1) * 2 + len(sequence_bytes)
                )
                assert this_sequence_offset <= 0xFFFF
                if len(sequence.frames) == 0:
                    sequence_ptrs.extend([0xFF, 0xFF])
                else:
                    sequence_ptrs.append(this_sequence_offset & 0xFF)
                    sequence_ptrs.append(this_sequence_offset >> 8)
                    for frame in sequence.frames:
                        sequence_bytes.append(frame.duration)
                        sequence_bytes.append(frame.mold_id)
                    sequence_bytes.append(0)
            sequence_ptrs.extend([0, 0])

            mold_offset_short = 0x0C + len(sequence_ptrs) + len(sequence_bytes)
            mold_offset.append(mold_offset_short & 0xFF)
            mold_offset.append((mold_offset_short >> 8) & 0xFF)
            subtile_indexes = []
            for mold_index, mold in enumerate(animation.molds):
                this_mold_offset = (
                    0x0C
                    + len(sequence_ptrs)
                    + len(sequence_bytes)
                    + (len(animation.molds) + 1) * 2
                    + len(mold_bytes)
                )
                assert this_mold_offset <= 0x7FFF
                animation.molds[mold_index].set_offset(this_mold_offset)
                if isinstance(mold, _WorkingGridplaneMold):
                    this_mold_offset += 0x80 << 8
                if len(mold.tiles) > 0:
                    mold_ptrs.append(this_mold_offset & 0xFF)
                    mold_ptrs.append((this_mold_offset >> 8) & 0xFF)
                    this_mold_bytes = bytearray()
                    if isinstance(mold, _WorkingGridplaneMold):
                        for tile_index, tile in enumerate(mold.tiles):
                            for _, subtile_byte in enumerate(tile.subtiles):
                                if subtile_byte >= 0x100:
                                    tile.set_is_16bit(True)
                            tile_bytes = bytearray([])
                            animation.molds[mold_index].tiles[tile_index].set_offset(
                                this_mold_offset + len(this_mold_bytes)
                            )
                            byte_1: int = (
                                (tile.format & 0x03)
                                + (tile.is_16bit << 3)
                                + (tile.y_plus << 4)
                                + (tile.y_minus << 5)
                                + (tile.mirror << 6)
                                + (tile.invert << 7)
                            )
                            tile_bytes.append(byte_1)
                            if tile.is_16bit:
                                subtile_short = 0
                                for subtile_index, subtile_byte in enumerate(
                                    tile.subtiles
                                ):
                                    if subtile_byte >= 0x100:
                                        subtile_short += 1 << subtile_index
                                tile_bytes.append(subtile_short & 0xFF)
                                tile_bytes.append((subtile_short >> 8) & 0xFF)
                            for subtile_byte in tile.subtiles:
                                tile_bytes.append(subtile_byte & 0xFF)
                            this_mold_bytes += tile_bytes
                    else:
                        for tile_index, tile in enumerate(mold.tiles):
                            tile_bytes = bytearray([])
                            animation.molds[mold_index].tiles[tile_index].set_offset(
                                this_mold_offset + len(this_mold_bytes)
                            )
                            found_clone = False
                            if isinstance(tile, _Clone):
                                byte_1: int = (
                                    (0x02) + (tile.mirror << 2) + (tile.invert << 3)
                                )
                                clone = tile.tiles[0]
                                found_offset = 0
                                tmp: int = mold_index
                                while tmp >= 0:
                                    mold = animation.molds[tmp]
                                    if not found_clone:
                                        for ct_index, compare_tile in enumerate(
                                            mold.tiles
                                        ):
                                            if not found_clone and not isinstance(
                                                compare_tile, _Clone
                                            ):
                                                if (
                                                    compare_tile.mirror == clone.mirror
                                                    and compare_tile.invert
                                                    == clone.invert
                                                    and compare_tile.subtiles
                                                    == clone.subtiles
                                                ):
                                                    confirm_tile = True
                                                    conf_i: int = 0
                                                    while (
                                                        conf_i < len(tile.tiles)
                                                        and confirm_tile
                                                    ):
                                                        tmp_tile_1 = tile.tiles[conf_i]
                                                        if ct_index + conf_i >= len(
                                                            mold.tiles
                                                        ):
                                                            confirm_tile = False
                                                            continue
                                                        tmp_tile_2 = mold.tiles[
                                                            ct_index + conf_i
                                                        ]
                                                        if not isinstance(
                                                            tmp_tile_2,
                                                            _WorkingNonGridplaneArrangement,
                                                        ):
                                                            confirm_tile = False
                                                            continue
                                                        if (
                                                            tmp_tile_1.x != tmp_tile_2.x
                                                            or tmp_tile_1.y
                                                            != tmp_tile_2.y
                                                            or tmp_tile_1.mirror
                                                            != tmp_tile_2.mirror
                                                            or tmp_tile_1.invert
                                                            != tmp_tile_2.invert
                                                            or tmp_tile_1.subtiles
                                                            != tmp_tile_2.subtiles
                                                        ):
                                                            confirm_tile = False
                                                            continue
                                                        conf_i += 1
                                                    if confirm_tile:
                                                        found_clone = True
                                                        found_offset = (
                                                            compare_tile.offset
                                                        )
                                    tmp -= 1
                                if found_clone:
                                    byte_1 += len(tile.tiles) << 4
                                    tile_bytes.append(byte_1)
                                    tile_bytes.append(tile.y)
                                    tile_bytes.append(tile.x)
                                    tile_bytes.append(found_offset & 0xFF)
                                    tile_bytes.append((found_offset >> 8) & 0x7F)
                                    this_mold_bytes += tile_bytes
                                else:
                                    raise InvalidSpriteConstructionException(
                                        f"no clones found for anim {anim_id} mold {mold_index}"
                                    )
                            else:
                                if anim_id <= 6:
                                    for subtile in tile.subtiles:
                                        if subtile not in subtile_indexes:
                                            subtile_indexes.append(subtile)
                                tile_bytes.append(tile.y ^ 0x80)
                                tile_bytes.append(tile.x ^ 0x80)
                                byte_upper_1 = 0
                                for index, subtile_byte in enumerate(tile.subtiles):
                                    if subtile_byte > 0:
                                        byte_upper_1 += 1 << (3 - index)
                                        if subtile_byte > 255:
                                            tile_to_set_format = (
                                                complete_animations[anim_id]
                                                .molds[mold_index]
                                                .tiles[tile_index]
                                            )
                                            assert isinstance(
                                                tile_to_set_format,
                                                _WorkingNonGridplaneArrangement,
                                            )
                                            tile_to_set_format.set_format(1)
                                            tile.set_format(1)
                                for subtile_byte in tile.subtiles:
                                    if subtile_byte > 0:
                                        tile_bytes.append(subtile_byte & 0xFF)
                                        if tile.format == 1:
                                            tile_bytes.append(
                                                (subtile_byte >> 8) & 0x01
                                            )
                                byte_lower_1: int = (
                                    (tile.format & 0x03)
                                    + (tile.mirror << 2)
                                    + (tile.invert << 3)
                                )
                                tile_bytes.insert(0, byte_lower_1 + (byte_upper_1 << 4))
                                this_mold_bytes += tile_bytes
                        this_mold_bytes.append(0)
                    mold_bytes += this_mold_bytes
                else:
                    mold_ptrs.extend([0xFF, 0xFF])
            if anim_id <= 6:
                subtile_indexes.sort()
            mold_ptrs.extend([0, 0])

            length_bytes_short: int = (
                2
                + len(sequence_offset)
                + len(mold_offset)
                + len(count_bytes)
                + len(misc_bytes)
                + len(sequence_ptrs)
                + len(sequence_bytes)
                + len(mold_ptrs)
                + len(mold_bytes)
            )
            length_bytes = bytearray(
                [length_bytes_short & 0xFF, (length_bytes_short >> 8) & 0xFF]
            )
            finished_bytes: bytearray = (
                length_bytes
                + sequence_offset
                + mold_offset
                + count_bytes
                + misc_bytes
                + sequence_ptrs
                + sequence_bytes
                + mold_ptrs
                + mold_bytes
            )

            animations_ready_to_place.append((anim_id, finished_bytes))

        animations_ready_to_place.sort(key=lambda x: len(x[1]), reverse=True)
        for anim_id, finished_bytes in animations_ready_to_place:
            anim_ptr = _place_bytes(finished_bytes) + 0xC00000
            animation_pointers_wip[anim_id] = anim_ptr

        for anim_ptr in animation_pointers_wip:
            assert anim_ptr is not None
            animation_pointers.extend(
                [anim_ptr & 0xFF, (anim_ptr >> 8) & 0xFF, (anim_ptr >> 16) & 0xFF]
            )

        anim_tile_ranges: list[tuple[int, bytearray]] = []
        for bank_index, bank in enumerate(_ANIMATION_DATA_BANKS):
            final_offset = bank.start + len(bank.raw_bytes)
            _ANIMATION_DATA_BANKS[bank_index].extend_raw_bytes(
                bytearray([0] * (bank.end - bank.start - len(bank.raw_bytes)))
            )
            # Write each bank to its own address
            anim_tile_ranges.append(
                (bank.start, _ANIMATION_DATA_BANKS[bank_index].raw_bytes)
            )

        sprite_data += bytearray(
            [0] * (SPRITE_PTRS_END - SPRITE_PTRS_START - len(sprite_data))
        )
        image_data += bytearray(
            [0] * (IMAGE_PTRS_END - IMAGE_PTRS_START - len(image_data))
        )
        animation_pointers += bytearray(
            [0] * (ANIMATION_PTRS_END - ANIMATION_PTRS_START - len(animation_pointers))
        )
        patch: dict[int, bytearray] = {}

        patch[0x250000] = bytearray(sprite_data)
        patch[0x251800] = bytearray(image_data) + bytearray(animation_pointers)
        for offset, animation in anim_tile_ranges:
            patch[offset] = animation
        for offset, subtiles in output_tile_ranges:
            patch[offset] = subtiles

        return patch
