#A0277_VOLCANO_HOMING_FIREBALL
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
	A_VisibilityOff(identifier="ACTION_277_visibility_off_0"),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 389, ["ACTION_277_clear_solidity_bits_4"]),
	A_SetPriority(2),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True, identifier="ACTION_277_clear_solidity_bits_4"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(NORMAL),
	A_JmpIfBitSet(TEMP_7044_3, ["ACTION_277_set_700C_to_pressed_button_10"]),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_277_reset_properties_59"]),
	A_Set700CToPressedButton(identifier="ACTION_277_set_700C_to_pressed_button_10"),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_277_pause_26"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_277_pause_25"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_277_pause_24"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_277_pause_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_277_pause_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_277_pause_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_277_pause_20"]),
	A_Pause(5),
	A_Pause(9, identifier="ACTION_277_pause_20"),
	A_Pause(13, identifier="ACTION_277_pause_21"),
	A_Pause(19, identifier="ACTION_277_pause_22"),
	A_Pause(23, identifier="ACTION_277_pause_23"),
	A_Pause(17, identifier="ACTION_277_pause_24"),
	A_Pause(11, identifier="ACTION_277_pause_25"),
	A_Pause(7, identifier="ACTION_277_pause_26"),
	A_VisibilityOn(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_PlaySound(sound=SO084_SMOKED, channel=4),
	A_FaceMario(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_37"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_37"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Jmp(["ACTION_277_pause_38"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_277_set_sprite_sequence_37"),
	A_Pause(8, identifier="ACTION_277_pause_38"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_44"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_44"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_Jmp(["ACTION_277_jump_to_height_silent_45"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_277_set_sprite_sequence_44"),
	A_JumpToHeight(height=180, silent=True, identifier="ACTION_277_jump_to_height_silent_45"),
	A_Pause(28),
	A_ResetProperties(),
	A_SequenceLoopingOn(),
	A_Pause(2, identifier="ACTION_277_pause_49"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_277_pause_49"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_56"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_56"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Jmp(["ACTION_277_pause_57"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_277_set_sprite_sequence_56"),
	A_Pause(4, identifier="ACTION_277_pause_57"),
	A_Jmp(["ACTION_277_visibility_off_0"]),
	A_ResetProperties(identifier="ACTION_277_reset_properties_59"),
	A_VisibilityOn(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_UnknownCommand(bytearray(b' \x07')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x14\x00\x01\x00\x00\x80\x03\x80')),
	A_UnknownCommand(bytearray(b'/\x00\x08\x80\x00\x01\x00')),
	A_FaceMario(identifier="ACTION_277_face_mario_66"),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	A_AddConstToVar(PRIMARY_TEMP_700C, 256),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True),
	A_Compare700CToVar(TEMP_7028),
	A_JmpIfLoadedMemoryIs0(["ACTION_277_pause_75"]),
	A_JmpIfLoadedMemoryIsBelow0(["ACTION_277_shift_z_down_pixels_77"]),
	A_JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_277_shift_z_up_pixels_79"]),
	A_Pause(1, identifier="ACTION_277_pause_75"),
	A_Jmp(["ACTION_277_face_mario_66"]),
	A_ShiftZDownPixels(1, identifier="ACTION_277_shift_z_down_pixels_77"),
	A_Jmp(["ACTION_277_face_mario_66"]),
	A_ShiftZUpPixels(1, identifier="ACTION_277_shift_z_up_pixels_79"),
	A_Jmp(["ACTION_277_face_mario_66"])
])
