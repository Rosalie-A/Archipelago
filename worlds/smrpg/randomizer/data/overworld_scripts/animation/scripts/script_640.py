#A0640_MIDAS_2ND_TUNNELS_PIRANHA
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
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SequenceLoopingOn(),
	A_FixedFCoordOn(),
	A_StartLoopNTimes(5),
	A_SetAllSpeeds(NORMAL),
	A_Walk1StepNortheast(),
	A_SetSequenceSpeed(FAST),
	A_JumpToHeight(56),
	A_Pause(16),
	A_JumpToHeight(56),
	A_Pause(16),
	A_SetSequenceSpeed(NORMAL),
	A_Walk1StepSouthwest(),
	A_EndLoop(),
	A_SetAllSpeeds(FAST),
	A_Walk1StepNortheast(),
	A_Pause(1, identifier="ACTION_640_pause_17"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_640_pause_17"]),
	A_SetAllSpeeds(VERY_FAST),
	A_Walk1StepSouthwest(),
	A_StartLoopNTimes(7),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_EndLoop(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(VERY_FAST),
	A_StartLoopNTimes(5),
	A_JumpToHeight(56),
	A_Walk1StepNortheast(),
	A_JumpToHeight(56),
	A_Walk1StepSouthwest(),
	A_EndLoop(),
	A_WalkNortheastSteps(5),
	A_Walk1StepEast(),
	A_ReturnQueue()
])
