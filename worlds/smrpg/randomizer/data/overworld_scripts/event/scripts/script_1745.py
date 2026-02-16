# E1745_WHIRLPOOL_SHOGUN
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
	FreezeAllNPCsUntilReturn(),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
		A_Compare700CToVar(X_COORD_1),
		A_JmpIfComparisonResultIsLesser(["EVENT_1745_action_queue_3_SUBSCRIPT_play_sound_10"]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4, identifier="EVENT_1745_action_queue_3_SUBSCRIPT_play_sound_10"),
		A_JumpToHeight(108),
		A_Pause(32)
	]),
	SetVarToConst(BATTLE_PACK_ID, 206),
	StartBattleWithPackAt700E(),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1745_action_queue_31"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1745_reset_and_choose_game_29"]),
	RemoveObjectAt70A8FromCurrentLevel(),
	Pause(1),
	DisableObjectTrigger(MEM_70A8),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	Pause(1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_TurnClockwise45DegreesNTimes(4),
		A_WalkFDirectionPixels(10),
		A_TurnClockwise45DegreesNTimes(4),
		A_SetAllSpeeds(NORMAL)
	]),
	SetBit(TEMP_7043_2),
	FadeInFromBlack(sync=False),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	StartLoopNTimes(2),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True)
	]),
	Inc(ACTIVE_NPC),
	EndLoop(),
	Pause(1),
	SetVarToConst(TIMER_701C, 90),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1789_WHIRLPOOL_SHOGUN_SUBROUTINE, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	SetBit(TEMP_7043_2),
	SetBit(TEMP_7043_3),
	UnfreezeAllNPCs(),
	Return(),
	ResetAndChooseGame(identifier="EVENT_1745_reset_and_choose_game_29"),
	Return(),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_UnknownCommand(bytearray(b'\xc8\x07')),
		A_SetVarToConst(Z_COORD_2, 0),
		A_UnknownCommand(bytearray(b'\x99')),
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_SetSolidityBits(cant_walk_through=True)
	], identifier="EVENT_1745_action_queue_31"),
	PauseActionScript(MARIO),
	ResetCoords(MARIO),
	Pause(1),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Y, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(FASTEST),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
		A_Compare700CToVar(Y_COORD_1),
		A_JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1745_action_queue_37_SUBSCRIPT_shift_south_pixels_7"]),
		A_WalkNorthPixels(14),
		A_Jmp(["EVENT_1745_action_queue_37_SUBSCRIPT_face_north_8"]),
		A_WalkSouthPixels(14, identifier="EVENT_1745_action_queue_37_SUBSCRIPT_shift_south_pixels_7"),
		A_FaceNorth(identifier="EVENT_1745_action_queue_37_SUBSCRIPT_face_north_8"),
		A_SetAllSpeeds(NORMAL),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Dec(TEMP_70AE),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False),
	UnfreezeAllNPCs(),
	Return(),
	FreezeAllNPCsUntilReturn(identifier="EVENT_1745_freeze_all_npcs_until_return_43"),
	Inc(ACTIVE_NPC),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 3, ["EVENT_1745_inc_52"]),
	SummonObjectToCurrentLevelAtMariosCoords(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO013_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0004),
		A_Mem700CXorConst(0x0004),
		A_FaceEast7C(),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\xb0\xff')),
		A_Walk1StepFDirection(),
		A_VisibilityOff(),
		A_BPL262728()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=108, silent=True),
		A_Walk1StepFDirection()
	]),
	AddCoins(10),
	Jmp(["EVENT_1745_unfreeze_all_npcs_58"]),
	Inc(ACTIVE_NPC, identifier="EVENT_1745_inc_52"),
	SummonObjectToCurrentLevelAtMariosCoords(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0004),
		A_Mem700CXorConst(0x0004),
		A_FaceEast7C(),
		A_FloatingOff(),
		A_JumpToHeight(160),
		A_WalkFDirectionSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_JumpToHeight(height=108, silent=True),
		A_Walk1StepFDirection()
	]),
	AddFrogCoins(1),
	SetVarToConst(TEMP_70AE, 0),
	UnfreezeAllNPCs(identifier="EVENT_1745_unfreeze_all_npcs_58"),
	Return(),
	FreezeAllNPCsUntilReturn(identifier="EVENT_1745_freeze_all_npcs_until_return_60"),
	SetVarToConst(TEMP_70AE, 0),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
		A_JumpToHeight(108),
		A_Pause(32),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
		A_SetAllSpeeds(NORMAL),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(cant_walk_through=True),
		A_SetBit(TEMP_7043_4)
	]),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Y, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(FAST),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
		A_Compare700CToVar(Y_COORD_1),
		A_JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1745_action_queue_65_SUBSCRIPT_shift_south_pixels_7"]),
		A_WalkNorthPixels(10),
		A_Jmp(["EVENT_1745_action_queue_65_SUBSCRIPT_face_north_8"]),
		A_WalkSouthPixels(10, identifier="EVENT_1745_action_queue_65_SUBSCRIPT_shift_south_pixels_7"),
		A_FaceNorth(identifier="EVENT_1745_action_queue_65_SUBSCRIPT_face_north_8"),
		A_SetAllSpeeds(NORMAL),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	UnfreezeAllNPCs(),
	Return()
])
