#A0711_BOOSTER_HILL_HENCHMAN_BOUNCE
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
	A_FixedFCoordOn(),
	A_Dec(TEMP_70AE),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_SetAllSpeeds(VERY_FAST),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_711_db_25"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_711_db_16"]),
	A_UnknownCommand(bytearray(b' \x00')),
	A_Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_8"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_8"]),
	A_TransferToXYZF(x=13, y=67, z=0, direction=EAST),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_15"]),
	A_JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	A_Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_15"),
	A_UnknownCommand(bytearray(b' \x00'), identifier="ACTION_711_db_16"),
	A_Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_17"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_17"]),
	A_TransferToXYZF(x=12, y=69, z=0, direction=EAST),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_24"]),
	A_JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	A_Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_24"),
	A_UnknownCommand(bytearray(b' \x00'), identifier="ACTION_711_db_25"),
	A_Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_26"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_26"]),
	A_TransferToXYZF(x=11, y=71, z=0, direction=EAST),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_34"]),
	A_TransferToXYZF(x=12, y=70, z=0, direction=EAST),
	A_JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	A_Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_34")
])
