# E3486_MIDAS_RIVER_BASE_AREA_LOADER
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	EnableControlsUntilReturn([]),
	SlowDownMusicTempoBy(duration=0, change=0),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_action_queue_5"]),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestPixels(4),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3486_action_queue_5"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetVRAMPriority(PRIORITY_3),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_WalkEastPixels(4),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1])
	]),
	JmpIfBitClear(BUCKET_WARP_BIT, ["EVENT_3486_jmp_if_bit_set_9"]),
	RemoveObjectFromCurrentLevel(NPC_3),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_3486_remove_from_current_level_11"], identifier="EVENT_3486_jmp_if_bit_set_9"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3486_action_queue_22"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_3486_remove_from_current_level_11"),
	RemoveObjectFromCurrentLevel(NPC_4),
	SetVarToConst(TEMP_702A, 0),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3486_run_event_as_subroutine_16"]),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3486_run_event_as_subroutine_16"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3486_ret_21"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3486_ret_21"]),
	RunEventAsSubroutine(E3892_MIDAS_RIVER_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3486_ret_21"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=17, y=15, z=10, direction=EAST),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(5)
	], identifier="EVENT_3486_action_queue_22"),
	FadeInFromBlack(sync=True),
	PlaySoundBalance(sound=SO048_MINECART_START, balance=30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(7)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(7),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_action_queue_29"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetAllSpeeds(FASTER),
		A_Walk1StepNorthwest(),
		A_JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704E_5, ["EVENT_3486_action_queue_28_SUBSCRIPT_shift_northeast_steps_5"]),
		A_WalkNortheastSteps(5),
		A_Jmp(["EVENT_3486_action_queue_29"]),
		A_WalkNortheastSteps(4, identifier="EVENT_3486_action_queue_28_SUBSCRIPT_shift_northeast_steps_5")
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_SetWalkingSpeed(SLOW)
	], identifier="EVENT_3486_action_queue_29"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_StartLoopNTimes(1),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_WalkNorthwestSteps(8),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=112, silent=True),
		A_WalkSoutheastSteps(3),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(1, identifier="EVENT_3486_action_queue_31_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_3486_action_queue_31_SUBSCRIPT_pause_6"]),
		A_ResetProperties(),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_JumpToHeight(height=112, silent=True),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_3486_action_queue_31_SUBSCRIPT_pause_12"),
		A_JmpIfMarioInAir(["EVENT_3486_action_queue_31_SUBSCRIPT_pause_12"]),
		A_SetAllSpeeds(NORMAL)
	]),
	RemoveObjectFromCurrentLevel(NPC_4),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_ret_51"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_3486_jmp_if_bit_set_46"]),
	SetBit(UNKNOWN_7065_6),
	SetBit(UNKNOWN_7065_7),
	SetBit(MAP_DIRECTIONAL_KERO_SEWERS_MIDAS_RIVER),
	SetBit(MAP_DIRECTIONAL_MIDAS_RIVER_TADPOLE_POND),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_0),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 32768),
	JmpIfComparisonResultIsLesser(["EVENT_3486_copy_var_to_var_44"]),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=MIDAS_RIVER_70B3, identifier="EVENT_3486_copy_var_to_var_44"),
	SetBit(TEMP_7043_2),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704E_5, ["EVENT_3486_jmp_to_event_50"], identifier="EVENT_3486_jmp_if_bit_set_46"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
		A_Pause(20),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
		A_SetAllSpeeds(FAST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(2),
		A_StartLoopNTimes(3),
		A_WalkWestPixels(4),
		A_WalkEastPixels(4),
		A_EndLoop(),
		A_WalkWestPixels(2),
		A_Walk1StepSouthwest(),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=1, silent=True),
		A_Pause(1, identifier="EVENT_3486_action_queue_48_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3486_action_queue_48_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	SetBit(UNKNOWN_MIDAS_RIVER_704E_5),
	JmpToEvent(E3479_MIDAS_RIVER_SCORE_SUBMISSION, identifier="EVENT_3486_jmp_to_event_50"),
	Return(identifier="EVENT_3486_ret_51")
])
