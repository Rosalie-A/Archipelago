from ...types.physical_objects import ItemNPC
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Packet
from ...data.variables.packet_names import *
from ...data.variables.event_script_names import *
from ...data.variables.sprite_names import *
from ...data.rooms.npcs import *


class DefaultItem(ItemNPC):
    _base = ITEM_BAG_NPC


class HammerObject(ItemNPC):
    _base = HAMMER_BASE


class StickObject(ItemNPC):
    _base = FROGGIE_STICK_BASE


class GreenShellObject(ItemNPC):
    _base = GREEN_SHELL_BASE


class MusicObject(ItemNPC):
    _base = MUSIC_BASE
    _chest_event_id: int = E0882_CHEST_FLOWER_ITEM_COLLECTION


class ChompObject(ItemNPC):
    _base = CHOMP_BASE


class RedShellObject(ItemNPC):
    _base = RED_SHELL_BASE


class ParasolObject(ItemNPC):
    _base = PARASOL_BASE


class FanObject(ItemNPC):
    _base = FAN_BASE


class TinyStarObject(ItemNPC):
    _base = TINY_STAR_BASE
    _chest_event_id: int = E0885_CHEST_STAR_PIECE_PACKET


class FryingPanObject(ItemNPC):
    _base = PAN_BASE


class CrownObject(ItemNPC):
    _base = CROWN_BASE
    _chest_event_id: int = E0890_CHEST_CROWN_PACKET


class ShoesObject(ItemNPC):
    _base = SHOES_BASE
    _chest_event_id: int = E0888_CHEST_SHOES_PACKET


class BroochObject(ItemNPC):
    _base = BROOCH_BASE
    _chest_event_id: int = E0887_CHEST_BROOCH_PACKET


class RingObject(ItemNPC):
    _base = RING_BASE
    _chest_event_id: int = E0886_CHEST_RING_PACKET


class FeatherObject(ItemNPC):
    _base = FEATHER_BASE
    _chest_event_id: int = E0884_CHEST_FEATHER_PACKET


class RedMushroomObject(ItemNPC):
    _base = RED_MUSHROOM_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class GreenMushroomObject(ItemNPC):
    _base = GREEN_MUSHROOM_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class YellowMushroomObject(ItemNPC):
    _base = YELLOW_MUSHROOM_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class RedSyrupObject(ItemNPC):
    _base = RED_SYRUP_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class GreenSyrupObject(ItemNPC):
    _base = GREEN_SYRUP_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class YellowSyrupObject(ItemNPC):
    _base = YELLOW_SYRUP_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class BlueSyrupObject(ItemNPC):
    _base = BLUE_SYRUP_BASE
    _chest_event_id: int = E0898_CHEST_BLUE_ITEM_COLLECTION


class StarDrinkObject(ItemNPC):
    _base = STAR_DRINK_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class RDrinkObject(ItemNPC):
    _base = R_DRINK_BASE
    _chest_event_id: int = E0898_CHEST_BLUE_ITEM_COLLECTION


class DDrinkObject(ItemNPC):
    _base = D_DRINK_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class PDrinkObject(ItemNPC):
    _base = P_DRINK_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class GreenJuiceObject(ItemNPC):
    _base = GREEN_JUICE_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class YellowJuiceObject(ItemNPC):
    _base = YELLOW_JUICE_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class RedJuiceObject(ItemNPC):
    _base = RED_JUICE_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class FrogDrinkObject(ItemNPC):
    _base = FROG_DRINK_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class CookieObject(ItemNPC):
    _base = COOKIE_BASE
    _chest_event_id: int = E0893_CHEST_COOKIE_PACKET


class YellowBombObject(ItemNPC):
    _base = YELLOW_BOMB_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class RedBombObject(ItemNPC):
    _base = RED_BOMB_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class BlueBombObject(ItemNPC):
    _base = BLUE_BOMB_BASE
    _chest_event_id: int = E0898_CHEST_BLUE_ITEM_COLLECTION


class GreenCandyObject(ItemNPC):
    _base = GREEN_CANDY_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class YellowMusicDrinkObject(ItemNPC):
    _base = YELLOW_MUSIC_DRINK_BASE
    _chest_event_id: int = E0899_CHEST_YELLOW_ITEM_COLLECTION


class BlueMusicDrinkObject(ItemNPC):
    _base = BLUE_MUSIC_DRINK_BASE
    _chest_event_id: int = E0898_CHEST_BLUE_ITEM_COLLECTION


class RedMusicDrinkObject(ItemNPC):
    _base = RED_MUSIC_DRINK_BASE
    _chest_event_id: int = E0897_CHEST_RED_ITEM_COLLECTION


class KeyObject(ItemNPC):
    _base = KEY_BASE
    _chest_event_id: int = E0882_CHEST_FLOWER_ITEM_COLLECTION


class SmallCoinObject(ItemNPC):
    _base = SMALL_COIN_BASE
    _chest_event_id: int = E3080_COIN_CHEST_QUICK_HIT


class SmallFrogCoinObject(ItemNPC):
    _base = SMALL_FROG_COIN_BASE
    _chest_event_id: int = E3084_FROG_COIN_CHEST_QUICK_HIT


class BlueCandyObject(ItemNPC):
    _base = BLUE_CANDY_BASE
    _chest_event_id: int = E0898_CHEST_BLUE_ITEM_COLLECTION


class MicrobombObject(ItemNPC):
    _base = MICROBOMB_BASE
    _chest_event_id: int = E0891_CHEST_BOMB_PACKET


class EggObject(ItemNPC):
    _base = EGG_BASE
    _chest_event_id: int = E0892_CHEST_EGG_PACKET


class GreenBombObject(ItemNPC):
    _base = GREEN_BOMB_BASE
    _chest_event_id: int = E0896_CHEST_GREEN_ITEM_COLLECTION


class CardObject(ItemNPC):
    _base = CARD_BASE
    _chest_event_id: int = E0895_CHEST_CARD_PACKET


class BananaObject(ItemNPC):
    _base = BANANA_BASE
    _chest_event_id: int = E0889_CHEST_BANANA_PEEL_PACKET


class BerryObject(ItemNPC):
    _base = BERRY_BASE
    _chest_event_id: int = E0894_CHEST_BERRY_PACKET


class BigCoinObject(ItemNPC):
    _base = BIG_COIN_BASE
    _chest_event_id: int = E3080_COIN_CHEST_QUICK_HIT


class BeetleObject(ItemNPC):
    _base = BEETLE_BASE
    _chest_event_id: int = E0917_CHEST_BEETLE_PACKET


class FlowerObject(ItemNPC):
    _base = FLOWER_BASE
    _chest_70a7_upper = 2
    _chest_event_id: int = E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST


class RecoveryMushroomObject(ItemNPC):
    _base = RECOVERY_MUSHROOM_BASE
    _chest_event_id: int = E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST


class FrogCoinObject(ItemNPC):
    _base = FROG_COIN_BASE
    _chest_event_id: int = E3084_FROG_COIN_CHEST_QUICK_HIT


class GloveObject(ItemNPC):
    _base = GLOVE_BASE
    _chest_event_id: int = E0950_CHEST_GLOVE_PACKET

class ProgressiveFireworksObject(ItemNPC):
    _base = ITEM_BAG_NPC
    _chest_event_id: int = E0934_PROGRESSIVE_FIREWORK_CHEST_PACKET

class CrystalObject(ItemNPC):
    _base = CRYSTAL_BASE
    _chest_event_id: int = E0951_CRYSTAL_CHEST_PACKET

class FireSpellObject(ItemNPC):
    _base = RED_ORB_BASE
    _chest_event_id: int = 0
class BlueSpellObject(ItemNPC):
    _base = BLUE_ORB_BASE
    _chest_event_id: int = 0
class GreenSpellObject(ItemNPC):
    _base = GREEN_ORB_BASE
    _chest_event_id: int = 0
class YellowSpellObject(ItemNPC):
    _base = YELLOW_ORB_BASE
    _chest_event_id: int = 0
class GraySpellObject(ItemNPC):
    _base = GRAY_ORB_BASE
    _chest_event_id: int = 0

# possibilities for more models
# urchin
# heart
# tiny bloober
# tiny toad
# character dolls (maybe in the future when they can be recruited in chests)
# cannonball
# tiny clouds
# amanita mushroom
# goombette
# tiny magmite
# shaman's wand?
# knife guy's knife
# bowyer arrow
# helio
# remo con x
# tiny gorgon
# lamb's lure sheep