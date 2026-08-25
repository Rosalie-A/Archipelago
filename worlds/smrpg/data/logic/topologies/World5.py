from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, UnusedLocation, StarPieceLocation, \
    BossFightLocation, RemakeBossFightLocation, RemakeStarPieceLocation, RemakeLocation, EXPStarLocation, ChestLocation
from ..regions.World4 import SeasideTown

from ..regions.World5 import *
from ..regions.World6 import NimbusLandEntrance

LandsEndEntrance.connections = [
    Connection(SeasideTown),
    Connection(LandsEnd, [CanAccessLandsEnd]),
    Connection(BeanValley),
    Connection(MonstroTown, [CanAccessMonstroTown])
]

LandsEnd.connections = [
    Connection(LandsEndEntrance),
    Connection(BelomeTemple)
]

LandsEnd.locations = [
    EXPStarLocation(LocationNames.LANDS_END_1ST_PURCHASE_CHEST),
    EXPStarLocation(LocationNames.LANDS_END_2ND_PURCHASE_CHEST),
    InvisibleFlagLocation(LocationNames.LANDS_END_ARROW_FLAG),
    ChestLocation(LocationNames.LANDS_END_BEE_ROOM_CHEST),
    BossFightLocation(LocationNames.LANDS_END_BELOME_TEMPLE_CLOUD_BOSS_FIGHT),
    StarPieceLocation(LocationNames.LANDS_END_BELOME_TEMPLE_CLOUD_STAR_PIECE),
    InvisibleFlagLocation(LocationNames.LANDS_END_CANNON_FLAG),
    ChestLocation(LocationNames.LANDS_END_CHOW_PIT_LEFT_CHEST),
    ChestLocation(LocationNames.LANDS_END_CHOW_PIT_RIGHT_CHEST),
    SMRPGLocation(LocationNames.LANDS_END_CLIFF_BUSH_FLAG),
    ChestLocation(LocationNames.LANDS_END_FIRST_CHEST),
    ChestLocation(LocationNames.LANDS_END_GROTTO_CORNER_CHEST),
    ChestLocation(LocationNames.LANDS_END_GROTTO_NEAR_SEWER_CHEST),
    ChestLocation(LocationNames.LANDS_END_GROTTO_FIRST_CHEST),
    InvisibleFlagLocation(LocationNames.LANDS_END_HILL_FLAG),
    InvisibleFlagLocation(LocationNames.LANDS_END_PLATFORM_FLAG),
    InvisibleFlagLocation(LocationNames.LANDS_END_SIGN_FLAG),
    RemakeLocation(LocationNames.LANDS_END_SKY_BRIDGE_FREESTANDING_ITEM),
    InvisibleFlagLocation(LocationNames.LANDS_END_STALAGMITE_FLAG),
    SMRPGLocation(LocationNames.LANDS_END_TROOPA_CLIMB_SUB_12_SECOND_PRIZE),
    InvisibleFlagLocation(LocationNames.LANDS_END_TWO_HILL_FLAG),
    EXPStarLocation(LocationNames.LANDS_END_WHIRLPOOL_1ST_UNDERGROUND_CHEST),
]

BelomeTemple.connections = [
    Connection(LandsEnd),
    Connection(BelomeTempleInner, [CanAccessTempleBoss]),
    Connection(BelomeTempleVault, [HasTempleKey])
]

BelomeTemple.locations = [
    ChestLocation(LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_LOWER_LEFT_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_MIDDLE_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_RIGHT_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_UPPER_LEFT_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_FIRST_FORTUNE_TELLING_ROOM_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_LEFT_MIDDLE_RIGHT_FORTUNE_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_LEFT_RIGHT_MIDDLE_FORTUNE_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_RIGHT_LEFT_MIDDLE_FORTUNE_CHEST),
    ChestLocation(LocationNames.BELOME_TEMPLE_RIGHT_MIDDLE_LEFT_FORTUNE_CHEST),
]

BelomeTempleInner.connections = [
    Connection(BelomeTemple)
]

BelomeTempleInner.locations = [
    BossFightLocation(LocationNames.BELOME_TEMPLE_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BELOME_TEMPLE_BOSS_STAR_PIECE),
    RemakeBossFightLocation(LocationNames.BELOME_TEMPLE_POSTGAME_BOSS_FIGHT, [PostgameTempleBossAccess]),
    RemakeStarPieceLocation(LocationNames.BELOME_TEMPLE_POSTGAME_BOSS_STAR_PIECE, [PostgameTempleBossAccess]),
    RemakeLocation(LocationNames.BELOME_TEMPLE_POSTGAME_PRIZE, [PostgameTempleBossAccess]),
]

BelomeTempleVault.connections = [
    Connection(BelomeTemple)
]

BelomeTempleVault.locations = [
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FLOWER_1),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FLOWER_2),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FLOWER_3),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FLOWER_4),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_1),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_2),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_3),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_4),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_5),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_6),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_7),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_8),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_LEFT_ITEM_BAG),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_MIDDLE_ITEM_BAG),
    SMRPGLocation(LocationNames.BELOME_TEMPLE_VAULT_RIGHT_ITEM_BAG),

]

MonstroTown.connections = [
    Connection(BelomeTempleInner, [CanAccessTempleBoss]),
]

MonstroTown.locations = [
    InvisibleFlagLocation(LocationNames.MONSTRO_BAT_FLAG),
    InvisibleFlagLocation(LocationNames.MONSTRO_ENTRANCE_SIGN_FLAG),
    InvisibleFlagLocation(LocationNames.MONSTRO_FAN_FLAG),
    InvisibleFlagLocation(LocationNames.MONSTRO_SHELL_FLAG),
    BossFightLocation(LocationNames.MONSTRO_TOWN_DOJO_FIRST_FIGHT),
    StarPieceLocation(LocationNames.MONSTRO_TOWN_DOJO_FIRST_FIGHT_STAR_PIECE),
    BossFightLocation(LocationNames.MONSTRO_TOWN_DOJO_SECOND_FIGHT),
    StarPieceLocation(LocationNames.MONSTRO_TOWN_DOJO_SECOND_FIGHT_STAR_PIECE),
    BossFightLocation(LocationNames.MONSTRO_TOWN_DOJO_THIRD_FIGHT),
    StarPieceLocation(LocationNames.MONSTRO_TOWN_DOJO_THIRD_FIGHT_STAR_PIECE),
    BossFightLocation(LocationNames.MONSTRO_TOWN_DOJO_FOURTH_FIGHT),
    StarPieceLocation(LocationNames.MONSTRO_TOWN_DOJO_FOURTH_FIGHT_STAR_PIECE),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_DOJO_PRIZE),
    RemakeBossFightLocation(LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_FIGHT, [PostgameDojoBossAccess]),
    RemakeLocation(LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_PRIZE, [PostgameDojoBossAccess]),
    RemakeStarPieceLocation(LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_STAR_PIECE, [PostgameDojoBossAccess]),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_ENTRANCE_CHEST),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_FLAG_EXCHANGE_PRIZE),
    RemakeBossFightLocation(LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_BOSS_FIGHT, [PostgameSealedDoorBoss]),
    RemakeLocation(LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_PRIZE, [PostgameSealedDoorBoss]),
    RemakeStarPieceLocation(LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_STAR_PIECE, [PostgameSealedDoorBoss]),
    BossFightLocation(LocationNames.MONSTRO_TOWN_SEALED_DOOR_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_SEALED_DOOR_PRIZE),
    StarPieceLocation(LocationNames.MONSTRO_TOWN_SEALED_DOOR_STAR_PIECE),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_SUPER_JUMP_FIRST_PRIZE),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_SUPER_JUMP_SECOND_PRIZE),
    SMRPGLocation(LocationNames.MONSTRO_TOWN_THWOMP_KEY),
]

BeanValley.connections = [
    Connection(LandsEndEntrance),
    Connection(NimbusLandEntrance),
    Connection(CrateGuysCasino, [HasBrightCard])
]

BeanValley.locations = [
    InvisibleFlagLocation(LocationNames.BEAN_VALLEY_BEANSTALK_BLOCK_FLAG),
    BossFightLocation(LocationNames.BEAN_VALLEY_BOSS_FIGHT),
    SMRPGLocation(LocationNames.BEAN_VALLEY_BOSS_REWARD),
    StarPieceLocation(LocationNames.BEAN_VALLEY_BOSS_STAR_PIECE),
    ChestLocation(LocationNames.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_CHEST_ABOVE_BOX_BOYS_ROOM),
    InvisibleFlagLocation(LocationNames.BEAN_VALLEY_CLOUDS_FLAG),
    ChestLocation(LocationNames.BEAN_VALLEY_CLOUDS_LOWER_LEFT_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_CLOUDS_LOWER_RIGHT_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_CLOUDS_SOLO_VINE_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_CLOUDS_UPPER_LEFT_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_CLOUDS_UPPER_RIGHT_CHEST),
    UnusedLocation(LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_HIGHER_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_HIGHEST_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_LOWER_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_LOWEST_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_MIDDLE_FREESTANDING_COIN),
    ChestLocation(LocationNames.BEAN_VALLEY_LEFT_PIRANHA_PIPE_CHEST),
    SMRPGLocation(LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_FREESTANDING_FROG_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_LOWER_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_UPPER_FREESTANDING_COIN),
    SMRPGLocation(LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_FREESTANDING_FROG_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_HIGHEST_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_LOWEST_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_MIDDLE_FREESTANDING_COIN),
    ChestLocation(LocationNames.BEAN_VALLEY_NORTH_UPPER_LEVEL_CHEST),
    InvisibleFlagLocation(LocationNames.BEAN_VALLEY_PIPE_FLAG),
    SMRPGLocation(LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_HIDDEN_STAIRWAY_ITEM),
    ChestLocation(LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_LEFT_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_RIGHT_CHEST),
    ChestLocation(LocationNames.BEAN_VALLEY_SOUTH_UPPER_LEVEL_CHEST),
    SMRPGLocation(LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_FREESTANDING_FROG_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_LOWER_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN),
    UnusedLocation(LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_UPPER_FREESTANDING_COIN),
]

CrateGuysCasino.connections = [
    Connection(BeanValley)
]

CrateGuysCasino.locations = [
    InvisibleFlagLocation(LocationNames.CASINO_BELL_FLAG),
    SMRPGLocation(LocationNames.GRATE_GUYS_CASINO_LOTW_PRIZE)
]