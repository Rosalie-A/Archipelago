#A0568_MUSTY_FEARS_1
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
	A_ShadowOn(),
	A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(6),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(4),
	A_EndLoop(),
	A_StartLoopNTimes(3),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOn(),
	A_ReturnQueue()
])

