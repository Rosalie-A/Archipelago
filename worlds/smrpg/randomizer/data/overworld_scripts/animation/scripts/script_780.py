#A0780_LANDS_END_WHIRLPOOLS
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
	A_FixedFCoordOn(),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(NORMAL),
	A_Pause(1, identifier="ACTION_780_pause_5"),
	A_JmpIfBitClear(TEMP_7044_5, ["ACTION_780_pause_5"]),
	A_SetPriority(3),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 319, ["ACTION_780_object_memory_modify_bits_44"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 403, ["ACTION_780_object_memory_modify_bits_44"]),
	A_Set700CToPressedButton(),
	A_DecVarFrom700C(SECONDARY_TEMP_7024),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_780_face_south_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_780_face_southwest_17"]),
	A_FaceNorth(),
	A_Jmp(["ACTION_780_jmp_if_bit_clear_39"]),
	A_FaceSouthwest(identifier="ACTION_780_face_southwest_17"),
	A_Jmp(["ACTION_780_jmp_if_bit_clear_30"]),
	A_FaceSouth(identifier="ACTION_780_face_south_19"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_780_set_animation_speed_24"], identifier="ACTION_780_jmp_if_bit_clear_20"),
	A_SetWalkingSpeed(FAST),
	A_ClearSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_Jmp(["ACTION_780_walk_1_step_f_direction_26"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_780_set_animation_speed_24"),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_26"),
	A_TurnClockwise45DegreesNTimes(7),
	A_WalkFDirectionSteps(2),
	A_TurnClockwise45DegreesNTimes(6),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_780_set_animation_speed_34"], identifier="ACTION_780_jmp_if_bit_clear_30"),
	A_SetWalkingSpeed(FAST),
	A_ClearSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_Jmp(["ACTION_780_shift_f_direction_steps_36"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_780_set_animation_speed_34"),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_WalkFDirectionSteps(2, identifier="ACTION_780_shift_f_direction_steps_36"),
	A_TurnClockwise45DegreesNTimes(7),
	A_Walk1StepFDirection(),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_780_pause_42"], identifier="ACTION_780_jmp_if_bit_clear_39"),
	A_Pause(24),
	A_Jmp(["ACTION_780_jmp_if_bit_clear_20"]),
	A_Pause(96, identifier="ACTION_780_pause_42"),
	A_Jmp(["ACTION_780_jmp_if_bit_clear_20"]),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6], identifier="ACTION_780_object_memory_modify_bits_44"),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_Set700CToPressedButton(),
	A_Compare700CToVar(TEMP_7026),
	A_JmpIfLoadedMemoryIs0(["ACTION_780_set_animation_speed_53"]),
	A_SetWalkingSpeed(SLOW),
	A_TurnClockwise45Degrees(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_780_object_memory_modify_bits_44"]),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_780_set_animation_speed_53"),
	A_FaceMario(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_780_set_animation_speed_67"]),
	A_JmpIfRandom2of3(['ACTION_780_turn_clockwise_45_degrees_n_times_60', 'ACTION_780_turn_clockwise_45_degrees_n_times_63']),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(8),
	A_Jmp(["ACTION_780_walk_1_step_f_direction_65"]),
	A_TurnClockwise45DegreesNTimes(4, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_60"),
	A_Pause(8),
	A_Jmp(["ACTION_780_walk_1_step_f_direction_65"]),
	A_TurnClockwise45DegreesNTimes(6, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_63"),
	A_Pause(8),
	A_Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_65"),
	A_Jmp(["ACTION_780_object_memory_modify_bits_44"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_780_set_animation_speed_67"),
	A_TurnClockwise45DegreesNTimes(4),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(4),
	A_Pause(4),
	A_JmpIfRandom2of3(['ACTION_780_turn_clockwise_45_degrees_n_times_75', 'ACTION_780_turn_clockwise_45_degrees_n_times_77']),
	A_TurnClockwise45DegreesNTimes(3),
	A_Jmp(["ACTION_780_walk_1_step_f_direction_78"]),
	A_TurnClockwise45DegreesNTimes(4, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_75"),
	A_Jmp(["ACTION_780_walk_1_step_f_direction_78"]),
	A_TurnClockwise45DegreesNTimes(5, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_77"),
	A_Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_78"),
	A_Jmp(["ACTION_780_object_memory_modify_bits_44"])
])
