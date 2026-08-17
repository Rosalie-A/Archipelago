from ..SMRPGRegion import SMRPGRegion

class NimbusLandEntrance(SMRPGRegion):
    name = "Nimbus Land Entrance"

class NimbusLand(SMRPGRegion):
    name = "Nimbus Land"

class NimbusCastle(SMRPGRegion):
    name = "Nimbus Castle"

class NimbusCastleInner(SMRPGRegion):
    name = "Nimbus Castle Inner"

class NimbusCastleDeep(SMRPGRegion):
    name = "Nimbus Castle Deep"

class BarrelVolcanoEntrance(SMRPGRegion):
    name = "Barrel Volcano Entrance"

class BarrelVolcano(SMRPGRegion):
    name = "Barrel Volcano"

world6_regions = [
    NimbusLandEntrance, NimbusLand, NimbusCastle, NimbusCastleInner, NimbusCastleDeep,
    BarrelVolcanoEntrance, BarrelVolcano
]