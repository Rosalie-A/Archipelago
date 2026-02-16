#A0673_PIPE_VAULT_FINAL_ROOM_GOOMBA
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
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_673_set_animation_speed_1"),
	A_JmpIfRandom1of2(["ACTION_673_walk_1_step_northeast_5"], identifier="ACTION_673_jmp_if_random_above_128_2"),
	A_Walk1StepSouthwest(),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNortheast(identifier="ACTION_673_walk_1_step_northeast_5"),
	A_JmpIfRandom1of2(["ACTION_673_walk_1_step_southwest_9"]),
	A_Walk1StepNortheast(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepSouthwest(identifier="ACTION_673_walk_1_step_southwest_9"),
	A_SetWalkingSpeed(SLOW),
	A_JmpIfRandom2of3(['ACTION_673_set_animation_speed_1', 'ACTION_673_jmp_if_random_above_128_2']),
	A_Jmp(["ACTION_673_walk_1_step_northeast_5"])
])
