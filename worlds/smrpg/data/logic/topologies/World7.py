from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, UnusedLocation, StarPieceLocation, \
    BossFightLocation, ChestLocation
from ..regions import MariosPad, NimbusLandEntrance

from ..regions.World7 import *

BowsersKeepEntrance.connections = [
    Connection(MariosPad),
    Connection(BowsersKeep),
    Connection(NimbusLandEntrance)
]

BowsersKeep.connections = [
    Connection(BowsersKeepEntrance),
    Connection(BowsersKeepInner, [CanClearBowsersKeep])
]

BowsersKeep.locations = [
    SMRPGLocation(LocationNames.BOWSERS_KEEP_DARK_ROOM_CHEST),
]

BowsersKeepInner.connections = [
    Connection(BowsersKeep),
    Connection(Factory, [CanAccessFactory])
]

BowsersKeepInner.locations = [
    ChestLocation(LocationNames.BOWSERS_KEEP_6_DOOR_ELEVATOR_PLATFORM_ROOM_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_CHEST),
    UnusedLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_LEFT_COIN),
    UnusedLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_RIGHT_COIN),
    ChestLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_LEFT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_RIGHT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_CHEST),
    UnusedLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_LEFT_COIN),
    UnusedLocation(LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_RIGHT_COIN),
    BossFightLocation(LocationNames.BOWSERS_KEEP_BATTLE_DOOR_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BOWSERS_KEEP_BATTLE_DOOR_STAR_PIECE),
    ChestLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_EXIT_CHEST),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_1),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_2),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_3),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_4),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_5),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_6),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_7),
    UnusedLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_8),
    ChestLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_LEFT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_RIGHT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_LEFT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_RIGHT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_1),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_2),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_3),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_4),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_5),
    ChestLocation(LocationNames.BOWSERS_KEEP_DOOR_PRIZE_6),
    BossFightLocation(LocationNames.BOWSERS_KEEP_FIRST_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BOWSERS_KEEP_FIRST_BOSS_STAR_PIECE),
    ChestLocation(LocationNames.BOWSERS_KEEP_MAGIKOOPAS_ROOM_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_NEAR_FIRST_SHOP_LEFT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_NEAR_FIRST_SHOP_RIGHT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_CENTER_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_EXIT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_LOWER_LEFT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_RIGHT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_ROOM_ENTRANCE_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_UPPER_LEFT_CHEST),
    BossFightLocation(LocationNames.BOWSERS_KEEP_SECOND_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BOWSERS_KEEP_SECOND_BOSS_STAR_PIECE),
    BossFightLocation(LocationNames.BOWSERS_KEEP_THIRD_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BOWSERS_KEEP_THIRD_BOSS_STAR_PIECE),
    ChestLocation(LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_ENTRANCE_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_EXIT_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_ENTRANCE_CHEST),
    ChestLocation(LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_EXIT_CHEST),
]

Factory.connections = [
    Connection(BowsersKeepEntrance)
]

Factory.locations = [
    InvisibleFlagLocation(LocationNames.FACTORY_BUTTON_FLAG),
    BossFightLocation(LocationNames.FACTORY_FINAL_BOSS_FIGHT),
    StarPieceLocation(LocationNames.FACTORY_FINAL_BOSS_STAR_PIECE),
    InvisibleFlagLocation(LocationNames.FACTORY_LUGNUT_FLAG),
    InvisibleFlagLocation(LocationNames.FACTORY_TRAMPOLINE_FLAG),
    BossFightLocation(LocationNames.INNER_FACTORY_FIRST_BOSS_FIGHT),
    StarPieceLocation(LocationNames.INNER_FACTORY_FIRST_BOSS_STAR_PIECE),
    BossFightLocation(LocationNames.INNER_FACTORY_SECOND_BOSS_FIGHT),
    StarPieceLocation(LocationNames.INNER_FACTORY_SECOND_BOSS_STAR_PIECE),
    BossFightLocation(LocationNames.INNER_FACTORY_THIRD_BOSS_FIGHT),
    StarPieceLocation(LocationNames.INNER_FACTORY_THIRD_BOSS_STAR_PIECE),
    BossFightLocation(LocationNames.INNER_FACTORY_FOURTH_BOSS_FIGHT),
    StarPieceLocation(LocationNames.INNER_FACTORY_FOURTH_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.INNER_FACTORY_TOAD_GIFT),
    ChestLocation(LocationNames.OUTER_FACTORY_BOLT_PLATFORM_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_CONVEYOR_ROOM_LEFT_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_CONVEYOR_ROOM_RIGHT_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_EARLY_SAVE_ROOM_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_FALLING_AXEM_ROOM_CHEST),
    BossFightLocation(LocationNames.OUTER_FACTORY_FIRST_BOSS_FIGHT),
    StarPieceLocation(LocationNames.OUTER_FACTORY_FIRST_BOSS_STAR_PIECE),
    ChestLocation(LocationNames.OUTER_FACTORY_PIT_BACK_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_PIT_FRONT_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_LEFT_CHEST),
    ChestLocation(LocationNames.OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_RIGHT_CHEST),
    BossFightLocation(LocationNames.OUTER_FACTORY_SECOND_BOSS_FIGHT),
    StarPieceLocation(LocationNames.OUTER_FACTORY_SECOND_BOSS_STAR_PIECE),
]