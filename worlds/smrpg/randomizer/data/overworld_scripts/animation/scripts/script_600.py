#A0600_MIDAS_RIVER_MID_RIGHT_TUNNEL_PLAYER_OUTER
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
	A_SetVarToConst(X_COORD_2, 8448),
	A_SetVarToConst(Y_COORD_2, 8832),
	A_SetVarToConst(Z_COORD_2, 0),
	A_UnknownCommand(bytearray(b'\x99')),
	A_SetAllSpeeds(NORMAL),
	A_VisibilityOn(),
	A_WalkNorthwestSteps(4),
	A_WalkNorthSteps(2),
	A_WalkNortheastSteps(3),
	A_WalkSoutheastSteps(8),
	A_ClearBit(TEMP_7043_5),
	A_WalkSouthSteps(2),
	A_WalkSoutheastSteps(2),
	A_Walk1StepEast(),
	A_WalkNortheastSteps(2),
	A_WalkSoutheastSteps(4),
	A_WalkNortheastSteps(4),
	A_Walk1StepEast(),
	A_Walk1StepSoutheast(),
	A_WalkSouthSteps(2),
	A_Walk1StepSouthwest(),
	A_SetBit(TEMP_7043_0),
	A_Walk1StepSouthwest(),
	A_ReturnQueue()
])
