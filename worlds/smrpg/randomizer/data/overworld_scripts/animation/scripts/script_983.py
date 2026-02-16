#A0983_DREAM_CUSHION_CHEF
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
	A_Pause(90),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_WalkSouthwestSteps(3, identifier="ACTION_983_shift_southwest_steps_3"),
	A_Pause(30),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_Pause(40),
	A_ResetProperties(),
	A_SetSequenceSpeed(FAST),
	A_WalkNortheastSteps(3),
	A_Pause(90),
	A_Jmp(["ACTION_983_shift_southwest_steps_3"])
])
