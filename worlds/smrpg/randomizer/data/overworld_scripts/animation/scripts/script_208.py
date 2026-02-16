#A0208_RAZ_ENDING
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
	A_FaceNortheast(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(VERY_FAST),
	A_StartLoopNTimes(1, identifier="ACTION_208_start_loop_n_times_3"),
	A_WalkNortheastPixels(2),
	A_WalkSouthwestPixels(2),
	A_Pause(30),
	A_EndLoop(),
	A_Pause(90),
	A_Jmp(["ACTION_208_start_loop_n_times_3"])
])
