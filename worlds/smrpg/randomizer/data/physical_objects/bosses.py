from typing import Sequence
from ...types.physical_objects import (
    BossNPC,
    SpriteAnimation,
    SpriteAnimationCollection,
)
from ..rooms.npcs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
)

croco_bag_loop = SpriteAnimation(sequence_id=5, total_duration=104)
croco_bag_hit = SpriteAnimation(sequence_id=4, contact_frame=152, total_duration=158)
croco_bag_summon = SpriteAnimation(sequence_id=6, total_duration=136)
croco_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
mack_hit = SpriteAnimation(sequence_id=4, contact_frame=22, total_duration=28)
mack_hit_fast = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=FAST
)
mack_challenge = SpriteAnimation(sequence_id=2, total_duration=12)

# Booster animations
booster_laugh = SpriteAnimation(sequence_id=2)
booster_punch = SpriteAnimation(
    sequence_id=3, contact_frame=74, total_duration=92, new_sprite_id=502
)
booster_jump = SpriteAnimation(sequence_id=4)
booster_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

# Johnny animations
small_johnny_sit = SpriteAnimation(sequence_id=10)

# Valentina animations
valentina_stand = SpriteAnimation(sequence_id=10)
valentina_laugh = SpriteAnimation(sequence_id=2)
valentina_hit = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
valentina_taunt = SpriteAnimation(sequence_id=4, total_duration=58)
valentina_recoil = SpriteAnimation(sequence_id=2, total_duration=34)

# Magikoopa animations
small_magikoopa_hit = SpriteAnimation(
    sequence_id=10, contact_frame=44, total_duration=72
)

# Shovel Knight animations
shovelknight_tile = SpriteAnimation(sequence_id=2)

# Belome animations
belome_attack = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
belome_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)
belome_wiggle = SpriteAnimation(sequence_id=4, total_duration=66)
belome_recoil = SpriteAnimation(sequence_id=2, total_duration=14)

# Boomer animations
boomer_alt_taunt = SpriteAnimation(sequence_id=1, total_duration=16)

# Terrapin animations
jagger_recoil = SpriteAnimation(sequence_id=2, total_duration=18)
jagger_look = SpriteAnimation(sequence_id=8)
jagger_punch = SpriteAnimation(sequence_id=4, contact_frame=54, total_duration=74)
jagger_taunt = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=38)

# Piranha Plant animations
piranha_taunt = SpriteAnimation(sequence_id=4, total_duration=16)
piranha_bite = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=52)
piranha_recoil = SpriteAnimation(sequence_id=2, total_duration=20)
piranha_chillin = SpriteAnimation(sequence_id=7, total_duration=16)

# Bloober animations
squid_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
squid_hit = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
squid_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)
squid_default = SpriteAnimation(sequence_id=0, total_duration=36)

# Jinx animations
jinx_punch = SpriteAnimation(sequence_id=3, contact_frame=10, total_duration=18)
jinx_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

punchinello_hit = SpriteAnimation(sequence_id=3, contact_frame=24, total_duration=34)
punchinello_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=23, speed=FAST)
punchinello_cast = SpriteAnimation(sequence_id=4, contact_frame=46, total_duration=54)
punchinello_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
punchinello_animations = SpriteAnimationCollection(
    recoil= punchinello_recoil,
    mines_punch= punchinello_hit,
    ship_beckon=punchinello_cast,
    dojo_challenge=punchinello_cast,
    statue_intro=punchinello_cast,
    statue_peck=punchinello_hit_fast,
    statue_flustered= punchinello_recoil,
    keep_challenge=punchinello_cast,
    keep_summon=punchinello_cast,
    chandelier_challenge=punchinello_cast,
    endgame_challenge=punchinello_cast
)
class HammerBroLargeObject(BossNPC):
    """Hammer Bro object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_NPC


class HammerBroSmallObject(BossNPC):
    """Small Hammer Bro object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_SMALL_NPC


class HammerBroStatueObject(BossNPC):
    """Hammer Bro statue object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_STATUE_NPC


class Croco1Object(BossNPC):
    """Croco 1 object in Mushroom Way Area 03."""

    _base = CROCO_1_NPC
    _eye_height = 16
    _tower_entrance_horizontal_shift = 9
    _animations = SpriteAnimationCollection(
        recoil=croco_recoil,
        bandits_way_distracted=croco_bag_loop,
        mines_punch=croco_bag_hit,
        chapel_laugh=croco_bag_loop,
        dojo_challenge=croco_bag_summon,
        statue_flustered=croco_recoil,
        keep_challenge=croco_bag_summon,
        keep_summon=croco_bag_hit,
        chandelier_challenge=croco_bag_summon,
        endgame_challenge=croco_bag_summon,
        tower_toss=croco_bag_hit
    )


class Croco2Object(BossNPC):
    """Croco 2 object in Mushroom Way Area 03."""

    _base = CROCO_2_NPC
    _eye_height = 16
    _animations = SpriteAnimationCollection(
        recoil=croco_recoil,
        bandits_way_distracted=croco_bag_loop,
        mines_punch=croco_bag_hit,
        chapel_laugh=croco_bag_loop,
        dojo_challenge=croco_bag_summon,
        statue_flustered=croco_recoil,
        keep_challenge=croco_bag_summon,
        keep_summon=croco_bag_hit,
        chandelier_challenge=croco_bag_summon,
        endgame_challenge=croco_bag_summon,
        tower_toss=croco_bag_hit
    )


class CrocoStatueObject(BossNPC):
    """Croco statue object in Mushroom Way Area 03."""

    _base = CROCO_STATUE_NPC
    _horizontal_pixel_shift = -3


class MackSmallObject(BossNPC):
    """Small Mack object in Mushroom Way Area 03."""

    _base = MACK_SMALL_NPC
    _eye_height = 19


class MackMediumObject(BossNPC):
    """Medium Mack object in Mushroom Way Area 03."""

    _base = MACK_MEDIUM_NPC


class MackBattleObject(BossNPC):
    """Battle Mack object in Mushroom Way Area 03."""

    _base = MACK_NPC
    _animations = SpriteAnimationCollection(
        mines_punch=mack_hit,
        statue_peck=mack_hit_fast,
        statue_flustered=mack_challenge,
        chandelier_challenge=mack_challenge,
        endgame_challenge=mack_hit,
    )


class MackStatueObject(BossNPC):
    """Mack statue object in Mushroom Way Area 03."""

    _base = MACK_STATUE_NPC


class PandoriteSmallObject(BossNPC):
    """Small Pandorite object in Mushroom Way Area 03."""

    _base = PANDORITE_SMALL_NPC


class PandoriteLargeObject(BossNPC):
    """Large Pandorite object in Mushroom Way Area 03."""

    _base = PANDORITE_NPC


class MimicStatueObject(BossNPC):
    """Mimic statue object in Mushroom Way Area 03."""

    _base = MIMIC_STATUEL_NPC
    _eye_height = 4
    _crown_height = 1


class Belome1SmallObject(BossNPC):
    """Small Belome 1 object in Mushroom Way Area 03."""

    _base = BELOME_SMALL_NPC


belome_animations = SpriteAnimationCollection(
    mines_punch=belome_attack,
    statue_intro=belome_wiggle,
    statue_flustered=belome_recoil,
    statue_peck=belome_attack_fast,
    chandelier_challenge=belome_attack,
    endgame_challenge=belome_attack,
)


class Belome1LargeObject(BossNPC):
    """Large Belome 1 object in Mushroom Way Area 03."""

    _base = BELOME_ST_TIME_NPC
    _animations = belome_animations


class Belome2SmallObject(BossNPC):
    """Small Belome 2 object in Mushroom Way Area 03."""

    _base = BELOME_2_SMALL_NPC


class Belome2LargeObject(BossNPC):
    """Large Belome 2 object in Mushroom Way Area 03."""

    _base = GOLDEN_BELOME_NPC
    _animations = belome_animations


class Belome3SmallObject(BossNPC):
    """Small Belome 3 object in Mushroom Way Area 03."""

    _base = BELOME_3_SMALL_NPC


class Belome3LargeObject(BossNPC):
    """Large Belome 3 object in Mushroom Way Area 03."""

    _base = BELOME_3_NPC
    _animations = belome_animations


class BelomeSmallStatueObject(BossNPC):
    """Small Belome statue object in Mushroom Way Area 03."""

    _base = BELOME_SMALL_STATUE


class BowyerSmallObject(BossNPC):
    """Small Bowyer object in Mushroom Way Area 03."""

    _base = BOWYER_SMALL_NPC
    _eye_height = 16


class BowyerStatueObject(BossNPC):
    """Bowyer statue object in Mushroom Way Area 03."""

    _base = BOWYER_STATUE_NPC


class BowyerLargeObject(BossNPC):
    """Large Bowyer object in Mushroom Way Area 03."""

    _base = BOWYER_NPC_BATTLE


# Punchinello
class PunchinelloSmallObject(BossNPC):
    """Small Punchinello object."""

    _base = PUNCHINELLO_SMALL_NPC


class PunchinelloLargeObject(BossNPC):
    """Large Punchinello object."""

    _base = PUNCHINELLO_NPC
    _animations=punchinello_animations


class Punchinello2LargeObject(BossNPC):
    """Large Punchinello object."""

    _base = PUNCHINELLO_POSTGAME_NPC
    _animations=punchinello_animations


# Dodo
class DodoSmallObject(BossNPC):
    """Small Dodo object."""

    _base = DODO_SMALL_NPC
    _eye_height = 16


class DodoLargeObject(BossNPC):
    """Large Dodo object."""

    _base = DODO_NPC


# Birdetta
class BirdettaSmallObject(BossNPC):
    """Small Birdetta object."""

    _base = BIRDETTA_SMALL_NPC
    _eye_height = 6


class BirdettaLargeObject(BossNPC):
    """Large Birdetta object."""

    _base = BIRDETTA_NPC


# Czar Dragon
class CzarDragonSmallObject(BossNPC):
    """Small Czar Dragon object."""

    _base = CZAR_DRAGON_SMALL_NPC
    _eye_height = 3


class CzarDragonMediumObject(BossNPC):
    """Medium Czar Dragon object."""

    _base = CZAR_DRAGON_BODY_NPC


class CzarDragonLargeObject(BossNPC):
    """Large Czar Dragon object."""

    _base = CZAR_DRAGON_NPC


# Boomer
class BoomerSmallObject(BossNPC):
    """Small Boomer object."""

    _base = BOOMER_SMALL_NPC


class BoomerLargeObject(BossNPC):
    """Large Boomer object."""

    _base = BOOMER_NPC


# Exor
class ExorSmallObject(BossNPC):
    """Small Exor object."""

    _base = EXOR_SMALL_NPC


# Domino
class DominoSmallObject(BossNPC):
    """Small Domino object."""

    _base = DOMINO_SMALL_NPC
    _eye_height = 12


# Cloaker
class CloakerLargeObject(BossNPC):
    """Large Cloaker object."""

    _base = CLOAKER_ST_TIME_NPC


# Smithy
class SmithySmallObject(BossNPC):
    """Small Smithy object."""

    _base = SMITHY_SMALL_NPC


class SmithyLargeObject(BossNPC):
    """Large Smithy object."""

    _base = SMITHY_LOWER_NPC


# Culex
class CulexSmallObject(BossNPC):
    """Small Culex object."""

    _base = CULEX_SMALL_NPC


class CulexLargeObject(BossNPC):
    """Large Culex object."""

    _base = CULEX_NPC


# Bundt
class BundtSmallObject(BossNPC):
    """Small Bundt object."""

    _base = BUNDT_OBJECT_NPC
    _eye_height = 8


class BundtLargeObject(BossNPC):
    """Large Bundt object."""

    _base = BUNDT_NPC


class Bundt2LargeObject(BossNPC):
    """Large Bundt object."""

    _base = BUNDT_2_NPC


# Johnny (Jonathan Jones)
class JohnnySmallObject(BossNPC):
    """Small Johnny object."""

    _base = JONATHAN_JONES_NPC
    _eye_height = 20
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=small_johnny_sit,
        chapel_laugh=small_johnny_sit,
        ship_beckon=small_johnny_sit,
        ship_chair=small_johnny_sit,
        statue_intro=small_johnny_sit,
        dojo_challenge=small_johnny_sit,
        keep_challenge=small_johnny_sit,
        chandelier_challenge=small_johnny_sit,
        endgame_challenge=small_johnny_sit,
    )


class JohnnyLargeObject(BossNPC):
    """Large Johnny object."""

    _base = JOHNNY_NPC


class Johnny2LargeObject(BossNPC):
    """Large Johnny object."""

    _base = JOHNNY_NPC_2


# Valentina
class ValentinaSmallObject(BossNPC):
    """Small Valentina object."""

    _base = VALENTINA_NPC_2
    _eye_height = 16
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=valentina_stand,
        chapel_laugh=valentina_laugh,
        ship_beckon=valentina_laugh,
        ship_chair=valentina_stand,
        dojo_challenge=valentina_laugh,
        statue_intro=valentina_laugh,
        keep_challenge=valentina_laugh,
        keep_summon=valentina_laugh,
        chandelier_challenge=valentina_laugh,
        endgame_challenge=valentina_laugh,
        look_at_ceiling_mold_id=8,
    )


class ValentinaLargeObject(BossNPC):
    """Large Valentina object."""

    _base = VALENTINA_NPC


# Knife Guy
class KnifeGuySmallObject(BossNPC):
    """Small Knife Guy object."""

    _base = KNIFE_GUY_JUGGLER_STILL_RED_BALLS_NPC


class KnifeGuyLargeObject(BossNPC):
    """Large Knife Guy object."""

    _base = KNIFE_GUY_NPC


# Grate Guy
class GrateGuySmallObject(BossNPC):
    """Small Grate Guy object."""

    _base = GRATE_GUY_FROM_CASINO_NPC
    _eye_height = 16


class GrateGuyLargeObject(BossNPC):
    """Large Grate Guy object."""

    _base = GRATE_GUY_NPC


# Mokura
class MokuraLargeObject(BossNPC):
    """Large Mokura object."""

    _base = MOKURA_NPC


class MokuraSmallObject(BossNPC):
    """Small Mokura object."""

    _base = MOKURA_S_CLOUD_BLUE_NPC_2
    _eye_height = 4
    _crown_height = 1


# Yaridovich
class YaridovichLargeObject(BossNPC):
    """Large Yaridovich object."""

    _base = YARIDOVICH_NPC


# Missing Small/Medium Classes


class MagikoopaSmallObject(BossNPC):
    """Small Magikoopa object."""

    _base = MAGIKOOPA_NPC
    _animations = SpriteAnimationCollection(
        mines_punch=small_magikoopa_hit,
        ship_beckon=small_magikoopa_hit,
        dojo_challenge=small_magikoopa_hit,
        keep_challenge=small_magikoopa_hit,
        keep_summon=small_magikoopa_hit,
        chandelier_challenge=small_magikoopa_hit,
        endgame_challenge=small_magikoopa_hit,
        tower_toss=small_magikoopa_hit
    )


class ClerkSmallObject(BossNPC):
    """Small Clerk object."""

    _base = FACTORY_CLERK_GREEN_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tile,
        chapel_laugh=shovelknight_tile,
        ship_chair=shovelknight_tile,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile
    )


class ManagerSmallObject(BossNPC):
    """Small Manager object."""

    _base = FACTORY_MANAGER_BLUE_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tile,
        chapel_laugh=shovelknight_tile,
        ship_chair=shovelknight_tile,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile
    )


class DirectorSmallObject(BossNPC):
    """Small Director object."""

    _base = FACTORY_DIRECTOR_RED_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tile,
        chapel_laugh=shovelknight_tile,
        ship_chair=shovelknight_tile,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile
    )


class HidonSmallObject(BossNPC):
    """Small Hidon object."""

    _base = HIDON_SMALL_NPC


class ChesterSmallObject(BossNPC):
    """Small Chester object."""

    _base = CHESTER_SMALL_NPC


class BoxBoySmallObject(BossNPC):
    """Small Box Boy object."""

    _base = BOX_BOY_SMALL_NPC


# Missing Large Classes


class ClerkLargeObject(BossNPC):
    """Large Clerk object."""

    _base = CLERK_LARGE_NPC


class ClerkBattleObject(BossNPC):
    """Battle Clerk object."""

    _base = CLERK_NPC


class ManagerLargeObject(BossNPC):
    """Large Manager object."""

    _base = MANAGER_LARGE_NPC


class ManagerBattleObject(BossNPC):
    """Battle Manager object."""

    _base = MANAGER_NPC


class DirectorBattleObject(BossNPC):
    """Battle Director object."""

    _base = DIRECTOR_NPC


class DirectorLargeObject(BossNPC):
    """Large Director object."""

    _base = DIRECTOR_LARGE_NPC


class HidonLargeObject(BossNPC):
    """Large Hidon object."""

    _base = HIDON_NPC


class ChesterLargeObject(BossNPC):
    """Large Chester object."""

    _base = CHESTER_NPC


class BoxBoyLargeObject(BossNPC):
    """Large Box Boy object."""

    _base = BOX_BOY_NPC


class MagikoopaLargeObject(BossNPC):
    """Large Magikoopa object."""

    _base = MAGIKOOPA_LARGE_NPC


class DominoLargeObject(BossNPC):
    """Large Domino object."""

    _base = DOMINO_LARGE_NPC


class MackLargeObject(BossNPC):
    """Large Mack object."""

    _base = MACK_LARGE_NPC


# Missing Statue Classes


class NimbusLandStatueObject(BossNPC):
    """Nimbus Land statue object."""

    _base = VALENTINA_STATUE_NPC


class BelomeStatueObject(BossNPC):
    """Belome statue object."""

    _base = GOLDEN_BELOME_NPC


class BoosterObject(BossNPC):
    """Booster object."""

    _base = BOOSTER_NPC
    _animations = SpriteAnimationCollection(
        recoil=booster_recoil,
        bandits_way_distracted=booster_laugh,
        mines_punch=booster_punch,
        chapel_laugh=booster_laugh,
        ship_beckon=booster_laugh,
        ship_chair=booster_laugh,
        dojo_challenge=booster_jump,
        statue_intro=booster_laugh,
        statue_flustered=booster_jump,
        keep_challenge=booster_jump,
        keep_summon=booster_laugh,
        chandelier_challenge=booster_punch,
        endgame_challenge=booster_punch,
        tpose_mold_id=12,
        tower_toss=booster_laugh
    )


class BoosterStatueObject(BossNPC):
    """Booster statue object."""

    _base = BOOSTER_STATUE_NPC


class JohnnyStatueObject(BossNPC):
    """Johnny statue object."""

    _base = JOHNNY_STATUE_NPC


class MagikoopaStatueObject(BossNPC):
    """Magikoopa statue object."""

    _base = MAGIKOOPA_STATUE_NPC
    _horizontal_pixel_shift = 2
    _north_facing_horizontal_pixel_shift = -4
    _north_facing_vertical_pixel_shift = -1


class ValentinaStatueObject(BossNPC):
    """Valentina statue object."""

    _base = VALENTINA_STATUE_NPC


class ShovelKnightStatueObject(BossNPC):
    """Shovel Knight statue object (Clerk/Manager/Director)."""

    _base = SHOVEL_KNIGHT_STATUE_NPC
    _horizontal_pixel_shift = -3
    _north_facing_horizontal_pixel_shift = -5


class YaridovichStatueObject(BossNPC):
    """Yaridovich statue object."""

    _base = YARIDOVICH_STATUE_NPC


class GrateGuyStatueObject(BossNPC):
    """Grate Guy statue object."""

    _base = GRATE_GUY_STATUE_NPC
    _horizontal_pixel_shift = -3
    _north_facing_horizontal_pixel_shift = -2


class JinxStatueObject(BossNPC):
    """Jinx statue object."""

    _base = JINX_STATUE_NPC


class MokuraStatueObject(BossNPC):
    """Mokura statue object."""

    _base = MOKURA_STATUE_NPC


class TerrapinObject(BossNPC):
    """Terrapin object."""

    _base = TERRAPIN_NPC
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=jagger_look,
        mines_punch=jagger_punch,
        chapel_laugh=jagger_look,
        ship_beckon=jagger_taunt,
        dojo_challenge=jagger_punch,
        statue_intro=jagger_look,
        statue_peck=jagger_taunt,
        statue_flustered=jagger_recoil,
        keep_challenge=jagger_punch,
        keep_summon=jagger_punch,
        chandelier_challenge=jagger_punch,
        endgame_challenge=jagger_punch,
        look_at_ceiling_mold_id=6,
        tower_toss=jagger_punch
    )


class TerrapinStatueObject(BossNPC):
    """Terrapin statue object."""

    _base = TERRAPIN_STATUE_NPC


class PiranhaPlantObject(BossNPC):
    """Piranha Plant object."""

    _base = PIRANHA_PLANT_NPC_3
    _eye_height = 14
    _animations = SpriteAnimationCollection(
        recoil=piranha_recoil,
        bandits_way_distracted=piranha_taunt,
        mines_punch=piranha_bite,
        chapel_laugh=piranha_chillin,
        ship_beckon=piranha_taunt,
        dojo_challenge=piranha_bite,
        statue_intro=piranha_bite,
        statue_peck=piranha_bite,
        statue_flustered=piranha_recoil,
        keep_challenge=piranha_bite,
        keep_summon=piranha_bite,
        chandelier_challenge=piranha_bite,
        endgame_challenge=piranha_bite,
        tpose_mold_id=3,
        tower_toss=piranha_bite
    )


class PiranhaPlantStatueObject(BossNPC):
    """Piranha Plant statue object."""

    _base = PIRANHA_PLANT_STATUE_NPC


class MegasmilaxLargeObject(BossNPC):
    """Large Megasmilax object."""

    _base = MEGASMILAX_NPC


class BlooberObject(BossNPC):
    """Bloober object."""

    _base = BLOOBER_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        tower_bullet=squid_hit,
        recoil=squid_recoil,
        mines_punch=squid_hit,
        dojo_challenge=squid_hit,
        statue_peck=squid_hit_fast,
        statue_flustered=squid_recoil,
        keep_challenge=squid_hit,
        keep_summon=squid_hit,
        chandelier_challenge=squid_hit,
        endgame_challenge=squid_hit,
        chapel_laugh=squid_default, 
        look_at_ceiling_mold_id=1,
        tpose_mold_id=2,
        tower_toss=squid_hit
    )


class BlooberStatueObject(BossNPC):
    """Bloober statue object."""

    _base = BLOOBER_STATUE_NPC


class FactoryChiefStatueObject(BossNPC):
    """Factory Chief statue object."""

    _base = FACTORY_CHIEF_STATUE_NPC
    _horizontal_pixel_shift = -1


chief_stab = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=38)
chief_stab_fast = SpriteAnimation(sequence_id=3, contact_frame=13, total_duration=19, speed=FAST)
chief_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
chief_cast = SpriteAnimation(sequence_id=4, total_duration=52, contact_frame=32)

class FactoryChiefObject(BossNPC):
    """Factory Chief object."""

    _base = FACTORY_CHIEF_NPC
    _animations = SpriteAnimationCollection(
        recoil=chief_recoil,
        bandits_way_distracted=chief_cast,
        mines_punch=chief_stab,
        chapel_laugh=chief_cast,
        ship_beckon=chief_cast,
        dojo_challenge=chief_stab,
        statue_intro=chief_cast,
        statue_peck=chief_stab_fast,
        statue_flustered=chief_recoil,
        keep_challenge=chief_stab,
        keep_summon=chief_cast,
        chandelier_challenge=chief_stab,
        endgame_challenge=chief_stab,
        look_at_ceiling_mold_id=17,
        tower_toss=chief_cast
    )


class AxemRedObject(BossNPC):
    """Axem Red object."""

    _base = AXEM_RED_NPC_2
    _eye_height = 15


class AxemRedStatueObject(BossNPC):
    """Axem Red statue object."""

    _base = AXEM_RED_STATUE_NPC
    _horizontal_pixel_shift = -6


class BundtStatueObject(BossNPC):
    """Bundt statue object."""

    _base = BUNDT_STATUE_NPC
    _horizontal_pixel_shift = -3


class CountDownGridplaneObject(BossNPC):
    """Count Down gridplane object."""

    _base = COUNT_DOWN_GRIDPLANE_NPC
    _eye_height = 6


class CountDownStatueObject(BossNPC):
    """Count Down statue object."""

    _base = COUNT_DOWN_STATUE_NPC
    _horizontal_pixel_shift = 4
    _vertical_pixel_shift = -1


class PunchinelloStatueObject(BossNPC):
    """Punchinello statue object."""

    _base = PUNCHINELLO_STATUE_NPC


class DodoStatueObject(BossNPC):
    """Dodo statue object."""

    _base = DODO_STATUE_NPC


class BirdettaStatueObject(BossNPC):
    """Birdetta statue object."""

    _base = BIRDETTA_STATUE_NPC


class CzarStatueObject(BossNPC):
    """Czar Dragon statue object."""

    _base = CZAR_DRAGON_STATUE_NPC


class BoomerStatueObject(BossNPC):
    """Boomer statue object."""

    _base = BOOMER_STATUE_NPC


class ExorStatueObject(BossNPC):
    """Exor statue object."""

    _base = EXOR_STATUE_NPC


class DominoStatueObject(BossNPC):
    """Domino statue object."""

    _base = DOMINO_STATUE_NPC


class SmithyStatueObject(BossNPC):
    """Smithy statue object."""

    _base = SMITHY_STATUE_NPC


class CulexStatueObject(BossNPC):
    """Culex statue object."""

    _base = CULEX_STATUE_NPC


class MallowStatueObject(BossNPC):
    """Mallow statue object."""

    _base = MALLOW_STATUE_NPC


# Missing Overworld Classes


class MachineYaridOverworldObject(BossNPC):
    """Machine Made Yaridovich overworld object."""

    _base = MACHINE_YARID_OVERWORLD_NPC


class SmithyBodyOverworldObject(BossNPC):
    """Smithy body overworld object."""

    _base = SMITHY_BODY_OVERWORLD_NPC


class BoomerOverworldObject(BossNPC):
    """Boomer overworld object."""

    _base = BOOMER_RED_NPC
    _animations = SpriteAnimationCollection(
        chandelier_challenge=boomer_alt_taunt, endgame_challenge=boomer_alt_taunt
    )


class YaridovichSmallObject(BossNPC):
    """Small Yaridovich object."""

    _base = SEASIDE_TOWN_FAKE_ELDER_GREEN_NPC
    _eye_height = 10


class YaridOverworldObject(BossNPC):
    """Yaridovich overworld object."""

    _base = YARIDOVICH_OUT_OF_BATTLE_NPC


class BowyerOverworldObject(BossNPC):
    """Bowyer overworld object."""

    _base = BOWYER_NPC_LARGE


# Postgame bosses - Small versions
class Punchinello2SmallObject(BossNPC):
    """Small Punchinello 2 object."""

    _base = PUNCHINELLO_2_SMALL_NPC


class Booster2SmallObject(BossNPC):
    """Small Booster 2 object."""

    _base = BOOSTER_2_SMALL_NPC


class Bundt2SmallObject(BossNPC):
    """Small Bundt 2 object."""

    _base = BUNDT_2_SMALL_NPC


class Johnny2SmallObject(BossNPC):
    """Small Johnny 2 object."""

    _base = JOHNNY_2_SMALL_NPC


jinx_animations = SpriteAnimationCollection(
    recoil=jinx_recoil,
    mines_punch=jinx_punch,
    ship_beckon=jinx_punch,
    dojo_challenge=jinx_punch,
    statue_intro=jinx_punch,
    statue_peck=jinx_punch,
    keep_challenge=jinx_punch,
    keep_summon=jinx_punch,
    chandelier_challenge=jinx_punch,
    endgame_challenge=jinx_punch,
    tower_toss=jinx_punch
)


class Jinx1SmallObject(BossNPC):
    """Small Jinx 1 object."""

    _base = JINX_1
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations


class Jinx2SmallObject(BossNPC):
    """Small Jinx 2 object."""

    _base = JINX_2
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations


class Jinx3SmallObject(BossNPC):
    """Small Jinx 3 object."""

    _base = JINX_3
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations


class Jinx4SmallObject(BossNPC):
    """Small Jinx 4 object."""

    _base = JINX_4
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations


class Culex3DSmallObject(BossNPC):
    """Small Culex 3D object."""

    _base = CULEX_2_SMALL_NPC
