#A0852_VALLEY_RIGHT_PIPE_2ND_GECKO_RUNNING
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
	A_VisibilityOn(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(FASTER),
	A_SequenceLoopingOn(),
	A_ResetProperties(),
	A_WalkNortheastSteps(5),
	A_Pause(16),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_WalkNorthwestPixels(8),
	A_WalkSouthwestSteps(3, identifier="ACTION_852_shift_southwest_steps_10"),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(3),
	A_Walk1StepNorthwest(),
	A_Jmp(["ACTION_852_shift_southwest_steps_10"])
])
