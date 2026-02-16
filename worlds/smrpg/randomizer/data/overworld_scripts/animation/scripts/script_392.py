#A0392_SLEEPING_WIGGLER_CAMERA
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
	A_SetWalkingSpeed(FAST, identifier="ACTION_392_set_animation_speed_0"),
	A_WalkNorthPixels(5),
	A_WalkSouthPixels(10),
	A_WalkNorthPixels(5),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_392_ret_6"]),
	A_Jmp(["ACTION_392_set_animation_speed_0"]),
	A_ReturnQueue(identifier="ACTION_392_ret_6")
])
