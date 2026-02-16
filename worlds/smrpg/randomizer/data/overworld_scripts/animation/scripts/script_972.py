#A0972_ENDING_CREDITS_CASTLE_ASSISTANT
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
	A_WalkNortheastSteps(2),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_FaceNorthwest(),
	A_Pause(24),
	A_FaceSouthwest(),
	A_Pause(24),
	A_FaceNortheast(),
	A_Pause(24),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSouthwestSteps(2),
	A_Pause(8),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_Pause(16),
	A_WalkNortheastSteps(3),
	A_Pause(104),
	A_WalkSouthwestSteps(8),
	A_SetWalkingSpeed(FASTER),
	A_WalkNortheastSteps(7),
	A_FaceNorthwest(),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
