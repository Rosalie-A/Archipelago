# E1571_MIDAS_RIVER_BARREL_SECTION_BUSINESS_LOGIC
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
	ClearBit(UNKNOWN_MIDAS_RIVER_7078_2),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 22),
	SetVarToConst(TEMP_7028, 21),
	RunBackgroundEvent(event_id=E1585_MIDAS_RIVER_BARREL_SUBROUTINE, return_on_level_exit=True),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthSteps(4)
	]),
	FreezeCamera(),
	Set7016701BToObjectXYZ(target=NPC_1, bit_7=True),
	SetAsyncActionScript(NPC_9, A0170_MIDAS_BARRELS_WATER_SPLASH),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=13, y=16, z=17, direction=EAST),
		A_FaceSouthwest(),
		A_Pause(9),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=0, silent=True),
		A_FloatingOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(FAST)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=64, silent=True),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_FloatingOn(),
		A_ShadowOn()
	]),
	SetSyncActionScript(NPC_1, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
	SetSyncActionScript(MARIO, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
	SetSyncActionScript(SCREEN_FOCUS, A0592_MIDAS_BARREL_CAMERA),
	MoveScriptToBackgroundThread2(),
	EnableControlsUntilReturn([A, B], identifier="EVENT_1571_enable_controls_until_return_22"),
	Pause(1, identifier="EVENT_1571_pause_23"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1571_clear_bit_34"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7078_2, ["EVENT_1571_adjust_music_tempo_84"]),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1571_jmp_if_mario_in_air_29"]),
	Jmp(["EVENT_1571_pause_23"]),
	JmpIfMarioInAir(["EVENT_1571_pause_23"], identifier="EVENT_1571_jmp_if_mario_in_air_29"),
	ClearBit(TEMP_7044_4),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_1571_pause_23"]),
	SetBit(TEMP_7044_4),
	Jmp(["EVENT_1571_pause_23"]),
	ClearBit(TEMP_7044_7, identifier="EVENT_1571_clear_bit_34"),
	PauseActionScript(MARIO),
	PauseActionScript(SCREEN_FOCUS),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	JmpIfMarioInAir(["EVENT_1571_copy_var_to_var_52"]),
	EnableControlsUntilReturn([]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(FAST)
	]),
	PauseActionScript(MEM_70A9),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(height=64, silent=True),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ResumeActionScript(MARIO),
	StoreSetBits(TEMP_7044_6),
	Pause(19),
	ResumeActionScript(SCREEN_FOCUS),
	Pause(1),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_ResetProperties()
	]),
	AddConstToVar(TEMP_702C, 65526),
	Jmp(["EVENT_1571_enable_controls_until_return_22"]),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1571_copy_var_to_var_52"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	PauseActionScript(MEM_70A8),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_1571_action_queue_74"]),
	EnableControlsUntilReturn([]),
	PauseActionScript(MEM_70A9),
	Pause(1, identifier="EVENT_1571_pause_58"),
	JmpIfMarioInAir(["EVENT_1571_pause_58"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=4),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(8)
	]),
	StoreSetBits(TEMP_7044_6),
	ResumeActionScript(MEM_70A8),
	ResumeActionScript(MARIO),
	Pause(9),
	PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
	Pause(10),
	ResumeActionScript(SCREEN_FOCUS),
	StartLoopNTimes(2),
	PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
	Pause(10),
	EndLoop(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(48),
		A_WalkNortheastPixels(4),
		A_ResetProperties()
	]),
	Jmp(["EVENT_1571_enable_controls_until_return_22"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(3)
	], identifier="EVENT_1571_action_queue_74"),
	ResumeActionScript(SCREEN_FOCUS),
	ResetCoords(MARIO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepSouthwest(),
		A_Walk1StepSouthwest()
	]),
	SetSyncActionScript(MARIO, A0592_MIDAS_BARREL_CAMERA),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_SetAllSpeeds(FAST)
	]),
	SwapVars(TEMP_7028, PRIMARY_TEMP_7000),
	SwapVars(TEMP_7026, PRIMARY_TEMP_7000),
	SwapVars(TEMP_7028, PRIMARY_TEMP_7000),
	Jmp(["EVENT_1571_pause_23"]),
	SlowDownMusicTempoBy(duration=30, change=0, identifier="EVENT_1571_adjust_music_tempo_84"),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	SetSyncActionScript(MEM_70A9, A0592_MIDAS_BARREL_CAMERA),
	SetSyncActionScript(MARIO, A0592_MIDAS_BARREL_CAMERA),
	PauseActionScript(SCREEN_FOCUS),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthwestSteps(14)
	]),
	FadeOutToBlack(sync=False, duration=32),
	EnterArea(room_id=R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA, face_direction=SOUTH, x=20, y=21, z=0),
	ClearBit(UNKNOWN_MIDAS_RIVER_7079_1),
	SetBit(TEMP_7043_1),
	JmpToEvent(E3486_MIDAS_RIVER_BASE_AREA_LOADER),
	Return()
])
