#A0038_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_LAKITU
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
	A_SequenceLoopingOn(),
	A_ShadowOff(),
	A_SetPriority(3),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
	A_WalkEastPixels(8),
	A_FaceSouthwest(),
	A_StartLoopNTimes(2),
	A_Pause(15),
	A_SetWalkingSpeed(FAST),
	A_SetBit(TEMP_7043_1),
	A_ShiftZUpPixels(10),
	A_ShiftZDownPixels(10),
	A_Pause(20),
	A_EndLoop(),
	A_Pause(30),
	A_SetBit(TEMP_7043_4),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(60),
	A_SetAllSpeeds(NORMAL),
	A_FixedFCoordOn(),
	A_WalkWestSteps(4),
	A_SetAllSpeeds(FAST),
	A_WalkNorthwestSteps(6),
	A_WalkNorthSteps(2),
	A_SetBit(TEMP_7043_4),
	A_SetSpriteSequence(index=3, looping=False),
	A_ReturnQueue()
])
