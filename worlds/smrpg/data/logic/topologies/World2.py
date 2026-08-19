from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, UnusedLocation, StarPieceLocation, \
    BossFightLocation, CharacterRecruitLocation, EXPStarLocation
from ..regions import MushroomKingdom

from ..regions.World2 import *
from ..regions.World3 import Moleville

KeroSewersEntrance.connections = [
    Connection(KeroSewers, [CanAccessKeroSewers]),
    Connection(MushroomKingdom),
    Connection(MidasRiver)
]

KeroSewers.connections = [
    Connection(KeroSewersEntrance),
    Connection(MidasRiver)
]

KeroSewers.locations = [
    InvisibleFlagLocation(LocationNames.KERO_GATE_FLAG),
    SMRPGLocation(LocationNames.KERO_SEWERS_BEFORE_BOSS_LOWER_CHEST),
    SMRPGLocation(LocationNames.KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_BEFORE_LANDS_END),
    SMRPGLocation(LocationNames.KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_AFTER_LANDS_END),
    BossFightLocation(LocationNames.KERO_SEWERS_BOSS_FIGHT),
    StarPieceLocation(LocationNames.KERO_SEWERS_BOSS_STAR_PIECE),
    EXPStarLocation(LocationNames.KERO_SEWERS_FOUR_RAT_ROOM_CHEST),
    SMRPGLocation(LocationNames.KERO_SEWERS_STAIRWAY_ROOM_LEFT_CHEST),
    SMRPGLocation(LocationNames.KERO_SEWERS_STAIRWAY_ROOM_RIGHT_CHEST)
]

MidasRiver.connections = [
    Connection(KeroSewersEntrance),
    Connection(TadpolePond)
]

MidasRiver.locations = [
    SMRPGLocation(LocationNames.MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_FREESTANDING_FROG_COIN),
    SMRPGLocation(LocationNames.MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_FREESTANDING_FLOWER),
    SMRPGLocation(LocationNames.MIDAS_RIVER_FIRST_PLAY_REWARD),
    SMRPGLocation(LocationNames.MIDAS_RIVER_UPPER_LEFT_TUNNEL_FREESTANDING_FROG_COIN),
    InvisibleFlagLocation(LocationNames.MIDAS_TREES_FLAG),
]

TadpolePond.connections = [
    Connection(MidasRiver),
    Connection(RoseWay)
]

TadpolePond.locations = [
    SMRPGLocation(LocationNames.TADPOLE_CABINET_FLAG),
    SMRPGLocation(LocationNames.TADPOLE_POND_CRICKET_JAM_EXCHANGE, [HasCricketPieAndJam]),
    SMRPGLocation(LocationNames.TADPOLE_POND_CRICKET_PIE_EXCHANGE, [HasCricketPie]),
    SMRPGLocation(LocationNames.MELODY_BAY_SONG_1_REWARD),
    SMRPGLocation(LocationNames.MELODY_BAY_SONG_2_REWARD, [HasMolevilleMines]),
    SMRPGLocation(LocationNames.MELODY_BAY_SONG_3_REWARD, [HasBelomeTemple]),
]

RoseWay.connections = [
    Connection(TadpolePond),
    Connection(RoseTown)
]

RoseWay.locations = [
    InvisibleFlagLocation(LocationNames.ROSE_WAY_DIRT_PATCH_FLAG),
    SMRPGLocation(LocationNames.ROSE_WAY_FIVE_CHEST_AREA_BOTTOM_LEFT_CHEST),
    SMRPGLocation(LocationNames.ROSE_WAY_FIVE_CHEST_AREA_TOP_MIDDLE_CHEST),
    SMRPGLocation(LocationNames.ROSE_WAY_FIVE_CHEST_BOTTOM_RIGHT_CHEST),
    SMRPGLocation(LocationNames.ROSE_WAY_FIVE_CHEST_TOP_LEFT_CHEST),
    SMRPGLocation(LocationNames.ROSE_WAY_FIVE_CHEST_TOP_RIGHT_CHEST),
    SMRPGLocation(LocationNames.ROSE_WAY_FREESTANDING_FLOWER),
    SMRPGLocation(LocationNames.ROSE_WAY_FREESTANDING_MUSHROOM),
    SMRPGLocation(LocationNames.ROSE_WAY_SWINGING_SHY_GUY_CHEST),
    UnusedLocation(LocationNames.ROSE_WAY_FREESTANDING_COIN_1),
    UnusedLocation(LocationNames.ROSE_WAY_FREESTANDING_COIN_2),
    UnusedLocation(LocationNames.ROSE_WAY_FREESTANDING_COIN_3),
    UnusedLocation(LocationNames.ROSE_WAY_FREESTANDING_COIN_4),
    UnusedLocation(LocationNames.ROSE_WAY_FREESTANDING_COIN_5),
]

RoseTown.connections = [
    Connection(RoseWay),
    Connection(ForestMazeEntrance),
    Connection(PipeVaultEntrance)
]

RoseTown.locations = [
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_BOWSER_FLAG),
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_GARDENER_BUCKET_FLAG, [CanAccessGardener]),
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_GARDENER_HYDRANT_FLAG, [CanAccessGardener]),
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_GARDENER_LEAF_FLAG, [CanAccessGardener]),
    SMRPGLocation(LocationNames.ROSE_TOWN_GARDENER_LEFT_CHEST, [CanAccessGardenerChests]),
    SMRPGLocation(LocationNames.ROSE_TOWN_GARDENER_RIGHT_CHEST, [CanAccessGardenerChests]),
    SMRPGLocation(LocationNames.ROSE_TOWN_INN_TOAD_GIFT),
    SMRPGLocation(LocationNames.ROSE_TOWN_GAZ_GIFT, [HasForestMaze]),
    SMRPGLocation(LocationNames.ROSE_TOWN_SHOP_LEFT_CHEST),
    SMRPGLocation(LocationNames.ROSE_TOWN_SHOP_RIGHT_CHEST),
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_SIGN_FLAG),
    InvisibleFlagLocation(LocationNames.ROSE_TOWN_SINK_FLAG),
    SMRPGLocation(LocationNames.ROSE_TOWN_UPPER_HOUSE_LEFT_CHEST),
    SMRPGLocation(LocationNames.ROSE_TOWN_UPPER_HOUSE_MAZE_SECRET_PRIZE, [CanAccessForestMaze]),
    SMRPGLocation(LocationNames.ROSE_TOWN_UPPER_HOUSE_RIGHT_CHEST),
    SMRPGLocation(LocationNames.ROSE_TOWN_UPPER_HOUSE_TOP_FLOOR_CHEST),
]

ForestMazeEntrance.connections = [
    Connection(RoseTown),
    Connection(ForestMaze, [CanAccessForestMaze])
]

ForestMaze.connections = [
    Connection(ForestMazeEntrance)
]

ForestMaze.locations = [
    SMRPGLocation(LocationNames.FOREST_MAZE_1ST_ROOM_CHEST),
    SMRPGLocation(LocationNames.FOREST_MAZE_BEFORE_MAZE_CHEST),
    BossFightLocation(LocationNames.FOREST_MAZE_BOSS_FIGHT),
    StarPieceLocation(LocationNames.FOREST_MAZE_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.FOREST_MAZE_BOTTOM_RIGHT_STUMP_CHEST),
    CharacterRecruitLocation(LocationNames.FOREST_MAZE_CHARACTER_RECRUIT),
    SMRPGLocation(LocationNames.FOREST_MAZE_FIRST_CHEST_AFTER_UNDERGROUND),
    SMRPGLocation(LocationNames.FOREST_MAZE_MIDDLE_LEFT_STUMP_CHEST),
    SMRPGLocation(LocationNames.FOREST_MAZE_SECRET_BOTTOM_MIDDLE_CHEST),
    SMRPGLocation(LocationNames.FOREST_MAZE_SECRET_BOTTOM_RIGHT_CHEST),
    SMRPGLocation(LocationNames.FOREST_MAZE_SECRET_LEFT_CHEST),
    InvisibleFlagLocation(LocationNames.FOREST_MAZE_SECRET_MUSHROOMS_FLAG),
    InvisibleFlagLocation(LocationNames.FOREST_MAZE_SECRET_STUMP_FLAG),
    SMRPGLocation(LocationNames.FOREST_MAZE_SECRET_TOP_MIDDLE_CHEST),
    SMRPGLocation(LocationNames.FOREST_MAZE_SECRET_TOP_RIGHT_CHEST),
    InvisibleFlagLocation(LocationNames.FOREST_MAZE_SECRET_WIGGLER_FLAG),
    SMRPGLocation(LocationNames.FOREST_MAZE_WIGGLER_CHEST),
]

PipeVaultEntrance.connections = [
    Connection(RoseTown),
    Connection(Moleville),
    Connection(PipeVault, [CanAccessPipeVault])
]

PipeVault.connections = [
    Connection(PipeVaultEntrance),
    Connection(YosterIsle)
]

PipeVault.locations = [
    InvisibleFlagLocation(LocationNames.PIPE_VAULT_EXTERIOR_FLAG),
    SMRPGLocation(LocationNames.PIPE_VAULT_GOOMBA_THUMPIN_FIRST_PRIZE),
    SMRPGLocation(LocationNames.PIPE_VAULT_GOOMBA_THUMPIN_SECOND_PRIZE),
    SMRPGLocation(LocationNames.PIPE_VAULT_NIPPER_ROOM_FIRST_CHEST),
    SMRPGLocation(LocationNames.PIPE_VAULT_NIPPER_ROOM_SECOND_CHEST),
    InvisibleFlagLocation(LocationNames.PIPE_VAULT_RED_PIPE_FLAG),
    SMRPGLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_BACK_CHEST),
    SMRPGLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FRONT_CHEST),
    SMRPGLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_MIDDLE_CHEST),
    UnusedLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_1),
    UnusedLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_2),
    UnusedLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_3),
    UnusedLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_4),
    UnusedLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_5),
    SMRPGLocation(LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_FROG_COIN),
]

YosterIsle.connections = [
    Connection(PipeVault)
]

YosterIsle.locations = [
    SMRPGLocation(LocationNames.YOSTER_ISLE_ENTRANCE_CHEST),
    SMRPGLocation(LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_1, [HasRaceCookies]),
    SMRPGLocation(LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_2, [HasRaceCookies]),
    SMRPGLocation(LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_3, [HasRaceCookies]),
    InvisibleFlagLocation(LocationNames.YOSTER_ISLE_GOAL_FLAG),
    InvisibleFlagLocation(LocationNames.YOSTER_ISLE_HUT_FLAG),
    SMRPGLocation(LocationNames.YOSTER_ISLE_RACE_STARTING_COOKIES),
]