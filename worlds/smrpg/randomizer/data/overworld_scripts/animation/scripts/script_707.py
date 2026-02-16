#A0707_BOOSTER_HILL_HENCHMAN
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
	A_SetPriority(2, identifier="ACTION_707_set_priority_0"),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(FASTER),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="hill_sprite_set_1"),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_WalkNorthwestSteps(6),
	A_SequenceLoopingOn(),
	A_FixedFCoordOn(),
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 60, identifier="ACTION_707_set_var_to_random_10"),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 30),
	A_JmpIfComparisonResultIsLesser(["ACTION_707_jmp_if_bit_set_24"]),
	A_LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_707_load_mem_13"),
	A_Pause(1),
	A_EndLoop(),
	A_JmpIfBitSet(TEMP_7043_3, ["ACTION_707_jmp_if_bit_set_24"]),
	A_SetWalkingSpeed(VERY_SLOW),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="hill_sprite_set_2"),
	A_WalkNorthwestPixels(8),
	A_WalkSoutheastPixels(8),
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
	A_Jmp(["ACTION_707_set_var_to_random_10"]),
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"], identifier="ACTION_707_jmp_if_bit_set_24"),
	A_JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_707_load_mem_13"]),
	A_Inc(TEMP_70AE),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
	A_JumpToHeight(56),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False, identifier="hill_sprite_set_3"),
	A_Pause(32),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="hill_sprite_set_4"),
	A_SetSequenceSpeed(FAST),
	A_WalkNorthwestSteps(6),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="hill_sprite_set_5"),
	A_WalkSoutheastSteps(3),
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_707_shift_southeast_steps_42"]),
	A_Dec(TEMP_70AE),
	A_WalkSoutheastSteps(3),
	A_Jmp(["ACTION_707_set_var_to_random_10"]),
	A_WalkSoutheastSteps(3, identifier="ACTION_707_shift_southeast_steps_42"),
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_707_set_animation_speed_43"),
	A_SetWalkingSpeed(SLOW),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Walk1StepSoutheast(identifier="ACTION_707_walk_1_step_southeast_46"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_707_walk_1_step_southeast_46"]),
	A_ReturnQueue()
])
