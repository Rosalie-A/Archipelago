#A0266_SEA_SHORE_BLOOBER
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
	A_SetMovementsBits(bit_0=True, cant_walk_under=True),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_266_set_animation_speed_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_266_pause_8"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_266_pause_7"]),
	A_Pause(3),
	A_Pause(3, identifier="ACTION_266_pause_7"),
	A_Pause(3, identifier="ACTION_266_pause_8"),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_266_set_animation_speed_9"),
	A_SequencePlaybackOff(),
	A_ShiftZDownSteps(4),
	A_FaceMario(),
	A_SequencePlaybackOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetWalkingSpeed(FAST),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(31),
	A_ShiftZUpPixels(2),
	A_WalkFDirectionPixels(1),
	A_EndLoop(),
	A_Jmp(["ACTION_266_set_animation_speed_9"])
])
