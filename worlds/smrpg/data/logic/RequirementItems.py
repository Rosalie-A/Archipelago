from .Requirement import StarPieceRequirement
from .RequirementItem import RequirementItem, RequirementItemGroup, RequirementItemMetaclass
from ..ItemNames import ItemNames


class Mario(RequirementItem):
    name = ItemNames.MARIO

class Mallow(RequirementItem):
    name = ItemNames.MALLOW

class Geno(RequirementItem):
    name = ItemNames.GENO

class Bowser(RequirementItem):
    name = ItemNames.BOWSER

class Toadstool(RequirementItem):
    name = ItemNames.TOADSTOOL

class Characters(RequirementItemGroup):
    name = "Characters"
    members = [Mario, Mallow, Geno, Bowser, Toadstool]

class Jump(RequirementItem):
    name = ItemNames.JUMP

class FireOrb(RequirementItem):
    name = ItemNames.FIRE_ORB

class SuperJump(RequirementItem):
    name = ItemNames.SUPER_JUMP

class SuperFlame(RequirementItem):
    name = ItemNames.SUPER_FLAME

class UltraJump(RequirementItem):
    name = ItemNames.ULTRA_JUMP

class UltraFlame(RequirementItem):
    name = ItemNames.ULTRA_FLAME

class Thunderbolt(RequirementItem):
    name = ItemNames.THUNDERBOLT

class Shocker(RequirementItem):
    name = ItemNames.SHOCKER

class Snowy(RequirementItem):
    name = ItemNames.SNOWY

class StarRain(RequirementItem):
    name = ItemNames.STAR_RAIN

class GenoBeam(RequirementItem):
    name = ItemNames.GENO_BEAM

class GenoWhirl(RequirementItem):
    name = ItemNames.GENO_WHIRL

class GenoBlast(RequirementItem):
    name = ItemNames.GENO_BLAST

class GenoFlash(RequirementItem):
    name = ItemNames.GENO_FLASH

class Terrorize(RequirementItem):
    name = ItemNames.TERRORIZE

class PoisonGas(RequirementItem):
    name = ItemNames.POISON_GAS

class Crusher(RequirementItem):
    name = ItemNames.CRUSHER

class BowserCrush(RequirementItem):
    name = ItemNames.BOWSER_CRUSH

class PsychBomb(RequirementItem):
    name = ItemNames.PSYCH_BOMB

class DamagingSpells(RequirementItemGroup):
    name = "Damaging Spells"
    members: list[RequirementItemMetaclass] = [
        Jump, FireOrb, SuperJump, SuperFlame, UltraJump, UltraFlame,
        Thunderbolt, Shocker, Snowy, StarRain,
        GenoBeam, GenoWhirl, GenoBlast, GenoFlash,
        Terrorize, PoisonGas, Crusher, BowserCrush,
        PsychBomb
    ]

class AxemRangers(RequirementItem):
    name = ItemNames.AXEM_RANGERS

class Belome1(RequirementItem):
    name = ItemNames.BELOME_1

class Belome2(RequirementItem):
    name = ItemNames.BELOME_2

class Belome3(RequirementItem):
    name = ItemNames.BELOME_3

class Birdetta(RequirementItem):
    name = ItemNames.BIRDETTA

class Boomer(RequirementItem):
    name = ItemNames.BOOMER

class Booster1(RequirementItem):
    name = ItemNames.BOOSTER_1

class Booster2(RequirementItem):
    name = ItemNames.BOOSTER_2

class Bowyer(RequirementItem):
    name = ItemNames.BOWYER

class BoxBoy(RequirementItem):
    name = ItemNames.BOX_BOY

class Bundt1(RequirementItem):
    name = ItemNames.BUNDT_1

class Bundt2(RequirementItem):
    name = ItemNames.BUNDT_2

class Chester(RequirementItem):
    name = ItemNames.CHESTER

class Clerk(RequirementItem):
    name = ItemNames.CLERK

class CloakerDomino(RequirementItem):
    name = ItemNames.CLOAKER_DOMINO

class Countdown(RequirementItem):
    name = ItemNames.COUNTDOWN

class Croco1(RequirementItem):
    name = ItemNames.CROCO_1

class Croco2(RequirementItem):
    name = ItemNames.CROCO_2

class Culex1(RequirementItem):
    name = ItemNames.CULEX_1

class Culex2(RequirementItem):
    name = ItemNames.CULEX_2

class CzarDragon(RequirementItem):
    name = ItemNames.CZAR_DRAGON

class Director(RequirementItem):
    name = ItemNames.DIRECTOR

class Dodo(RequirementItem):
    name = ItemNames.DODO

class Exor(RequirementItem):
    name = ItemNames.EXOR

class Gunyolk(RequirementItem):
    name = ItemNames.GUNYOLK

class HammerBros(RequirementItem):
    name = ItemNames.HAMMER_BROS

class Hidon(RequirementItem):
    name = ItemNames.HIDON

class Jagger(RequirementItem):
    name = ItemNames.JAGGER

class Jinx1(RequirementItem):
    name = ItemNames.JINX_1

class Jinx2(RequirementItem):
    name = ItemNames.JINX_2

class Jinx3(RequirementItem):
    name = ItemNames.JINX_3

class Jinx4(RequirementItem):
    name = ItemNames.JINX_4

class Johnny1(RequirementItem):
    name = ItemNames.JOHNNY_1

class Johnny2(RequirementItem):
    name = ItemNames.JOHNNY_2

class Kamek(RequirementItem):
    name = ItemNames.KAMEK

class KingCalamari(RequirementItem):
    name = ItemNames.KING_CALAMARI

class KnifeGuyCrateGuy(RequirementItem):
    name = ItemNames.KNIFE_GUY_CRATE_GUY

class Mack(RequirementItem):
    name = ItemNames.MACK

class Manager(RequirementItem):
    name = ItemNames.MANAGER

class Megasmilax(RequirementItem):
    name = ItemNames.MEGASMILAX

class Mokura(RequirementItem):
    name = ItemNames.MOKURA

class Pandorite(RequirementItem):
    name = ItemNames.PANDORITE

class Punchinello1(RequirementItem):
    name = ItemNames.PUNCHINELLO_1

class Punchinello2(RequirementItem):
    name = ItemNames.PUNCHINELLO_2

class Smithy(RequirementItem):
    name = ItemNames.SMITHY

class Valentina(RequirementItem):
    name = ItemNames.VALENTINA

class Yaridovich(RequirementItem):
    name = ItemNames.YARIDOVICH

class BossFights(RequirementItemGroup):
    name = "Boss Fights"
    members = [
        AxemRangers, Belome1, Belome2, Belome3, Birdetta, Boomer, Booster1, Booster2,
        Bowyer, BoxBoy, Bundt1, Bundt2, Chester, Clerk, CloakerDomino, Countdown,
        Croco1, Croco2, Culex1, Culex2, CzarDragon, Director, Dodo, Exor, Gunyolk,
        HammerBros, Hidon, Jagger, Jinx1, Jinx2, Jinx3, Jinx4, Johnny1, Johnny2, Kamek,
        KingCalamari, KnifeGuyCrateGuy, Mack, Manager, Megasmilax, Mokura, Pandorite,
        Punchinello1, Punchinello2, Smithy, Valentina, Yaridovich
    ]

boss_fight_names = [boss.name.value for boss in BossFights.members]

class MushroomWay(RequirementItem):
    name = ItemNames.MUSHROOM_WAY

class RareFrogCoin(RequirementItem):
    name = ItemNames.RARE_FROG_COIN

class BanditsWay(RequirementItem):
    name = ItemNames.BANDITS_WAY

class MushroomKingdom(RequirementItem):
    name = ItemNames.MUSHROOM_KINGDOM

class CricketPie(RequirementItem):
    name = ItemNames.CRICKET_PIE

class CricketJam(RequirementItem):
    name = ItemNames.CRICKET_JAM

class ForestMaze(RequirementItem):
    name = ItemNames.FOREST_MAZE

class Seed(RequirementItem):
    name = ItemNames.SEED

class Fertilizer(RequirementItem):
    name = ItemNames.FERTILIZER

class RaceCookies(RequirementItem):
    name = ItemNames.RACE_COOKIES

class Boshi(RequirementItem):
    name = ItemNames.BOSHI

class BambinoBomb(RequirementItem):
    name = ItemNames.BAMBINO_BOMB

class StayVoucher(RequirementItem):
    name = ItemNames.STAY_VOUCHER

class MolevilleMines(RequirementItem):
    name = ItemNames.MOLEVILLE_MINES

class ElderKey(RequirementItem):
    name = ItemNames.ELDER_KEY

class RoomKey(RequirementItem):
    name = ItemNames.ROOM_KEY

class MarioDoll(RequirementItem):
    name = ItemNames.MARIO_DOLL

class BoosterTower(RequirementItem):
    name = ItemNames.BOOSTER_TOWER

class BoosterHill(RequirementItem):
    name = ItemNames.BOOSTER_HILL

class Shoes(RequirementItem):
    name = ItemNames.SHOES

class Ring(RequirementItem):
    name = ItemNames.RING

class Brooch(RequirementItem):
    name = ItemNames.BROOCH

class Crown(RequirementItem):
    name = ItemNames.CROWN

class WeddingGear(RequirementItemGroup):
    name = "Wedding Gear"
    members: list[RequirementItemMetaclass] = [Shoes, Ring, Brooch, Crown]

class StarPiece(RequirementItem):
    name = ItemNames.STAR_PIECE

class Marrymore(RequirementItem):
    name = ItemNames.MARRYMORE

class SunkenShip(RequirementItem):
    name = ItemNames.SUNKEN_SHIP

class ShedKey(RequirementItem):
    name = ItemNames.SHED_KEY

class SeasideTown(RequirementItem):
    name = ItemNames.SEASIDE_TOWN

class TempleKey(RequirementItem):
    name = ItemNames.TEMPLE_KEY

class BelomeTemple(RequirementItem):
    name = ItemNames.BELOME_TEMPLE

class Dojo(RequirementItem):
    name = ItemNames.DOJO

class SealedDoor(RequirementItem):
    name = ItemNames.SEALED_DOOR

class BeanValley(RequirementItem):
    name = ItemNames.BEAN_VALLEY

class GoldPaint(RequirementItem):
    name = ItemNames.GOLD_PAINT

class CastleKey1(RequirementItem):
    name = ItemNames.CASTLE_KEY_1

class CastleKey2(RequirementItem):
    name = ItemNames.CASTLE_KEY_2

class NimbusLand(RequirementItem):
    name = ItemNames.NIMBUS_LAND

class BarrelVolcano(RequirementItem):
    name = ItemNames.BARREL_VOLCANO

class BowsersKeep(RequirementItem):
    name = ItemNames.BOWSERS_KEEP

class Fireworks(RequirementItem):
    name = ItemNames.REGULAR_FIREWORKS

class ShinyStone(RequirementItem):
    name = ItemNames.SHINY_STONE

class CarboCookie(RequirementItem):
    name = ItemNames.CARBO_COOKIE

class BrightCard(RequirementItem):
    name = ItemNames.BRIGHT_CARD

class ExtraShinyStone(RequirementItem):
    name = ItemNames.EXTRA_SHINY_STONE

class MimicLauncher1(RequirementItem):
    name = ItemNames.FIRST_MIMIC_LAUNCHER

class MimicLauncher2(RequirementItem):
    name = ItemNames.SECOND_MIMIC_LAUNCHER

class MimicLauncher3(RequirementItem):
    name = ItemNames.THIRD_MIMIC_LAUNCHER
