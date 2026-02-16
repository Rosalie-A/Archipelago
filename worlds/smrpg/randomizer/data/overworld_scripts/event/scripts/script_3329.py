# E3329_JUMPING_FIREBALLS
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
	Pause(1, identifier="EVENT_3329_pause_0"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3329_pause_0"]),
	JmpIfBitSet(TEMP_7076_0, ["EVENT_3329_pause_0"]),
	EnableControls([]),
	ClearBit(TEMP_7044_4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9"]),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True, identifier="EVENT_3329_action_queue_6_SUBSCRIPT_set_solidity_bits_1"),
		A_SetBit(TEMP_7044_4),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(8),
		A_Pause(1, identifier="EVENT_3329_action_queue_6_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_3329_action_queue_6_SUBSCRIPT_pause_6"]),
		A_ResetProperties(),
		A_Set700CToObjectCoord(target_npc=NPC_0, coord=COORD_F),
		A_FaceEast7C(),
		A_Pause(1),
		A_UnknownCommand(bytearray(b'\xfd\x9c:'))
	]),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Jmp(["EVENT_3329_pause_0"]),
	NonEmbeddedActionQueue(required_offset=0x34, subscript=[
		A_FaceSouthwest7D(arg=0x14),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16"]),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10"),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17"]),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12"),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17"]),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_14"),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17"]),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16"),
		A_UnknownCommand(bytearray(b'\xfd\x9ci'), identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17"),
		A_JmpIfObjectWithinRange(comparing_npc=NPC_0, usually=0, tiles=8, destinations=["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_27"]),
		A_JmpIfObjectWithinRange(comparing_npc=NPC_0, usually=0, tiles=16, destinations=["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_25"]),
		A_JmpIfObjectWithinRange(comparing_npc=NPC_0, usually=0, tiles=28, destinations=["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_23"]),
		A_JumpToHeight(height=384, silent=True),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_npc_coords_28"]),
		A_JumpToHeight(height=320, silent=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_23"),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_npc_coords_28"]),
		A_JumpToHeight(height=256, silent=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_25"),
		A_Jmp(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_npc_coords_28"]),
		A_JumpToHeight(height=192, silent=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_27"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=MARIO, destinations=["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_clear_solidity_bits_29"], identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_npc_coords_28"),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_clear_solidity_bits_29"),
		A_Pause(4),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_UnknownCommand(bytearray(b'\xc8\x14')),
		A_UnknownCommand(bytearray(b'\xfd\xc7')),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkTo70167018(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(1, identifier="EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_pause_37"),
		A_JmpIfMarioInAir(["EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_pause_37"]),
		A_Jmp(["EVENT_3329_action_queue_6_SUBSCRIPT_set_solidity_bits_1"])
	], identifier="EVENT_3329_non_embedded_action_queue_9")
])
