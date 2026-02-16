#A0270_SHIP_BLOOBER
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
	A_SetPriority(3),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_270_set_animation_speed_2"),
	A_SequencePlaybackOff(),
	A_ShiftZDownSteps(5),
	A_FaceMario(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032),
	A_SequencePlaybackOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetWalkingSpeed(FAST),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(39),
	A_ShiftZUpPixels(2),
	A_WalkFDirectionPixels(1),
	A_EndLoop(),
	A_Jmp(["ACTION_270_set_animation_speed_2"])
])
