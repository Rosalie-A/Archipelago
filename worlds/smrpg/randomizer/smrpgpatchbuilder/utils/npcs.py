"""Utils for NPCs"""

from math import ceil

def min_vram(number_of_tiles: int):
    """Get the expected min vram size from the given number of tiles."""
    return ceil(max(0, number_of_tiles - 4) / 4)
