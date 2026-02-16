#A0974_ENDING_CREDITS_CASTLE_GOOMBA
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
	A_WalkSoutheastSteps(2),
	A_WalkNortheastSteps(2),
	A_Walk1StepSoutheast(),
	A_SetWalkingSpeed(FAST),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(3),
	A_SetWalkingSpeed(SLOW),
	A_WalkNorthwestSteps(5),
	A_WalkNorthwestPixels(8),
	A_Walk1StepSouthwest(),
	A_WalkSoutheastPixels(8),
	A_Pause(24),
	A_SequenceLoopingOn(),
	A_JumpToHeight(64),
	A_Pause(32),
	A_FaceNorthwest(),
	A_Pause(32),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
