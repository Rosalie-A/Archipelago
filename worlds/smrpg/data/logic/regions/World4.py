from ..SMRPGRegion import SMRPGRegion


class StarHill(SMRPGRegion):
    name = "Star Hill"

class SeasideTown(SMRPGRegion):
    name = "Seaside Town"

class SeasideTownCliff(SMRPGRegion):
    name = "Seaside Town Cliff"

class Sea(SMRPGRegion):
    name = "Sea"

class SunkenShip(SMRPGRegion):
    name = "Sunken Ship"

world4_regions = [
    StarHill, SeasideTown, SeasideTownCliff, Sea, SunkenShip
]