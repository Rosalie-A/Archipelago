#A0941_VOLCANO_1ST_BOSS
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
	A_VisibilityOff(),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80')),
	A_Pause(500),
	A_StartLoopNTimes(9),
	A_VisibilityOn(),
	A_Pause(4),
	A_VisibilityOff(),
	A_Pause(4),
	A_EndLoop(),
	A_PlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
	A_StartLoopNTimes(9),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(9),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOn(),
	A_Jmp(["ACTION_936_pause_16"])
])
