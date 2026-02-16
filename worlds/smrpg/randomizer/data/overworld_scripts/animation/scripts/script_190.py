#A0190_ABYSS_BOLT
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
	A_Pause(1, identifier="ACTION_190_pause_0"),
	A_FaceSoutheast(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(NORMAL),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_190_pause_0"]),
	A_JmpIfBitClear(TEMP_7044_6, ["ACTION_190_pause_0"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_190_jmp_if_var_equals_const_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_190_jmp_if_var_equals_const_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_190_jmp_if_var_equals_const_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_190_jmp_if_var_equals_const_18"]),
	A_JmpIfVarEqualsConst(FACTORY_FALL_5, 0, ["ACTION_190_pause_0"]),
	A_Dec(FACTORY_FALL_5),
	A_SetSpriteSequence(index=1, looping=False, mirror_sprite=True),
	A_WalkNorthwestPixels(5),
	A_ClearBit(TEMP_7043_3),
	A_ClearBit(TEMP_7044_6),
	A_Jmp(["ACTION_190_pause_0"]),
	A_JmpIfVarEqualsConst(FACTORY_FALL_5, 16, ["ACTION_190_pause_0"], identifier="ACTION_190_jmp_if_var_equals_const_18"),
	A_Inc(FACTORY_FALL_5),
	A_SetSpriteSequence(index=2, looping=False, mirror_sprite=True),
	A_WalkSoutheastPixels(5),
	A_ClearBit(TEMP_7043_3),
	A_ClearBit(TEMP_7044_6),
	A_Jmp(["ACTION_190_pause_0"])
])
