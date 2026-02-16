from ...types.physical_objects import HenchmanNPC, SpriteAnimation, SpriteAnimationCollection
from ..rooms.npcs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import FAST

# Animation definitions for henchmen (from data_old/npcs.py)
shyster_taunt = SpriteAnimation(sequence_id=4, contact_frame=56, total_duration=56)
shyster_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
shyster_fast = SpriteAnimation(sequence_id=4, contact_frame=28, total_duration=28, speed=FAST)

crook_scratch = SpriteAnimation(sequence_id=4, total_duration=20, contact_frame=10)

bomb_tick = SpriteAnimation(sequence_id=4, total_duration=22, contact_frame=11)
bomb_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

snifit_shoot = SpriteAnimation(sequence_id=4, total_duration=60)
snifit_taunt = SpriteAnimation(sequence_id=5, contact_frame=30, total_duration=46)
snifit_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

torte_taunt = SpriteAnimation(sequence_id=3, total_duration=40)
torte_taunt_fast = SpriteAnimation(sequence_id=3, total_duration=20, speed=FAST)

squid_hit = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
squid_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=24, speed=FAST)
squid_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

goombette_hit = SpriteAnimation(sequence_id=3, contact_frame=42, total_duration=52)
goombette_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=21, total_duration=26, speed=FAST)
goombette_taunt = SpriteAnimation(sequence_id=2, total_duration=12)

bandana_attack = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=50)
bandana_taunt = SpriteAnimation(sequence_id=4, total_duration=36)

drillbit_hit = SpriteAnimation(sequence_id=3, contact_frame=54, total_duration=64)
drillbit_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=27, total_duration=32, speed=FAST)
drillbit_recoil = SpriteAnimation(sequence_id=2, total_duration=14)

fireball_spin = SpriteAnimation(sequence_id=3, contact_frame=40, total_duration=62)
fireball_spin_fast = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=31, speed=FAST)
fireball_recoil = SpriteAnimation(sequence_id=2, total_duration=12)

piranha_bite = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=52)
piranha_taunt = SpriteAnimation(sequence_id=4, total_duration=16)
piranha_recoil = SpriteAnimation(sequence_id=2, total_duration=20)

bird_attack = SpriteAnimation(sequence_id=3, contact_frame=24, total_duration=36)

eggbert_expand = SpriteAnimation(sequence_id=2, total_duration=32)

axem_black_hit = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=64)
axem_pink_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=58)
axem_yellow_hit = SpriteAnimation(sequence_id=3, contact_frame=82, total_duration=108)
axem_yellow_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=41, total_duration=54, speed=FAST)
axem_green_hit = SpriteAnimation(sequence_id=3, contact_frame=56, total_duration=84)
axem_green_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=28, total_duration=42, speed=FAST)

jinx_punch = SpriteAnimation(sequence_id=3, contact_frame=10, total_duration=18)
jinx_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

hammer_hit = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=36)

mallowclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
mallowclone_mad = SpriteAnimation(sequence_id=4, contact_frame=8, total_duration=16)

genoclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
genoclone_mad = SpriteAnimation(sequence_id=4, contact_frame=6, total_duration=12)

bowserclone_laugh = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
bowserclone_mad = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)

peachclone_mad = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)


class ShysterHenchman(HenchmanNPC):
    """Shyster henchman NPC for boss fights."""

    _base = SHYSTER_NPC
    _animations = SpriteAnimationCollection(
        recoil=shyster_recoil,
        tower_bullet=shyster_taunt,
        kitchen_prep=shyster_taunt,
        factory_pierce=shyster_fast,
    )


class CrookHenchman(HenchmanNPC):
    """Crook henchman NPC for boss fights."""

    _base = CROOK_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=crook_scratch,
        kitchen_prep=crook_scratch,
        factory_pierce=crook_scratch,
    )


class BobOmbHenchman(HenchmanNPC):
    """Bob-omb henchman NPC for boss fights."""

    _base = BOB_OMB_NPC
    _animations = SpriteAnimationCollection(
        recoil=bomb_recoil,
        tower_bullet=bomb_tick,
        kitchen_prep=bomb_tick,
        factory_pierce=bomb_tick,
    )


class MicrobombHenchman(HenchmanNPC):
    """Microbomb henchman NPC for boss fights."""

    _base = MICROBOMB_NPC


class SpookumHenchman(HenchmanNPC):
    """Spookum henchman NPC for boss fights."""

    _base = SPOOKUM_NPC
    _animations = SpriteAnimationCollection(
        recoil=snifit_recoil,
        tower_bullet=snifit_shoot,
        kitchen_prep=snifit_taunt,
        factory_pierce=snifit_taunt,
    )


class TorteHenchman(HenchmanNPC):
    """Torte henchman NPC for boss fights."""

    _base = TORTE_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=torte_taunt,
        kitchen_prep=torte_taunt,
        factory_pierce=torte_taunt_fast,
    )


class BlooberHenchman(HenchmanNPC):
    """Bloober henchman NPC for boss fights."""

    _base = BLOOBER_NPC
    _animations = SpriteAnimationCollection(
        recoil=squid_recoil,
        tower_bullet=squid_hit,
        mines_punch=squid_hit,
        dojo_challenge=squid_hit,
        statue_peck=squid_hit_fast,
        statue_flustered=squid_recoil,
    )


class TinyBlooberHenchman(HenchmanNPC):
    """Tiny Bloober henchman NPC for boss fights."""

    _base = TINY_BLOOBER


class GoombetteLowerHenchman(HenchmanNPC):
    """Goombette henchman NPC for boss fights."""

    _base = GOOMBETTE_LOWER_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=goombette_hit,
        kitchen_prep=goombette_taunt,
        factory_pierce=goombette_hit_fast,
    )


class BandanaBlueHenchman(HenchmanNPC):
    """Bandana Blue henchman NPC for boss fights."""

    _base = BANDANA_BLUE_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=bandana_taunt,
        kitchen_prep=bandana_attack,
        factory_pierce=bandana_attack,
    )


class BandanaRedHenchman(HenchmanNPC):
    """Bandana Red henchman NPC for boss fights."""

    _base = BANDANA_RED_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=bandana_taunt,
        kitchen_prep=bandana_attack,
        factory_pierce=bandana_attack,
    )


class DrillbitHenchman(HenchmanNPC):
    """Drillbit (Fake Seaside Town Toad) henchman NPC for boss fights."""

    _base = SEASIDE_TOWN_FAKE_GREEN_NPC
    _animations = SpriteAnimationCollection(
        recoil=drillbit_recoil,
        tower_bullet=drillbit_hit,
        kitchen_prep=drillbit_hit,
        factory_pierce=drillbit_hit_fast,
    )


class MokuraHenchman(HenchmanNPC):
    """Mokura henchman NPC for boss fights."""

    _base = MOKURA_S_CLOUD_BLUE_NPC_2


class MariocloneHenchman(HenchmanNPC):
    """Mario clone henchman NPC for boss fights."""

    _base = MARIO_CLONE_WALKING_DOWN_LEFT_NPC


class MallowcloneHenchman(HenchmanNPC):
    """Mallow clone henchman NPC for boss fights."""

    _base = MALLOW_WALKING_DOWN_LEFT_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=mallowclone_laugh,
        kitchen_prep=mallowclone_mad,
        factory_pierce=mallowclone_mad,
    )


class GenocloneHenchman(HenchmanNPC):
    """Geno clone henchman NPC for boss fights."""

    _base = GENO_WALKING_DOWN_LEFT_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=genoclone_laugh,
        kitchen_prep=genoclone_mad,
        factory_pierce=genoclone_mad,
    )


class BowsercloneHenchman(HenchmanNPC):
    """Bowser clone henchman NPC for boss fights."""

    _base = BOWSER_WALKING_DOWN_LEFT_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=bowserclone_laugh,
        kitchen_prep=bowserclone_mad,
        factory_pierce=bowserclone_mad,
    )


class BowsercloneHenchman_2(HenchmanNPC):
    """Bowser clone henchman NPC variant 2 for boss fights."""

    _base = BOWSER_WALKING_DOWN_LEFT_NPC_2
    _animations = SpriteAnimationCollection(
        tower_bullet=bowserclone_laugh,
        kitchen_prep=bowserclone_mad,
        factory_pierce=bowserclone_mad,
    )


class PeachcloneHenchman(HenchmanNPC):
    """Peach clone henchman NPC for boss fights."""

    _base = TOADSTOOL_WALKING_DOWN_LEFT_NPC_4
    _animations = SpriteAnimationCollection(
        tower_bullet=peachclone_mad,
        kitchen_prep=peachclone_mad,
        factory_pierce=peachclone_mad,
    )


class FireCrystalHenchman(HenchmanNPC):
    """Fire Crystal henchman NPC for boss fights."""

    _base = FIRE_CRYSTAL_GRIDPLANE_NPC


class WaterCrystalHenchman(HenchmanNPC):
    """Water Crystal henchman NPC for boss fights."""

    _base = WATER_CRYSTAL_GRIDPLANE_NPC


class EarthCrystalHenchman(HenchmanNPC):
    """Earth Crystal henchman NPC for boss fights."""

    _base = EARTH_CRYSTAL_GRIDPLANE_NPC


class WindCrystalHenchman(HenchmanNPC):
    """Wind Crystal henchman NPC for boss fights."""

    _base = WIND_CRYSTAL_GRIDPLANE_NPC


class PiranhaPlantHenchman(HenchmanNPC):
    """Piranha Plant henchman NPC for boss fights."""

    _base = PIRANHA_PLANT_NPC
    _animations = SpriteAnimationCollection(
        recoil=piranha_recoil,
        tower_bullet=piranha_bite,
        kitchen_prep=piranha_taunt,
        factory_pierce=piranha_bite,
    )


class FeatherHenchman(HenchmanNPC):
    """Feather henchman NPC for Dodo boss fight."""

    _base = FEATHER_NPC


class EggbertHenchman(HenchmanNPC):
    """Eggbert henchman NPC for boss fights."""

    _base = EGGBERT_GRIDPLANE_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=eggbert_expand,
        kitchen_prep=eggbert_expand,
        factory_pierce=eggbert_expand,
    )


class BluebirdHenchman(HenchmanNPC):
    """Bluebird henchman NPC for boss fights."""

    _base = BLUEBIRD_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=bird_attack,
        kitchen_prep=bird_attack,
        factory_pierce=bird_attack,
    )


class BirdyHenchman(HenchmanNPC):
    """Birdy henchman NPC for boss fights."""

    _base = BIRDY_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=bird_attack,
        kitchen_prep=bird_attack,
        factory_pierce=bird_attack,
    )


class HelioHenchman(HenchmanNPC):
    """Helio henchman NPC for boss fights."""

    _base = HELIO_NPC


class SparkyHenchman(HenchmanNPC):
    """Sparky/Pyrosphere henchman NPC for boss fights."""

    _base = SPARKY_NPC
    _animations = SpriteAnimationCollection(
        recoil=fireball_recoil,
        tower_bullet=fireball_spin,
        kitchen_prep=fireball_spin,
        factory_pierce=fireball_spin_fast,
    )


class AxemBlackHenchman(HenchmanNPC):
    """Axem Black henchman NPC for boss fights."""

    _base = AXEM_BLACK_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=axem_black_hit,
        kitchen_prep=axem_black_hit,
        factory_pierce=axem_black_hit,
    )


class AxemPinkHenchman(HenchmanNPC):
    """Axem Pink henchman NPC for boss fights."""

    _base = AXEM_PINK_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=axem_pink_hit,
        kitchen_prep=axem_pink_hit,
        factory_pierce=axem_pink_hit,
    )


class AxemYellowHenchman(HenchmanNPC):
    """Axem Yellow henchman NPC for boss fights."""

    _base = AXEM_YELLOW_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=axem_yellow_hit_fast,
        kitchen_prep=axem_yellow_hit,
    )


class AxemGreenHenchman(HenchmanNPC):
    """Axem Green henchman NPC for boss fights."""

    _base = AXEM_GREEN_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=axem_green_hit,
        kitchen_prep=axem_green_hit,
        factory_pierce=axem_green_hit_fast,
    )


class JinxCloneHenchman(HenchmanNPC):
    """Jinx clone henchman NPC for boss fights."""

    _base = JINX_1
    _animations = SpriteAnimationCollection(
        recoil=jinx_recoil,
        dojo_challenge=jinx_punch,
    )


class DingalingHenchman(HenchmanNPC):
    """Ding-a-ling henchman NPC for boss fights."""

    _base = DINGALING_GRIDPLANE_NPC


class MadMalletHenchman(HenchmanNPC):
    """Mad Mallet henchman NPC for boss fights."""

    _base = MAD_MALLET_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=hammer_hit,
        kitchen_prep=hammer_hit,
        factory_pierce=hammer_hit,
    )


class PounderHenchman(HenchmanNPC):
    """Pounder henchman NPC for boss fights."""

    _base = POUNDER_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=hammer_hit,
        kitchen_prep=hammer_hit,
        factory_pierce=hammer_hit,
    )


class PoundetteHenchman(HenchmanNPC):
    """Poundette henchman NPC for boss fights."""

    _base = POUNDETTE_NPC
    _animations = SpriteAnimationCollection(
        tower_bullet=hammer_hit,
        kitchen_prep=hammer_hit,
        factory_pierce=hammer_hit,
    )


class AeroHenchman(HenchmanNPC):
    """Aero henchman NPC for boss fights."""

    _base = AERO_NPC
