from ..SMRPGRegion import SMRPGRegion


class BowsersKeepEntrance(SMRPGRegion):
    name = "Bowser's Keep Entrance"

class BowsersKeep(SMRPGRegion):
    name = "Bowser's Keep"

class BowsersKeepInner(SMRPGRegion):
    name = "Bowser's Keep Inner"

class Factory(SMRPGRegion):
    name = "Factory"

world7_regions = [
    BowsersKeepEntrance, BowsersKeep, BowsersKeepInner, Factory
]