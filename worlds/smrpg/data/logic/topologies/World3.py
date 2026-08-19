from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, UnusedLocation, StarPieceLocation, \
    BossFightLocation, CharacterRecruitLocation, RemakeBossFightLocation, RemakeStarPieceLocation, RemakeLocation, \
    EXPStarLocation
from ..regions.World2 import PipeVaultEntrance

from ..regions.World3 import *
from ..regions.World4 import StarHill

Moleville.connections = [
    Connection(PipeVaultEntrance),
    Connection(BoosterPass),
    Connection(MolevilleMines, [CanAccessMolevilleMines])
]

Moleville.locations = [
    InvisibleFlagLocation(LocationNames.MOLEVILLE_BED_FLAG),
    InvisibleFlagLocation(LocationNames.MOLEVILLE_HYDRANT_FLAG),
    InvisibleFlagLocation(LocationNames.MOLEVILLE_MOUNTAIN_BUSH_FLAG),
    InvisibleFlagLocation(LocationNames.MOLEVILLE_MOUNTAIN_GO_FLAG),
    SMRPGLocation(LocationNames.MOLEVILLE_BUCKET_GIRL, [HasMolevilleMines]),
    SMRPGLocation(LocationNames.MOLEVILLE_FIREWORKS_SHOP_FIRST_ITEM, [HasMolevilleMines]),
    SMRPGLocation(LocationNames.MOLEVILLE_FIRST_TREASURE_SHOP_ITEM, [CanAccessTreasureSeller1]),
    SMRPGLocation(LocationNames.MOLEVILLE_SECOND_TREASURE_SHOP_ITEM, [CanAccessTreasureSeller2]),
    SMRPGLocation(LocationNames.MOLEVILLE_THIRD_TREASURE_SHOP_ITEM, [CanAccessTreasureSeller3]),
]

MolevilleMines.connections = [
    Connection(Moleville),
    Connection(MolevilleMinesInner, [CanAccessInnerMolevilleMines])
]

MolevilleMines.locations = [
    InvisibleFlagLocation(LocationNames.MOLEVILLE_MINES_ARROWS_FLAG),
    InvisibleFlagLocation(LocationNames.MOLEVILLE_MINES_CEILING_FLAG),
    InvisibleFlagLocation(LocationNames.MOLEVILLE_MINES_ENTRY_FLAG),
    BossFightLocation(LocationNames.MOLEVILLE_MINES_FIRST_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_FIRST_BOSS_ITEM),
    StarPieceLocation(LocationNames.MOLEVILLE_MINES_FIRST_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_LEFT_BANDIT),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_RIGHT_BANDIT),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_TRAMPOLINE_BANDIT),
]

MolevilleMinesInner.connections = [
    Connection(MolevilleMines)
]

MolevilleMinesInner.locations = [
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_BEFORE_BOSS_LEFT_CHEST),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_BEFORE_BOSS_UPPER_CHEST),
    CharacterRecruitLocation(LocationNames.MOLEVILLE_MINES_CHARACTER_RECRUIT),
    BossFightLocation(LocationNames.MOLEVILLE_MINES_SECOND_BOSS_FIGHT),
    StarPieceLocation(LocationNames.MOLEVILLE_MINES_SECOND_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_SHY_GUY_CART),
    EXPStarLocation(LocationNames.MOLEVILLE_MINES_TWO_LEVEL_TRAINTRACK_ROOM_CHEST),
    SMRPGLocation(LocationNames.MOLEVILLE_MINES_NEAR_FINAL_TRAIN_TRACKS_CHEST),
    RemakeBossFightLocation(LocationNames.MOLEVILLE_MINES_POSTGAME_BOSS_FIGHT, [PostgameMolevilleAccess]),
    RemakeLocation(LocationNames.MOLEVILLE_MINES_POSTGAME_PRIZE, [PostgameMolevilleAccess]),
    RemakeStarPieceLocation(LocationNames.MOLEVILLE_MINES_POSTGAME_BOSS_STAR_PIECE, [PostgameMolevilleAccess]),

]

BoosterPass.connections = [
    Connection(Moleville),
    Connection(BoosterTowerEntrance)
]

BoosterPass.locations = [
    InvisibleFlagLocation(LocationNames.BOOSTER_PASS_CORNER_BUSH_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_PASS_FREESTANDING_FLOWER),
    SMRPGLocation(LocationNames.BOOSTER_PASS_MAIN_AREA_BUSH_CHECK),
    SMRPGLocation(LocationNames.BOOSTER_PASS_MAIN_AREA_LEFT_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_PASS_MAIN_AREA_RIGHT_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_PASS_SECRET_LEFT_CHEST, [CanAccessBoosterTower]),
    SMRPGLocation(LocationNames.BOOSTER_PASS_SECRET_MIDDLE_CHEST, [CanAccessBoosterTower]),
    SMRPGLocation(LocationNames.BOOSTER_PASS_SECRET_RIGHT_CHEST, [CanAccessBoosterTower]),
]

BoosterTowerEntrance.connections = [
    Connection(BoosterPass),
    Connection(BoosterHillEntrance),
    Connection(BoosterTower, [CanAccessBoosterTower])
]

BoosterTowerEntrance.locations = [
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_EXTERIOR_SIGN_FLAG),
]

BoosterTower.connections = [
    Connection(BoosterTowerEntrance)
]

BoosterTower.locations = [
    BossFightLocation(LocationNames.BOOSTER_TOWER_BALCONY_BOSS_FIGHT),
    StarPieceLocation(LocationNames.BOOSTER_TOWER_BALCONY_BOSS_STAR_PIECE),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_BEETLE_CAGE_FLAG),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_BROKEN_FRAME_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_ITEM),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_1),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_2),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_3),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_4),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_5),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_6),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_7),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_8),
    UnusedLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_9),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_1),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_2),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_3),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_4),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_CURTAIN_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_CURTAIN_PRIZE, [CanAccessCurtain]),
    BossFightLocation(LocationNames.BOOSTER_TOWER_CURTAIN_ROOM_BOSS_FIGHT, [CanAccessCurtain]),
    StarPieceLocation(LocationNames.BOOSTER_TOWER_CURTAIN_ROOM_BOSS_STAR_PIECE, [CanAccessCurtain]),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_DESK_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_ELDER_KEY_ROOM, [HasElderKey]),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_FIRST_STAIRWAY_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_KNIFE_GUY_REWARD, [HasBoosterTower]),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_KNIFE_GUY_MAXED_OUT_REWARD, [HasBoosterTower]),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_MARIO_DOLL, [CanAccessCurtain]),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_MASHER_CHEST),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_MASHER_ROOM_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_PARACHUTE_ROOM_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_PARACHUTE_ROOM_STAIR_CREVICE),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_PORTRAIT_PRIZE),
    RemakeBossFightLocation(LocationNames.BOOSTER_TOWER_POSTGAME_BOSS_FIGHT, [PostgameCurtainAccess]),
    RemakeStarPieceLocation(LocationNames.BOOSTER_TOWER_POSTGAME_BOSS_STAR_PIECE, [PostgameCurtainAccess]),
    RemakeLocation(LocationNames.BOOSTER_TOWER_POSTGAME_PRIZE, [PostgameCurtainAccess]),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_RAILWAY_ROOM),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_ROOM_KEY_CHEST, [HasRoomKey]),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_THWOMP_INVISIBLE_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_TOP_FLOOR_CORNER_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_TOP_FLOOR_LOWER_CHEST),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_TOP_FLOOR_UPPER_CHEST),
    InvisibleFlagLocation(LocationNames.BOOSTER_TOWER_TOY_BOX_FLAG),
    SMRPGLocation(LocationNames.BOOSTER_TOWER_UPPER_THWOMP_ROOM_CHEST),
]

BoosterHillEntrance.connections = [
    Connection(BoosterTowerEntrance),
    Connection(Marrymore),
    Connection(BoosterHill, [CanAccessBoosterHill])
]

BoosterHill.locations = [
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_1),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_2),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_3),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_4),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_5),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_6),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_7),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_8),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_9),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_10),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_11),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_12),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_13),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_14),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_15),
    SMRPGLocation(LocationNames.BOOSTER_HILL_FLOWER_16),
]

Marrymore.connections = [
    Connection(BoosterHillEntrance),
    Connection(StarHill),
    Connection(MarrymoreChapel, [CanAccessMarrymoreChapel])
]

Marrymore.locations = [
    InvisibleFlagLocation(LocationNames.MARRYMORE_CURTAINS_FLAG),
    InvisibleFlagLocation(LocationNames.MARRYMORE_HALLWAY_FLAG),
    SMRPGLocation(LocationNames.MARRYMORE_INN_ELDERLY_GUESTS_MAJOR_TIP),
    SMRPGLocation(LocationNames.MARRYMORE_INN_REGULAR_ROOM_CHEST),
    InvisibleFlagLocation(LocationNames.MARRYMORE_OUTSIDE_CRATE_FLAG),
    InvisibleFlagLocation(LocationNames.MARRYMORE_WINDOW_FLAG),
    InvisibleFlagLocation(LocationNames.MARRYMORE_SUITE_BED_FLAG),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_1),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_2),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_3),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_4),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_5),
    SMRPGLocation(LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_6),
]

MarrymoreChapel.connections = [
    Connection(Marrymore)
]

MarrymoreChapel.locations = [
    InvisibleFlagLocation(LocationNames.MARRYMORE_FIREPLACE_FLAG),
    InvisibleFlagLocation(LocationNames.MARRYMORE_KITCHEN_FLAG),
    SMRPGLocation(LocationNames.MARRYMORE_SNIFIT_1_CHAPEL_ITEM),
    SMRPGLocation(LocationNames.MARRYMORE_SNIFIT_2_CHAPEL_ITEM),
    SMRPGLocation(LocationNames.MARRYMORE_SNIFIT_3_CHAPEL_ITEM),
    RemakeBossFightLocation(LocationNames.MARRYMORE_POSTGAME_BOSS_FIGHT, [PostgameMarrymoreAccess]),
    RemakeStarPieceLocation(LocationNames.MARRYMORE_POSTGAME_BOSS_STAR_PIECE, [PostgameMarrymoreAccess]),
    RemakeLocation(LocationNames.MARRYMORE_POSTGAME_PRIZE, [PostgameMarrymoreAccess]),
    InvisibleFlagLocation(LocationNames.MARRYMORE_ORGAN_FLAG),
    SMRPGLocation(LocationNames.MARRYMORE_ALTAR_CHAPEL_ITEM),
    InvisibleFlagLocation(LocationNames.MARRYMORE_ALTAR_FLAG),
    BossFightLocation(LocationNames.MARRYMORE_BOSS_FIGHT, [CanAccessMarrymoreBoss]),
    StarPieceLocation(LocationNames.MARRYMORE_BOSS_STAR_PIECE, [CanAccessMarrymoreBoss]),
    CharacterRecruitLocation(LocationNames.MARRYMORE_CHARACTER_RECRUIT),
]