#A0727_MAGMITES
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
	A_JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_727_set_animation_speed_11"], identifier="ACTION_727_jmp_if_var_equals_const_0"),
	A_Pause(40, identifier="ACTION_727_pause_1"),
	A_JmpIfRandom1of2(["ACTION_727_pause_1"]),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(SLOW),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_727_pause_1"]),
	A_Walk1StepFDirection(),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_FaceMario(),
	A_Jmp(["ACTION_727_pause_1"]),
	A_SetSequenceSpeed(FASTEST, identifier="ACTION_727_set_animation_speed_11"),
	A_SetWalkingSpeed(NORMAL),
	A_Walk1StepFDirection(),
	A_JumpToHeight(height=0, silent=True),
	A_FaceMario(),
	A_JmpIfRandom2of3(['ACTION_727_turn_clockwise_45_degrees_n_times_18', 'ACTION_727_turn_clockwise_45_degrees_n_times_20']),
	A_Jmp(["ACTION_727_pause_1"]),
	A_TurnClockwise45DegreesNTimes(1, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_18"),
	A_Jmp(["ACTION_727_pause_1"]),
	A_TurnClockwise45DegreesNTimes(7, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_20"),
	A_Jmp(["ACTION_727_pause_1"])
])
