#A0982_DREAM_CUSHION_CHEF
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
	A_Pause(120),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(3, identifier="ACTION_982_shift_southeast_steps_3"),
	A_FaceNortheast(),
	A_Pause(60),
	A_WalkNorthwestSteps(3),
	A_FaceNortheast(),
	A_Pause(60),
	A_Jmp(["ACTION_982_shift_southeast_steps_3"])
])
