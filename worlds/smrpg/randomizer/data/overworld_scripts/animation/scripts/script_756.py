#A0756_STAR_HILL_3RD_ROOM_SACKIT
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
	A_ShiftToXYCoords(x=28, y=121),
	A_ShadowOn(),
	A_FaceNorthwest(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SequenceLoopingOn(),
	A_VisibilityOn(),
	A_WalkNorthwestSteps(8),
	A_WalkSouthwestSteps(4),
	A_WalkNorthwestSteps(8),
	A_Pause(8),
	A_ShadowOff(),
	A_JumpToHeight(128),
	A_SetWalkingSpeed(FASTER),
	A_WalkNorthwestSteps(5),
	A_Pause(56),
	A_SetWalkingSpeed(VERY_FAST),
	A_SetSequenceSpeed(FASTEST),
	A_WalkNorthwestSteps(8),
	A_VisibilityOff(),
	A_ReturnQueue()
])
