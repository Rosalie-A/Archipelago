# E0470_GREEN_YOSHI
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
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_7085_4, ["EVENT_256_ret_0"]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_470_jmp_if_bit_set_61', 'EVENT_470_jmp_if_bit_set_61']),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_470_action_queue_57"]),
	Jmp(["EVENT_470_play_sound_21"]),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6, identifier="EVENT_470_play_sound_21"),
	UnsyncDialog(),
	CloseDialog(),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	Jmp(["EVENT_470_pause_action_script_38"]),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	PauseActionScript(NPC_9, identifier="EVENT_470_pause_action_script_38"),
	SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_Set700CToObjectCoord(target_npc=NPC_9, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 4),
		A_Mem700CAndConst(0x0007),
		A_FaceEast7C(),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_703E),
		A_FixedFCoordOn()
	], identifier="EVENT_470_start_embedded_action_script_40"),
	SetBit(TEMP_7044_4),
	Return(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_FaceMario()
	], identifier="EVENT_470_action_queue_57"),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	RunDialog(dialog_id=DI0900_YOSHI_AFTER_YOU_ENABLE_HIM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_470_start_embedded_action_script_40"]),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_470_pause_action_script_63"], identifier="EVENT_470_jmp_if_bit_set_61"),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_470_pause_action_script_63"),
	PauseActionScript(NPC_9),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	UnknownCommand(bytearray(b'\xfdE')),
	FreezeCamera(),
	SetBit(TEMP_7044_5),
	SetBit(TEMP_7044_4),
	Set7016701BToObjectXYZ(target=NPC_9, bit_7=True),
	AddConstToVar(Z_COORD_2, 1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_UnknownCommand(bytearray(b'\x98')),
		A_VisibilityOff(),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75"])
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff()
	]),
	Jmp(["EVENT_470_action_queue_76"]),
	NonEmbeddedActionQueue(required_offset=0xA1, subscript=[
		A_PlaySound(sound=SO063_YOSHI_TALK, channel=4),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 1, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 2, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 3, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 4, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 5, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_18"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 6, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_20"]),
		A_JmpIfVarEqualsConst(ROSE_WAY_703E, 7, ["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_22"]),
		A_SetSpriteSequence(index=4, sprite_offset=6, is_sequence=True, looping=False, mirror_sprite=True),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False, mirror_sprite=True, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_10"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=2, sprite_offset=6, is_sequence=True, looping=False, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_12"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_14"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=4, sprite_offset=6, is_sequence=True, looping=False, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_16"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=False, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_18"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=3, sprite_offset=6, is_sequence=True, looping=False, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_20"),
		A_Jmp(["EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"]),
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=False, mirror_sprite=True, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_sprite_sequence_22"),
		A_SetVarToConst(Z_COORD_2, 0, identifier="EVENT_470_non_embedded_action_queue_75_SUBSCRIPT_set_var_to_const_23"),
		A_UnknownCommand(bytearray(b'\x9a')),
		A_VisibilityOn(),
		A_FixedFCoordOff(),
		A_SequencePlaybackOff(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_ShadowOn(),
		A_ReturnQueue()
	], identifier="EVENT_470_non_embedded_action_queue_75"),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_TransferToObjectXY(MARIO),
		A_SequenceLoopingOff()
	], identifier="EVENT_470_action_queue_76"),
	RememberLastObject(),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=3),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=5),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=7),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return()
])
