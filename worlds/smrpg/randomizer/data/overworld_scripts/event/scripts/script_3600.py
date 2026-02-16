# E3600_MUSHROOM_DERBY_GOAL_TILE
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
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3584_ret_0"]),
	JmpIfBitClear(UNKNOWN_MUSHROOM_DERBY_7085_4, ["EVENT_3584_ret_0"]),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_7085_4),
	FreezeCamera(),
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	UnknownCommand(bytearray(b'\xfdE')),
	PauseActionScript(MARIO),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_WalkToXYCoords(x=20, y=61)
	]),
	CloseDialog(),
	PauseActionScript(NPC_9),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	StartAsyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SetAllSpeeds(NORMAL)
	]),
	JmpIfBitClear(YOSTER_ISLE_LIBERATED_2, ["EVENT_3600_jmp_if_bit_set_165"], identifier="EVENT_3600_jmp_if_bit_clear_13"),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_action_queue_64"]),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_3600_action_queue_64"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3600_action_queue_64"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest()
	]),
	SetSyncActionScript(NPC_9, A0680_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(MARIO, A0681_MUSHROOM_DERBY_UNKNOWN),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=17, y=49)
	], identifier="EVENT_3600_action_queue_21"),
	UnsyncActionScript(NPC_3),
	UnsyncActionScript(NPC_2),
	UnsyncActionScript(NPC_10),
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7044_7),
	UnsyncActionScript(MARIO),
	UnsyncActionScript(NPC_9),
	PauseActionScript(MARIO),
	PauseActionScript(NPC_9),
	JmpToSubroutine(["EVENT_3600_fade_out_music_to_volume_113"]),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_46"]),
	CopyVarToVar(from_var=UNKNOWN_70EE, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3600_play_sound_42"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	RemoveOneOfItemFromInventory(YoshiCookieItem),
	EndLoop(),
	SetVarToConst(UNKNOWN_70EE, 0),
	SetVarToConst(UNKNOWN_70EB, 0),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequenceLoopingOff()
	]),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6, identifier="EVENT_3600_play_sound_42"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	Jmp(["EVENT_3600_play_sound_47"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest()
	], identifier="EVENT_3600_action_queue_46"),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_3600_play_sound_47"),
	CopyVarToVar(from_var=UNKNOWN_70D6, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=UNKNOWN_70BA, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_3600_mem_7000_shift_left_59"], identifier="EVENT_3600_jmp_if_var_equals_const_53"),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	Inc(PRIMARY_TEMP_7000),
	EndLoop(),
	Dec(TEMP_7026),
	Jmp(["EVENT_3600_jmp_if_var_equals_const_53"]),
	VarShiftLeft(PRIMARY_TEMP_7000, 1, identifier="EVENT_3600_mem_7000_shift_left_59"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70B8),
	RunDialog(dialog_id=DI0943_GOT_X_COOKIES, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	RunEventAsSubroutine(E3599_MUSHROOM_DERBY_PRIZE_CALCULATOR),
	Jmp(["EVENT_3600_pause_123"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=17, y=49)
	], identifier="EVENT_3600_action_queue_64"),
	JmpToSubroutine(["EVENT_3600_jmp_if_bit_set_84"]),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_79"]),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	RunDialog(dialog_id=DI0893_YOSHI_LOST, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	CopyVarToVar(from_var=UNKNOWN_70EE, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3600_jmp_78"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	RemoveOneOfItemFromInventory(YoshiCookieItem),
	EndLoop(),
	SetVarToConst(UNKNOWN_70EE, 0),
	SetVarToConst(UNKNOWN_70EB, 0),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequenceLoopingOff()
	]),
	Jmp(["EVENT_3600_pause_123"], identifier="EVENT_3600_jmp_78"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	], identifier="EVENT_3600_action_queue_79"),
	Pause(10),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	RunDialog(dialog_id=DI0894_YOSHI_LOST, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3600_pause_123"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3600_unsync_action_script_91"], identifier="EVENT_3600_jmp_if_bit_set_84"),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_3600_unsync_action_script_97"]),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_unsync_action_script_103"]),
	UnsyncActionScript(NPC_3),
	UnsyncActionScript(NPC_2),
	UnsyncActionScript(NPC_10),
	Jmp(["EVENT_3600_pause_action_script_108"]),
	UnsyncActionScript(NPC_2, identifier="EVENT_3600_unsync_action_script_91"),
	UnsyncActionScript(NPC_10),
	SetBit(TEMP_7044_7),
	PauseActionScript(NPC_3),
	UnsyncActionScript(NPC_3),
	Jmp(["EVENT_3600_pause_action_script_108"]),
	UnsyncActionScript(NPC_3, identifier="EVENT_3600_unsync_action_script_97"),
	UnsyncActionScript(NPC_10),
	SetBit(TEMP_7044_7),
	PauseActionScript(NPC_2),
	UnsyncActionScript(NPC_2),
	Jmp(["EVENT_3600_pause_action_script_108"]),
	UnsyncActionScript(NPC_3, identifier="EVENT_3600_unsync_action_script_103"),
	UnsyncActionScript(NPC_2),
	SetBit(TEMP_7044_7),
	PauseActionScript(NPC_10),
	UnsyncActionScript(NPC_10),
	PauseActionScript(NPC_2, identifier="EVENT_3600_pause_action_script_108"),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_10),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_0),
	FadeOutMusicToVolume(duration=3, volume=0, identifier="EVENT_3600_fade_out_music_to_volume_113"),
	Pause(120),
	PlayMusicAtDefaultVolume(M0004_YO_STERISLAND),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_120"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastPixels(8),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(2),
		A_SetSequenceSpeed(SLOW),
		A_FaceSouthwest()
	]),
	Pause(30),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastPixels(8),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(1),
		A_SetSequenceSpeed(SLOW)
	], identifier="EVENT_3600_action_queue_120"),
	Pause(30),
	Return(),
	Pause(30, identifier="EVENT_3600_pause_123"),
	SetVarToConst(ROSE_TOWN_ARROW_POSITION, 0),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_6),
	ClearBit(TEMP_7044_7),
	SetBit(TEMP_7043_3),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_3),
	ClearBit(TEMP_7044_6),
	JmpToSubroutine(["EVENT_3600_action_queue_301"]),
	SetSyncActionScript(NPC_2, A0682_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_10, A0685_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_3, A0683_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_5, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetBit(TEMP_7044_5),
	SetBit(TEMP_7044_4),
	SetVarToConst(ROSE_WAY_703E, 7),
	UnfreezeCamera(),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_enable_controls_157"]),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	EnableControls([LEFT, RIGHT, DOWN, UP]),
	SetSyncActionScript(NPC_1, A0684_MUSHROOM_DERBY_UNKNOWN),
	ClearBit(MUSHROOM_DERBY_MANUAL),
	Return(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3600_enable_controls_157"),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_SetSolidityBits(cant_walk_through=True),
		A_SetSolidityBits(bit_4=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(NPC_1, A0496_MUSHROOM_DERBY_REFEREE),
	ClearBit(MUSHROOM_DERBY_AUTO),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_4),
	Return(),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_set_bit_262"], identifier="EVENT_3600_jmp_if_bit_set_165"),
	SetVarToConst(UNKNOWN_70EE, 0),
	SetVarToConst(UNKNOWN_70EB, 0),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest()
	]),
	SetSyncActionScript(NPC_9, A0680_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(MARIO, A0681_MUSHROOM_DERBY_UNKNOWN),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	UnsyncActionScript(NPC_10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_BounceToXYWithHeight(x=21, y=63, height=0),
		A_FaceNorthwest()
	]),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_3),
	SetBit(TEMP_7043_1),
	UnsyncActionScript(MARIO),
	UnsyncActionScript(NPC_9),
	PauseActionScript(MARIO),
	PauseActionScript(NPC_9),
	Pause(10),
	FadeOutMusicToVolume(duration=3, volume=0),
	Pause(120),
	StopMusic(),
	PlayMusicAtDefaultVolume(M0004_YO_STERISLAND),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(2),
		A_FaceSouthwest(),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(6),
		A_WalkNortheastSteps(12),
		A_FaceSoutheast(),
		A_SetSequenceSpeed(SLOW),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNorthwestSteps(4),
		A_WalkNortheastSteps(2),
		A_SetSequenceSpeed(SLOW),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	SetAsyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	Pause(10),
	SetAsyncActionScript(NPC_10, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=20, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	SetAsyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	SetAsyncActionScript(NPC_1, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(3),
		A_SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(1, identifier="EVENT_3600_action_queue_227_SUBSCRIPT_pause_4"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_3600_action_queue_227_SUBSCRIPT_pause_4"])
	]),
	Pause(10),
	SetBit(COMPLETED_MUSHROOM_DERBY),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_3600_action_queue_231_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3600_action_queue_231_SUBSCRIPT_pause_1"])
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(8),
		A_SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	SetBit(YOSTER_ISLE_LIBERATED_1),
	EnterArea(room_id=R034_YOSTER_ISLE, face_direction=NORTHWEST, x=20, y=61, z=0, run_entrance_event=True),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_TransferToXYZF(x=21, y=62, z=0, direction=EAST)
	]),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=20, y=61, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Pause(10),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	Pause(10),
	RunEventAsSubroutine(E0181_NPC_QUEST_4_CONTAINER),
	Pause(10),
	RunEventAsSubroutine(E1256_UNLOCK_MOLEVILLE_IF_GATED_BY_BOSHI),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_PlaySound(sound=SO063_YOSHI_TALK, channel=6),
		A_SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(30)
	]),
	SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNorth(),
		A_Pause(60),
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_SetSequenceSpeed(NORMAL)
	]),
	SetSyncActionScript(NPC_9, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	SetBit(YOSTER_ISLE_LIBERATED_2),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3600_set_bit_262"),
	PauseActionScript(NPC_10),
	UnsyncActionScript(NPC_10),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_10),
	Pause(30),
	FadeOutMusicToVolume(duration=3, volume=0),
	Pause(120),
	StopMusic(),
	PlayMusicAtDefaultVolume(M0004_YO_STERISLAND),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceNorthwest()
	]),
	Pause(30),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=False, mirror_sprite=True)
	]),
	PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	SetBit(YOSTER_ISLE_LIBERATED_1),
	EnterArea(room_id=R034_YOSTER_ISLE, face_direction=NORTHWEST, x=20, y=61, z=0, run_entrance_event=True),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_TransferToXYZF(x=21, y=62, z=0, direction=EAST)
	]),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=20, y=61, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(30)
	]),
	SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(GOT_FREE_COOKIES),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	], identifier="EVENT_3600_action_queue_301"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Return()
])
