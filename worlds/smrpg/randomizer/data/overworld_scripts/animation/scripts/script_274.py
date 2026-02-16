#A0274_SEWER_4_RAT_ROOM_BOOS
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
	A_SetSequenceSpeed(SLOW, identifier="ACTION_274_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_JmpIfBitSet(TEMP_7076_0, ["ACTION_274_sequence_looping_off_63"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_DecVarFrom700C(TEMP_7028),
	A_AddConstToVar(PRIMARY_TEMP_700C, 256),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 128),
	A_JmpIfComparisonResultIsLesser(["ACTION_274_set_700C_to_object_coord_13"]),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 384),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_274_set_700C_to_object_coord_13"]),
	A_Jmp(["ACTION_274_shift_f_direction_pixels_24"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, identifier="ACTION_274_set_700C_to_object_coord_13"),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True),
	A_DecVarFrom700C(TEMP_7028),
	A_AddConstToVar(PRIMARY_TEMP_700C, 256),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 64),
	A_JmpIfComparisonResultIsLesser(["ACTION_274_face_mario_23"]),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 320),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_274_face_mario_23"]),
	A_Jmp(["ACTION_274_shift_f_direction_pixels_24"]),
	A_FaceMario(identifier="ACTION_274_face_mario_23"),
	A_WalkFDirectionPixels(1, identifier="ACTION_274_shift_f_direction_pixels_24"),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, identifier="ACTION_274_set_700C_to_object_coord_25"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 192),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True),
	A_Compare700CToVar(TEMP_7028),
	A_JmpIfLoadedMemoryIs0(["ACTION_274_pause_33"]),
	A_JmpIfLoadedMemoryIsBelow0(["ACTION_274_shift_z_down_pixels_35"]),
	A_JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_274_shift_z_up_pixels_37"]),
	A_Pause(1, identifier="ACTION_274_pause_33"),
	A_Jmp(["ACTION_274_pause_38"]),
	A_ShiftZDownPixels(1, identifier="ACTION_274_shift_z_down_pixels_35"),
	A_Jmp(["ACTION_274_pause_38"]),
	A_ShiftZUpPixels(1, identifier="ACTION_274_shift_z_up_pixels_37"),
	A_Pause(2, identifier="ACTION_274_pause_38"),
	A_JmpIfBitSet(TEMP_7076_0, ["ACTION_274_sequence_looping_off_63"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
	A_FaceMario(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_DecVarFrom700C(TEMP_7028),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_274_set_700C_to_object_coord_53"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_274_set_700C_to_object_coord_53"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_274_set_700C_to_object_coord_53"]),
	A_Jmp(["ACTION_274_set_animation_speed_0"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, identifier="ACTION_274_set_700C_to_object_coord_53"),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_DecVarFrom700C(TEMP_7028),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_274_sequence_looping_off_63"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_274_sequence_looping_off_63"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_274_sequence_looping_off_63"]),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=80, tiles=0, destinations=["ACTION_274_set_700C_to_object_coord_25"]),
	A_Jmp(["ACTION_274_set_animation_speed_0"]),
	A_SequenceLoopingOff(identifier="ACTION_274_sequence_looping_off_63"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_274_set_sprite_sequence_70"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_274_set_sprite_sequence_72"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_274_set_sprite_sequence_74"]),
	A_SetSpriteSequence(index=9, looping=False, mirror_sprite=True),
	A_Jmp(["ACTION_274_pause_38"]),
	A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True, identifier="ACTION_274_set_sprite_sequence_70"),
	A_Jmp(["ACTION_274_pause_38"]),
	A_SetSpriteSequence(index=8, looping=False, identifier="ACTION_274_set_sprite_sequence_72"),
	A_Jmp(["ACTION_274_pause_38"]),
	A_SetSpriteSequence(index=9, looping=False, identifier="ACTION_274_set_sprite_sequence_74"),
	A_Jmp(["ACTION_274_pause_38"])
])
