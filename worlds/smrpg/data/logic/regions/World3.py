from ..SMRPGRegion import SMRPGRegion


class Moleville(SMRPGRegion):
    name = "Moleville"

class MolevilleMines(SMRPGRegion):
    name = "Moleville Mines"

class MolevilleMinesInner(SMRPGRegion):
    name = "Moleville Mines Inner"

class BoosterPass(SMRPGRegion):
    name = "Booster Pass"

class BoosterTowerEntrance(SMRPGRegion):
    name = "Booster Tower Entrance"

class BoosterTower(SMRPGRegion):
    name = "Booster Tower"

class BoosterHillEntrance(SMRPGRegion):
    name = "Booster Hill Entrance"

class BoosterHill(SMRPGRegion):
    name = "Booster Hill"

class Marrymore(SMRPGRegion):
    name = "Marrymore"

class MarrymoreChapel(SMRPGRegion):
    name = "Marrymore Chapel"

world3_regions = [
    Moleville, MolevilleMines, MolevilleMinesInner, BoosterPass, BoosterTowerEntrance,
    BoosterTower, BoosterHillEntrance, BoosterHill, Marrymore, MarrymoreChapel
]