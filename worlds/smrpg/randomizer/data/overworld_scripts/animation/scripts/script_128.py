#A0128_WALK_RANDOM_DIRECTIONS
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
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1], identifier="ACTION_128_set_object_memory_bits_0"),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JmpIfRandom2of3(['ACTION_128_set_animation_speed_5', 'ACTION_128_pause_13']),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepSoutheast(),
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_128_set_animation_speed_5"),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	A_Walk1StepSoutheast(identifier="ACTION_128_walk_1_step_southeast_9"),
	A_Pause(30),
	A_JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	A_Walk1StepNortheast(identifier="ACTION_128_walk_1_step_northeast_12"),
	A_Pause(60, identifier="ACTION_128_pause_13"),
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_128_set_animation_speed_14"),
	A_JmpIfRandom2of3(['ACTION_128_walk_1_step_northwest_23', 'ACTION_128_walk_1_step_northeast_12']),
	A_Walk1StepSouthwest(),
	A_Pause(20),
	A_JmpIfRandom1of2(["ACTION_128_set_object_memory_bits_0"]),
	A_Pause(30),
	A_JmpIfRandom2of3(['ACTION_128_walk_1_step_southeast_9', 'ACTION_128_pause_25']),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNortheast(),
	A_Walk1StepNorthwest(identifier="ACTION_128_walk_1_step_northwest_23"),
	A_Jmp(["ACTION_128_set_animation_speed_14"]),
	A_Pause(60, identifier="ACTION_128_pause_25"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(2),
	A_Jmp(["ACTION_128_set_animation_speed_14"])
])
