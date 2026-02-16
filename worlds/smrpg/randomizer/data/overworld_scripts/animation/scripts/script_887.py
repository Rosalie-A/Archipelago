#A0887_NIMBUS_RED_BIRD
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_887_set_animation_speed_0"),
	A_SetSequenceSpeed(NORMAL),
	A_WalkSoutheastSteps(3),
	A_JmpIfRandom1of2(["ACTION_887_walk_1_step_southwest_5"]),
	A_Pause(60),
	A_Walk1StepSouthwest(identifier="ACTION_887_walk_1_step_southwest_5"),
	A_JmpIfRandom1of2(["ACTION_887_shift_northwest_steps_8"]),
	A_Pause(30),
	A_WalkNorthwestSteps(3, identifier="ACTION_887_shift_northwest_steps_8"),
	A_JmpIfRandom1of2(["ACTION_887_walk_1_step_northeast_11"]),
	A_Pause(30),
	A_Walk1StepNortheast(identifier="ACTION_887_walk_1_step_northeast_11"),
	A_Jmp(["ACTION_887_set_animation_speed_0"])
])
