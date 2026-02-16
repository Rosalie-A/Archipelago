
from django.core.management.base import BaseCommand
import math, functools, copy, string, random

from smrpgpatchbuilder.datatypes.sprites.ids.misc import SPRITE_PTRS_END, UNCOMPRESSED_GFX_START, PALETTE_OFFSET, IMAGE_PTRS_END, ANIMATION_PTRS_END, SPRITE_PTRS_START, IMAGE_PTRS_START, ANIMATION_PTRS_START, UNCOMPRESSED_GFX_END

class ImagePack:
    index: int = 0
    graphics_pointer: int = 0
    palette_pointer: int = 0
    def __init__(self, index: int, graphics_pointer: int, palette_pointer: int):
        self.index = index
        self.graphics_pointer = graphics_pointer
        self.palette_pointer = palette_pointer

class AnimationSequenceFrame:
    duration: int = 0
    mold_id: int = 0
    def __init__(self, duration: int, mold_id: int):
        self.duration = duration
        self.mold_id = mold_id

class AnimationSequence:
    frames: list[AnimationSequenceFrame] = []
    def __init__(self, frames: list[AnimationSequenceFrame]):
        self.frames = frames

    @property
    def total_duration(self) -> int:
        """Sum of all frame durations in this sequence."""
        return sum(frame.duration for frame in self.frames)

class Tile:
    mirror: bool = False
    invert: bool = False
    format: int = 0
    is_16bit: bool = False
    y_plus: int = 0
    y_minus: int = 0
    y: int = 0
    x: int = 0
    subtile_bytes: list[bytearray | None]
    length: int = 0
    offset: int = 0
    is_clone: bool = False
    subtile_ids: list[int]
    def __init__(self, mirror: bool, invert: bool, format: int, length: int, subtile_bytes: list[bytearray | None], is_16bit: bool = False, y_plus: int = 0, y_minus: int = 0, x: int = 0, y: int = 0, is_clone: bool = False):
        self.mirror = mirror
        self.invert = invert
        self.format = format
        self.length = length
        self.subtile_bytes = subtile_bytes
        self.is_16bit = is_16bit
        self.y_plus = y_plus
        self.y_minus = y_minus
        self.y = y
        self.x = x
    def __str__(self):
        return "<Tile mirror=%r invert=%r x=%i y=%i subtiles=%r>" % (self.mirror, self.invert, self.x, self.y, self.subtile_bytes)

class Clone:
    is_clone: bool = True
    offset: int = 0
    y: int = 0
    x: int = 0
    mirror: bool = False
    invert: bool = False
    tiles: list[Tile] = []
    def __init__(self, x: int = 0, y: int = 0, mirror: bool = False, invert: bool = False, tiles: list[Tile] | None = None):
        self.y = y
        self.x = x
        self.tiles = tiles if tiles is not None else []
        self.mirror = mirror
    def __str__(self):
        return "<Clone mirror=%r invert=%r x=%i y=%i tiles=[\n    %s\n  ]>" % (self.mirror, self.invert, self.x, self.y, "\n    ".join([t.__str__() for t in self.tiles]))

class Mold:
    index: int
    gridplane: bool
    offset: int
    tiles: list[Tile | Clone]
    def __init__(self, index: int, gridplane: bool, tiles: list[Tile | Clone]):
        self.index = index
        self.gridplane = gridplane
        self.tiles = tiles

    def __str__(self):
        return "<Mold %i gridplane=%r tiles=[\n  %s\n]>" % (self.index, self.gridplane, "\n  ".join([t.__str__() for t in self.tiles]))

class AnimationPackProperties:
    molds: list[Mold] = []
    sequences: list[AnimationSequence] = []
    vram_size: int = 0
    def __init__(self, sequences: list[AnimationSequence], molds: list[Mold], vram_size: int):
        self.molds = molds # gridplanemold or nongridplanemold
        self.sequences = sequences
        self.vram_size = vram_size

class AnimationPack:
    index: int
    length: int
    unknown: int
    properties: AnimationPackProperties
    def __init__(self, index: int, properties: AnimationPackProperties, length: int = 0, unknown: int = 0):
        self.index = index
        self.properties = properties
        self.length = length
        self.unknown = unknown

class Sprite:
    index: int = 0
    image_num: int = 0
    palette_offset: int = 0
    animation_num: int = 0
    unknown: int = 0
    def __init__(self, index: int, image_num: int, animation_num: int, palette_offset: int, unknown: int = 0):
        self.index = index
        self.image_num = image_num
        self.animation_num = animation_num
        self.palette_offset = palette_offset
        self.unknown = unknown

class CompleteSprite:
    animation: AnimationPack
    palette_id: int
    palette_offset: int
    unknown_num: int
    animation_num: int
    def __init__(self, animation: AnimationPack, palette_id: int, palette_offset: int = 0, unknown_num: int = 0):
        self.animation = animation
        self.palette_id = palette_id
        self.palette_offset = palette_offset
        self.unknown_num = unknown_num

def sortByUsedSprites(tup1: tuple[tuple[int, ...], list[int]], tup2: tuple[tuple[int, ...], list[int]]) -> int:
    l1 = tup1[1]
    l2 = tup2[1]
    if len(l1) < len(l2):
        l1 += [0] * (len(l2) - len(l1))
    elif len(l1) > len(l2):
        l2 += [0] * (len(l1) - len(l2))
    used = zip(l1, l2)
    for x in used:
        if x[0] < x[1]:
            return -1
        elif x[0] > x[1]:
            return 1
    return 0

def is_significant_tile(tiledata: tuple[int, ...]) -> bool:
    return len([a for a in tiledata if a > 0]) > 4

def tileset_similarity(tileset1: list[tuple[int, ...]], tileset2: list[tuple[int, ...]]) -> int:
    sanitized_t1 = [t for t in tileset1 if is_significant_tile(t)]
    sanitized_t2 = [t for t in tileset2 if is_significant_tile(t)]
    t1 = set(sanitized_t1)
    t2 = set(sanitized_t2)
    similarity = len(set(t1).intersection(set(t2)))
    return similarity

alphabet = string.ascii_lowercase + string.digits

def random_tile_id() -> str:
    return ''.join(random.choices(alphabet, k=8))

class AnimationBank:
    # Remove class-level mutable defaults to avoid sharing across instances
    start: int
    end: int
    tiles: bytearray

    @property
    def remaining_space(self) -> int:
        return self.end - self.start - len(self.tiles)

    @property
    def current_offset(self) -> int:
        return self.start + len(self.tiles)

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.tiles = bytearray([])

def is_same_animation(animation1: AnimationPack, animation2: AnimationPack) -> bool:
    if animation1.unknown != animation2.unknown:
        return False
    if animation1.properties.vram_size != animation2.properties.vram_size:
        return False
    if len(animation1.properties.molds) != len(animation2.properties.molds):
        return False
    if len(animation1.properties.sequences) != len(animation2.properties.sequences):
        return False
    molds = zip(animation1.properties.molds, animation2.properties.molds)
    for m in molds:
        if m[0].gridplane != m[1].gridplane:
            return False
        if len(m[0].tiles) != len(m[1].tiles):
            return False
        for i in range(len(m[0].tiles)):
            ts1 = m[0].tiles[i]
            ts2 = m[1].tiles[i]
            if ts1.is_clone != ts2.is_clone:
                return False
            if ts1.mirror != ts2.mirror:
                return False
            if ts1.invert != ts2.invert:
                return False
            if ts1.x != ts2.x:
                return False
            if ts1.y != ts2.y:
                return False
            if isinstance(ts1, Tile) and isinstance(ts2, Tile) and ts1.y_plus != ts2.y_plus:
                return False
            if isinstance(ts1, Tile) and isinstance(ts2, Tile) and ts1.y_minus != ts2.y_minus:
                return False
            if isinstance(ts1, Tile) and isinstance(ts2, Tile) and ts1.subtile_bytes != ts2.subtile_bytes:
                return False
            if isinstance(ts1, Clone) and isinstance(ts2, Clone):
                if len(ts1.tiles) != len(ts2.tiles):
                    return False
                clonecheck = zip(ts1.tiles, ts2.tiles)
                for ccheck in clonecheck:
                    if ccheck[0].mirror != ccheck[1].mirror:
                        return False
                    if ccheck[0].invert != ccheck[1].invert:
                        return False
                    if ccheck[0].x != ccheck[1].x:
                        return False
                    if ccheck[0].y != ccheck[1].y:
                        return False
                    if ccheck[0].y_plus != ccheck[1].y_plus:
                        return False
                    if ccheck[0].y_minus != ccheck[1].y_minus:
                        return False
                    if ccheck[0].subtile_bytes != ccheck[1].subtile_bytes:
                        return False
    sequences = zip(animation1.properties.sequences, animation2.properties.sequences)
    for s in sequences:
        s1 = s[0]
        s2 = s[1]
        if len(s1.frames) != len(s2.frames):
            return False
        for i in range(len(s1.frames)):
            as1 = s1.frames[i]
            as2 = s2.frames[i]
            if as1.duration != as2.duration:
                return False
            if as1.mold_id != as2.mold_id:
                return False
    return True

def is_clone_start(tile: Tile | Clone, compare_tile: Tile | Clone) -> tuple[bool, int, int]:
    if isinstance(compare_tile, Clone):
        return False, 0, 0
    if isinstance(tile, Tile) and tile.subtile_bytes != compare_tile.subtile_bytes:
        return False, 0, 0
    if compare_tile.x > 255 or compare_tile.y > 255:
        return False, 0, 0
    if tile.x - compare_tile.x < 0 or tile.y - compare_tile.y < 0:
        return False, 0, 0
    if tile.mirror != compare_tile.mirror or tile.invert != compare_tile.invert:
        return False, 0, 0
    return True, tile.x - compare_tile.x, tile.y - compare_tile.y

def is_clone_continuation(tile: Tile | Clone, compare_tile: Tile | Clone, x_offset: int, y_offset: int) -> bool:
    if isinstance(compare_tile, Clone) or isinstance(tile, Clone):
        return False
    if tile.subtile_bytes != compare_tile.subtile_bytes:
        return False
    if (tile.x - compare_tile.x) != x_offset or (tile.y - compare_tile.y) != y_offset:
        return False
    if tile.mirror != compare_tile.mirror:
        return False
    if tile.invert != compare_tile.invert:
        return False
    return True

class CloneCandidate:
    mold_id: int
    start_index: int
    end_index: int
    x_offset: int
    y_offset: int

    def __init__(self, mold_id: int, start_index: int, end_index: int, x_offset: int, y_offset: int):
        self.mold_id = mold_id
        self.start_index = start_index
        self.end_index = end_index
        self.x_offset = x_offset
        self.y_offset = y_offset

    def __eq__(self, other: object) -> bool:
        """value-based equality: two clonecandidate instances are equal when all identifying
        fields match (mold, start, end, x_offset, y_offset)."""
        if not isinstance(other, CloneCandidate):
            return NotImplemented
        return (
            self.mold_id == other.mold_id
            and self.start_index == other.start_index
            and self.end_index == other.end_index
            and self.x_offset == other.x_offset
            and self.y_offset == other.y_offset
        )

    def __hash__(self) -> int:
        """Hash compatible with __eq__ so instances can be used in sets/dicts."""
        return hash((self.mold_id, self.start_index, self.end_index, self.x_offset, self.y_offset))

# find all possible clones of the tile within the given mold tileset
def get_clone_ranges(mold_id: int, tiles: list[Tile | Clone], tile_index: int, compare_tiles: list[Tile | Clone], index: int=0, index2: int=0) -> list[CloneCandidate]:
    tile = tiles[tile_index]
    clone_candidates: list[CloneCandidate] = []
    # don't compare to self
    if mold_id == index2:
        tile_compare_index = tile_index - 1
    else:
        tile_compare_index = len(compare_tiles) - 1

    is_candidate = False
    x_offset = 0
    y_offset = 0
    start = tile_compare_index
    end = tile_compare_index
    check = tile_index

    # final eligibility check of potential clone, adds if passes
    def finish_candidate(end_index: int, start_index: int, x_offset: int, y_offset: int):
        cloned = compare_tiles[start_index:end_index+1]
        if len(cloned) == 0:
            return 
        elif x_offset < 0 or y_offset < 0:
            return 
        elif len(cloned) == 1:
            if tile.x > 255 or tile.y > 255:
                pass
            elif isinstance(tile, Tile) and max(tile.subtile_ids) > 255:
                pass
            elif isinstance(tile, Tile) and len([sb for sb in tile.subtile_ids if sb != 0]) > 2:
                pass
            else:
                return
        clone_candidates.append(CloneCandidate(mold_id, start_index, end_index+1, x_offset, y_offset))
        
    while tile_compare_index >= 0:
        compare_tile = compare_tiles[tile_compare_index]
        is_ending = False
        if not is_candidate:
            is_candidate, x_offset, y_offset = is_clone_start(tile, compare_tile)
            if is_candidate:
                end = tile_compare_index
        elif is_candidate:
            is_ending = (end - tile_compare_index == 15) or (mold_id == index2 and check == end) or not is_clone_continuation(tiles[check], compare_tile, x_offset, y_offset)
        if is_candidate:
            if is_ending or tile_compare_index == 0 or check == 0:
                start = tile_compare_index
                if is_ending:
                    start += 1
                finish_candidate(end, start, x_offset, y_offset)
                is_candidate = False
                x_offset = 0
                y_offset = 0
                mirror = False
                invert = False
                check = tile_index
            else:
                check = max(0, check - 1)
        tile_compare_index -= 1

    # need some way to detect internal clones within the same mold
    # most likely want to do this after looking for clones elsewhere

    return clone_candidates

def find_clones(tiles: list[Tile | Clone], molds: list[Mold], index: int = 0, index2: int = 0) -> list[Tile | Clone]:
    output: list[Tile | Clone] = []
    tmp_output: list[Tile | Clone] = []

    tile_index = len(tiles) - 1
    # iterate backwards thru tiles in the mold we're currently forming
    while tile_index >= 0:
        clone_candidates: list[CloneCandidate] = []
        tile = tiles[tile_index]
        if isinstance(tile, Clone):
            tmp_output.insert(0, tile)
            tile_index -= 1
            continue
        # iterate backwards thru molds to start looking for clones
        mold_index = len(molds) - 1
        while mold_index >= 0:
            mold = molds[mold_index]
            if not mold.gridplane:
                # look for any possible point in previous molds that looks like it could be a clone range ending with this tile
                clone_candidates += get_clone_ranges(mold_index, tiles, tile_index, mold.tiles, index, index2)
            mold_index -= 1

        # if eligible ranges found, create clone container for all tiles in range
        if len(clone_candidates) > 0:
            eligible_candidates = [c for c in clone_candidates if c.x_offset <= 255 and c.y_offset <= 255]
            ineligible_candidates = [c for c in clone_candidates if c not in eligible_candidates] # todo: will this equate two instances of clonecandidate?
            # clone detection just doesnt work out sometimes, ie 3 sets of the same tiles that overall are >255 apart
            # in those cases, un-clone them and just treat as normal tiles
            if len(eligible_candidates) == 0:
                candidate = max(ineligible_candidates, key=lambda item: item.end_index - item.start_index)
                decoupled_tiles = copy.deepcopy(molds[candidate.mold_id].tiles[candidate.start_index:candidate.end_index])
                decoupled_tiles.reverse()
                for c_tile in decoupled_tiles:
                    tmp_output.insert(0, c_tile)
            else:
                candidate = max(eligible_candidates, key=lambda item: item.end_index - item.start_index)
                t = molds[candidate.mold_id].tiles[candidate.start_index:candidate.end_index]
                for tc in t:
                    assert isinstance(tc, Tile)
                tmp_output.insert(0, Clone(
                    mirror=False,
                    invert=False,
                    x=candidate.x_offset,
                    y=candidate.y_offset,
                    tiles=[tc for tc in t if isinstance(tc, Tile)]
                ))
            tile_index -= (candidate.end_index - candidate.start_index)
        # otherwise just append the tile and move onto the next one
        else:
            tmp_output.insert(0, tile)
            tile_index -= 1

    # after scanning previous molds, check for internal clones as well
    tile_index = len(tmp_output) - 1
    ineligible_to_be_clones: list[int] = []
    while tile_index >= 0:
        tile = tmp_output[tile_index]
        if tile_index in ineligible_to_be_clones or isinstance(tile, Clone):
            output.insert(0, tile)
            tile_index -= 1
            continue

        clone_candidates = get_clone_ranges(len(molds), tmp_output, tile_index, tmp_output, index, index2)
        if len(clone_candidates) > 0:
            candidate = max(clone_candidates, key=lambda item: item.end_index - item.start_index)
            output.insert(0, Clone(
                mirror=False,
                invert=False,
                x=candidate.x_offset,
                y=candidate.y_offset,
                tiles=[t for t in tmp_output[candidate.start_index:candidate.end_index] if isinstance(t, Tile)]
            ))
            tile_index -= (candidate.end_index - candidate.start_index)
            ineligible_to_be_clones.extend(list(range(candidate.start_index, candidate.end_index)))
        else:
            output.insert(0, tile)
            tile_index -= 1

    return output

class WIPSprite:
    tiles: list[tuple[int, ...]]
    tile_group: str 
    relative_offset: int
    sprite_data: CompleteSprite

    def __init__(self, sprite_data: CompleteSprite):
        self.sprite_data = sprite_data

class TileGroup:
    tiles: list[tuple[int, ...]]
    used_by: list[int]
    extra: list[tuple[int, ...]]
    variance: bool
    offset: int

    def __init__(self, tiles: list[tuple[int, ...]], used_by: list[int], extra: list[tuple[int, ...]]):
        self.tiles = tiles
        self.used_by = used_by
        self.extra = extra

class SpriteCollection:
    sprites: list[CompleteSprite]
    sprite_data_begins: int 
    image_and_animation_data_begins: int
    animation_data_banks: list[AnimationBank]
    uncompressed_tile_banks: list[AnimationBank]

    def assemble_from_tables_(self,sprites: list[Sprite], images: list[ImagePack], animations: list[AnimationPack], output_tile_ranges: list[tuple[int, bytearray]]=[]) -> tuple[bytearray, bytearray, bytearray, list[tuple[int, bytearray]], list[tuple[int, bytearray]]]:

        sprite_data: list[int] = []
        image_data: list[int] = []
        animation_pointers: list[int] = []

        def place_bytes(these_bytes: bytearray, identifier: str = "unknown", remaining_items: list[tuple[int, int]] | None = None) -> int:
            # find bank with most space
            highest_space = 0
            index = 0
            for b_index, b in enumerate(self.animation_data_banks):
                if highest_space < b.remaining_space:
                    highest_space = b.remaining_space
                    index = b_index
            if len(these_bytes) > self.animation_data_banks[index].remaining_space:
                # Build detailed error message
                error_lines = [
                    f"Could not place animation data into any bank.",
                    f"Animation: {identifier}",
                    f"Data size: {len(these_bytes):,} bytes",
                    "",
                    "Available banks (sorted by remaining space):",
                ]
                sorted_banks = sorted(
                    enumerate(self.animation_data_banks),
                    key=lambda x: x[1].remaining_space,
                    reverse=True
                )
                for b_index, b in sorted_banks:
                    error_lines.append(
                        f"  Bank {b_index}: 0x{b.start:06X}-0x{b.end:06X} "
                        f"({b.remaining_space:,} bytes remaining of {b.end - b.start:,})"
                    )
                if remaining_items:
                    total_remaining = sum(size for _, size in remaining_items)
                    error_lines.append("")
                    error_lines.append(f"Remaining animations to place: {len(remaining_items)} ({total_remaining:,} bytes total)")
                    error_lines.append("Sizes: " + ", ".join(f"{size:,}" for _, size in remaining_items[:20]))
                    if len(remaining_items) > 20:
                        error_lines.append(f"  ... and {len(remaining_items) - 20} more")
                raise Exception("\n".join(error_lines))
            offset = self.animation_data_banks[index].current_offset
            self.animation_data_banks[index].tiles += these_bytes
            return offset

        used_animations: list[int] = []

        for sprite in sprites:
            assert sprite.image_num <= 0x1FF
            assert sprite.palette_offset <= 7
            sprite_data.append(sprite.image_num & 0xFF)
            sprite_data.append(((sprite.image_num >> 8) & 0x01) + (sprite.palette_offset << 1) + (sprite.unknown << 4))
            assert sprite.animation_num <= 0xFFFF
            sprite_data.append(sprite.animation_num & 0xFF)
            sprite_data.append((sprite.animation_num >> 8) & 0xFF)
            if sprite.animation_num not in used_animations:
                used_animations.append(sprite.animation_num)

        for image in images:
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
        animation_pointers_wip: list[int | None] = [None] * len(animations)

        for anim_id, animation in enumerate(animations):

            if anim_id not in used_animations:
                animation = AnimationPack(anim_id, unknown=0x0002, properties=AnimationPackProperties(vram_size=2048,
                    molds=[
                        Mold(0, gridplane=False,
                            tiles=[]
                        ),
                    ],
                    sequences=[
                        AnimationSequence(
                            frames=[]
                        ),
                    ]
                ))

            length_bytes = bytearray()
            sequence_offset = bytearray([0x0C, 0x00])
            mold_offset = bytearray()
            num_sequences = len(animation.properties.sequences)
            num_molds = len(animation.properties.molds)
            assert num_molds <= 32
            assert num_sequences <= 32
            count_bytes = bytearray([num_sequences, num_molds])
            vram = animation.properties.vram_size >> 8
            misc_bytes = bytearray([vram & 0xFF, (vram >> 8) & 0xFF, 0x02, 0x00])
            sequence_ptrs = bytearray([])
            sequence_bytes = bytearray([])
            mold_ptrs = bytearray([])
            mold_bytes = bytearray([])

            for sequence in animation.properties.sequences:
                this_sequence_offset = 0x0C + (len(animation.properties.sequences) + 1) * 2 + len(sequence_bytes)
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
            subtile_indexes: list[int] = []
            for mold_index, mold in enumerate(animation.properties.molds):
                this_mold_offset = 0x0C + len(sequence_ptrs) + len(sequence_bytes) + (len(animation.properties.molds) + 1) * 2 + len(mold_bytes)
                assert this_mold_offset <= 0x7FFF
                animation.properties.molds[mold_index].offset = this_mold_offset
                if mold.gridplane:
                    this_mold_offset += (0x80 << 8)
                if len(mold.tiles) > 0:
                    mold_ptrs.append(this_mold_offset & 0xFF)
                    mold_ptrs.append((this_mold_offset >> 8) & 0xFF)
                    this_mold_bytes = bytearray([])
                    if mold.gridplane:
                        for tile_index, tile in enumerate(mold.tiles):
                            if not isinstance(tile, Tile):
                                continue
                            for i, subtile_id in enumerate(tile.subtile_ids):
                                if subtile_id >= 0x100:
                                    tile.is_16bit = True
                            tile_bytes = bytearray([])
                            animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                            byte_1 = (tile.format & 0x03) + (tile.is_16bit << 3) + (tile.y_plus << 4) + (tile.y_minus << 5) + (tile.mirror << 6) + (tile.invert << 7)
                            tile_bytes.append(byte_1)
                            if tile.is_16bit:
                                subtile_short = 0
                                for i, subtile_id in enumerate(tile.subtile_ids):
                                    if subtile_id >= 0x100:
                                        subtile_short += (1 << i)
                                tile_bytes.append(subtile_short & 0xFF)
                                tile_bytes.append((subtile_short >> 8) & 0xFF)
                            for subtile_id in tile.subtile_ids:
                                tile_bytes.append(subtile_id & 0xFF)
                            this_mold_bytes += tile_bytes
                    else:
                        for tile_index, tile in enumerate(mold.tiles):
                            tile_bytes = bytearray([])
                            animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                            found_clone = False
                            if isinstance(tile, Clone):
                                byte_1 = (0x02) + (tile.mirror << 2) + (tile.invert << 3)
                                ct = tile.tiles[0]
                                found_offset = 0
                                tmp = mold_index
                                while tmp >= 0:
                                    m = animation.properties.molds[tmp]
                                    if not found_clone:
                                        for ct_index, compare_tile in enumerate(m.tiles):
                                            if not found_clone and isinstance(compare_tile, Tile):
                                                if compare_tile.mirror == ct.mirror and compare_tile.invert == ct.invert and compare_tile.subtile_bytes == ct.subtile_bytes:
                                                    confirm_tile = True
                                                    conf_i = 0
                                                    while conf_i < len(tile.tiles) and confirm_tile:
                                                        tmp_tile_1 = tile.tiles[conf_i]
                                                        if ct_index + conf_i >= len(m.tiles):
                                                            confirm_tile = False
                                                            continue
                                                        tmp_tile_2 = m.tiles[ct_index + conf_i]
                                                        if isinstance(tmp_tile_2, Clone):
                                                            confirm_tile = False
                                                            continue
                                                        elif tmp_tile_1.x != tmp_tile_2.x or tmp_tile_1.y != tmp_tile_2.y or tmp_tile_1.mirror != tmp_tile_2.mirror or tmp_tile_1.invert != tmp_tile_2.invert or tmp_tile_1.subtile_bytes != tmp_tile_2.subtile_bytes:
                                                            confirm_tile = False
                                                            continue
                                                        conf_i += 1
                                                    if confirm_tile:
                                                        found_clone = True
                                                        found_offset = compare_tile.offset
                                    tmp -= 1
                                if found_clone:
                                    byte_1 += (len(tile.tiles) << 4)
                                    tile_bytes.append(byte_1)
                                    tile_bytes.append(tile.y)
                                    tile_bytes.append(tile.x)
                                    tile_bytes.append(found_offset & 0xFF)
                                    tile_bytes.append((found_offset >> 8) & 0x7F)
                                    this_mold_bytes += tile_bytes
                                else:
                                    raise Exception("no clones found for anim %i mold %i" % (anim_id, mold_index))
                            else:
                                if anim_id <= 6:
                                    for st in tile.subtile_ids:
                                        if st not in subtile_indexes:
                                            subtile_indexes.append(st)
                                tile_bytes.append((tile.y & 0xFF) ^ 0x80)
                                tile_bytes.append((tile.x & 0xFF) ^ 0x80)
                                byte_upper_1 = 0
                                for i, subtile_id in enumerate(tile.subtile_ids):
                                    if subtile_id > 0:
                                        byte_upper_1 += (1 << (3-i))
                                        if subtile_id > 255:
                                            t = animations[anim_id].properties.molds[mold_index].tiles[tile_index]
                                            assert isinstance(t, Tile)
                                            t.format = 1
                                            animations[anim_id].properties.molds[mold_index].tiles[tile_index] = t
                                            tile.format = 1
                                for i, subtile_id in enumerate(tile.subtile_ids):
                                    if subtile_id > 0:
                                        tile_bytes.append(subtile_id & 0xFF)
                                        if tile.format == 1:
                                            tile_bytes.append((subtile_id >> 8) & 0x01)
                                byte_lower_1 = (tile.format & 0x03) + (tile.mirror << 2) + (tile.invert << 3)
                                tile_bytes.insert(0, byte_lower_1 + (byte_upper_1 << 4))
                                this_mold_bytes += tile_bytes
                        this_mold_bytes.append(0)
                    mold_bytes += this_mold_bytes
                else:
                    mold_ptrs.extend([0xFF, 0xFF])
            if anim_id <= 6:
                subtile_indexes.sort()
            mold_ptrs.extend([0, 0])

            length_bytes_short = 2 + len(sequence_offset) + len(mold_offset) + len(count_bytes) + len(misc_bytes) + len(sequence_ptrs) + len(sequence_bytes) + len(mold_ptrs) + len(mold_bytes)
            length_bytes = bytearray([length_bytes_short & 0xFF, (length_bytes_short >> 8) & 0xFF])
            finished_bytes = length_bytes + sequence_offset + mold_offset + count_bytes + misc_bytes + sequence_ptrs + sequence_bytes + mold_ptrs + mold_bytes

            animations_ready_to_place.append((anim_id, finished_bytes))

        animations_ready_to_place.sort(key=lambda x: len(x[1]), reverse=True)
        for i, (anim_id, finished_bytes) in enumerate(animations_ready_to_place):
            # Calculate remaining items (including current) for error reporting
            remaining = [(aid, len(fb)) for aid, fb in animations_ready_to_place[i:]]
            anim_ptr = place_bytes(finished_bytes, f"animation #{anim_id}", remaining) + 0xC00000
            animation_pointers_wip[anim_id] = anim_ptr

        for anim_ptr in animation_pointers_wip:
            assert anim_ptr is not None
            animation_pointers.extend([anim_ptr & 0xFF, (anim_ptr >> 8) & 0xFF, (anim_ptr >> 16) & 0xFF])

        anim_tile_ranges: list[tuple[int, bytearray]] = []
        for bank_index, b in enumerate(self.animation_data_banks):
            self.animation_data_banks[bank_index].tiles += bytearray([0] * (b.end - b.start - len(b.tiles)))
            # Write each bank to its own address
            anim_tile_ranges.append((b.start, self.animation_data_banks[bank_index].tiles))

        sprite_data += bytearray([0] * (SPRITE_PTRS_END - SPRITE_PTRS_START - len(sprite_data)))
        image_data += bytearray([0] * (IMAGE_PTRS_END - IMAGE_PTRS_START - len(image_data)))
        animation_pointers += bytearray([0] * (ANIMATION_PTRS_END - ANIMATION_PTRS_START - len(animation_pointers)))
        
        return bytearray(sprite_data), bytearray(image_data), bytearray(animation_pointers), anim_tile_ranges, output_tile_ranges

    def assemble_from_tables(self, sprites: list[CompleteSprite], insert_whitespace=False) -> tuple[bytearray, bytearray, bytearray, list[tuple[int, bytearray]], list[tuple[int, bytearray]]]:
        # CRITICAL: Reset all banks before assembling to prevent data from previous runs
        for bank in self.uncompressed_tile_banks:
            bank.tiles = bytearray([])

        for bank in self.animation_data_banks:
            bank.tiles = bytearray([])

        tile_groups: dict[str, TileGroup] = {}
        wip_sprites: list[WIPSprite] = []

        def get_most_similar_tileset(ts: list[tuple[int, ...]]) -> tuple[str | None, float]:
            best: str | None = None
            best_similarity: int = 0
            for k in tile_groups:
                similarity = tileset_similarity(ts, tile_groups[k].tiles)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best = k
            if best is not None:
                return best, max(best_similarity/len(ts), best_similarity/len(tile_groups[best].tiles))
            else:
                return None, 0

        def get_comparative_similarity(key1: int, key2: int) -> float:
            similarity = tileset_similarity(wip_sprites[key1].tiles, wip_sprites[key2].tiles) / len([y for y in wip_sprites[key1].tiles if is_significant_tile(y)])
            if similarity == 1:
                return int(similarity)
            return math.trunc(round(similarity * 10.0)) / 10

        def rearrange_tiles(group: TileGroup) -> TileGroup:
            tile_use: list[tuple[tuple[int, ...], list[int]]] = []
            relevant_sprites = group.used_by
            all_tiles = group.tiles

            for tile in all_tiles:
                sprites_using_this_tile: list[int] = []
                for sprite_id in relevant_sprites:
                    if tile in wip_sprites[sprite_id].tiles:
                        sprites_using_this_tile.append(sprite_id)
                tile_use.append((tile, sprites_using_this_tile))

            tile_use.sort(key=functools.cmp_to_key(sortByUsedSprites))

            return TileGroup(
                used_by=group.used_by,
                tiles=[t[0] for t in tile_use],
                extra=group.extra
            )

        unique_tiles_length = 0

        def place_bytes(these_bytes: bytearray, identifier: str = "unknown", remaining_items: list[tuple[str, int]] | None = None) -> int:
            # The SNES reads graphics data in blocks, and some ROM editors (like LAZYSHELL)
            # read 0x4000 bytes for each sprite graphics block. To prevent corruption from
            # cross-bank reads, ensure at least 0x4000 bytes remain after placement.
            GRAPHICS_READ_SIZE = 0x4000

            # CRITICAL: ImagePacket pointers are masked with 0xFFF0, so tiles MUST be placed
            # on 16-byte aligned addresses. Add padding if needed.
            REQUIRED_ALIGNMENT = 0x10

            # find bank with most space that can accommodate data + buffer
            highest_space: int = 0
            index: int = 0
            for b_index, b in enumerate(self.uncompressed_tile_banks):
                total_space_needed = len(these_bytes) + GRAPHICS_READ_SIZE
                if b.remaining_space >= total_space_needed:
                    if highest_space < b.remaining_space:
                        highest_space = b.remaining_space
                        index = b_index

            # If no bank can accommodate data + buffer, fall back to largest available bank
            if highest_space == 0:
                for b_index, b in enumerate(self.uncompressed_tile_banks):
                    if b.remaining_space >= len(these_bytes):
                        if highest_space < b.remaining_space:
                            highest_space = b.remaining_space
                            index = b_index

            if len(these_bytes) > self.uncompressed_tile_banks[index].remaining_space:
                # Build detailed error message
                error_lines = [
                    f"Could not place tile data into any bank.",
                    f"Tile group: {identifier}",
                    f"Data size: {len(these_bytes):,} bytes",
                    "",
                    "Available tile banks (sorted by remaining space):",
                ]
                sorted_banks = sorted(
                    enumerate(self.uncompressed_tile_banks),
                    key=lambda x: x[1].remaining_space,
                    reverse=True
                )
                for b_index, b in sorted_banks:
                    error_lines.append(
                        f"  Bank {b_index}: 0x{b.start:06X}-0x{b.end:06X} "
                        f"({b.remaining_space:,} bytes remaining of {b.end - b.start:,})"
                    )
                if remaining_items:
                    total_remaining = sum(size for _, size in remaining_items)
                    error_lines.append("")
                    error_lines.append(f"Remaining tile groups to place: {len(remaining_items)} ({total_remaining:,} bytes total)")
                    error_lines.append("Sizes: " + ", ".join(f"{size:,}" for _, size in remaining_items[:20]))
                    if len(remaining_items) > 20:
                        error_lines.append(f"  ... and {len(remaining_items) - 20} more")
                raise Exception("\n".join(error_lines))

            # Align to required boundary by adding padding if necessary
            current_offset = self.uncompressed_tile_banks[index].current_offset
            misalignment = current_offset % REQUIRED_ALIGNMENT
            if misalignment != 0:
                padding_needed = REQUIRED_ALIGNMENT - misalignment
                self.uncompressed_tile_banks[index].tiles += bytearray(padding_needed)
                current_offset += padding_needed

            offset = current_offset
            self.uncompressed_tile_banks[index].tiles += these_bytes
            return offset

        # collect unique subtiles and group sprites by graphic similarity
        for index, sprite in enumerate(sprites):
            wip_sprite = WIPSprite(sprite)

            unique_subtiles: list[tuple[int, ...]] = []
            for mold in sprite.animation.properties.molds:
                for tile in [t for t in mold.tiles if isinstance(t, Tile)]:
                    for subtile in tile.subtile_bytes:
                        if subtile is not None:
                            hashable = tuple(subtile)
                            if hashable not in unique_subtiles:
                                unique_subtiles.append(hashable)
            key, sim = get_most_similar_tileset(unique_subtiles)

            if key is None or sim < 0.075: # 0.075 seems to be the sweet spot
                tile_id = random_tile_id()
                while tile_id in tile_groups:
                    tile_id = random_tile_id()
                tile_groups[tile_id] = TileGroup(tiles=unique_subtiles, used_by=[index], extra=[])
                key = tile_id
            else:
                tile_groups[key].used_by.append(index)
                # CRITICAL: Preserve order while removing duplicates. Using set() would randomize order!
                combined = tile_groups[key].tiles + unique_subtiles
                seen = set()
                ordered_unique = []
                for tile in combined:
                    if tile not in seen:
                        seen.add(tile)
                        ordered_unique.append(tile)
                tile_groups[key].tiles = ordered_unique
            wip_sprite.tiles = unique_subtiles
            wip_sprite.tile_group = key
            wip_sprite.relative_offset = 0
            wip_sprites.append(wip_sprite)

        # within each tile group, determine which sprites actually use which tiles
        for k in tile_groups:
            # group tiles together by proximity
            has_variance = False
            if len(tile_groups[k].used_by) > 1:
                variance = []
                for t in tile_groups[k].used_by:
                    variance.append([get_comparative_similarity(t, x) for x in tile_groups[k].used_by])
                for x in range(len(variance)):
                    for y in range(x+1, len(variance)):
                        if variance[x][y] != 1 and variance[y][x] != 1:
                            has_variance = True
            if has_variance:
                tile_groups[k] = rearrange_tiles(tile_groups[k])
            else:
                tile_groups[k].tiles = tile_groups[k].tiles
            tile_groups[k].variance = has_variance
            unique_tiles_length += len(tile_groups[k].tiles)

        # calculate free space
        free_tiles = (UNCOMPRESSED_GFX_END - UNCOMPRESSED_GFX_START - (unique_tiles_length * 0x20)) // 0x20
        free_tiles -= 64
        if free_tiles < 0:
            free_tiles = 0

        complete_sprites: list[Sprite] = []
        complete_images: list[ImagePack] = []
        complete_animations: list[AnimationPack] = []

        # find sprites which are going to cause problems because os ubtile deltas > 512
        # and duplicate tiles where necessary
        for sprite_index, sprite in enumerate(wip_sprites):
            tile_key = sprite.tile_group
            available_tiles = tile_groups[tile_key].tiles
            if len(sprite.tiles) == 0:
                lowest_subtile_index = 0
            else:
                lowest_subtile_index = len(available_tiles)
                highest_subtile_index = 0
                all_indexes_for_this_tile = []
                for t in sprite.tiles:
                    tilegroup_index_of_this_tile = available_tiles.index(t)
                    if tilegroup_index_of_this_tile not in all_indexes_for_this_tile:
                        all_indexes_for_this_tile.append(tilegroup_index_of_this_tile)
                    if tilegroup_index_of_this_tile < lowest_subtile_index:
                        lowest_subtile_index = tilegroup_index_of_this_tile
                    if tilegroup_index_of_this_tile > highest_subtile_index:
                        highest_subtile_index = tilegroup_index_of_this_tile
                all_indexes_for_this_tile.sort()
                
                if highest_subtile_index - lowest_subtile_index > 510:
                    extra_tiles = []
                    smallest_range = highest_subtile_index - lowest_subtile_index
                    cutoff_index = lowest_subtile_index
                    for tg_index, st_index in enumerate(all_indexes_for_this_tile):
                        next_tg_index = tg_index + 1
                        next_st_index = st_index+ 1
                        if next_tg_index >= len(all_indexes_for_this_tile):
                            continue

                        tiles_needing_shift = all_indexes_for_this_tile[0:next_tg_index]
                        tentative_clones = [t for t in tiles_needing_shift if available_tiles[t] not in tile_groups[tile_key].extra]

                        remanining_buffer = available_tiles[next_st_index:]

                        this_range = len(remanining_buffer) + len(tile_groups[tile_key].extra) + len(tentative_clones)

                        if this_range < smallest_range:
                            smallest_range = this_range
                            cutoff_index = next_st_index
                    # if still too big, convert into its own tileset?
                    lowest_subtile_index = cutoff_index
                    # add too-low sprite ids to be duped at the end
                    new_tile_pool = tile_groups[tile_key].tiles[cutoff_index:] + tile_groups[tile_key].extra
                    for t_index in all_indexes_for_this_tile:
                        this_tile = available_tiles[t_index]
                        if this_tile not in extra_tiles and this_tile not in new_tile_pool:
                            extra_tiles.append(this_tile)
                    tile_groups[tile_key].extra.extend(extra_tiles)

            wip_sprites[sprite_index].relative_offset = lowest_subtile_index

        # start placing tile groups and get offsets for them
        sortable_tile_groups: list[tuple[str, TileGroup]] = []
        for key in tile_groups:
            sortable_tile_groups.append((key, tile_groups[key]))
        
        
        sortable_tile_groups.sort(key=lambda x: len(x[1].tiles), reverse=True)
        # Pre-calculate sizes for remaining items reporting
        tile_group_sizes = [(key, sum(len(bytearray(t)) for t in group.tiles + group.extra))
                           for key, group in sortable_tile_groups]
        for i, (tile_key, group) in enumerate(sortable_tile_groups):
            tilebytes = bytearray([])
            for t in group.tiles + group.extra:
                tilebytes += bytearray(t)
            # Calculate remaining items for error reporting
            remaining = tile_group_sizes[i:]
            group_offset = place_bytes(tilebytes, f"tile_group '{tile_key}'", remaining)
            tile_groups[tile_key].offset = group_offset

        # start building stuff
        for sprite_index, sprite in enumerate(wip_sprites):
            tile_key = sprite.tile_group
            available_tiles = tile_groups[tile_key].tiles[sprite.relative_offset:] + tile_groups[tile_key].extra

            lowest_subtile_index = len(available_tiles)
            highest_subtile_index = 0
            all_indexes_for_this_tile = []
            for t in sprite.tiles:
                tilegroup_index_of_this_tile = available_tiles.index(t)
                if tilegroup_index_of_this_tile < lowest_subtile_index:
                    lowest_subtile_index = tilegroup_index_of_this_tile
                if tilegroup_index_of_this_tile > highest_subtile_index:
                    highest_subtile_index = tilegroup_index_of_this_tile


            inserting_whitespace_before = False
            whitespace_amount = 0
            # check if this tile group has already been placed
            offset = tile_groups[tile_key].offset + sprite.relative_offset * 0x20

            if len(available_tiles) > 510:
                subtile_subtract = lowest_subtile_index
            else:
                subtile_subtract = 0
            # get image pack #, or create new
            if not inserting_whitespace_before:
                offset += ((subtile_subtract) * 0x20)
            # need to change this to accommodate diff offsets in same tile group
            palette_ptr = PALETTE_OFFSET + sprite.sprite_data.palette_id * 30
            image_index_to_use = len(complete_images)
            for image_index, image in enumerate(complete_images):
                if image.graphics_pointer == offset and image.palette_pointer == palette_ptr:
                    image_index_to_use = image_index
            if image_index_to_use == len(complete_images):
                complete_images.append(ImagePack(image_index_to_use, offset, palette_ptr))

            # get animation #, or create new
            animation_num_to_use = len(complete_animations)
            for prev_sprite_index, prev_sprite in enumerate(wip_sprites[0:sprite_index]):
                if is_same_animation(sprite.sprite_data.animation, prev_sprite.sprite_data.animation):
                    animation_num_to_use = complete_sprites[prev_sprite_index].animation_num
            # if not found, create new
            if animation_num_to_use == len(complete_animations):
                molds: list[Mold] = []
                for mold_index, m in enumerate(sprite.sprite_data.animation.properties.molds):
                    # build numerical subtile bytes
                    these_tiles: list[Tile | Clone] = []
                    for tile in [t for t in m.tiles if isinstance(t, Tile)]:
                        subtile_ids: list[int] = []
                        for subtile in tile.subtile_bytes:
                            if subtile is None:
                                subtile_index = 0
                            else:
                                subtile_index = available_tiles.index(tuple(subtile)) + 1 - subtile_subtract
                                if inserting_whitespace_before:
                                    subtile_index += whitespace_amount
                            subtile_ids.append(subtile_index)
                        this_tile = copy.deepcopy(tile)
                        this_tile.subtile_ids = subtile_ids
                        these_tiles.append(this_tile)
                    this_mold = copy.deepcopy(m)

                    # create clones and use in mold
                    if not this_mold.gridplane:
                        clones = find_clones(these_tiles, molds, sprite_index, mold_index)
                        these_tiles = clones
                    this_mold.tiles = these_tiles
                    molds.append(this_mold)

                this_props = copy.deepcopy(sprite.sprite_data.animation.properties)
                this_props.molds = molds
                complete_animations.append(AnimationPack(animation_num_to_use, length=sprite.sprite_data.animation.length, unknown=sprite.sprite_data.animation.unknown, properties=this_props))

            # create sprite pack
            complete_sprites.append(Sprite(len(complete_sprites), image_index_to_use, animation_num_to_use, sprite.sprite_data.palette_offset, sprite.sprite_data.unknown_num))
        

        output_tile_ranges: list[tuple[int, bytearray]] = []
        final_offset = self.uncompressed_tile_banks[0].start
        for bank_index, b in enumerate(self.uncompressed_tile_banks):
            final_offset = b.start + len(b.tiles)
            self.uncompressed_tile_banks[bank_index].tiles += bytearray([0] * (b.end - b.start - len(b.tiles)))
            # Write each bank to its own address
            output_tile_ranges.append((b.start, self.uncompressed_tile_banks[bank_index].tiles))
        
        if len(complete_images) > 512:
            raise ValueError("too many images: %i" % len(complete_images))
        if len(complete_images) < 512:
            ind = len(complete_images)
            while ind < 512:
                complete_images.append(ImagePack(ind, UNCOMPRESSED_GFX_START + final_offset, 0x250000))
                ind += 1
        if len(complete_animations) < 444:
            ind = len(complete_animations)
            while ind < 444:
                complete_animations.append(AnimationPack(ind, unknown=0x0002, properties=AnimationPackProperties(
                    vram_size=2048,
                    molds=[Mold(0, gridplane=False, tiles=[])],
                    sequences=[AnimationSequence(frames=[])]
                )))
                ind += 1

        return self.assemble_from_tables_(complete_sprites, complete_images, complete_animations, output_tile_ranges)

    def render(self, whitespace: bool = False) -> list[tuple[int, bytearray]]:
        sprite_data, image_data, animation_pointers, animation_data, tiles = self.assemble_from_tables(self.sprites, whitespace)

        # Zero out all sprite data ranges before writing to prevent leftover data
        zero_ranges = []

        # Zero sprite data region
        sprite_data_size = len(sprite_data)
        zero_ranges.append((self.sprite_data_begins, bytearray(sprite_data_size)))

        # Zero image and animation data region
        image_animation_size = len(image_data) + len(animation_pointers)
        zero_ranges.append((self.image_and_animation_data_begins, bytearray(image_animation_size)))

        # Zero all animation data banks
        for bank in self.animation_data_banks:
            bank_size = bank.end - bank.start
            zero_ranges.append((bank.start, bytearray(bank_size)))

        # Zero all uncompressed tile banks
        for bank in self.uncompressed_tile_banks:
            bank_size = bank.end - bank.start
            zero_ranges.append((bank.start, bytearray(bank_size)))

        # Return zeros first, then actual data (so data overwrites zeros)
        return zero_ranges + [
            (self.sprite_data_begins, sprite_data),
            (self.image_and_animation_data_begins, image_data + animation_pointers),
        ] + animation_data + tiles

    def __init__(self, sprites: list[CompleteSprite], animation_data_banks: list[AnimationBank], uncompressed_tile_banks: list[AnimationBank], sprite_data_begins: int, image_and_animation_data_begins: int):
        self.sprites = sprites
        self.sprite_data_begins = sprite_data_begins
        self.image_and_animation_data_begins = image_and_animation_data_begins
        self.animation_data_banks = animation_data_banks
        self.uncompressed_tile_banks = uncompressed_tile_banks