#A0959_FINAL_FACTORY_ROOM_MASS_PRODUCED_NPC_PICKED_UP
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
	A_SetWalkingSpeed(FASTEST, identifier="ACTION_959_set_animation_speed_0"),
	A_ShadowOn(),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkWestPixels(4),
	A_SetWalkingSpeed(SLOW),
	A_SetBit(TEMP_7044_1),
	A_WalkNorthSteps(2),
	A_WalkNorthPixels(8),
	A_JmpIfBitSet(TEMP_7044_0, ["ACTION_959_shift_z_up_steps_11"], identifier="ACTION_959_jmp_if_bit_set_8"),
	A_Pause(1),
	A_Jmp(["ACTION_959_jmp_if_bit_set_8"]),
	A_ShiftZUpSteps(3, identifier="ACTION_959_shift_z_up_steps_11"),
	A_WalkToXYCoords(x=3, y=88),
	A_ShadowOff(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSoutheastPixels(8),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZDownSteps(3),
	A_Pause(12),
	A_ClearBit(TEMP_7044_0),
	A_ClearBit(TEMP_7044_1),
	A_WalkToXYCoords(x=10, y=103),
	A_ShiftToXYCoords(x=1, y=77),
	A_JmpIfBitSet(TEMP_7044_2, ["ACTION_959_ret_25"]),
	A_Jmp(["ACTION_959_set_animation_speed_0"]),
	A_ReturnQueue(identifier="ACTION_959_ret_25")
])
