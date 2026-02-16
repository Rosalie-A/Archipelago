#A0044_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_CHOW
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
	A_Pause(55),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNortheastPixels(8, identifier="ACTION_44_shift_northeast_pixels_5"),
	A_Pause(20),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(SLOW),
	A_JumpToHeight(height=40, silent=True),
	A_WalkSouthwestPixels(12),
	A_Pause(25),
	A_SetWalkingSpeed(VERY_SLOW),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNortheastPixels(4),
	A_Jmp(["ACTION_44_shift_northeast_pixels_5"])
])
