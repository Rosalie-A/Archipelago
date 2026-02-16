from enum import Enum, IntEnum
from .types.classes import Music
from .music import NormalBattleMusic, MidbossMusic, BossMusic, Smithy1Music, CulexMusic, CorndillyMusic

class Battlefields(IntEnum):
    """Enumeration for ID values for battlefields."""

    FOREST = 0x00
    BOWYER = 0x01
    BEANSTALKS = 0x02
    KING_CALAMARI = 0x03
    SUNKEN_SHIP = 0x04
    MOLEVILLE_MINES = 0x05
    BOWSERS_KEEP = 0x07
    CZAR_DRAGON = 0x08
    MUSHROOM_WAY = 0x09
    MOUNTAINS = 0x0A
    HOUSE = 0x0B
    BOOSTER_TOWER = 0x0C
    MUSHROOM_KINGDOM = 0x0D
    UNDERWATER = 0x0E
    MUSHROOM_KINGDOM_THRONE_ROOM = 0x0F
    EXOR = 0x10
    CLOWN_BROS = 0x11
    COUNTDOWN = 0x12
    GATE = 0x13
    VOLCANO = 0x14
    KERO_SEWERS = 0x15
    NIMBUS_CASTLE = 0x16
    BIRDETTA = 0x17
    VALENTINA = 0x18
    UNDERGROUND = 0x19
    MUSHROOM_KINGDOM_OUTSIDE = 0x1C
    BOOMER = 0x1D
    PLATEAU = 0x21
    SEA_ENCLAVE = 0x22
    BUNDT = 0x23
    STAR_HILL = 0x24
    YARIDOVICH = 0x25
    SEA = 0x26
    AXEM_RANGERS = 0x27
    CLOAKER_DOMINO = 0x28
    BEAN_VALLEY = 0x29
    BELOME_TEMPLE = 0x2A
    DESERT = 0x2B
    SMITHY = 0x2C
    SMITHY_FINAL = 0x2D
    JINX_DOJO = 0x2E
    CULEX = 0x2F
    FACTORY = 0x30
    BEAN_VALLEY_UNDERGROUND = 0x31

class BattleMusic(Music, Enum):
    """Enumeration for ID values for battle music."""

    NORMAL_MUSIC = NormalBattleMusic
    BOSS_1 = MidbossMusic
    BOSS_2 = BossMusic
    SMITHY = Smithy1Music
    CULEX = CulexMusic
    CORN = CorndillyMusic
