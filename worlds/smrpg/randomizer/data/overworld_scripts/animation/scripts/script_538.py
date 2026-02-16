#A0538_RIGHT_GOOMBA_IN_MUSHROOM_WAY_2
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
	A_SetBit(TEMP_7044_5),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSoutheastSteps(7),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(1),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_WalkSoutheastSteps(1),
	A_Pause(60),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNorthwestSteps(9),
	A_Pause(5),
	A_ClearBit(TEMP_7044_5),
	A_ReturnQueue()
])
