# E3824_YOSTER_ISLE_LOADER
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
	SetVarToConst(UNKNOWN_70EE, 0),
	SetVarToConst(UNKNOWN_70EB, 0),
	SetVarToConst(UNKNOWN_7100, 0),
	ClearBit(YOSHI_UNKNOWN_7061_7),
	ClearBit(MUSHROOM_DERBY_MANUAL),
	ClearBit(MUSHROOM_DERBY_AUTO),
	SetTempAsyncActionScript(NPC_1, A0803_INC_PALETTE_ROW),
	SetTempAsyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
	SetTempAsyncActionScript(NPC_5, A0803_INC_PALETTE_ROW),
	SetTempAsyncActionScript(NPC_4, A0803_INC_PALETTE_ROW),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_TransferXYZFPixels(x=0, y=252, z=0, direction=EAST)
	]),
	JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_3824_pause_action_script_45"]),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_9),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=14, y=86, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=21, y=58, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_5, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
	JmpIfBitSet(YOSTER_ISLE_LIBERATED_1, ["EVENT_3824_jmp_if_bit_clear_31"], identifier="EVENT_3824_jmp_if_bit_set_23"),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_3824_jmp_if_bit_set_32"]),
	FadeInFromBlack(sync=False, identifier="EVENT_3824_fade_in_from_black_async_25"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3824_ret_30"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3824_ret_30"]),
	RunEventAsSubroutine(E3901_YOSTER_ISLE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3824_ret_30"),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_3824_clear_bit_39"], identifier="EVENT_3824_jmp_if_bit_clear_31"),
	JmpIfBitSet(UNKNOWN_7084_1, ["EVENT_3824_summon_to_current_level_41"], identifier="EVENT_3824_jmp_if_bit_set_32"),
	SummonObjectToCurrentLevel(NPC_13),
	ApplyTileModToLevel(use_alternate=True, room_id=R034_YOSTER_ISLE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=0),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=15, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetPriority(3),
		A_FloatingOff()
	]),
	JmpIfBitSet(YOSTER_ISLE_LIBERATED_1, ["EVENT_3824_clear_bit_39"], identifier="EVENT_3824_jmp_if_bit_set_37"),
	Jmp(["EVENT_3824_fade_in_from_black_async_25"]),
	ClearBit(YOSTER_ISLE_LIBERATED_1, identifier="EVENT_3824_clear_bit_39"),
	Return(),
	SummonObjectToCurrentLevel(NPC_11, identifier="EVENT_3824_summon_to_current_level_41"),
	RemoveObjectFromCurrentLevel(NPC_13),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetPriority(3),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn()
	]),
	Jmp(["EVENT_3824_jmp_if_bit_set_37"]),
	PauseActionScript(NPC_3, identifier="EVENT_3824_pause_action_script_45"),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=11, y=82, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=11, y=83, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=9, y=80, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=16, y=64, z=0, direction=EAST),
		A_SetPriority(3),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=19, y=60, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_VisibilityOff()
	]),
	SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
	Jmp(["EVENT_3824_jmp_if_bit_set_23"])
])
