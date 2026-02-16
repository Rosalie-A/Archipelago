#A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK
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
	A_ClearBit(TEMP_7042_0),
	A_ClearBit(TEMP_7042_1),
	A_ClearBit(TEMP_7042_2),
	A_ClearBit(TEMP_7042_3),
	A_ClearBit(TEMP_7042_4),
	A_ClearBit(TEMP_7042_5),
	A_ClearBit(TEMP_7042_7),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestSteps(2),
	A_WalkNortheastSteps(3),
	A_WalkNorthwestSteps(4),
	A_WalkSouthwestSteps(2),
	A_FaceSoutheast(),
	A_SetSequenceSpeed(SLOW),
	A_ClearBit(TEMP_7043_1),
	A_ReturnQueue()
])
