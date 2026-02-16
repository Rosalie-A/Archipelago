# E3220_SHIP_BARREL_PUZZLE_BARREL_MOVEMENT
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3220_clear_bit_4"]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequencePlaybackOn(),
		A_SetAllSpeeds(VERY_SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(4),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestPixels(8),
		A_SetAllSpeeds(NORMAL),
		A_JumpToHeight(height=48, silent=True),
		A_WalkSouthwestPixels(20),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_PlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_ReturnQueue(),
		A_CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C(),
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff(),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_ReturnQueue()
	]),
	Return(),
	ClearBit(TEMP_7044_6, identifier="EVENT_3220_clear_bit_4"),
	ActionQueueSync(target=MARIO, subscript=[
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_8"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_8"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_8"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_15"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_15"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_15"]),
		A_Jmp(["EVENT_3220_action_queue_5_SUBSCRIPT_ret_21"]),
		A_FixedFCoordOn(identifier="EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_8"),
		A_SequenceLoopingOn(),
		A_Pause(5),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_SetBit(TEMP_7044_6),
		A_Jmp(["EVENT_3220_action_queue_5_SUBSCRIPT_ret_21"]),
		A_FixedFCoordOn(identifier="EVENT_3220_action_queue_5_SUBSCRIPT_fixed_f_coord_on_15"),
		A_SequenceLoopingOn(),
		A_Pause(5),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_SetBit(TEMP_7044_6),
		A_ReturnQueue(identifier="EVENT_3220_action_queue_5_SUBSCRIPT_ret_21")
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_9"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_9"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_9"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_21"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_21"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_21"]),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_Jmp(["EVENT_3220_action_queue_6_SUBSCRIPT_sequence_looping_off_37"]),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_9"),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Jmp(["EVENT_3220_action_queue_6_SUBSCRIPT_object_memory_clear_bit_32"]),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_3220_action_queue_6_SUBSCRIPT_set_sprite_sequence_21"),
		A_WalkSoutheastPixels(1),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_WalkSoutheastPixels(1),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_WalkSoutheastPixels(1),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_WalkSoutheastPixels(1),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
		A_WalkSoutheastPixels(1),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="EVENT_3220_action_queue_6_SUBSCRIPT_object_memory_clear_bit_32"),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
		A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 21, ["EVENT_3220_action_queue_6_SUBSCRIPT_sequence_looping_off_37"]),
		A_SetBit(TEMP_7044_5),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOff(identifier="EVENT_3220_action_queue_6_SUBSCRIPT_sequence_looping_off_37"),
		A_SequencePlaybackOff()
	]),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_3220_ret_11"]),
	SetSyncActionScript(NPC_2, A0336_SHIP_BARREL_PUZZLE_BUTTON),
	Inc(TEMP_70AE),
	ClearBit(TEMP_7044_6),
	Return(identifier="EVENT_3220_ret_11")
])
