#A0033_FIRST_WIGGLER_BEHIND_STUMP
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
	A_FaceNortheast(),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(2),
	A_Walk1StepNortheast(),
	A_WalkSoutheastSteps(2),
	A_SetPriority(3),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_33_shift_southwest_steps_11"]),
	A_WalkSouthwestSteps(5),
	A_SetPriority(2),
	A_WalkNorthwestSteps(4),
	A_Jmp(["ACTION_33_set_priority_18"]),
	A_WalkSouthwestSteps(3, identifier="ACTION_33_shift_southwest_steps_11"),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_SetPriority(2),
	A_WalkNorthwestSteps(2),
	A_SetPriority(3, identifier="ACTION_33_set_priority_18"),
	A_WalkNortheastSteps(3),
	A_SetPriority(2),
	A_JmpIfBitSet(TEMP_7044_0, ["ACTION_33_walk_1_step_northeast_24"]),
	A_Walk1StepSoutheast(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_Walk1StepNortheast(identifier="ACTION_33_walk_1_step_northeast_24"),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Walk1StepSoutheast(),
	A_FaceSouthwest(),
	A_Jmp(["ACTION_32_walk_1_step_f_direction_33"])
])
