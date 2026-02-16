#A0713_LANDS_END_SHOGUN
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
	A_SequenceLoopingOn(),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 319, ["ACTION_713_pause_33"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 403, ["ACTION_713_pause_33"]),
	A_SetPriority(3),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_713_set_animation_speed_8"], identifier="ACTION_713_jmp_if_bit_set_6"),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_SetAllSpeeds(FAST, identifier="ACTION_713_set_animation_speed_8"),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_SetAllSpeeds(NORMAL),
	A_ClearBit(TEMP_7043_1),
	A_ClearSolidityBits(cant_walk_through=True),
	A_VisibilityOff(),
	A_SetVarToConst(TEMP_70AE, 0),
	A_Pause(56),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 8),
	A_Inc(PRIMARY_TEMP_700C),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(8),
	A_EndLoop(),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_SetAllSpeeds(FAST),
	A_SetBit(TEMP_7043_1),
	A_ClearBit(TEMP_7043_4),
	A_VisibilityOn(),
	A_SetSolidityBits(cant_walk_through=True),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_SetAllSpeeds(NORMAL),
	A_Pause(100),
	A_Jmp(["ACTION_713_jmp_if_bit_set_6"]),
	A_Pause(1, identifier="ACTION_713_pause_33"),
	A_JmpIfBitClear(TEMP_7044_5, ["ACTION_713_pause_33"]),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_713_set_animation_speed_37"], identifier="ACTION_713_jmp_if_bit_set_35"),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_SetAllSpeeds(FAST, identifier="ACTION_713_set_animation_speed_37"),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_SetAllSpeeds(NORMAL),
	A_ClearBit(TEMP_7043_1),
	A_ClearSolidityBits(cant_walk_through=True),
	A_VisibilityOff(),
	A_SetVarToConst(TEMP_70AE, 0),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 32768),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7034),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 16384),
	A_JmpIfComparisonResultIsLesser(["ACTION_713_set_var_to_const_51"]),
	A_SetVarToConst(PRIMARY_TEMP_700C, 1),
	A_Jmp(["ACTION_713_add_short_mem_to_700C_52"]),
	A_SetVarToConst(PRIMARY_TEMP_700C, 0, identifier="ACTION_713_set_var_to_const_51"),
	A_AddVarTo700C(SECONDARY_TEMP_7024, identifier="ACTION_713_add_short_mem_to_700C_52"),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7026),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetBit(TEMP_7044_4),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_UnknownCommand(bytearray(b'\x97\x11')),
	A_ClearBit(TEMP_7044_4),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_700C),
	A_DecVarFrom700C(SECONDARY_TEMP_7024),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_713_set_object_memory_bits_66"]),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	A_Jmp(["ACTION_713_pause_67"]),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0], identifier="ACTION_713_set_object_memory_bits_66"),
	A_Pause(1, identifier="ACTION_713_pause_67"),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_SetAllSpeeds(FAST),
	A_SetBit(TEMP_7043_1),
	A_ClearBit(TEMP_7043_4),
	A_SetSolidityBits(cant_walk_through=True),
	A_VisibilityOn(),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_SetAllSpeeds(NORMAL),
	A_Pause(100),
	A_Jmp(["ACTION_713_jmp_if_bit_set_35"])
])
