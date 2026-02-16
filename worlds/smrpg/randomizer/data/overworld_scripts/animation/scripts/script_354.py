#A0354_LANDS_END_FLOWER_TOWER_BEES
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
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_354_face_northeast_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_354_set_solidity_bits_30"]),
	A_SetSolidityBits(cant_jump_through=True),
	A_FaceSoutheast(),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[1], identifier="ACTION_354_set_object_memory_bits_7"),
	A_SetWalkingSpeed(SLOW),
	A_AddZCoord1Step(),
	A_StartLoopNTimes(7),
	A_TurnClockwise45DegreesNTimes(7),
	A_Walk1StepFDirection(),
	A_Pause(16),
	A_JmpIfRandom1of2(["ACTION_354_end_loop_16"]),
	A_Pause(16),
	A_EndLoop(identifier="ACTION_354_end_loop_16"),
	A_DecZCoord1Step(),
	A_Pause(20),
	A_Jmp(["ACTION_354_set_object_memory_bits_7"]),
	A_FaceNortheast(identifier="ACTION_354_face_northeast_20"),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_354_set_animation_speed_21"),
	A_ShiftZUpSteps(3),
	A_ShiftZDownSteps(2),
	A_JmpIfBitSet(TEMP_7043_3, ["ACTION_354_set_solidity_bits_30"]),
	A_DecZCoord1Step(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkFDirectionSteps(4),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_354_set_animation_speed_21"]),
	A_SetSolidityBits(cant_pass_walls=True, identifier="ACTION_354_set_solidity_bits_30"),
	A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	A_SetAllSpeeds(FAST, identifier="ACTION_354_set_animation_speed_32"),
	A_StartLoopNTimes(1),
	A_TurnClockwise45Degrees(),
	A_WalkFDirectionSteps(2),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 3072),
	A_JmpIfComparisonResultIsLesser(["ACTION_354_set_animation_speed_42"]),
	A_SetAllSpeeds(NORMAL),
	A_EndLoop(),
	A_Jmp(["ACTION_354_set_animation_speed_32"]),
	A_SetAllSpeeds(FAST, identifier="ACTION_354_set_animation_speed_42"),
	A_WalkSoutheastSteps(3),
	A_WalkNortheastSteps(6),
	A_Jmp(["ACTION_354_set_animation_speed_32"])
])
