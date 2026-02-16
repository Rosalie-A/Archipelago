#A0818_LANDS_END_CHOW_JUMP_OUT_OF_PIT
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
	A_VisibilityOn(),
	A_SetAllSpeeds(FAST),
	A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
	A_JumpToHeight(128),
	A_Walk1StepFDirection(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Pause(1, identifier="ACTION_818_pause_6"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_818_pause_6"]),
	A_Set700CToPressedButton(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_818_set_solidity_bits_11"]),
	A_SetBit(TEMP_7044_7),
	A_SetSolidityBits(cant_walk_under=True, identifier="ACTION_818_set_solidity_bits_11"),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetPriority(3),
	A_JmpIfRandom1of2(["ACTION_818_set_animation_speed_19"], identifier="ACTION_818_jmp_if_random_above_128_14"),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_818_set_animation_speed_15"),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_818_jmp_if_random_above_128_14"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_818_set_animation_speed_19"),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_818_set_animation_speed_15"])
])
