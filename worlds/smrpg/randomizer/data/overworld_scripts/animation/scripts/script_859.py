#A0859_ABYSS_BEFORE_1ST_BOSS_SCREW_2
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
	A_Pause(1, identifier="ACTION_859_pause_0"),
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(NORMAL),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_859_pause_0"]),
	A_JmpIfBitClear(TEMP_7044_6, ["ACTION_859_pause_0"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_859_jmp_if_var_equals_const_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_859_jmp_if_var_equals_const_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_859_jmp_if_var_equals_const_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_859_jmp_if_var_equals_const_19"]),
	A_JmpIfVarEqualsConst(FACTORY_FALL_3, 16, ["ACTION_859_pause_0"]),
	A_Inc(FACTORY_FALL_3),
	A_SetSpriteSequence(index=1, looping=False),
	A_WalkNortheastPixels(5),
	A_ClearBit(TEMP_7043_0),
	A_ClearBit(TEMP_7043_1),
	A_ClearBit(TEMP_7044_6),
	A_Jmp(["ACTION_859_pause_0"]),
	A_JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["ACTION_859_pause_0"], identifier="ACTION_859_jmp_if_var_equals_const_19"),
	A_Dec(FACTORY_FALL_3),
	A_SetSpriteSequence(index=2, looping=False),
	A_WalkSouthwestPixels(5),
	A_ClearBit(TEMP_7043_1),
	A_ClearBit(TEMP_7044_6),
	A_Jmp(["ACTION_859_pause_0"])
])
