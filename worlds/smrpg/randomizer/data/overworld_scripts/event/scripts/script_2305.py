# E2305_SLOT_CHEST_TEMPLATE
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
	JmpIfBitSet(TEMP_7044_2, ["EVENT_2305_jmp_if_bit_set_15"]),
	SetBit(TEMP_7044_2),
	PauseActionScript(NPC_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=1, looping=False),
		A_Pause(6),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Pause(6),
	SummonObjectToCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	Pause(1),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(17)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(17)
	]),
	SetSyncActionScript(NPC_1, A0185_CHEST_SLOT_MACHINE_ROLLER),
	SetSyncActionScript(NPC_2, A0186_CHEST_SLOT_MACHINE_ROLLER),
	SetSyncActionScript(NPC_3, A0184_CHEST_SLOT_MACHINE_ROLLER),
	Return(),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_2305_jmp_if_bit_set_19"], identifier="EVENT_2305_jmp_if_bit_set_15"),
	SetBit(TEMP_7044_3),
	PauseActionScript(NPC_3),
	Return(),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_2305_disable_trigger_23"], identifier="EVENT_2305_jmp_if_bit_set_19"),
	SetBit(TEMP_7044_4),
	PauseActionScript(NPC_1),
	Return(),
	DisableObjectTrigger(MEM_70A8, identifier="EVENT_2305_disable_trigger_23"),
	PauseActionScript(NPC_2),
	Pause(16),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastPixels(8)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestPixels(8)
	]),
	StopEmbeddedActionScript(NPC_2),
	StopEmbeddedActionScript(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_5),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=1, looping=False),
		A_Pause(16),
		A_VisibilityOff()
	]),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 0, ["EVENT_2305_jmp_if_var_equals_const_38"]),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 1, ["EVENT_2305_jmp_if_var_equals_const_41"]),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 2, ["EVENT_2305_jmp_if_var_equals_const_44"]),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2305_jmp_if_var_equals_const_47"], identifier="EVENT_2305_jmp_if_var_equals_const_38"),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2305_jmp_if_var_equals_const_49"]),
	Jmp(["EVENT_2305_jmp_if_var_equals_const_52"]),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2305_jmp_if_var_equals_const_55"], identifier="EVENT_2305_jmp_if_var_equals_const_41"),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2305_jmp_if_var_equals_const_58"]),
	Jmp(["EVENT_2305_jmp_if_var_equals_const_60"]),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2305_jmp_if_var_equals_const_63"], identifier="EVENT_2305_jmp_if_var_equals_const_44"),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2305_jmp_if_var_equals_const_66"]),
	Jmp(["EVENT_2305_jmp_if_var_equals_const_69"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_summon_to_current_level_71"], identifier="EVENT_2305_jmp_if_var_equals_const_47"),
	Jmp(["EVENT_2305_play_sound_76"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_play_sound_76"], identifier="EVENT_2305_jmp_if_var_equals_const_49"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_play_sound_81"]),
	Jmp(["EVENT_2305_action_queue_92"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_play_sound_76"], identifier="EVENT_2305_jmp_if_var_equals_const_52"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_action_queue_92"]),
	Jmp(["EVENT_2305_play_sound_88"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_play_sound_76"], identifier="EVENT_2305_jmp_if_var_equals_const_55"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_play_sound_81"]),
	Jmp(["EVENT_2305_action_queue_92"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_summon_to_current_level_71"], identifier="EVENT_2305_jmp_if_var_equals_const_58"),
	Jmp(["EVENT_2305_play_sound_81"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_action_queue_92"], identifier="EVENT_2305_jmp_if_var_equals_const_60"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_play_sound_81"]),
	Jmp(["EVENT_2305_play_sound_88"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_play_sound_76"], identifier="EVENT_2305_jmp_if_var_equals_const_63"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_action_queue_92"]),
	Jmp(["EVENT_2305_play_sound_88"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2305_action_queue_92"], identifier="EVENT_2305_jmp_if_var_equals_const_66"),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2305_play_sound_81"]),
	Jmp(["EVENT_2305_play_sound_88"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 2, ["EVENT_2305_summon_to_current_level_71"], identifier="EVENT_2305_jmp_if_var_equals_const_69"),
	Jmp(["EVENT_2305_play_sound_88"]),
	SummonObjectToCurrentLevel(NPC_4, identifier="EVENT_2305_summon_to_current_level_71"),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	AddFrogCoins(1),
	Jmp(["EVENT_2305_action_queue_99"]),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_2305_play_sound_76"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Add7000ToMaxFP(),
	Jmp(["EVENT_2305_action_queue_99"]),
	PlaySound(sound=SO071_MUSHROOM_CURE, channel=6, identifier="EVENT_2305_play_sound_81"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	RestoreAllHP(),
	RestoreAllFP(),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_15=True),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_15=True),
	Jmp(["EVENT_2305_action_queue_99"]),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2305_play_sound_88"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	AddToInventory(RockCandyItem),
	Jmp(["EVENT_2305_action_queue_99"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	], identifier="EVENT_2305_action_queue_92"),
	Pause(32),
	StartBattleAtBattlefield(PACK158_VALLEY_CHEST_FIGHT, BF21_KERO_SEWERS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2305_remove_from_current_level_97"]),
	ResetAndChooseGame(),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_2305_remove_from_current_level_97"),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(32),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	], identifier="EVENT_2305_action_queue_99"),
	Return()
])
