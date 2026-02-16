#A0993_KEEP_BRIDGE_GOOMBA
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
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastSteps(5, identifier="ACTION_993_shift_northeast_steps_2"),
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(2),
	A_FixedFCoordOff(),
	A_FaceNortheast(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastSteps(3),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastSteps(1),
	A_WalkSoutheastSteps(1),
	A_WalkSouthwestSteps(1),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestSteps(10),
	A_WalkNorthwestSteps(1),
	A_Jmp(["ACTION_993_shift_northeast_steps_2"])
])
