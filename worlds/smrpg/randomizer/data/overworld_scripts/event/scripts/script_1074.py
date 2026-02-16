# E1074_MELODY_BAY_SONG_JUDGED
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
	SetBit(TEMP_7044_2, identifier="EVENT_1074_set_bit_0"),
	UnfreezeCamera(),
	StopMusicFDA2(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastPixels(8),
		A_Pause(45),
		A_SetPriority(2),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SequenceLoopingOn(),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(9),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(4)
	]),
	Pause(15),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(12)
	]),
	JmpIfBitSet(TOADOFSKY_REMOVED, ["EVENT_1074_copy_var_to_var_16"]),
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1074_copy_var_to_var_16"]),
	JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1074_jmp_if_bit_clear_14"]),
	JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1074_jmp_if_bit_clear_12"]),
	JmpToEvent(E1079_MELODY_BAY_SONG_1_VALIDATOR),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1074_copy_var_to_var_16"], identifier="EVENT_1074_jmp_if_bit_clear_12"),
	JmpToEvent(E1080_MELODY_BAY_SONG_2_VALIDATOR),
	JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_1074_copy_var_to_var_16"], identifier="EVENT_1074_jmp_if_bit_clear_14"),
	JmpToEvent(E1081_MELODY_BAY_SONG_3_VALIDATOR),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1074_copy_var_to_var_16"),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_0, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_0),
	Pause(35),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_1, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_1),
	Pause(35),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_2, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_2),
	Pause(35),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_3, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_3),
	Pause(35),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_4, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_4),
	Pause(35),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_5, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_5),
	Pause(35),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_6, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_6),
	Pause(35),
	CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	SetSyncActionScript(NPC_7, A0572_MELODY_BAY_TADPOLE_INCORRECT),
	ClearBit(TEMP_7043_7),
	Pause(35),
	Pause(45),
	PlayMusicAtCurrentVolume(M0017_TADPOLEPOND),
	Jmp(["EVENT_1074_action_queue_120"]),
	Pause(15, identifier="EVENT_1074_pause_59"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2725_SONG_SIMILARITY_0, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	Pause(15, identifier="EVENT_1074_pause_64"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2726_SONG_SIMILARITY_1, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	Pause(15, identifier="EVENT_1074_pause_71"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2727_SONG_SIMILARITY_2, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	Pause(15, identifier="EVENT_1074_pause_78"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2728_SONG_SIMILARITY_3, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	Pause(15, identifier="EVENT_1074_pause_85"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True),
		A_SetAllSpeeds(VERY_FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(10),
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2729_SONG_SIMILARITY_4, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	Pause(15, identifier="EVENT_1074_pause_92"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(96),
		A_Pause(60),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8)
	]),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest(),
		A_SetPriority(2)
	]),
	Pause(15),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Pause(15),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1074_run_event_as_subroutine_103"]),
	JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1074_run_event_as_subroutine_107"]),
	JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1074_run_event_as_subroutine_111"]),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_1074_run_event_as_subroutine_103"),
	Pause(30),
	SetBit(MELODY_BAY_ITEM_1_GRANTED),
	Jmp(["EVENT_1074_action_queue_115"]),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER, identifier="EVENT_1074_run_event_as_subroutine_107"),
	Pause(30),
	SetBit(MELODY_BAY_ITEM_2_GRANTED),
	Jmp(["EVENT_1074_action_queue_115"]),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER, identifier="EVENT_1074_run_event_as_subroutine_111"),
	Pause(30),
	SetBit(MELODY_BAY_ITEM_3_GRANTED),
	SetBit(UNKNOWN_7093_0),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(112),
		A_WalkSoutheastSteps(7),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(80),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff()
	], identifier="EVENT_1074_action_queue_115"),
	RemoveObjectFromCurrentLevel(NPC_8),
	SetBit(TOADOFSKY_REMOVED),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest(),
		A_Pause(5)
	], identifier="EVENT_1074_action_queue_120"),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1074_play_sound_130"], identifier="EVENT_1074_jmp_if_var_equals_const_123"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1074_play_sound_132"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1074_play_sound_134"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1074_play_sound_136"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1074_play_sound_138"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1074_play_sound_140"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1074_play_sound_142"]),
	PlaySound(sound=SO036_TADPOLE_POND_STAFF_DO, channel=6, identifier="EVENT_1074_play_sound_130"),
	Return(),
	PlaySound(sound=SO037_TADPOLE_POND_STAFF_RE, channel=6, identifier="EVENT_1074_play_sound_132"),
	Return(),
	PlaySound(sound=SO038_TADPOLE_POND_STAFF_MI, channel=6, identifier="EVENT_1074_play_sound_134"),
	Return(),
	PlaySound(sound=SO039_TADPOLE_POND_STAFF_FA, channel=6, identifier="EVENT_1074_play_sound_136"),
	Return(),
	PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6, identifier="EVENT_1074_play_sound_138"),
	Return(),
	PlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=6, identifier="EVENT_1074_play_sound_140"),
	Return(),
	PlaySound(sound=SO042_TADPOLE_POND_STAFF_TI, channel=6, identifier="EVENT_1074_play_sound_142"),
	Return()
])
