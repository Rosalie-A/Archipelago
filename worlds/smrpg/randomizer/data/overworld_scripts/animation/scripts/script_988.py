#A0988_SMITHY_COMPONENT
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
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_988_set_animation_speed_3"]),
	A_TransferXYZFPixels(x=252, y=6, z=30, direction=NORTHEAST),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_988_set_animation_speed_3"),
	A_ShiftZDownPixels(1),
	A_Pause(8),
	A_ShiftZDownPixels(1),
	A_Pause(12),
	A_ShiftZUpPixels(1),
	A_Pause(8),
	A_ShiftZUpPixels(1),
	A_Pause(12),
	A_JmpIfBitSet(TEMP_7043_5, ["ACTION_988_ret_14"]),
	A_Jmp(["ACTION_988_set_animation_speed_3"]),
	A_ReturnQueue(identifier="ACTION_988_ret_14")
])
