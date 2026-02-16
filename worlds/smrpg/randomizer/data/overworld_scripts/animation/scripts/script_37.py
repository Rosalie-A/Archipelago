#A0037_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_GOOMBETTE
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
	A_SequenceLoopingOn(),
	A_Pause(40),
	A_WalkSoutheastSteps(2),
	A_SetAllSpeeds(FAST),
	A_JumpToHeight(96),
	A_WalkSoutheastSteps(3),
	A_SetAllSpeeds(NORMAL),
	A_FixedFCoordOn(),
	A_Walk1StepEast(),
	A_FixedFCoordOff(),
	A_Walk1StepNortheast(),
	A_SetAllSpeeds(FAST),
	A_StartLoopNTimes(1),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_EndLoop(),
	A_SetBit(TEMP_7043_2),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetAllSpeeds(FAST),
	A_Walk1StepWest(),
	A_JumpToHeight(96),
	A_WalkNorthwestSteps(3),
	A_SetAllSpeeds(NORMAL),
	A_WalkNorthwestSteps(4),
	A_PlaySound(sound=SO065_THWOMP_STOMP, channel=4),
	A_SetSequenceSpeed(SLOW),
	A_SetSpriteSequence(index=2, looping=False),
	A_Pause(40),
	A_SetSequenceSpeed(NORMAL),
	A_WalkWestSteps(3),
	A_WalkNorthwestSteps(2),
	A_SetAllSpeeds(FAST),
	A_JumpToHeight(96),
	A_WalkNorthwestSteps(3),
	A_SetAllSpeeds(NORMAL),
	A_WalkNorthwestSteps(2),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_WalkNorthwestSteps(2),
	A_SetPriority(3),
	A_Walk1StepNorthwest(),
	A_SetBit(TEMP_7043_3),
	A_ReturnQueue()
])
