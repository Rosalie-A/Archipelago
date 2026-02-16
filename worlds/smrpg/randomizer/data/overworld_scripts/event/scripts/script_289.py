# E0289_INNS_CONTAINER
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
	Set7000ToCurrentLevel(identifier="EVENT_289_set_7000_to_current_level_0"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 485, ["EVENT_289_set_var_to_const_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 493, ["EVENT_289_set_var_to_const_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 85, ["EVENT_289_jmp_if_bit_set_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 86, ["EVENT_289_set_bit_14"]),
	SetVarToConst(SECONDARY_TEMP_7024, 3),
	SetBit(TEMP_7042_7),
	JmpToEvent(E0273_SLEEP_IN_INNS),
	SetVarToConst(SECONDARY_TEMP_7024, 3, identifier="EVENT_289_set_var_to_const_8"),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_INN),
	JmpToEvent(E0273_SLEEP_IN_INNS),
	SetVarToConst(SECONDARY_TEMP_7024, 3, identifier="EVENT_289_set_var_to_const_11"),
	SetBit(MUSHROOM_KINGDOM_INN),
	JmpToEvent(E0273_SLEEP_IN_INNS),
	SetBit(TEMP_7044_2, identifier="EVENT_289_set_bit_14"),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_289_set_7010_to_object_xyz_36"], identifier="EVENT_289_jmp_if_bit_set_15"),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_289_set_7010_to_object_xyz_36"]),
	RunDialog(dialog_id=DI0766_ROSE_TOWN_INNKEEPER, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_289_pause_29"]),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0767_ROSE_TOWN_INN_CONFIRM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_289_set_bit_27"]),
	SetBit(OCCUPIED_ROSE_TOWN_INN),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	SetBit(ROSE_TOWN_LIBERATED_INN, identifier="EVENT_289_set_bit_27"),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	Pause(10, identifier="EVENT_289_pause_29"),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0768_ROSE_TOWN_INN_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	Set70107015ToObjectXYZ(target=NPC_0, bit_7=True, identifier="EVENT_289_set_7010_to_object_xyz_36"),
	CompareVarToConst(X_COORD_1, 5),
	JmpIfComparisonResultIsLesser(["EVENT_256_ret_0"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_289_jmp_if_bit_set_15"]),
	EnableControlsUntilReturn([]),
	UnsyncDialog(),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_1),
	RunDialog(dialog_id=DI0776_ROSE_TOWN_NEXT_MORNING, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_289_pause_54"]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_289_action_queue_47_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_289_action_queue_47_SUBSCRIPT_pause_6"]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI0777_ROSE_TOWN_NEXT_MORNING_CONFIRM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Return(),
	Pause(10, identifier="EVENT_289_pause_54"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
		A_UnknownCommand(bytearray(b'\xfd$\x00\x10')),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=PRIMARY_TEMP_7000),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_9"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_15"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_21"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_27"]),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_9"),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Jmp(["EVENT_289_action_queue_55_SUBSCRIPT_pause_32"]),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_15"),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Jmp(["EVENT_289_action_queue_55_SUBSCRIPT_pause_32"]),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_21"),
		A_Pause(20),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Jmp(["EVENT_289_action_queue_55_SUBSCRIPT_pause_32"]),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_289_action_queue_55_SUBSCRIPT_set_sprite_sequence_27"),
		A_Pause(20),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20, identifier="EVENT_289_action_queue_55_SUBSCRIPT_pause_32"),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI0778_ROSE_TOWN_NEXT_MORNING_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	Return()
])
