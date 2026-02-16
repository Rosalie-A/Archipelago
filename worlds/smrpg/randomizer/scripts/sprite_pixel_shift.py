"""Utility functions for shifting pixel data in gridplane sprites.

This module provides functions to decode SNES 4bpp planar tile data,
shift pixels by arbitrary offsets, and re-encode back to 4bpp format.

Usage:
    python -m randomizer.scripts.sprite_pixel_shift <sprite_id> <dx> <dy>

Example:
    python -m randomizer.scripts.sprite_pixel_shift 960 4 7

This will output the shifted subtile_bytes for all gridplane molds in the
specified sprite, which can be copied into the sprite file.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.graphics.classes import Mold


def decode_4bpp_subtile(data: bytearray | None) -> list[list[int]]:
    """Decode a 32-byte SNES 4bpp planar subtile into an 8x8 pixel array.

    SNES 4bpp format:
    - Bytes 0-15: Bitplanes 0 and 1, interleaved by row
    - Bytes 16-31: Bitplanes 2 and 3, interleaved by row

    For row y:
      - byte[2y] = bitplane 0
      - byte[2y+1] = bitplane 1
      - byte[16+2y] = bitplane 2
      - byte[16+2y+1] = bitplane 3

    Pixel x uses bit (7-x) from each bitplane byte (MSB = leftmost pixel).

    Args:
        data: 32-byte bytearray, or None for empty/transparent tile

    Returns:
        8x8 list of 4-bit color indices (0 = transparent)
    """
    if data is None:
        return [[0] * 8 for _ in range(8)]

    assert len(data) == 32, f"Expected 32 bytes, got {len(data)}"

    pixels: list[list[int]] = []
    for y in range(8):
        row: list[int] = []
        bp0 = data[2 * y]
        bp1 = data[2 * y + 1]
        bp2 = data[16 + 2 * y]
        bp3 = data[16 + 2 * y + 1]

        for x in range(8):
            bit_pos = 7 - x
            color = (
                ((bp0 >> bit_pos) & 1) |
                (((bp1 >> bit_pos) & 1) << 1) |
                (((bp2 >> bit_pos) & 1) << 2) |
                (((bp3 >> bit_pos) & 1) << 3)
            )
            row.append(color)
        pixels.append(row)

    return pixels


def encode_4bpp_subtile(pixels: list[list[int]]) -> bytearray:
    """Encode an 8x8 pixel array back to 32-byte SNES 4bpp planar format.

    Args:
        pixels: 8x8 list of 4-bit color indices

    Returns:
        32-byte bytearray in SNES 4bpp planar format
    """
    assert len(pixels) == 8 and all(len(row) == 8 for row in pixels)

    data = bytearray(32)

    for y in range(8):
        bp0 = 0
        bp1 = 0
        bp2 = 0
        bp3 = 0

        for x in range(8):
            color = pixels[y][x] & 0x0F
            bit_pos = 7 - x

            if color & 1:
                bp0 |= (1 << bit_pos)
            if color & 2:
                bp1 |= (1 << bit_pos)
            if color & 4:
                bp2 |= (1 << bit_pos)
            if color & 8:
                bp3 |= (1 << bit_pos)

        data[2 * y] = bp0
        data[2 * y + 1] = bp1
        data[16 + 2 * y] = bp2
        data[16 + 2 * y + 1] = bp3

    return data


def is_subtile_empty(pixels: list[list[int]]) -> bool:
    """Check if an 8x8 pixel array is all zeros (transparent)."""
    return all(pixels[y][x] == 0 for y in range(8) for x in range(8))


def get_gridplane_dimensions(format_val: int) -> tuple[int, int]:
    """Get grid dimensions (width, height in subtiles) for a gridplane format.

    Format values:
        0 = 3x3 (24x24 pixels)
        1 = 3x4 (24x32 pixels)
        2 = 4x3 (32x24 pixels)
        3 = 4x4 (32x32 pixels)
    """
    if format_val == 0:
        return (3, 3)
    elif format_val == 1:
        return (3, 4)
    elif format_val == 2:
        return (4, 3)
    elif format_val == 3:
        return (4, 4)
    else:
        raise ValueError(f"Unknown gridplane format: {format_val}")


def shift_gridplane_mold(mold: Mold, dx: int, dy: int) -> None:
    """Shift all pixel data in a gridplane mold by (dx, dy) pixels.

    Pixels that shift off the edge are lost. Pixels shift into previously
    empty areas. The mold's subtiles are modified in place.

    Args:
        mold: A gridplane mold with a single tile containing subtiles
        dx: Pixels to shift right (positive) or left (negative)
        dy: Pixels to shift down (positive) or up (negative)
    """
    if not mold.gridplane:
        raise ValueError("Can only shift gridplane molds")

    tile = mold.tiles[0]
    subtiles = tile.subtile_bytes
    format_val = tile.format

    grid_w, grid_h = get_gridplane_dimensions(format_val)
    total_subtiles = grid_w * grid_h

    if len(subtiles) != total_subtiles:
        raise ValueError(f"Expected {total_subtiles} subtiles for format {format_val}, got {len(subtiles)}")

    img_w = grid_w * 8
    img_h = grid_h * 8

    # Decode all subtiles into full image
    full_image: list[list[int]] = [[0] * img_w for _ in range(img_h)]

    for subtile_idx, subtile_data in enumerate(subtiles):
        subtile_x = subtile_idx % grid_w
        subtile_y = subtile_idx // grid_w
        subtile_pixels = decode_4bpp_subtile(subtile_data)

        for py in range(8):
            for px in range(8):
                img_x = subtile_x * 8 + px
                img_y = subtile_y * 8 + py
                full_image[img_y][img_x] = subtile_pixels[py][px]

    # Create shifted image
    shifted_image: list[list[int]] = [[0] * img_w for _ in range(img_h)]

    for src_y in range(img_h):
        for src_x in range(img_w):
            dst_x = src_x + dx
            dst_y = src_y + dy

            if 0 <= dst_x < img_w and 0 <= dst_y < img_h:
                shifted_image[dst_y][dst_x] = full_image[src_y][src_x]

    # Split back into subtiles
    new_subtiles: list[bytearray | None] = []

    for subtile_idx in range(total_subtiles):
        subtile_x = subtile_idx % grid_w
        subtile_y = subtile_idx // grid_w

        subtile_pixels: list[list[int]] = []
        for py in range(8):
            row: list[int] = []
            for px in range(8):
                img_x = subtile_x * 8 + px
                img_y = subtile_y * 8 + py
                row.append(shifted_image[img_y][img_x])
            subtile_pixels.append(row)

        if is_subtile_empty(subtile_pixels):
            new_subtiles.append(None)
        else:
            new_subtiles.append(encode_4bpp_subtile(subtile_pixels))

    tile.subtile_bytes = new_subtiles


def print_shifted_sprite(sprite_id: int, dx: int, dy: int) -> None:
    """Load a sprite, shift its gridplane molds, and print the new subtile_bytes.

    Args:
        sprite_id: The sprite ID to load (e.g., 960)
        dx: Pixels to shift right (positive) or left (negative)
        dy: Pixels to shift down (positive) or up (negative)
    """
    import copy
    import importlib

    # Try to import the sprite module
    module_name = f"randomizer.data.sprites.objects.sprite_{sprite_id}"
    try:
        sprite_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Could not find sprite module: {module_name}")
        return

    sprite = copy.deepcopy(sprite_module.sprite)
    molds = sprite.animation.properties.molds

    print(f"# Sprite {sprite_id} - shifted by ({dx}, {dy}) pixels")
    print(f"# Gridplane molds only; non-gridplane molds unchanged")
    print()

    for i, mold in enumerate(molds):
        if mold.gridplane:
            shift_gridplane_mold(mold, dx, dy)
            tile = mold.tiles[0]

            print(f"# Mold {i} - gridplane format {tile.format}")
            print("subtile_bytes=[")
            for sb in tile.subtile_bytes:
                if sb is None:
                    print("    None,")
                else:
                    print(f"    bytearray({repr(bytes(sb))}),")
            print("]")
            print()
        else:
            print(f"# Mold {i} - non-gridplane (skipped)")
            print()


def visualize_mold(sprite_id: int, mold_index: int, dx: int = 0, dy: int = 0) -> None:
    """Visualize a gridplane mold before and after shifting.

    Args:
        sprite_id: The sprite ID to load
        mold_index: Which mold to visualize
        dx: Pixels to shift right
        dy: Pixels to shift down
    """
    import copy
    import importlib

    module_name = f"randomizer.data.sprites.objects.sprite_{sprite_id}"
    try:
        sprite_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Could not find sprite module: {module_name}")
        return

    sprite = copy.deepcopy(sprite_module.sprite)
    molds = sprite.animation.properties.molds

    if mold_index >= len(molds):
        print(f"Error: Mold {mold_index} does not exist (sprite has {len(molds)} molds)")
        return

    mold = molds[mold_index]
    if not mold.gridplane:
        print(f"Error: Mold {mold_index} is not a gridplane mold")
        return

    tile = mold.tiles[0]
    grid_w, grid_h = get_gridplane_dimensions(tile.format)
    img_w, img_h = grid_w * 8, grid_h * 8

    def build_image(tile):
        img = [[0] * img_w for _ in range(img_h)]
        for idx, data in enumerate(tile.subtile_bytes):
            sx, sy = idx % grid_w, idx // grid_w
            pixels = decode_4bpp_subtile(data)
            for py in range(8):
                for px in range(8):
                    img[sy * 8 + py][sx * 8 + px] = pixels[py][px]
        return img

    def print_image(img, label):
        print(f"\n{label}:")
        for row in img:
            print("".join(["." if p == 0 else hex(p)[2:] for p in row]))

    print_image(build_image(tile), f"BEFORE shift (mold {mold_index})")

    if dx != 0 or dy != 0:
        shift_gridplane_mold(mold, dx, dy)
        print_image(build_image(tile), f"AFTER shift (+{dx} right, +{dy} down)")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m randomizer.scripts.sprite_pixel_shift <sprite_id> <dx> <dy>")
        print("  python -m randomizer.scripts.sprite_pixel_shift --visualize <sprite_id> <mold_index> [dx] [dy]")
        print()
        print("Examples:")
        print("  python -m randomizer.scripts.sprite_pixel_shift 960 4 7")
        print("  python -m randomizer.scripts.sprite_pixel_shift --visualize 960 0 4 7")
        sys.exit(1)

    if sys.argv[1] == "--visualize":
        if len(sys.argv) < 4:
            print("Usage: --visualize <sprite_id> <mold_index> [dx] [dy]")
            sys.exit(1)
        sprite_id = int(sys.argv[2])
        mold_index = int(sys.argv[3])
        dx = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        dy = int(sys.argv[5]) if len(sys.argv) > 5 else 0
        visualize_mold(sprite_id, mold_index, dx, dy)
    else:
        if len(sys.argv) < 4:
            print("Usage: <sprite_id> <dx> <dy>")
            sys.exit(1)
        sprite_id = int(sys.argv[1])
        dx = int(sys.argv[2])
        dy = int(sys.argv[3])
        print_shifted_sprite(sprite_id, dx, dy)
