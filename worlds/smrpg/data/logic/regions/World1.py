from ..SMRPGRegion import SMRPGRegion


class MariosPad(SMRPGRegion):
    name = "Mario's Pad"

class MushroomWay(SMRPGRegion):
    name = "Mushroom Way"

class MushroomKingdom(SMRPGRegion):
    name = "Mushroom Kingdom"

class MushroomKingdomInvaded(SMRPGRegion):
    name = "Mushroom Kingdom Invaded"

class BanditsWayEntrance(SMRPGRegion):
    name = "Bandit's Way Entrance"

class BanditsWay(SMRPGRegion):
    name = "Bandit's Way"

world1_regions = [
    MariosPad, MushroomWay, MushroomKingdom, MushroomKingdomInvaded,
    BanditsWayEntrance, BanditsWay
]