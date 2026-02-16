#A0787_PLAYER_COWERS_IN_CORNER
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 346, ["ACTION_787_set_animation_speed_10"]),
	A_SetWalkingSpeed(VERY_FAST),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_SetPriority(3),
	A_FixedFCoordOn(),
	A_WalkNorthwestSteps(2),
	A_FixedFCoordOff(),
	A_FaceNorthwest(),
	A_SetWalkingSpeed(FASTEST, identifier="ACTION_787_set_animation_speed_10"),
	A_SequencePlaybackOff(),
	A_FixedFCoordOn(),
	A_WalkNorthwestPixels(1, identifier="ACTION_787_shift_northwest_pixels_13"),
	A_WalkSoutheastPixels(1),
	A_Jmp(["ACTION_787_shift_northwest_pixels_13"])
])
