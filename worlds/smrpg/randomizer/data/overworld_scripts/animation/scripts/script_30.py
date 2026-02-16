#A0030_POST_THRONE_BIRDS_3_TO_7
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
	A_SetSequenceSpeed(SLOW, identifier="ACTION_30_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepSoutheast(),
	A_JmpIfRandom1of2(["ACTION_30_pause_8"]),
	A_Walk1StepNorthwest(identifier="ACTION_30_walk_1_step_northwest_5"),
	A_JmpIfRandom1of2(["ACTION_30_pause_14"]),
	A_Jmp(["ACTION_30_set_animation_speed_0"]),
	A_Pause(30, identifier="ACTION_30_pause_8"),
	A_FaceNortheast(),
	A_Pause(30),
	A_FaceSouthwest(),
	A_Pause(30),
	A_Jmp(["ACTION_30_walk_1_step_northwest_5"]),
	A_Pause(30, identifier="ACTION_30_pause_14"),
	A_FaceSouthwest(),
	A_Pause(30),
	A_FaceNortheast(),
	A_Pause(30),
	A_Jmp(["ACTION_30_set_animation_speed_0"])
])
