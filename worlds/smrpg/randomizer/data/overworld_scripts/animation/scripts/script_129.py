#A0129_WALLET_TOAD_OCCUPIED
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
	A_SetSequenceSpeed(FAST, identifier="ACTION_129_set_animation_speed_0"),
	A_WalkSouthwestPixels(22),
	A_Walk1StepSouthwest(),
	A_Walk1StepSoutheast(),
	A_Walk1StepSoutheast(),
	A_WalkSoutheastPixels(11),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(22),
	A_WalkNorthwestPixels(11),
	A_WalkNorthwestSteps(2),
	A_Walk1StepSouthwest(),
	A_FaceSoutheast(),
	A_Pause(1, identifier="ACTION_129_pause_12"),
	A_JmpIfBitSet(TEMP_7044_5, ["ACTION_129_set_animation_speed_0"]),
	A_Jmp(["ACTION_129_pause_12"])
])
