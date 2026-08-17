from ..SMRPGRegion import SMRPGRegion


class LandsEndEntrance(SMRPGRegion):
    name = "Land's End Entrance"

class LandsEnd(SMRPGRegion):
    name = "Land's End"

class BelomeTemple(SMRPGRegion):
    name = "Belome Temple"

class BelomeTempleInner(SMRPGRegion):
    name = "Belome Temple Inner"

class BelomeTempleVault(SMRPGRegion):
    name = "Belome Temple Vault"

class MonstroTown(SMRPGRegion):
    name = "Monstro Town"

class BeanValley(SMRPGRegion):
    name = "Bean Valley"

class CrateGuysCasino(SMRPGRegion):
    name = "Crate Guy's Casino"

world5_regions = [
    LandsEndEntrance, LandsEnd, BelomeTemple, BelomeTempleInner, BelomeTempleVault,
    MonstroTown, BeanValley, CrateGuysCasino
]