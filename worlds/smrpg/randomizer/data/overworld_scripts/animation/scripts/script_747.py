#A0747_STAR_HILL_1ST_ROOM_NORTH_SACKIT
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
	A_ShiftToXYCoords(x=2, y=84),
	A_ShadowOn(),
	A_FaceSoutheast(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SequenceLoopingOn(),
	A_VisibilityOn(),
	A_StartLoopNTimes(2),
	A_WalkSoutheastSteps(4),
	A_WalkNortheastSteps(4),
	A_EndLoop(),
	A_WalkSoutheastSteps(2),
	A_Pause(8),
	A_ShadowOff(),
	A_JumpToHeight(128),
	A_SetWalkingSpeed(FASTER),
	A_WalkSoutheastSteps(5),
	A_Pause(64),
	A_SetWalkingSpeed(VERY_FAST),
	A_SetSequenceSpeed(FASTEST),
	A_WalkSoutheastSteps(10),
	A_VisibilityOff(),
	A_ReturnQueue()
])
