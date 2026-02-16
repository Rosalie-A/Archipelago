# E3359_KEEP_INITIATE_COIN_GAME
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
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_WalkToXYCoords(x=23, y=81),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetPriority(3),
		A_ShiftZUpSteps(4),
		A_WalkToXYCoords(x=24, y=79)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(4)
	]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	SetBit(TEMP_7044_7),
	SetVarToConst(ROSE_WAY_703C, 21),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	FreezeCamera(),
	MoveScriptToBackgroundThread2(),
	SetVarToConst(ROSE_WAY_703A, 4, identifier="EVENT_3359_set_var_to_const_10"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNortheastSteps(3)
	]),
	Pause(1, identifier="EVENT_3359_pause_12"),
	Set7000ToTappedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3359_dec_18"]),
	JmpIfVarEqualsConst(ROSE_WAY_703A, 4, ["EVENT_3359_pause_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 32, ["EVENT_3359_action_queue_23"]),
	Jmp(["EVENT_3359_pause_12"]),
	Dec(ROSE_WAY_703A, identifier="EVENT_3359_dec_18"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_3359_action_queue_19_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3359_action_queue_19_SUBSCRIPT_pause_1"]),
		A_Pause(8)
	]),
	JmpIfVarEqualsConst(ROSE_WAY_703C, 0, ["EVENT_3359_resume_action_script_57"]),
	JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["EVENT_3359_action_queue_23"]),
	Jmp(["EVENT_3359_pause_12"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSouthwestSteps(3)
	], identifier="EVENT_3359_action_queue_23"),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_FixedFCoordOn(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(48),
		A_Walk1StepSouthwest(),
		A_EndLoop()
	]),
	SetBit(TEMP_7044_7),
	SetVarToRandom(ROSE_WAY_703A, 4),
	Inc(ROSE_WAY_703A),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(80),
		A_Pause(3),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Pause(10),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	], identifier="EVENT_3359_action_queue_30"),
	Pause(8),
	RunBackgroundEvent(event_id=E3360_KEEP_COIN_GAME_CHEST, return_on_level_exit=True),
	Pause(32),
	JmpIfVarEqualsConst(ROSE_WAY_703C, 0, ["EVENT_3359_resume_action_script_39"]),
	Dec(ROSE_WAY_703A),
	JmpIfVarNotEqualsConst(ROSE_WAY_703A, 0, ["EVENT_3359_action_queue_30"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(48),
		A_Walk1StepNortheast(),
		A_EndLoop()
	]),
	Jmp(["EVENT_3359_set_var_to_const_10"]),
	ResumeActionScript(NPC_2, identifier="EVENT_3359_resume_action_script_39"),
	Pause(16),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
	Pause(16),
	PlayMusicAtDefaultVolume(M0009_VICTORY),
	SetBit(TEMP_7044_7),
	Pause(32),
	UnfreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShiftZUpSteps(5),
		A_WalkToXYCoords(x=29, y=70),
		A_ShiftZDownSteps(2),
		A_ShiftZDownPixels(8)
	]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, mod_id=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(32),
		A_Walk1StepNortheast()
	]),
	SetVarToConst(ROSE_WAY_703E, 0),
	JmpToEvent(E1955_KEEP_COIN_GAME_ROOM_EXIT_CONTAINER),
	Return(),
	ResumeActionScript(NPC_2, identifier="EVENT_3359_resume_action_script_57"),
	Pause(8),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
	Pause(8),
	PlayMusicAtDefaultVolume(M0066_BOWSER_SCASTLE_2NDTIME),
	SlowDownMusic(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1907_DUPLICATE, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	Pause(240),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE)
])
