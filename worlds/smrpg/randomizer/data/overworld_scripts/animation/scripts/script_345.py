#A0345_SHIP_1ST_WATER_ROOM_FISH
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_345_set_animation_speed_0"),
	A_Inc(TEMP_702C),
	A_CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_700C),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_345_shift_f_direction_steps_6"]),
	A_SetWalkingSpeed(NORMAL),
	A_WalkFDirectionSteps(2, identifier="ACTION_345_shift_f_direction_steps_6"),
	A_Inc(TEMP_702C),
	A_CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_700C),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_345_face_mario_13"]),
	A_TurnRandomDirection(),
	A_Jmp(["ACTION_345_set_animation_speed_0"]),
	A_FaceMario(identifier="ACTION_345_face_mario_13"),
	A_Jmp(["ACTION_345_set_animation_speed_0"])
])
