# E3126_MIMIC_2_CHEST
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
	JmpIfBitSet(MIMIC_2_CLEARED, ["EVENT_3126_set_var_to_const_32"]),
	RunEventAsSubroutine(E0096_REVERT_ALL_CLONE_CHESTS_MIMIC_2),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x03\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	PlaySound(sound=SO014_FLOWER, channel=6),
	CreatePacketAt7010(packet=P004_MIMIC_POOF_ON_DEFEAT, destinations=["EVENT_3126_pause_12"]),
	Pause(8, identifier="EVENT_3126_pause_12"),
	Pause(12),
	PlaySound(sound=SO000_SILENCE, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 513),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitSet(GAME_OVER, ["EVENT_3126_reset_and_choose_game_35"]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%@\x00\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_JmpIfBitSet(RUN_AWAY, ["EVENT_3126_action_queue_20_SUBSCRIPT_object_memory_clear_bit_9"]),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOff(),
		A_ReturnQueue(),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="EVENT_3126_action_queue_20_SUBSCRIPT_object_memory_clear_bit_9"),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_ReturnQueue()
	]),
	ClearBit(UNKNOWN_MIMIC_BIT),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3126_ret_34"]),
	SetBit(UNKNOWN_MIMIC_BIT),
	SetBit(MIMIC_2_CLEARED),
	SetSyncActionScript(MEM_70A8, A0015_DO_NOTHING),
	SetVarToConst(PRIMARY_TEMP_7000, 513),
	SetVarToConst(PRIMARY_TEMP_7000, 513),
	RunEventAsSubroutine(E0253_NPC_QUEST_1_GRANT),
	RunEventAsSubroutine(E1250_MIMIC_2_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 513),
	JmpToEvent(E0170_MIMIC_2_GRANT_STAR_PIECE_CONTAINER),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 513, identifier="EVENT_3126_set_var_to_const_32"),
	JmpToEvent(E0245_CHEST_3_GRANT),
	Return(identifier="EVENT_3126_ret_34"),
	ResetAndChooseGame(identifier="EVENT_3126_reset_and_choose_game_35")
])
