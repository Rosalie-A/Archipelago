#A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE
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
	A_VisibilityOff(),
	A_TransferToXYZF(x=7, y=18, z=6, direction=EAST),
	A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
	A_SetPriority(3),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_FaceMario(),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_299_set_var_to_random_66"]),
	A_SetBit(TEMP_7043_1),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_299_jmp_if_bit_set_23"], identifier="ACTION_299_jmp_if_var_equals_const_10"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_299_jmp_if_bit_set_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_299_jmp_if_bit_set_35"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_299_jmp_if_bit_set_29"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_299_jmp_if_bit_set_41"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_299_jmp_if_bit_set_41"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_299_jmp_if_bit_set_23"]),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_299_clear_bit_47"], identifier="ACTION_299_jmp_if_bit_set_17"),
	A_SetBit(TEMP_7043_1),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(height=64, silent=True),
	A_WalkSouthwestPixels(48),
	A_Jmp(["ACTION_299_set_priority_62"]),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_299_clear_bit_50"], identifier="ACTION_299_jmp_if_bit_set_23"),
	A_SetBit(TEMP_7043_2),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(height=64, silent=True),
	A_WalkSoutheastPixels(48),
	A_Jmp(["ACTION_299_set_priority_62"]),
	A_JmpIfBitSet(TEMP_7043_3, ["ACTION_299_clear_bit_53"], identifier="ACTION_299_jmp_if_bit_set_29"),
	A_SetBit(TEMP_7043_3),
	A_SetWalkingSpeed(FASTER),
	A_JumpToHeight(height=64, silent=True),
	A_WalkWestPixels(72),
	A_Jmp(["ACTION_299_set_priority_62"]),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_299_clear_bit_56"], identifier="ACTION_299_jmp_if_bit_set_35"),
	A_SetBit(TEMP_7043_4),
	A_JumpToHeight(height=80, silent=True),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthPixels(36),
	A_Jmp(["ACTION_299_set_priority_62"]),
	A_JmpIfBitSet(TEMP_7043_5, ["ACTION_299_clear_bit_59"], identifier="ACTION_299_jmp_if_bit_set_41"),
	A_SetBit(TEMP_7043_5),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(height=64, silent=True),
	A_WalkNorthwestPixels(48),
	A_Jmp(["ACTION_299_set_priority_62"]),
	A_ClearBit(TEMP_7043_1, identifier="ACTION_299_clear_bit_47"),
	A_JmpIfRandom1of2(["ACTION_299_jmp_if_bit_set_35"]),
	A_Jmp(["ACTION_299_jmp_if_bit_set_29"]),
	A_ClearBit(TEMP_7043_2, identifier="ACTION_299_clear_bit_50"),
	A_JmpIfRandom1of2(["ACTION_299_jmp_if_bit_set_17"]),
	A_Jmp(["ACTION_299_jmp_if_bit_set_35"]),
	A_ClearBit(TEMP_7043_3, identifier="ACTION_299_clear_bit_53"),
	A_JmpIfRandom1of2(["ACTION_299_jmp_if_bit_set_41"]),
	A_Jmp(["ACTION_299_jmp_if_bit_set_17"]),
	A_ClearBit(TEMP_7043_4, identifier="ACTION_299_clear_bit_56"),
	A_JmpIfRandom1of2(["ACTION_299_jmp_if_bit_set_17"]),
	A_Jmp(["ACTION_299_jmp_if_bit_set_23"]),
	A_ClearBit(TEMP_7043_5, identifier="ACTION_299_clear_bit_59"),
	A_JmpIfRandom1of2(["ACTION_299_jmp_if_bit_set_29"]),
	A_Jmp(["ACTION_299_jmp_if_bit_set_17"]),
	A_SetPriority(2, identifier="ACTION_299_set_priority_62"),
	A_Pause(1, identifier="ACTION_299_pause_63"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_299_pause_63"]),
	A_Jmp(["ACTION_302_pause_0"]),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 8, identifier="ACTION_299_set_var_to_random_66"),
	A_Jmp(["ACTION_299_jmp_if_var_equals_const_10"])
])
