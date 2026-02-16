#A0131_EAST_GUARD_OCCUPIED
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
	A_SetPriority(3, identifier="ACTION_131_set_priority_0"),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(5),
	A_Pause(1, identifier="ACTION_131_pause_3"),
	A_JmpIfBitSet(TEMP_7044_4, ["ACTION_131_shift_northwest_steps_6"]),
	A_Jmp(["ACTION_131_pause_3"]),
	A_WalkNorthwestSteps(5, identifier="ACTION_131_shift_northwest_steps_6"),
	A_Pause(1, identifier="ACTION_131_pause_7"),
	A_JmpIfBitSet(TEMP_7044_3, ["ACTION_131_set_priority_0"]),
	A_Jmp(["ACTION_131_pause_7"])
])
