#A0034_INNER_FORST_WIGGLER_SOUTHWEST
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
	A_JmpIfBitSet(TEMP_7044_5, ["ACTION_34_jmp_if_bit_set_3"]),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_34_face_northeast_29"]),
	A_Jmp(["ACTION_34_face_northeast_20"]),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_34_face_northeast_11"], identifier="ACTION_34_jmp_if_bit_set_3"),
	A_FaceSouthwest(),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_SetPriority(3),
	A_WalkSouthwestSteps(2),
	A_SetPriority(2),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceNortheast(identifier="ACTION_34_face_northeast_11"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_Walk1StepNortheast(),
	A_Walk1StepNorthwest(),
	A_WalkSouthwestSteps(10),
	A_SetPriority(3),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceNortheast(identifier="ACTION_34_face_northeast_20"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_Walk1StepNortheast(),
	A_Walk1StepSoutheast(),
	A_SetPriority(3),
	A_WalkSouthwestSteps(10),
	A_Walk1StepNorthwest(),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_FaceNortheast(identifier="ACTION_34_face_northeast_29"),
	A_JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	A_Walk1StepNortheast(),
	A_Walk1StepNorthwest(),
	A_WalkSouthwestSteps(10),
	A_Walk1StepNorthwest(),
	A_WalkNortheastSteps(5),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_SetPriority(3),
	A_StartLoopNTimes(1),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_EndLoop(),
	A_WalkNortheastSteps(2),
	A_SetPriority(2),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True, identifier="ACTION_34_clear_solidity_bits_48"),
	A_SetVarToConst(SECONDARY_TEMP_7024, 20),
	A_SetWalkingSpeed(NORMAL),
	A_Set700CToPressedButton(),
	A_DecVarFrom700C(SECONDARY_TEMP_7024),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_34_load_mem_60"]),
	A_UnknownCommand(bytearray(b'\xc8\x07')),
	A_AddConstToVar(Z_COORD_2, 128),
	A_AddConstToVar(X_COORD_2, 64),
	A_UnknownCommand(bytearray(b'\x99')),
	A_Jmp(["ACTION_34_visibility_on_65"]),
	A_LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_34_load_mem_60"),
	A_Pause(8),
	A_EndLoop(),
	A_Pause(1),
	A_SetSequenceSpeed(FAST),
	A_VisibilityOn(identifier="ACTION_34_visibility_on_65"),
	A_SetPriority(3),
	A_AddZCoord1Step(),
	A_Walk1StepFDirection(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 4),
	A_JmpIfComparisonResultIsLesser(["ACTION_34_set_priority_74"]),
	A_SetPriority(2),
	A_Jmp(["ACTION_34_dec_z_coord_1_step_75"]),
	A_SetPriority(3, identifier="ACTION_34_set_priority_74"),
	A_DecZCoord1Step(identifier="ACTION_34_dec_z_coord_1_step_75"),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_DecZCoord1Step(),
	A_ReturnQueue()
])
