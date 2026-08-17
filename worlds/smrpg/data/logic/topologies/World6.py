from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, StarPieceLocation, BossFightLocation, \
    EXPStarLocation
from ..regions.World4 import SeasideTown
from ..regions.World5 import BeanValley

from ..regions.World6 import *
from ..regions.World7 import BowsersKeepEntrance

NimbusLandEntrance.connections = [
    Connection(BeanValley),
    Connection(BarrelVolcanoEntrance),
    Connection(BowsersKeepEntrance),
    Connection(NimbusLand, [CanAccessNimbusLand])
]

NimbusLand.connections = [
    Connection(NimbusLandEntrance),
    Connection(NimbusCastle, [CanAccessNimbusCastle])
]

NimbusLand.locations = [
    InvisibleFlagLocation(LocationNames.NIMBUS_GOLD_GOOMBA_FLAG),
    SMRPGLocation(LocationNames.NIMBUS_INN_LOBBY_FLAG),
    SMRPGLocation(LocationNames.NIMBUS_LAND_DREAM_CUSHION_1ST_ITEM),
    SMRPGLocation(LocationNames.NIMBUS_LAND_DREAM_CUSHION_2ND_ITEM),
    SMRPGLocation(LocationNames.NIMBUS_LAND_GARRO_CHECK),
    SMRPGLocation(LocationNames.NIMBUS_LAND_SHOP_CHEST),
    InvisibleFlagLocation(LocationNames.NIMBUS_OUTDOOR_FLAG),
]

NimbusCastle.connections = [
    Connection(NimbusLand),
    Connection(NimbusCastleInner, [CanAccessInnerNimbus])
]

NimbusCastle.locations = [
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_5_DOOR_ROOM_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_BUSINESS_CENTRE_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_LOWER_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_UPPER_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_GIANT_EGG_PRIZE),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_SINGLE_GOLD_BIRD_ROOM_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_WEST_CELLAR_CIVILIAN),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_WEST_CELLAR_GUARD),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_LEFT_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_RIGHT_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_WEST_TWO_LEVEL_ROOM_CHEST),
    SMRPGLocation(LocationNames.NIMBUS_LAND_DODOS_STATUE_GAME_PRIZE),
    InvisibleFlagLocation(LocationNames.NIMBUS_PLANT_FLAG),

]

NimbusCastleInner.connections = [
    Connection(NimbusCastle),
    Connection(NimbusCastleDeep, [CanAccessLateNimbus])
]

NimbusCastleInner.locations = [
    SMRPGLocation(LocationNames.NIMBUS_LAND_GIANT_EGG_BOSS_FIGHT),
    SMRPGLocation(LocationNames.NIMBUS_LAND_GIANT_EGG_BOSS_STAR_PIECE),

]

NimbusCastleDeep.connections = [
    Connection(NimbusCastleInner)
]

NimbusCastleDeep.locations = [
    InvisibleFlagLocation(LocationNames.NIMBUS_BIRD_FLAG),
    InvisibleFlagLocation(LocationNames.NIMBUS_HOT_SPRINGS_FLAG),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_POST_INVASION_NORTH_CELLAR),
    SMRPGLocation(LocationNames.NIMBUS_LAND_FINAL_BOSS_FIGHT),
    SMRPGLocation(LocationNames.NIMBUS_LAND_FINAL_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.NIMBUS_LAND_POST_INVASION_OFF_CLOUD_ITEM),
    SMRPGLocation(LocationNames.NIMBUS_LAND_POST_INVASION_UPPER_RIGHT_HOUSE),
    SMRPGLocation(LocationNames.NIMBUS_LAND_STATUE_KEEPER_BOSS_FIGHT),
    SMRPGLocation(LocationNames.NIMBUS_LAND_STATUE_KEEPER_BOSS_STAR_PIECE),
    EXPStarLocation(LocationNames.NIMBUS_CASTLE_POST_THRONE_CHEST_OCCUPIED),
    SMRPGLocation(LocationNames.NIMBUS_CASTLE_POST_THRONE_CHEST_UNOCCUPIED),

]

BarrelVolcanoEntrance.connections = [
    Connection(NimbusLandEntrance),
    Connection(BarrelVolcano, [CanAccessBarrelVolcano])
]

BarrelVolcano.connections = [
    Connection(BarrelVolcanoEntrance)
]

BarrelVolcano.locations = [
    BossFightLocation(LocationNames.BARREL_VOLCANO_FIRST_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BARREL_VOLCANO_FIRST_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_FIRST_DONUT_LIFT_ROOM_LEFT_FREESTANDING_FROG_COIN),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_HINOPIO_SHOP_CHEST),
    InvisibleFlagLocation(LocationNames.BARREL_VOLCANO_INN_SIGN_FLAG),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_LAVA_POOL_FREESTANDING_FROG_COIN),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_REVERSE_LAVA_RECOIL_FROG_COIN),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_SAVE_ROOM_LOWER_CHEST),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_SAVE_ROOM_UPPER_CHEST),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_SECOND_ARROW_SIGN_ROOM_LEFT_CHEST),
    BossFightLocation(LocationNames.BARREL_VOLCANO_SECOND_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BARREL_VOLCANO_SECOND_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_SECRET_ROOM_LEFT_CHEST),
    SMRPGLocation(LocationNames.BARREL_VOLCANO_SECRET_ROOM_RIGHT_CHEST),
    EXPStarLocation(LocationNames.BARREL_VOLCANO_STAR_CHEST),
    InvisibleFlagLocation(LocationNames.BARREL_VOLCANO_STUMPET_FLAG),
]