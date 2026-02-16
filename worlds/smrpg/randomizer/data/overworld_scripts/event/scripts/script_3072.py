# E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST
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
	DisableObjectTrigger(MEM_70A8),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	Mem7000AndConst(0x00F0),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
	SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 0, ["EVENT_3072_play_sound_16"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 16, ["EVENT_3072_enable_controls_29"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 32, ["EVENT_3072_play_sound_90"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 48, ["EVENT_3072_play_sound_95"]),
	Jmp(["EVENT_3072_ret_98"]),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3072_play_sound_16"),
	CreatePacketAt7010(packet=P001_FLASHING_POOF_MUSHROOM, destinations=["EVENT_3072_ret_98"]),
	RestoreAllHP(),
	RestoreAllFP(),
	SetVarToConst(TIMER_7020, 8),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7020, bit_4=True, bit_5=True),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 453, ["EVENT_3072_enable_controls_until_return_25"]),
	Jmp(["EVENT_3072_ret_98"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3072_enable_controls_until_return_25"),
	Pause(8),
	PrioritySet(mainscreen=[LAYER_L3], subscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], colour_math=[BACKGROUND, HALF_INTENSITY]),
	Jmp(["EVENT_3072_ret_98"]),
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_3072_enable_controls_29"),
	PlaySound(sound=SO014_FLOWER, channel=6),
	CreatePacketAt7010(packet=P003_BRIEF_STAR, destinations=["EVENT_3072_ret_98"]),
	StopMusicFDA0(),
	SetVarToConst(TIMER_7022, 550),
	RunBackgroundEventWithPause(event_id=E3076_EXP_STAR_CHEST_BACKGROUND, timer_var=TIMER_7022, bit_4=True, bit_5=True),
	SetBit(TEMP_7076_0),
	RunEventAsSubroutine(E0357_EXP_STAR_MUSIC_EXPERIMENT),
	JmpIfBitClear(PROGRESSIVE_STAR_EXP_ENABLED, ["EVENT_3072_jmp_if_bit_clear_47"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 0, ["EVENT_3072_set_var_to_const_60"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 1, ["EVENT_3072_set_var_to_const_63"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 2, ["EVENT_3072_set_var_to_const_66"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 3, ["EVENT_3072_set_var_to_const_69"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 4, ["EVENT_3072_set_var_to_const_72"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 5, ["EVENT_3072_set_var_to_const_75"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 6, ["EVENT_3072_set_var_to_const_78"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 7, ["EVENT_3072_set_var_to_const_78"]),
	Return(),
	JmpIfBitClear(PROGRESSIVE_BOSS_EXP_ENABLED, ["EVENT_3072_copy_var_to_var_81"], identifier="EVENT_3072_jmp_if_bit_clear_47"),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 21),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_78"]),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 15),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_75"]),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 10),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_72"]),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 6),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_69"]),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 3),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_66"]),
	CompareVarToConst(BOSS_VICTORY_COUNTER, 1),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3072_set_var_to_const_63"]),
	SetVarToConst(ITEM_ID, 16, identifier="EVENT_3072_set_var_to_const_60"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 17, identifier="EVENT_3072_set_var_to_const_63"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 18, identifier="EVENT_3072_set_var_to_const_66"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 19, identifier="EVENT_3072_set_var_to_const_69"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 20, identifier="EVENT_3072_set_var_to_const_72"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 21, identifier="EVENT_3072_set_var_to_const_75"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	SetVarToConst(ITEM_ID, 23, identifier="EVENT_3072_set_var_to_const_78"),
	Jmp(["EVENT_3072_copy_var_to_var_81"]),
	Return(),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3072_copy_var_to_var_81"),
	Mem7000AndConst(0x000F),
	SetEXPPacketTo7000(),
	MarioGlows(),
	ClearBit(EXP_STAR_BIT_6),
	ClearBit(UNKNOWN_7064_4),
	ClearBit(EXP_STAR_BIT_5),
	CreatePacketAtObjectCoords(packet=P022_RECURSIVE_SPARKLES, target_npc=MARIO, destinations=["EVENT_3072_jmp_89"]),
	Jmp(["EVENT_3072_ret_98"], identifier="EVENT_3072_jmp_89"),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3072_play_sound_90"),
	CreatePacketAt7010(packet=P000_FLASHING_POOF_FLOWER, destinations=["EVENT_3072_ret_98"]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Add7000ToMaxFP(),
	Jmp(["EVENT_3072_ret_98"]),
	PlaySound(sound=SO094_FROG_COIN, channel=6, identifier="EVENT_3072_play_sound_95"),
	CreatePacketAt7010(packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_3072_ret_98"]),
	AddFrogCoins(1),
	Return(identifier="EVENT_3072_ret_98")
])
