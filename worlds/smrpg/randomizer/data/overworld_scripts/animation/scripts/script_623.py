#A0623_SMALL_EXPLOSION_FLASH_7_TIMES
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
	A_VisibilityOff(),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetWalkingSpeed(FASTEST),
	A_WalkWestPixels(20),
	A_ShiftZUpPixels(8),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_StartLoopNTimes(7),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(3),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestPixels(3),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestSteps(2),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthwestSteps(4),
	A_VisibilityOff(),
	A_ReturnQueue()
])
