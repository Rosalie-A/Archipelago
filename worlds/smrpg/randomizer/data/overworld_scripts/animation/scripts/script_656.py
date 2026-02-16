#A0656_RUNNING_YELLOW_YOSHI
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
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[1], identifier="ACTION_656_set_object_memory_bits_0"),
	A_SetSolidityBits(cant_walk_through=True),
	A_SetSolidityBits(bit_4=True),
	A_SetVarToConst(TEMP_702A, 7),
	A_SetVarToConst(ROSE_WAY_703A, 20),
	A_SetSequenceSpeed(FAST, identifier="ACTION_656_set_animation_speed_5"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepNortheast(),
	A_JmpToSubroutine(["ACTION_656_dec_29"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
	A_JmpIfRandom2of3(['ACTION_656_set_animation_speed_5', 'ACTION_656_jmp_if_var_equals_const_12']),
	A_Jmp(["ACTION_656_set_animation_speed_5"]),
	A_JmpIfVarEqualsConst(TEMP_702A, 0, ["ACTION_656_set_animation_speed_5"], identifier="ACTION_656_jmp_if_var_equals_const_12"),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNortheast(),
	A_JmpToSubroutine(["ACTION_656_dec_29"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
	A_JmpToSubroutine(["ACTION_656_dec_31"]),
	A_JmpIfRandom2of3(['ACTION_656_jmp_if_var_equals_const_12', 'ACTION_656_set_animation_speed_5']),
	A_Jmp(["ACTION_656_jmp_if_var_equals_const_12"]),
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_656_set_animation_speed_21"),
	A_FaceSouthwest(),
	A_Pause(60),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestSteps(20),
	A_FaceNortheast(),
	A_Pause(60),
	A_Jmp(["ACTION_656_set_object_memory_bits_0"]),
	A_Dec(ROSE_WAY_703A, identifier="ACTION_656_dec_29"),
	A_ReturnQueue(),
	A_Dec(TEMP_702A, identifier="ACTION_656_dec_31"),
	A_ReturnQueue()
])
