#A0821_KEEP_VERTICAL_PLATFORMS_IN_LAVA_ROOM
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
	A_SetSolidityBits(bit_4=True),
	A_SetWalkingSpeed(SLOW),
	A_FixedFCoordOn(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_821_set_animation_speed_28"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_821_shift_southwest_steps_19"]),
	A_SetPriority(3),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65515),
	A_Inc(PRIMARY_TEMP_700C),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(9),
	A_EndLoop(),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0001),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_821_shift_z_up_steps_16"]),
	A_Pause(96),
	A_ShiftZUpSteps(3, identifier="ACTION_821_shift_z_up_steps_16"),
	A_ShiftZDownSteps(3),
	A_Jmp(["ACTION_821_shift_z_up_steps_16"]),
	A_WalkSouthwestSteps(2, identifier="ACTION_821_shift_southwest_steps_19"),
	A_ShiftZUpSteps(5),
	A_Walk1StepSouthwest(),
	A_Pause(32),
	A_Walk1StepNortheast(),
	A_ShiftZDownSteps(5),
	A_WalkNortheastSteps(2),
	A_Pause(32),
	A_Jmp(["ACTION_821_shift_southwest_steps_19"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_821_set_animation_speed_28"),
	A_ShiftZUpSteps(3),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpSteps(4),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpSteps(3),
	A_StartLoopNTimes(7),
	A_ShiftZDownPixels(4),
	A_ShiftZUpPixels(4),
	A_EndLoop(),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownSteps(10),
	A_Jmp(["ACTION_821_set_animation_speed_28"])
])
