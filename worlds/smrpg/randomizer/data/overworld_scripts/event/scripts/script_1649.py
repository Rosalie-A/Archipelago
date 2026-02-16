# E1649_MOLEVILLE_LIBERATED_EXTERIOR_LOADER
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
	JmpIfBitClear(CARBO_COOKIE_GIVEN, ["EVENT_1649_set_var_to_const_6"]),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_7, R108_MOLEVILLE_OUTSIDE),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 24, identifier="EVENT_1649_set_var_to_const_6"),
	FadeOutMusicToVolume(duration=1, volume=127),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShiftZDownPixels(5)
	]),
	JmpIfBitClear(TEMP_7042_1, ["EVENT_1649_jmp_if_bit_set_11"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=0),
	JmpIfBitSet(MINECART_CRASH_CUTSCENE_CLEARED, ["EVENT_1649_clear_bit_25"], identifier="EVENT_1649_jmp_if_bit_set_11"),
	JmpIfBitClear(BUCKET_WARP_DIRECTIONAL_BIT, ["EVENT_1649_fade_in_from_black_async_16"]),
	ClearBit(BUCKET_WARP_DIRECTIONAL_BIT),
	ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
	JmpToEvent(E0081_MARIO_LANDS_SUBROUTINE),
	FadeInFromBlack(sync=False, identifier="EVENT_1649_fade_in_from_black_async_16"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1649_jmp_to_event_23"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1649_jmp_to_event_23"]),
	RunEventAsSubroutine(E3897_MOLEVILLE_STAR_PIECE_SIGNAL),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT, ["EVENT_1649_ret_24"]),
	SetVarToConst(PRIMARY_TEMP_7000, 523),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE, identifier="EVENT_1649_jmp_to_event_23"),
	Return(identifier="EVENT_1649_ret_24"),
	ClearBit(MINECART_CRASH_CUTSCENE_CLEARED, identifier="EVENT_1649_clear_bit_25"),
	JmpIfBitSet(OPTIONAL_MINECART_CLEARED, ["EVENT_1649_fade_out_music_to_volume_48"]),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferXYZFSteps(x=0, y=0, z=20, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x00')),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	FadeInFromBlack(sync=True),
	PlaySoundBalance(sound=SO019_LONG_FALL, balance=255),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkWestSteps(7),
		A_WalkSouthwestSteps(8),
		A_WalkSouthSteps(5)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOff(),
		A_SetPriority(3),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(19),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x01\x00\xe0\xff')),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_Walk1StepSouthwest(),
		A_ShadowOn()
	]),
	FadeOutMusicToVolume(duration=1, volume=0),
	FadeOutToBlack(sync=True, duration=15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepSouthwest(),
		A_FloatingOff(),
		A_BPL262728()
	]),
	RunEventAtReturn(E1650_MOLEVILLE_LIBERATED_EXTERIOR_LOADER_CONTD),
	Return(),
	FadeOutMusicToVolume(duration=2, volume=0, identifier="EVENT_1649_fade_out_music_to_volume_48"),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferXYZFSteps(x=0, y=0, z=18, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x00')),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthwestSteps(4)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_ShadowOff(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_StartLoopNTimes(5),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_EndLoop(),
		A_WalkNorthPixels(4)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO021_RUMBLING, channel=4),
		A_JumpToHeight(64),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(2),
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepSouthwest(),
		A_SetAllSpeeds(SLOW),
		A_Walk1StepSouthwest(),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=False),
		A_SetSolidityBits(cant_walk_through=True),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=104, silent=True),
		A_Walk1StepNorth(),
		A_FloatingOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Pause(1, identifier="EVENT_1649_action_queue_59_SUBSCRIPT_pause_5"),
		A_JmpIfMarioInAir(["EVENT_1649_action_queue_59_SUBSCRIPT_pause_5"]),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	SetVarToConst(TEMP_7034, 6),
	SetVarToConst(X_COORD_1, 13312),
	SetVarToConst(Y_COORD_1, 5632),
	SetVarToConst(Z_COORD_1, 1024),
	StartLoopNTimes(11),
	Pause(1, identifier="EVENT_1649_pause_65"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1649_pause_65"]),
	Pause(5),
	AddConstToVar(TEMP_7034, 3),
	AddConstToVar(Z_COORD_1, 128),
	EndLoop(),
	UnfreezeCamera(),
	StopMusic(),
	Pause(24),
	PlayMusicAtDefaultVolume(M0033_MOLEVILLE),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Walk1StepSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1100_MINECART_SCORE, above_object=NPC_8, closable=False, sync=False, multiline=True, use_background=False),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	RunDialogForDuration(dialog_id=DI1101_MINECART_HIGH_SCORE, duration=0, sync=False),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	Compare7000ToVar(TEMP_702E),
	JmpIfComparisonResultIsLesser(["EVENT_1649_run_dialog_duration_86"]),
	RunDialogForDuration(dialog_id=DI1102_MINECART_DID_NOT_SET_PB, duration=1, sync=False),
	Jmp(["EVENT_1649_clear_bit_104"]),
	RunDialogForDuration(dialog_id=DI1103_MINECART_SET_PB, duration=1, sync=False, identifier="EVENT_1649_run_dialog_duration_86"),
	JmpIfBitClear(MINECART_INITIATE_FREEPLAY, ["EVENT_1649_clear_bit_104"]),
	SetSyncActionScript(NPC_3, A0650_BLUE_CLOUD_MOVEMENT),
	RunDialog(dialog_id=DI1116_WON_AFTER_WAGER, above_object=NPC_8, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(FAST)
	]),
	StartLoopNTimes(4),
	AddCoins(10),
	PlaySound(sound=SO013_COIN, channel=6),
	Pause(1, identifier="EVENT_1649_pause_95"),
	Set70107015ToObjectXYZ(target=NPC_3),
	AddConstToVar(X_COORD_1, 160),
	AddConstToVar(Z_COORD_1, 352),
	CreatePacketAt7010(packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_1649_pause_95"]),
	Pause(30),
	EndLoop(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(15),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(60),
		A_ResetProperties()
	]),
	ClearBit(MINECART_INITIATE_FREEPLAY, identifier="EVENT_1649_clear_bit_104"),
	Return()
])
