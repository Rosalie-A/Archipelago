#A0045_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_PATH
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
	A_VisibilityOn(),
	A_Pause(117),
	A_JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["ACTION_45_reset_properties_13"]),
	A_JumpToHeight(108),
	A_WalkSouthwestSteps(2),
	A_SetBit(MIDAS_RIVER_TUNNEL_4_PRIZE),
	A_StartLoopNTimes(4),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ReturnQueue(),
	A_ResetProperties(identifier="ACTION_45_reset_properties_13"),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FASTER),
	A_Walk1StepEast(),
	A_Walk1StepWest(),
	A_Jmp(["ACTION_45_reset_properties_13"])
])
