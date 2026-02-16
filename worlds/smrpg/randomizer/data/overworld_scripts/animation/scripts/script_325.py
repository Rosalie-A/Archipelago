#A0325_INVISIBLE_ITEM_SHIFT_2
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
	A_SetWalkingSpeed(NORMAL),
	A_WalkSoutheastSteps(2),
	A_FaceNortheast(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(30),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(VERY_FAST),
	A_StartLoopNTimes(1),
	A_WalkNortheastPixels(4),
	A_WalkSouthwestPixels(4),
	A_Pause(20),
	A_EndLoop(),
	A_Pause(74),
	A_FaceSoutheast(),
	A_FixedFCoordOff(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkSoutheastSteps(1),
	A_WalkNortheastSteps(4),
	A_VisibilityOff(),
	A_FaceSouthwest(),
	A_Pause(180),
	A_VisibilityOn(),
	A_WalkSouthwestSteps(4),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_FaceNortheast(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(30),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(VERY_FAST),
	A_StartLoopNTimes(1),
	A_WalkNortheastPixels(4),
	A_WalkSouthwestPixels(4),
	A_Pause(20),
	A_EndLoop(),
	A_Pause(74),
	A_FaceSoutheast(),
	A_FixedFCoordOff(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepSoutheast(),
	A_TransferToXYZF(x=6, y=88, z=0, direction=EAST),
	A_ReturnQueue()
])
