#A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE
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
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_98_set_animation_speed_0"),
	A_Walk1StepSouthwest(),
	A_JmpIfRandom1of2(["ACTION_98_pause_6"]),
	A_Walk1StepNortheast(identifier="ACTION_98_walk_1_step_northeast_3"),
	A_JmpIfRandom1of2(["ACTION_98_pause_12"]),
	A_Jmp(["ACTION_98_set_animation_speed_0"]),
	A_Pause(30, identifier="ACTION_98_pause_6"),
	A_FaceNorthwest(),
	A_Pause(30),
	A_FaceSoutheast(),
	A_Pause(30),
	A_Jmp(["ACTION_98_walk_1_step_northeast_3"]),
	A_Pause(30, identifier="ACTION_98_pause_12"),
	A_FaceSoutheast(),
	A_Pause(30),
	A_FaceNorthwest(),
	A_Pause(30),
	A_Jmp(["ACTION_98_set_animation_speed_0"])
])
