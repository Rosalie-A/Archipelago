#A0594_MIDAS_BARREL_RIGHT_LANE_TO_LEFT
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
	A_SetAllSpeeds(FAST),
	A_WalkSouthwestSteps(11),
	A_SetBit(TEMP_7044_5),
	A_WalkSouthwestSteps(2),
	A_ClearBit(TEMP_7044_5),
	A_SetBit(TEMP_7044_7),
	A_Pause(2),
	A_Walk1StepNorthwest(),
	A_Walk1StepNorthwest(),
	A_Walk1StepSouthwest(identifier="ACTION_594_walk_1_step_southwest_9"),
	A_Jmp(["ACTION_594_walk_1_step_southwest_9"])
])
