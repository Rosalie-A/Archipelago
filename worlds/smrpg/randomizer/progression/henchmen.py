from ..data.enemies.enemies import *
import random

layouts: dict[int, list[tuple[int, int]]] = {
    1: [(167, 135)],
    2: [(135, 119), (215, 135)],
    3: [(167, 111), (167, 135), (215, 135)],
    4: [(151, 127), (167, 103), (199, 151), (215, 127)],
    5: [(167, 103), (135, 119), (183, 127), (199, 151), (231, 135)],
    6: [(135, 119), (167, 103), (167, 135), (199, 119), (199, 151), (231, 135)]
}

# TORTE PACKS ALWAYS NEED FIRST 4 NONE

def create_henchmen_formation():
    size = round(random.triangular(1, 6, 2.5))
    layout = layouts[size]
