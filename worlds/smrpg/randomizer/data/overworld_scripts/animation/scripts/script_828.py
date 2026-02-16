#A0828_BIG_CONVEYOR_ROOM_BOO
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
	A_SetWalkingSpeed(SLOW),
	A_SetPriority(3),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_828_shift_northeast_steps_37"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_828_shift_southwest_steps_33"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_828_shift_northwest_steps_29"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_828_shift_southwest_steps_26"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_828_shift_southeast_steps_19"]),
	A_WalkNortheastSteps(6, identifier="ACTION_828_shift_northeast_steps_13"),
	A_WalkNorthwestSteps(2),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestSteps(4),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestSteps(5),
	A_WalkSoutheastSteps(5, identifier="ACTION_828_shift_southeast_steps_19"),
	A_WalkSouthwestSteps(2),
	A_WalkSoutheastSteps(4),
	A_WalkSouthwestSteps(2),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(6),
	A_Jmp(["ACTION_828_shift_northeast_steps_13"]),
	A_WalkSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_26"),
	A_WalkSoutheastSteps(5),
	A_Walk1StepSouthwest(),
	A_WalkNorthwestSteps(3, identifier="ACTION_828_shift_northwest_steps_29"),
	A_WalkNortheastSteps(3),
	A_WalkNorthwestSteps(2),
	A_Jmp(["ACTION_828_shift_southwest_steps_26"]),
	A_WalkSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_33"),
	A_WalkNorthwestSteps(2),
	A_WalkSouthwestSteps(2),
	A_Walk1StepNorthwest(),
	A_WalkNortheastSteps(3, identifier="ACTION_828_shift_northeast_steps_37"),
	A_WalkSoutheastSteps(3),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_828_shift_southwest_steps_33"])
])
