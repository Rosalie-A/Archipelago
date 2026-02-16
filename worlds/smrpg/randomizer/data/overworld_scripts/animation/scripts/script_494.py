#A0494_FAST_SPINY
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
	A_SetBit(TEMP_7043_2),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_VisibilityOn(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(FASTER),
	A_WalkNorthwestSteps(5),
	A_WalkNorthwestPixels(5),
	A_Pause(24),
	A_FaceNortheast(),
	A_Pause(8),
	A_WalkSoutheastSteps(5),
	A_WalkSoutheastPixels(5),
	A_VisibilityOff(),
	A_Pause(48),
	A_ClearBit(TEMP_7043_2),
	A_ReturnQueue()
])
