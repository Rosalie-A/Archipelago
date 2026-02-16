#A1003_KEEP_ORIGINAL_THRONE_ROOM_TROOPA
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
	A_SetSequenceSpeed(FAST, identifier="ACTION_1003_set_animation_speed_0"),
	A_SetWalkingSpeed(FAST),
	A_WalkSoutheastPixels(8),
	A_WalkSoutheastSteps(2),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSoutheastSteps(1),
	A_FaceNorthwest(),
	A_Pause(10),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(FAST),
	A_WalkNorthwestSteps(2),
	A_WalkNorthwestPixels(8),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestSteps(1),
	A_FaceSoutheast(),
	A_Pause(10),
	A_Jmp(["ACTION_1003_set_animation_speed_0"])
])
