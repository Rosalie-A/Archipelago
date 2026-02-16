#A0602_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_PLAYER_OUTER
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
	A_ClearSolidityBits(cant_pass_walls=True),
	A_ClearBit(TEMP_7043_0),
	A_SetVarToConst(X_COORD_2, 4608),
	A_SetVarToConst(Y_COORD_2, 13568),
	A_SetVarToConst(Z_COORD_2, 0),
	A_UnknownCommand(bytearray(b'\x99')),
	A_SetAllSpeeds(NORMAL),
	A_VisibilityOn(),
	A_WalkNortheastSteps(6),
	A_Walk1StepNorth(),
	A_WalkNorthwestSteps(4),
	A_WalkNorthSteps(2),
	A_WalkNorthwestSteps(4),
	A_WalkSouthwestSteps(3),
	A_WalkSouthSteps(2),
	A_WalkSoutheastSteps(3),
	A_Walk1StepSouth(),
	A_WalkSouthwestSteps(3),
	A_Walk1StepWest(),
	A_WalkNorthwestSteps(2),
	A_Walk1StepNorth(),
	A_WalkNorthwestSteps(3),
	A_WalkSouthwestSteps(2),
	A_SetBit(TEMP_7043_0),
	A_Walk1StepSouthwest(),
	A_ReturnQueue()
])
