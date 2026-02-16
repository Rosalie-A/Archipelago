#A0365_BOOSTER_HILL_LEFTOVER_FLOWERS_PICKED_UP
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
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_SetWalkingSpeed(NORMAL),
	A_FloatingOff(),
	A_JumpToHeight(112),
	A_Pause(12),
	A_FloatingOff(),
	A_StartLoopNTimes(8),
	A_VisibilityOn(),
	A_Pause(4),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_ReturnQueue()
])
