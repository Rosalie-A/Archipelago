#A0109_MK_HALL_REPEATING_HENCHMEN_STARTING
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
	A_SetPriority(3),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpPixels(20),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpPixels(10),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(2),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZDownPixels(2),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZDownPixels(10),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownPixels(20),
	A_Pause(2),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetWalkingSpeed(FASTEST, identifier="ACTION_109_set_animation_speed_28"),
	A_ShiftZUpPixels(20),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpPixels(10),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(2),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZDownPixels(2),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZDownPixels(10),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownPixels(20),
	A_Pause(2),
	A_Jmp(["ACTION_109_set_animation_speed_28"])
])
