#A0655_BOOSTER_HILL_LAYER_2
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
	A_SetWalkingSpeed(NORMAL),
	A_StartLoopNTimes(199),
	A_WalkWestPixels(1),
	A_Pause(20),
	A_EndLoop(),
	A_StartLoopNTimes(99),
	A_WalkWestPixels(1),
	A_Pause(20),
	A_EndLoop(),
	A_SetBit(TEMP_7043_6),
	A_StartLoopNTimes(25),
	A_WalkWestPixels(1),
	A_Pause(20),
	A_EndLoop(),
	A_SetBit(TEMP_7043_4),
	A_ReturnQueue()
])
