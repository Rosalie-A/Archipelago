#A0488_FOREST_MAZE_AREA_RECRUITABLE_CHARACTER
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
	A_JmpIfBitSet(FOREST_LIBERATED, ["ACTION_488_clear_bit_10"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_5, ["ACTION_488_clear_bit_10"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_7, ["ACTION_488_clear_bit_10"]),
	A_JmpIfBitSet(DIRECTIONAL_7046_0, ["ACTION_488_clear_bit_10"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_0, ["ACTION_488_shift_to_xy_coords_24"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_1, ["ACTION_488_shift_to_xy_coords_36"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_488_clear_bit_10"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_488_shift_to_xy_coords_48"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_4, ["ACTION_488_shift_to_xy_coords_60"]),
	A_JmpIfBitSet(DIRECTIONAL_7046_1, ["ACTION_488_shift_to_xy_coords_13"]),
	A_ClearBit(DIRECTIONAL_7045_5, identifier="ACTION_488_clear_bit_10"),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftToXYCoords(x=8, y=61, identifier="ACTION_488_shift_to_xy_coords_13"),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_1"),
	A_Pause(2, identifier="ACTION_488_pause_15"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_488_set_animation_speed_18"]),
	A_Jmp(["ACTION_488_pause_15"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_488_set_animation_speed_18"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_2"),
	A_WalkSoutheastSteps(2),
	A_WalkSoutheastPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftToXYCoords(x=8, y=47, identifier="ACTION_488_shift_to_xy_coords_24"),
	A_WalkSoutheastPixels(8),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_3"),
	A_Pause(2, identifier="ACTION_488_pause_27"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_488_set_animation_speed_30"]),
	A_Jmp(["ACTION_488_pause_27"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_488_set_animation_speed_30"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_4"),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftToXYCoords(x=8, y=47, identifier="ACTION_488_shift_to_xy_coords_36"),
	A_WalkSoutheastPixels(8),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_5"),
	A_Pause(2, identifier="ACTION_488_pause_39"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_488_set_animation_speed_42"]),
	A_Jmp(["ACTION_488_pause_39"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_488_set_animation_speed_42"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_6"),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftToXYCoords(x=8, y=47, identifier="ACTION_488_shift_to_xy_coords_48"),
	A_WalkSoutheastPixels(8),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_7"),
	A_Pause(2, identifier="ACTION_488_pause_51"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_488_set_animation_speed_54"]),
	A_Jmp(["ACTION_488_pause_51"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_488_set_animation_speed_54"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_11"),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftToXYCoords(x=3, y=47, identifier="ACTION_488_shift_to_xy_coords_60"),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_8"),
	A_Pause(52),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=3, sprite_offset=2, looping=False, mirror_sprite=True, identifier="forest_character_animation_9"),
	A_Pause(16),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="forest_character_animation_10"),
	A_WalkNorthwestSteps(2),
	A_VisibilityOff(),
	A_ReturnQueue()
])
