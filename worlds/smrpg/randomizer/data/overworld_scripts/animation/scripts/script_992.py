#A0992_DEFAULT_SEQUENCE_IN_CHEST
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
    A_JmpIfVarEqualsConst(ITEM_ID, HoneySyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID, MapleSyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID, RoyalSyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID, PureWaterItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID, RedEssenceItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID, YoshiAdeItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID, CricketJamItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem().item_id, ["A0992_juice"]), # sequence 2 also used for keys
    A_JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID, EnergizerItem().item_id, ["A0992_p"]),
    A_JmpIfVarEqualsConst(ITEM_ID, PowerBlastItem().item_id, ["A0992_p"]),
    A_JmpIfVarEqualsConst(ITEM_ID, BracerItem().item_id, ["A0992_d"]),
    A_JmpIfVarEqualsConst(ITEM_ID, CrystallineItem().item_id, ["A0992_d"]),
    A_JmpIfVarEqualsConst(ITEM_ID, FroggieDrinkItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID, ElixirItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID, MegalixirItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID, KerokeroColaItem().item_id, ["A0992_frog"]),
    A_JmpIfVarEqualsConst(ITEM_ID, FreshenUpItem().item_id, ["A0992_r"]),
    A_JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem().item_id, ["A0992_r"]),
    A_JmpIfVarEqualsConst(ITEM_ID, PickMeUpItem().item_id, ["A0992_star"]),
    A_JmpIfVarEqualsConst(ITEM_ID, YoshiCandyItem().item_id, ["A0992_candy"]),
    A_JmpIfVarEqualsConst(ITEM_ID, RockCandyItem().item_id, ["A0992_candy"]),
    A_JmpIfVarEqualsConst(ITEM_ID, CymbalsItem().item_id, ["A0992_candy"]), # sequence 9 also used for music notes
    A_JmpIfVarEqualsConst(ITEM_ID, SonicCymbalItem().item_id, ["A0992_candy"]), 
    A_JmpIfVarEqualsConst(ITEM_ID, FrightBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID, SleepyBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID, IceBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID, FireBombItem().item_id, ["A0992_bomb"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="A0992_default"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="A0992_syrup"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="A0992_juice"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="A0992_p"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True, identifier="A0992_d"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True, identifier="A0992_music"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=True, identifier="A0992_frog"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=7, is_sequence=True, looping=True, identifier="A0992_r"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, identifier="A0992_star"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, identifier="A0992_candy"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True, identifier="A0992_bomb"),
	A_FloatingOff(identifier="A0992_begin_animation"),
	A_VisibilityOff(),
	A_Pause(9),
	A_VisibilityOn(),
	A_Pause(26),
	A_VisibilityOff(),
	A_ReturnQueue()
])
