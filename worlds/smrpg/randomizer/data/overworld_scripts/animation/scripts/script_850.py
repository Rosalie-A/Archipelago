#A0850_BOOSTER_PASS_APPRENTICE
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
	A_SetWalkingSpeed(FAST),
	A_WalkSouthwestPixels(4),
	A_WalkSoutheastSteps(2),
	A_WalkSoutheastPixels(4),
	A_StartLoopNTimes(17, identifier="ACTION_850_start_loop_n_times_5"),
	A_JumpToHeight(108),
	A_WalkSoutheastSteps(2),
	A_EndLoop(),
	A_Pause(48),
	A_FaceSouthwest(),
	A_Pause(5),
	A_FaceNorthwest(),
	A_Pause(24),
	A_StartLoopNTimes(17),
	A_JumpToHeight(108),
	A_WalkNorthwestSteps(2),
	A_EndLoop(),
	A_Pause(48),
	A_FaceNortheast(),
	A_Pause(5),
	A_FaceSoutheast(),
	A_Pause(24),
	A_Jmp(["ACTION_850_start_loop_n_times_5"])
])
