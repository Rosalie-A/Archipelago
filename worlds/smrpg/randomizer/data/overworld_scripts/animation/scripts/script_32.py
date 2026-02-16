#A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP
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
	A_FaceSoutheast(),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(3),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(2),
	A_SetPriority(2),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_32_shift_northwest_steps_10"]),
	A_WalkNorthwestSteps(4),
	A_WalkSouthwestSteps(5),
	A_Jmp(["ACTION_32_shift_southeast_steps_16"]),
	A_WalkNorthwestSteps(2, identifier="ACTION_32_shift_northwest_steps_10"),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_WalkSouthwestSteps(3),
	A_WalkSoutheastSteps(2, identifier="ACTION_32_shift_southeast_steps_16"),
	A_SetPriority(3),
	A_JmpIfBitSet(TEMP_7044_0, ["ACTION_32_walk_1_step_northeast_27"]),
	A_WalkNortheastSteps(2),
	A_ShiftZUpSteps(2, identifier="ACTION_32_shift_z_up_steps_20"),
	A_SetPriority(3),
	A_Walk1StepFDirection(),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_DecZCoord1Step(),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_Walk1StepNortheast(identifier="ACTION_32_walk_1_step_northeast_27"),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_FaceNorthwest(),
	A_Walk1StepFDirection(identifier="ACTION_32_walk_1_step_f_direction_33"),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"])
])
