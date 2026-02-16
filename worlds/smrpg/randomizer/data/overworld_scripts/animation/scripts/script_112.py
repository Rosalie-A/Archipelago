#A0112_MK_HALL_TOAD
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
	A_SetSequenceSpeed(FAST),
	A_VisibilityOff(),
	A_Pause(30, identifier="ACTION_112_pause_2"),
	A_ClearBit(TEMP_7043_1),
	A_VisibilityOn(),
	A_WalkSoutheastSteps(9),
	A_VisibilityOff(),
	A_Pause(150),
	A_SetBit(TEMP_7043_2),
	A_Pause(100),
	A_VisibilityOn(),
	A_WalkNorthwestSteps(9),
	A_VisibilityOff(),
	A_ClearBit(TEMP_7043_2),
	A_Pause(1, identifier="ACTION_112_pause_14"),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_112_pause_2"]),
	A_Jmp(["ACTION_112_pause_14"])
])
