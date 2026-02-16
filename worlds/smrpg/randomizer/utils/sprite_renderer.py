"""Utility for rendering SMRPG sprites to PNG images with custom palettes.

This module provides functionality to:
1. Decode SNES 4bpp graphics data from sprite subtiles
2. Apply custom palettes to sprites
3. Render sprites to PIL Images
4. Scale images using nearest-neighbor interpolation
"""

from PIL import Image
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, Mold, Tile


def decode_snes_4bpp_subtile(subtile_bytes: bytearray) -> list[int]:
    """Decode a single 8x8 SNES 4bpp subtile to palette indices.

    SNES 4bpp format stores 4 bits per pixel in a planar format:
    - 32 bytes total per 8x8 tile
    - Bytes 0-15: bitplane 0 and 1 (interleaved)
    - Bytes 16-31: bitplane 2 and 3 (interleaved)

    Args:
        subtile_bytes: 32-byte bytearray containing SNES 4bpp data

    Returns:
        List of 64 palette indices (0-15), row-major order
    """
    if len(subtile_bytes) != 32:
        raise ValueError(f"Subtile must be exactly 32 bytes, got {len(subtile_bytes)}")

    pixels = []
    for y in range(8):
        # Each row of 8 pixels
        # Bitplanes 0-1 are in bytes 0-15 (interleaved by row)
        # Bitplanes 2-3 are in bytes 16-31 (interleaved by row)
        bp0 = subtile_bytes[y * 2]
        bp1 = subtile_bytes[y * 2 + 1]
        bp2 = subtile_bytes[16 + y * 2]
        bp3 = subtile_bytes[16 + y * 2 + 1]

        # Extract 8 pixels from this row
        for x in range(8):
            # Bit position (MSB first)
            bit = 7 - x

            # Combine bits from all 4 bitplanes
            pixel = (
                ((bp0 >> bit) & 1) |
                (((bp1 >> bit) & 1) << 1) |
                (((bp2 >> bit) & 1) << 2) |
                (((bp3 >> bit) & 1) << 3)
            )
            pixels.append(pixel)

    return pixels


def render_tile_to_pixels(tile: Tile, palette_colors: list[int], gridplane: bool = True) -> list[list[tuple]]:
    """Render a single tile to a 2D array of RGBA colors.

    Args:
        tile: A Tile object containing subtiles
        palette_colors: List of 15 RGB colors as 0xRRGGBB integers
        gridplane: If True, use gridplane format sizes. If False, use metasprite sizes.

    Returns:
        2D list of RGBA tuples: result[y][x] = (R, G, B, A) where A=0 is transparent, A=255 is opaque
    """
    # Gridplane format: 3x3 or 4x4 arrangement of 8x8 subtiles
    # Metasprite format: smaller arrangements, typically 2x2
    if gridplane:
        format_sizes = {
            0: (3, 3),
            1: (3, 4),
            2: (4, 3),
            3: (4, 4),
        }
    else:
        # Metasprite format sizes (2x2 for format 0)
        format_sizes = {
            0: (2, 2),
            1: (2, 2),
            2: (2, 2),
            3: (2, 2),
        }

    cols, rows = format_sizes.get(tile.format, (2, 2) if not gridplane else (4, 4))
    tile_width = cols * 8
    tile_height = rows * 8

    # Initialize output image with transparent pixels
    pixels = [[(0, 0, 0, 0) for _ in range(tile_width)] for _ in range(tile_height)]

    # Process each subtile
    subtile_bytes_list = tile.subtile_bytes
    for i, subtile_bytes in enumerate(subtile_bytes_list):
        if subtile_bytes is None:
            # Empty subtile, skip
            continue

        # Calculate subtile position in gridplane
        subtile_row = i // cols
        subtile_col = i % cols

        # Decode subtile to palette indices
        subtile_pixels = decode_snes_4bpp_subtile(subtile_bytes)

        # Place subtile pixels in output image
        for py in range(8):
            for px in range(8):
                palette_idx = subtile_pixels[py * 8 + px]

                # Calculate output position
                out_y = subtile_row * 8 + py
                out_x = subtile_col * 8 + px

                # Apply mirroring if needed
                if tile.mirror:
                    out_x = tile_width - 1 - out_x
                if tile.invert:
                    out_y = tile_height - 1 - out_y

                # Palette index 0 is transparent, others use palette colors
                if palette_idx == 0:
                    pixels[out_y][out_x] = (0, 0, 0, 0)  # Transparent with alpha=0
                else:
                    # Get RGB from palette (palette_idx 1-15 maps to colors 0-14)
                    color = palette_colors[palette_idx - 1]
                    r = (color >> 16) & 0xFF
                    g = (color >> 8) & 0xFF
                    b = color & 0xFF
                    pixels[out_y][out_x] = (r, g, b, 255)  # Opaque with alpha=255

    return pixels


def render_metasprite_to_image(
    mold: Mold,
    palette_colors: list[int],
    scale: int = 4
) -> Image.Image:
    """Render a metasprite (non-gridplane) with multiple positioned tiles.

    Args:
        mold: A Mold object containing multiple tiles with X/Y positions
        palette_colors: List of 15 RGB colors as 0xRRGGBB integers
        scale: Scale factor for output image (default: 4 for 4x)

    Returns:
        PIL Image with the rendered sprite (RGBA mode)
    """
    if len(mold.tiles) == 0:
        raise ValueError("Mold has no tiles to render")

    # Calculate bounding box from all tiles
    min_x = min(tile.x for tile in mold.tiles)
    min_y = min(tile.y for tile in mold.tiles)

    # Calculate max bounds by adding tile dimensions
    max_x = max(tile.x + 16 for tile in mold.tiles)  # Assuming 2x2 = 16 pixels
    max_y = max(tile.y + 16 for tile in mold.tiles)

    canvas_width = max_x - min_x
    canvas_height = max_y - min_y

    # Create canvas
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))

    # Render each tile and composite onto canvas
    for tile in mold.tiles:
        # Render this tile
        pixels_2d = render_tile_to_pixels(tile, palette_colors, gridplane=False)

        # Get tile dimensions
        tile_height = len(pixels_2d)
        tile_width = len(pixels_2d[0]) if tile_height > 0 else 0

        # Create tile image
        tile_img = Image.new('RGBA', (tile_width, tile_height))
        tile_data = []

        for row in pixels_2d:
            for r, g, b, a in row:
                # Use the alpha channel from render_tile_to_pixels
                tile_data.append((r, g, b, a))

        tile_img.putdata(tile_data)

        # Calculate position on canvas (relative to min_x, min_y)
        pos_x = tile.x - min_x
        pos_y = tile.y - min_y

        # Composite onto canvas
        canvas.paste(tile_img, (pos_x, pos_y), tile_img)

    # Crop to non-transparent bounds
    bbox = canvas.getbbox()
    if bbox:
        canvas = canvas.crop(bbox)

    # Scale using nearest-neighbor (no interpolation)
    if scale > 1:
        new_size = (canvas.width * scale, canvas.height * scale)
        canvas = canvas.resize(new_size, Image.NEAREST)

    return canvas


def render_sprite_to_image(
    sprite: CompleteSprite,
    palette_colors: list[int],
    mold_index: int = 0,
    scale: int = 4
) -> Image.Image:
    """Render a sprite with a custom palette to a PIL Image.

    Supports both gridplane and metasprite formats.

    Args:
        sprite: A CompleteSprite object from patchbuilder
        palette_colors: List of 15 RGB colors as 0xRRGGBB integers
        mold_index: Which mold to render (default: 0 for standing pose)
        scale: Scale factor for output image (default: 4 for 4x)

    Returns:
        PIL Image with the rendered sprite (RGBA mode)
    """
    # Get the animation pack and mold
    animation_pack = sprite.animation
    if mold_index >= len(animation_pack.properties.molds):
        raise ValueError(f"Mold index {mold_index} out of range (max: {len(animation_pack.properties.molds) - 1})")

    mold: Mold = animation_pack.properties.molds[mold_index]

    if len(mold.tiles) == 0:
        raise ValueError("Mold has no tiles to render")

    # Check if this is a gridplane or metasprite
    if mold.gridplane:
        # Gridplane: single tile arranged in a grid
        tile: Tile = mold.tiles[0]
        pixels_2d = render_tile_to_pixels(tile, palette_colors, gridplane=True)

        # Get dimensions
        height = len(pixels_2d)
        width = len(pixels_2d[0]) if height > 0 else 0

        # Create PIL Image (RGBA for transparency)
        img = Image.new('RGBA', (width, height))
        img_data = []

        for row in pixels_2d:
            for r, g, b, a in row:
                # Use the alpha channel from render_tile_to_pixels
                img_data.append((r, g, b, a))

        img.putdata(img_data)

        # Crop to non-transparent bounds
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)

        # Scale using nearest-neighbor (no interpolation)
        if scale > 1:
            new_size = (img.width * scale, img.height * scale)
            img = img.resize(new_size, Image.NEAREST)

        return img
    else:
        # Metasprite: multiple tiles with X/Y positioning
        return render_metasprite_to_image(mold, palette_colors, scale)


def generate_ally_palette_preview(
    sprite_id: int,
    palette_class,
    output_path: str,
    mold_index: int = 0,
    scale: int = 4
) -> None:
    """Generate a preview image for an ally character palette.

    Args:
        sprite_id: Sprite ID (0=mario, 7=toadstool, 13=bowser, 19=mallow, 25=geno)
        palette_class: A palette class with colours/poison_colours/underwater_colours attributes
        output_path: Where to save the PNG file
        mold_index: Which mold to render (default: 0)
        scale: Scale factor (default: 4)
    """
    from randomizer.data.sprites import sprites

    # Get the sprite object
    sprite_module = getattr(sprites, f'sprite_{sprite_id}')
    sprite: CompleteSprite = sprite_module

    # Get palette colors
    if hasattr(palette_class, 'colours'):
        palette_colors = palette_class.colours
    elif hasattr(palette_class, 'colors'):
        palette_colors = palette_class.colors
    else:
        raise ValueError("Palette class must have 'colours' or 'colors' attribute")

    # Render to image
    img = render_sprite_to_image(sprite, palette_colors, mold_index, scale)

    # Save
    img.save(output_path, 'PNG')
