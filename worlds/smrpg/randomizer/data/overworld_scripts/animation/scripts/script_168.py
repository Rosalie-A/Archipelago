#A0168_BANDITS_WAY_3_CHOW
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
	A_SetPriority(3, identifier="ACTION_168_set_priority_0"),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(identifier="ACTION_168_sequence_looping_on_2"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNorthwestPixels(8),
	A_Pause(20),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(SLOW),
	A_JumpToHeight(height=36, silent=True),
	A_WalkSoutheastPixels(8),
	A_Pause(25),
	A_Jmp(["ACTION_168_sequence_looping_on_2"])
])
