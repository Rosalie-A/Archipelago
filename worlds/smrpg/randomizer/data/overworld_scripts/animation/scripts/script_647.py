#A0647_MIDAS_MID_RIGHT_TUNNEL_CAMERA
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
	A_Pause(30),
	A_SetWalkingSpeed(SLOW),
	A_WalkEastSteps(7),
	A_SetWalkingSpeed(NORMAL),
	A_WalkEastSteps(2),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepEast(),
	A_SetWalkingSpeed(NORMAL),
	A_ReturnQueue()
])
