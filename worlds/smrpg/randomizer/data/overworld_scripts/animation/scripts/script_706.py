#A0706_MOLEVILLE_LIBERATED_ENTRANCE_MOLE
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
	A_SetAllSpeeds(SLOW),
	A_WalkFDirectionSteps(2, identifier="ACTION_706_shift_f_direction_steps_2"),
	A_Pause(20),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(20),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(8),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(20),
	A_TurnClockwise45DegreesNTimes(6),
	A_Jmp(["ACTION_706_shift_f_direction_steps_2"])
])
