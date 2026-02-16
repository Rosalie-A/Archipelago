#A0829_KEEP_XY_PLATFORMS
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
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetPriority(3),
	A_SetWalkingSpeed(NORMAL),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 28, ["ACTION_829_shift_f_direction_steps_9"]),
	A_WalkFDirectionSteps(8, identifier="ACTION_829_shift_f_direction_steps_5"),
	A_Pause(16),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_829_shift_f_direction_steps_5"]),
	A_WalkFDirectionSteps(2, identifier="ACTION_829_shift_f_direction_steps_9"),
	A_Pause(4),
	A_TurnClockwise45DegreesNTimes(6),
	A_Jmp(["ACTION_829_shift_f_direction_steps_9"])
])
