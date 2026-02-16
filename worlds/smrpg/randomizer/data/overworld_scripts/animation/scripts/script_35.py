#A0035_INNER_FORST_WIGGLER_NORTHEAST
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
	A_JmpIfBitSet(TEMP_7044_5, ["ACTION_35_jmp_if_bit_set_3"]),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_35_face_southwest_31"]),
	A_Jmp(["ACTION_35_face_southwest_21"]),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_35_face_southwest_11"], identifier="ACTION_35_jmp_if_bit_set_3"),
	A_FaceNortheast(),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(2),
	A_WalkNortheastSteps(2),
	A_SetPriority(3),
	A_WalkNortheastSteps(2),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceSouthwest(identifier="ACTION_35_face_southwest_11"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(3),
	A_Walk1StepSouthwest(),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(10),
	A_SetPriority(2),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceSouthwest(identifier="ACTION_35_face_southwest_21"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(3),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_SetPriority(2),
	A_WalkNortheastSteps(10),
	A_Walk1StepSoutheast(),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceSouthwest(identifier="ACTION_35_face_southwest_31"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(3),
	A_Walk1StepSouthwest(),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(10),
	A_Walk1StepSoutheast(),
	A_WalkSouthwestSteps(5),
	A_SetPriority(2),
	A_StartLoopNTimes(2),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_EndLoop(),
	A_WalkSouthwestSteps(2),
	A_SetPriority(3),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"])
])
