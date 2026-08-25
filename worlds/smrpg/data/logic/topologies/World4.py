from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, StarPieceLocation, UnusedLocation, \
    BossFightLocation, RemakeBossFightLocation, RemakeStarPieceLocation, RemakeLocation, EXPStarLocation, ChestLocation
from ..regions.World5 import LandsEndEntrance
from ..regions.World3 import Marrymore

from ..regions.World4 import *

StarHill.connections = [
    Connection(Marrymore),
    Connection(SeasideTown)
]

StarHill.locations = [
    StarPieceLocation(LocationNames.STAR_HILL_FREESTANDING_STAR_PIECE),
    InvisibleFlagLocation(LocationNames.STAR_HILL_NORTH_STAR_FLAG)
]

SeasideTown.connections = [
    Connection(StarHill),
    Connection(Sea, [CanAccessSea]),
    Connection(SeasideTownCliff, [CanAccessSeasideBoss]),
    Connection(LandsEndEntrance)
]

SeasideTown.locations = [
    InvisibleFlagLocation(LocationNames.SEASIDE_TOWN_ANCHOR_FLAG),
    InvisibleFlagLocation(LocationNames.SEASIDE_TOWN_BUCKET_FLAG),
    InvisibleFlagLocation(LocationNames.SEASIDE_TOWN_FLOWERS_FLAG),
    InvisibleFlagLocation(LocationNames.SEASIDE_TOWN_HYDRANT_FLAG),
    InvisibleFlagLocation(LocationNames.SEASIDE_TOWN_SHED_BOX_FLAG, [HasSeasideTown]),
    SMRPGLocation(LocationNames.SEASIDE_TOWN_SHED_RESCUE, [HasSeasideElder]),
]

SeasideTownCliff.connections = [
    Connection(SeasideTown)
]

SeasideTownCliff.locations = [
    BossFightLocation(LocationNames.SEASIDE_TOWN_BOSS_FIGHT),
    SMRPGLocation(LocationNames.SEASIDE_TOWN_BOSS_PRIZE),
    StarPieceLocation(LocationNames.SEASIDE_TOWN_BOSS_STAR_PIECE),
]

Sea.connections = [
    Connection(SeasideTown),
    Connection(SunkenShip)
]

Sea.locations = [
    InvisibleFlagLocation(LocationNames.SEA_ARROW_FLAG),
    InvisibleFlagLocation(LocationNames.SEA_BOXES_FLAG),
    ChestLocation(LocationNames.SEA_SAVE_ROOM_BACK_CHEST),
    ChestLocation(LocationNames.SEA_SAVE_ROOM_FRONT_CHEST),
    ChestLocation(LocationNames.SEA_SAVE_ROOM_MIDDLE_CHEST),
    EXPStarLocation(LocationNames.SEA_STARSLAP_ROOM_CHEST),
    InvisibleFlagLocation(LocationNames.SEA_STALAGNATE_FLAG),
    InvisibleFlagLocation(LocationNames.SEA_UNDERWATER_SAIL_FLAG),
    ChestLocation(LocationNames.SEA_WHIRLPOOL_ROOM_CHEST),
]

SunkenShip.connections = [
    Connection(Sea)
]

SunkenShip.locations = [
    SMRPGLocation(LocationNames.SUNKEN_SHIP_3D_MAZE_PRIZE),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_BARREL_SWITCH_PRIZE),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_CANNONBALL_PUZZLE_PRIZE),
    ChestLocation(LocationNames.SUNKEN_SHIP_CLONE_ROOM_CHEST),
    UnusedLocation(LocationNames.SUNKEN_SHIP_COIN_SNAKE_PUZZLE_PRIZE),
    BossFightLocation(LocationNames.SUNKEN_SHIP_FINAL_BOSS_FIGHT),
    StarPieceLocation(LocationNames.SUNKEN_SHIP_FINAL_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_FIRST_STAIRWAY_CHEST),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_FIRST_STAIRWAY_FREESTANDING_FLOWER),
    ChestLocation(LocationNames.SUNKEN_SHIP_HIDDEN_BOX_ROOM_CHEST),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_HIDDEN_UNDERWATER_ROOM_CHEST),
    ChestLocation(LocationNames.SUNKEN_SHIP_HIDONS_ROOM_LEFT_CHEST),
    ChestLocation(LocationNames.SUNKEN_SHIP_HIDONS_ROOM_RIGHT_CHEST),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_LARGE_POOL_FREESTANDING_FROG_COIN),
    ChestLocation(LocationNames.SUNKEN_SHIP_NEAR_FINAL_BOSS_CHEST),
    ChestLocation(LocationNames.SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_LEFT_CHEST),
    ChestLocation(LocationNames.SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_RIGHT_CHEST),
    BossFightLocation(LocationNames.SUNKEN_SHIP_PASSWORD_BOSS_FIGHT),
    StarPieceLocation(LocationNames.SUNKEN_SHIP_PASSWORD_BOSS_STAR_PIECE),
    RemakeBossFightLocation(LocationNames.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT, [PostgameSunkenShipAccess]),
    RemakeStarPieceLocation(LocationNames.SUNKEN_SHIP_POSTGAME_BOSS_STAR_PIECE, [PostgameSunkenShipAccess]),
    RemakeLocation(LocationNames.SUNKEN_SHIP_POSTGAME_PRIZE, [PostgameSunkenShipAccess]),
    ChestLocation(LocationNames.SUNKEN_SHIP_SHOP_AREA_CHEST),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_TRAMPOLINE_PUZZLE_PRIZE),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_TROOPA_CANNONBALL_PRIZE),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_1),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_2),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_3),
    SMRPGLocation(LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_4),
]