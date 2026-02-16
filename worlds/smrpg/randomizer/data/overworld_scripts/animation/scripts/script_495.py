#A0495_FAST_SPINY
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
	A_SetBit(TEMP_7043_1),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_VisibilityOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthwestSteps(3),
	A_VisibilityOff(),
	A_ShiftToXYCoords(x=19, y=85),
	A_Pause(96),
	A_ClearBit(TEMP_7043_1),
	A_ReturnQueue()
])
