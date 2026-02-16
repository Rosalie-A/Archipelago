#A0281_KEEP_TOPPER_GAME_SET_BUTTON_OR_BALL_STATE
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
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65515),
	A_SetVarToConst(TEMP_7026, 1),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_281_copy_var_to_var_7"]),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_VarShiftLeft(TEMP_7026, 255),
	A_EndLoop(),
	A_CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C, identifier="ACTION_281_copy_var_to_var_7"),
	A_Mem700CAndVar(TEMP_7026),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 0),
	A_JmpIfLoadedMemoryIsNot0(["ACTION_281_jmp_to_subroutine_18"]),
	A_JmpToSubroutine(["ACTION_281_copy_var_to_var_25"]),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(1),
	A_ReturnQueue(),
	A_JmpToSubroutine(["ACTION_281_copy_var_to_var_25"], identifier="ACTION_281_jmp_to_subroutine_18"),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(1),
	A_ReturnQueue(),
	A_CopyVarToVar(from_var=ROSE_WAY_703C, to_var=PRIMARY_TEMP_700C, identifier="ACTION_281_copy_var_to_var_25"),
	A_Mem700CAndVar(TEMP_7026),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
	A_Mem700CAndVar(TEMP_7026),
	A_Compare700CToVar(TEMP_7028),
	A_JmpIfLoadedMemoryIs0(["ACTION_281_ret_33"]),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_ReturnQueue(identifier="ACTION_281_ret_33")
])
