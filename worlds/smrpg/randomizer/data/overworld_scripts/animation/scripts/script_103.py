#A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START
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
	A_ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_103_clear_solidity_bits_0"),
	A_FloatingOff(),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpPixels(9),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_103_set_animation_speed_5"),
	A_ShiftZUpPixels(5),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(3),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_103_set_animation_speed_9"),
	A_ShiftZUpPixels(2),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZUpPixels(1),
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_103_set_animation_speed_15"),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZDownPixels(2),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(3),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_103_set_animation_speed_23"),
	A_ShiftZDownPixels(5),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownPixels(9),
	A_JmpIfBitSet(TEMP_7043_5, ["ACTION_103_ret_29"]),
	A_Jmp(["ACTION_103_clear_solidity_bits_0"]),
	A_ReturnQueue(identifier="ACTION_103_ret_29")
])
