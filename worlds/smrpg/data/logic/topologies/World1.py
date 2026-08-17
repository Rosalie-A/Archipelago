from ..Connection import Connection
from ..Requirements import *
from ..SMRPGLocation import SMRPGLocation, LocationNames, InvisibleFlagLocation, UnusedLocation, StarPieceLocation, \
    BossFightLocation, CharacterRecruitLocation, RemakeLocation, EXPStarLocation

from ..regions.World1 import *
from ..regions.World2 import KeroSewersEntrance
from ..regions.World7 import BowsersKeepEntrance

MariosPad.connections = [
    Connection(BowsersKeepEntrance),
    Connection(MushroomWay),
]

MariosPad.locations = [
    SMRPGLocation(LocationNames.STARTER_ITEM_1),
    SMRPGLocation(LocationNames.STARTER_ITEM_2),
    SMRPGLocation(LocationNames.STARTER_ITEM_3),
    SMRPGLocation(LocationNames.STARTER_ITEM_4),
    CharacterRecruitLocation(LocationNames.STARTER_CHARACTER_1),
    CharacterRecruitLocation(LocationNames.STARTER_CHARACTER_2),
    CharacterRecruitLocation(LocationNames.STARTER_CHARACTER_3),
    CharacterRecruitLocation(LocationNames.STARTER_CHARACTER_4),
    CharacterRecruitLocation(LocationNames.STARTER_CHARACTER_5),
    InvisibleFlagLocation(LocationNames.MARIOS_PAD_BED_FLAG),
    InvisibleFlagLocation(LocationNames.MARIOS_PAD_HAT_FLAG),
    InvisibleFlagLocation(LocationNames.MARIOS_PAD_LANTERN_FLAG),
    InvisibleFlagLocation(LocationNames.MARIOS_PAD_STEAMWHISTLE_FLAG),
    SMRPGLocation(LocationNames.INVISIBLE_FLAG_1),
    SMRPGLocation(LocationNames.INVISIBLE_FLAG_2),
    SMRPGLocation(LocationNames.INVISIBLE_FLAG_3),
    BossFightLocation(LocationNames.MIMIC_CHEST_1_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MIMIC_CHEST_1_FIRST_REWARD),
    SMRPGLocation(LocationNames.MIMIC_CHEST_1_RELOAD_REWARD),
    StarPieceLocation(LocationNames.MIMIC_CHEST_1_STAR_PIECE),
    BossFightLocation(LocationNames.MIMIC_CHEST_2_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MIMIC_CHEST_2_FIRST_REWARD),
    SMRPGLocation(LocationNames.MIMIC_CHEST_2_RELOAD_REWARD),
    StarPieceLocation(LocationNames.MIMIC_CHEST_2_STAR_PIECE),
    BossFightLocation(LocationNames.MIMIC_CHEST_3_BOSS_FIGHT),
    StarPieceLocation(LocationNames.MIMIC_CHEST_3_STAR_PIECE),
]

MushroomWay.connections = [
    Connection(MariosPad),
    Connection(MushroomKingdom)
]

MushroomWay.locations = [
    BossFightLocation(LocationNames.MUSHROOM_WAY_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_BOSS_REWARD),
    StarPieceLocation(LocationNames.MUSHROOM_WAY_BOSS_STAR_PIECE),
    CharacterRecruitLocation(LocationNames.MUSHROOM_WAY_CHARACTER_JOIN),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_FIRST_CHEST),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_FIRST_TOAD_REWARD),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_SECOND_CHEST),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_FLOWER_JUMP_LEFT_CHEST),
    RemakeLocation(LocationNames.MUSHROOM_WAY_LEFT_FREESTANDING_ITEM),
    RemakeLocation(LocationNames.MUSHROOM_WAY_RIGHT_FREESTANDING_ITEM),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_SECOND_ROOM_RIGHT_CHEST),
    SMRPGLocation(LocationNames.MUSHROOM_WAY_SECOND_TOAD_REWARD),
    InvisibleFlagLocation(LocationNames.MUSHROOM_WAY_TREE_FLAG)
]

MushroomKingdom.connections = [
    Connection(MushroomWay),
    Connection(BanditsWayEntrance),
    Connection(KeroSewersEntrance)
]

MushroomKingdom.locations = [
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_CASTLE_MAIN_HALLWAY_CHEST),
    InvisibleFlagLocation(LocationNames.MUSHROOM_KINGDOM_EMPTY_HOUSE_FLAG),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_GAMEBOY_KID, [HasMushroomKingdom]),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_SHOP_BASEMENT_LEFT_CHEST),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_SHOP_BASEMENT_RIGHT_CHEST),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_SHOP_FREE_ITEM),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_SHOP_RARE_FROG_COIN_EXCHANGE, [HasMushroomKingdom]),
    InvisibleFlagLocation(LocationNames.MUSHROOM_KINGDOM_SIGN_FLAG),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_CHAIR_ITEM),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_LIBERATED),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_LIBERATED),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_LIBERATED),
]

BanditsWayEntrance.connections = [
    Connection(BanditsWay, [CanAccessBanditsWay])
]

BanditsWay.connections = [
    Connection(BanditsWayEntrance),
    Connection(MushroomKingdomInvaded)
]

BanditsWay.locations = [
    UnusedLocation(LocationNames.BANDITS_WAY_1ST_COIN),
    UnusedLocation(LocationNames.BANDITS_WAY_2ND_COIN),
    UnusedLocation(LocationNames.BANDITS_WAY_3RD_COIN),
    BossFightLocation(LocationNames.BANDITS_WAY_BOSS_FIGHT),
    SMRPGLocation(LocationNames.BANDITS_WAY_BOSS_REWARD_1),
    SMRPGLocation(LocationNames.BANDITS_WAY_BOSS_REWARD_2),
    StarPieceLocation(LocationNames.BANDITS_WAY_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.BANDITS_WAY_CROCO_CHASE_CHEST),
    SMRPGLocation(LocationNames.BANDITS_WAY_DOG_JUMP_CHEST),
    SMRPGLocation(LocationNames.BANDITS_WAY_FLOWER_CHEST),
    InvisibleFlagLocation(LocationNames.BANDITS_WAY_FLOWER_FLAG),
    SMRPGLocation(LocationNames.BANDITS_WAY_LONG_ROOM_CHEST),
    EXPStarLocation(LocationNames.BANDITS_WAY_STAR_CHEST),
]

MushroomKingdomInvaded.connections = [
    Connection(BanditsWay, [HasBanditsWay])
]

MushroomKingdomInvaded.locations = [
    BossFightLocation(LocationNames.MUSHROOM_KINGDOM_BOSS_FIGHT),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_EASTERN_GUARD_RESCUE),
    StarPieceLocation(LocationNames.MUSHROOM_KINGDOM_INVASION_BOSS_STAR_PIECE),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_INVASION_FAMILY_RESCUE),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_INVASION_GUEST_ROOM),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_TOAD_RESCUE_ITEM),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_OCCUPIED),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_OCCUPIED),
    SMRPGLocation(LocationNames.MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_OCCUPIED)
]
