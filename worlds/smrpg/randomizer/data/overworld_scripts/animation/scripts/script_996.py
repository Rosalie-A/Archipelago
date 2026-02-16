#A0996_KEEP_BRIDGE_GOOMBA
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
	A_SetSequenceSpeed(FAST, identifier="ACTION_996_set_animation_speed_0"),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestSteps(5),
	A_WalkNorthwestSteps(1),
	A_WalkNortheastSteps(11),
	A_WalkSoutheastSteps(1),
	A_WalkSouthwestSteps(1),
	A_FaceNortheast(),
	A_FixedFCoordOn(),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestSteps(2),
	A_FixedFCoordOff(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestSteps(3),
	A_Jmp(["ACTION_996_set_animation_speed_0"])
])
