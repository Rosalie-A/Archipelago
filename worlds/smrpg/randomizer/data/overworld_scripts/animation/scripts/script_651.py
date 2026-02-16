#A0651_MOKURA_PACKET

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
	A_JmpIfVarEqualsConst(TEMP_7034, 65535, ["ACTION_651_set_priority_22"]),
	A_JmpIfVarEqualsConst(TEMP_7034, 61166, ["ACTION_651_visibility_off_19"]),
	A_JmpIfVarEqualsConst(TEMP_7034, 56797, ["ACTION_651_set_animation_speed_31"]),
	A_JmpIfVarEqualsConst(TEMP_7034, 52428, ["ACTION_651_set_priority_38"]),
	A_CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_700C),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 32768),
	A_JmpIfComparisonResultIsLesser(["ACTION_651_face_east_7C_10"]),
	A_Mem700CAndConst(0x00FF),
	A_SetVRAMPriority(PRIORITY_3),
	A_FaceEast7C(identifier="ACTION_651_face_east_7C_10"),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(SLOW),
	A_SetPriority(3),
	A_WalkFDirectionPixels(12),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_WalkFDirectionPixels(4),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_VisibilityOff(identifier="ACTION_651_visibility_off_19"),
	A_TransferXYZFPixels(x=0, y=0, z=24, direction=EAST),
	A_VisibilityOn(),
	A_SetPriority(3, identifier="ACTION_651_set_priority_22"),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(12),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_ShiftZUpPixels(4),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetSequenceSpeed(FAST, identifier="ACTION_651_set_animation_speed_31"),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(12),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_ShiftZUpPixels(4),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetPriority(3, identifier="ACTION_651_set_priority_38"),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ShadowOff(),
	A_SetSolidityBits(cant_walk_through=True),
	A_SetSequenceSpeed(FAST),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_651_face_mario_48"], identifier="ACTION_651_jmp_if_object_within_range_43"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_651_jmp_if_object_within_range_43"]),
	A_FaceMario(identifier="ACTION_651_face_mario_48"),
	A_SetWalkingSpeed(FAST),
	A_TurnClockwise45DegreesNTimes(4),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(4),
	A_Pause(4),
	A_JmpIfRandom2of3(['ACTION_651_turn_clockwise_45_degrees_n_times_57', 'ACTION_651_turn_clockwise_45_degrees_n_times_59']),
	A_TurnClockwise45DegreesNTimes(3),
	A_Jmp(["ACTION_651_walk_1_step_f_direction_60"]),
	A_TurnClockwise45DegreesNTimes(4, identifier="ACTION_651_turn_clockwise_45_degrees_n_times_57"),
	A_Jmp(["ACTION_651_walk_1_step_f_direction_60"]),
	A_TurnClockwise45DegreesNTimes(5, identifier="ACTION_651_turn_clockwise_45_degrees_n_times_59"),
	A_Walk1StepFDirection(identifier="ACTION_651_walk_1_step_f_direction_60"),
	A_Jmp(["ACTION_651_jmp_if_object_within_range_43"])
])
