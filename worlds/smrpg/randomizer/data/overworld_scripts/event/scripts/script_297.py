# E0297_MUSHROOM_KINGDOM_RUNNING_KID
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
	JmpIfMarioOnAnObjectOrNot(['EVENT_297_set_7000_to_current_level_3', 'EVENT_297_set_7000_to_current_level_3']),
	RunDialog(dialog_id=DI0534_MUSHROOM_KINGDOM_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	Set7000ToCurrentLevel(identifier="EVENT_297_set_7000_to_current_level_3"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 495, ["EVENT_256_ret_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 51, ["EVENT_256_ret_0"]),
	ResumeActionScript(MEM_70A8),
	Pause(1, identifier="EVENT_297_pause_7"),
	JmpIfMarioInAir(["EVENT_297_pause_7"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	StartLoopNTimes(239),
	Pause(1),
	JmpIfMarioInAir(["EVENT_256_ret_0"]),
	EndLoop(),
	EnableControlsUntilReturn([]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_297_set_7000_to_object_coord_19"]),
	Set7000ToObjectCoord(target_npc=NPC_6, coord=COORD_F, pixel=True),
	Jmp(["EVENT_297_copy_var_to_var_20"]),
	Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_F, pixel=True, identifier="EVENT_297_set_7000_to_object_coord_19"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C, identifier="EVENT_297_copy_var_to_var_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_JumpToHeight(64),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_southwest_7"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_northeast_9"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_northwest_11"]),
		A_Walk1StepSoutheast(),
		A_Jmp(["EVENT_297_action_queue_21_SUBSCRIPT_pause_12"]),
		A_Walk1StepSouthwest(identifier="EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_southwest_7"),
		A_Jmp(["EVENT_297_action_queue_21_SUBSCRIPT_pause_12"]),
		A_Walk1StepNortheast(identifier="EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_northeast_9"),
		A_Jmp(["EVENT_297_action_queue_21_SUBSCRIPT_pause_12"]),
		A_Walk1StepNorthwest(identifier="EVENT_297_action_queue_21_SUBSCRIPT_walk_1_step_northwest_11"),
		A_Pause(1, identifier="EVENT_297_action_queue_21_SUBSCRIPT_pause_12"),
		A_JmpIfMarioInAir(["EVENT_297_action_queue_21_SUBSCRIPT_pause_12"]),
		A_SequencePlaybackOn(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_TurnClockwise45DegreesNTimes(1, identifier="EVENT_297_action_queue_21_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19"),
		A_Pause(2),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_297_action_queue_21_SUBSCRIPT_start_loop_n_times_24"]),
		A_Jmp(["EVENT_297_action_queue_21_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19"]),
		A_StartLoopNTimes(2, identifier="EVENT_297_action_queue_21_SUBSCRIPT_start_loop_n_times_24"),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
