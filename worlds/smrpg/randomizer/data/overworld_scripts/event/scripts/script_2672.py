# E2672_TOWER_KNIFE_GUY_MINIGAME_BUSINESS_LOGIC
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2672_set_var_to_const_2"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x94')),
		A_AddConstToVar(Y_COORD_2, 2),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(1, identifier="EVENT_2672_action_queue_1_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_2672_action_queue_1_SUBSCRIPT_pause_3"]),
		A_UnknownCommand(bytearray(b'\x98')),
		A_FaceNorth(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetVarToConst(TEMP_70AE, 20, identifier="EVENT_2672_set_var_to_const_2"),
	ResumeActionScript(NPC_0),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferXYZFPixels(x=244, y=1, z=0, direction=EAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=12, y=1, z=0, direction=EAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RememberLastObject(),
	Pause(10),
	SetSyncActionScript(NPC_0, A0893_KNIFE_GUY_HIDING),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702C),
	CompareVarToConst(TEMP_702C, 10),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_set_var_to_random_27"]),
	CompareVarToConst(TEMP_702C, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_set_var_to_random_21"]),
	SetVarToRandom(TEMP_702A, 5, identifier="EVENT_2672_set_var_to_random_16"),
	CompareVarToConst(TEMP_702A, 1),
	JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_16"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_LoadMemory(TEMP_702A),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_Pause(16),
		A_EndLoop(),
		A_JmpIfRandom1of2(["EVENT_2672_action_queue_19_SUBSCRIPT_set_sprite_sequence_13"]),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_5),
		A_ClearBit(TEMP_7044_6),
		A_Jmp(["EVENT_2672_jmp_20"]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False, identifier="EVENT_2672_action_queue_19_SUBSCRIPT_set_sprite_sequence_13"),
		A_Pause(16),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_6),
		A_ClearBit(TEMP_7044_5)
	]),
	Jmp(["EVENT_2672_action_queue_32"], identifier="EVENT_2672_jmp_20"),
	SetVarToRandom(TEMP_702A, 7, identifier="EVENT_2672_set_var_to_random_21"),
	CompareVarToConst(TEMP_702A, 1),
	JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_21"]),
	SetBit(TEMP_7043_7),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FASTER),
		A_LoadMemory(TEMP_702A),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_Pause(14),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_Pause(14),
		A_EndLoop(),
		A_JmpIfRandom1of2(["EVENT_2672_action_queue_25_SUBSCRIPT_set_sprite_sequence_13"]),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_5),
		A_ClearBit(TEMP_7044_6),
		A_Jmp(["EVENT_2672_jmp_26"]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False, identifier="EVENT_2672_action_queue_25_SUBSCRIPT_set_sprite_sequence_13"),
		A_Pause(14),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_6),
		A_ClearBit(TEMP_7044_5)
	]),
	Jmp(["EVENT_2672_action_queue_32"], identifier="EVENT_2672_jmp_26"),
	SetVarToRandom(TEMP_702A, 7, identifier="EVENT_2672_set_var_to_random_27"),
	CompareVarToConst(TEMP_702A, 1),
	JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_27"]),
	SetBit(TEMP_7044_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_LoadMemory(TEMP_702A),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=2, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=4, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=8, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=10, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=12, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=14, is_mold=True, looping=True),
		A_Pause(3),
		A_EndLoop(),
		A_JmpIfRandom1of2(["EVENT_2672_action_queue_31_SUBSCRIPT_set_sprite_sequence_27"]),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True),
		A_Pause(1),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_5),
		A_ClearBit(TEMP_7044_6),
		A_Jmp(["EVENT_2672_action_queue_32"]),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, identifier="EVENT_2672_action_queue_31_SUBSCRIPT_set_sprite_sequence_27"),
		A_Pause(3),
		A_SetSpriteSequence(index=2, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=4, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=8, is_mold=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=10, is_mold=True, looping=True),
		A_Pause(1),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7044_6),
		A_ClearBit(TEMP_7044_5)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL)
	], identifier="EVENT_2672_action_queue_32"),
	SetSyncActionScript(NPC_0, A0893_KNIFE_GUY_HIDING),
	RunDialog(dialog_id=DI2550_WHICH_HAND, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	DisableObjectTrigger(NPC_0),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_jump_through=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSolidityBits(cant_jump_through=True)
	]),
	SetBit(TEMP_7043_2),
	RememberLastObject(),
	Return(),
	CloseDialog(identifier="EVENT_2672_close_dialog_41"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	Inc(UNKNOWN_70C9),
	CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E2671_TOWER_KNIFE_GUY_CHECK_IF_SIDEQUEST_COMPLETED),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_jmp_if_bit_set_71"]),
	RunEventAsSubroutine(E2668_KNIFE_GUY_SECOND_GRANT),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_set_var_to_const_68"]),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7044_4),
	Jmp(["EVENT_2672_run_event_as_subroutine_66"]),
	CloseDialog(identifier="EVENT_2672_close_dialog_51"),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2672_clear_bit_57"]),
	Dec(PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70C9),
	ClearBit(TEMP_7043_2, identifier="EVENT_2672_clear_bit_57"),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_2672_set_action_script_62"]),
	SetSyncActionScript(NPC_0, A0894_KNIFE_GUY_HOLDING_BALL),
	Pause(90),
	Jmp(["EVENT_2672_set_action_script_64"]),
	SetSyncActionScript(NPC_0, A0895_KNIFE_GUY_HOLDING_BALL, identifier="EVENT_2672_set_action_script_62"),
	Pause(90),
	SetSyncActionScript(NPC_0, A0892_KNIFE_GUY_DEFAULT, identifier="EVENT_2672_set_action_script_64"),
	Jmp(["EVENT_2672_clear_bit_75"]),
	RunEventAsSubroutine(E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE, identifier="EVENT_2672_run_event_as_subroutine_66"),
    PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Jmp(["EVENT_2672_clear_bit_75"]),
    JmpIfBitSet(KNIFE_GUY_SECOND_PRIZE_AWARDED, ["EVENT_2672_run_event_as_subroutine_66"], identifier="EVENT_2672_set_var_to_const_68"),
    SetBit(KNIFE_GUY_SECOND_PRIZE_AWARDED),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Jmp(["EVENT_2672_clear_bit_75"]),
	JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_2672_run_event_as_subroutine_66"], identifier="EVENT_2672_jmp_if_bit_set_71"),
	SetBit(KNIFE_GUY_PRIZE_GRANTED),
	RunDialog(dialog_id=DI0038_KNIFE_GUY_PRIZE_GRANT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	ClearBit(TEMP_7043_2, identifier="EVENT_2672_clear_bit_75"),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_6),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7044_4),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_0),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_jump_through=True),
		A_TransferXYZFPixels(x=12, y=255, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_jump_through=True),
		A_TransferXYZFPixels(x=244, y=255, z=0, direction=EAST)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_0, A0892_KNIFE_GUY_DEFAULT),
	EnableObjectTrigger(NPC_0),
	Return()
])
