# E0931_INITATIE_YOSHI_RACE_FOR_GAMBLING
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

script = EventScript([
	JmpIfBitSet(YOSHI_UNKNOWN_7061_7, ["EVENT_931_run_event_as_subroutine_83"]),
	SetVarToConst(UNKNOWN_70BA, 0),
	SetVarToConst(UNKNOWN_70D6, 0),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=6, y=66)
	]),
	RunDialog(dialog_id=DI2356_RACE_BOSHI_CASUAL, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	JmpIfDialogOptionBSelected(["EVENT_931_run_dialog_63"]),
	StoreItemAmountTo7000(YoshiCookieItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_931_run_dialog_60"]),
	RunEventAsSubroutine(E1970_BOSHI_ODDS_CALCULATOR),
	CompareVarToConst(PRIMARY_TEMP_7000, 42),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_27"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 40),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_29"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 37),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_31"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 32),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_33"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 24),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_25"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 14),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_931_set_var_to_const_35"]),
	SetVarToConst(UNKNOWN_70BA, 3),
	Jmp(["EVENT_931_copy_var_to_var_37"]),
	SetVarToConst(UNKNOWN_70BA, 5, identifier="EVENT_931_set_var_to_const_25"),
	Jmp(["EVENT_931_copy_var_to_var_37"]),
	SetVarToConst(UNKNOWN_70BA, 20, identifier="EVENT_931_set_var_to_const_27"),
	Jmp(["EVENT_931_copy_var_to_var_42"]),
	SetVarToConst(UNKNOWN_70BA, 10, identifier="EVENT_931_set_var_to_const_29"),
	Jmp(["EVENT_931_copy_var_to_var_42"]),
	SetVarToConst(UNKNOWN_70BA, 8, identifier="EVENT_931_set_var_to_const_31"),
	Jmp(["EVENT_931_copy_var_to_var_42"]),
	SetVarToConst(UNKNOWN_70BA, 6, identifier="EVENT_931_set_var_to_const_33"),
	Jmp(["EVENT_931_copy_var_to_var_42"]),
	SetVarToConst(UNKNOWN_70BA, 4, identifier="EVENT_931_set_var_to_const_35"),
	Jmp(["EVENT_931_copy_var_to_var_42"]),
	CopyVarToVar(from_var=UNKNOWN_70BA, to_var=PRIMARY_TEMP_7000, identifier="EVENT_931_copy_var_to_var_37"),
	VarShiftLeft(PRIMARY_TEMP_7000, 1),
	RunDialog(dialog_id=DI2358_BOSHI_ODDS, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_931_set_bit_57"]),
	Jmp(["EVENT_931_set_bit_47"]),
	CopyVarToVar(from_var=UNKNOWN_70BA, to_var=PRIMARY_TEMP_7000, identifier="EVENT_931_copy_var_to_var_42"),
	VarShiftLeft(PRIMARY_TEMP_7000, 1),
	RunDialog(dialog_id=DI2357_BOSHI_ODDS, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_931_set_bit_57"]),
	Jmp(["EVENT_931_set_bit_47"]),
	SetBit(MUSHROOM_DERBY_MANUAL, identifier="EVENT_931_set_bit_47"),
	ClearBit(MUSHROOM_DERBY_AUTO),
	RunDialog(dialog_id=DI2359_COOKIE_BET_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_931_run_dialog_49"),
	StoreItemAmountTo7000(YoshiCookieItem),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	JmpToSubroutine(["EVENT_930_enable_controls_until_return_85"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70D6),
	RunDialog(dialog_id=DI2361_BOSHI_STARTS_RACE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_931_copy_var_to_var_66"]),
	SetBit(MUSHROOM_DERBY_AUTO, identifier="EVENT_931_set_bit_57"),
	ClearBit(MUSHROOM_DERBY_MANUAL),
	Jmp(["EVENT_931_run_dialog_49"]),
	RunDialog(dialog_id=DI2363_CANT_RACE_WITHOUT_COOKIES, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_931_run_dialog_60"),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(identifier="EVENT_931_ret_62"),
	RunDialog(dialog_id=DI2360_BOSHI_CHAT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_931_run_dialog_63"),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	CopyVarToVar(from_var=UNKNOWN_70D6, to_var=PRIMARY_TEMP_7000, identifier="EVENT_931_copy_var_to_var_66"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	RemoveOneOfItemFromInventory(YoshiCookieItem),
	EndLoop(),
	SetBit(YOSHI_UNKNOWN_7061_7),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=11, y=82, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=11, y=83, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=10, y=80, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	JmpToEvent(E0458_MUSHROOM_DERBY_BEGINS),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_931_run_event_as_subroutine_83"),
	RunDialog(dialog_id=DI2383_BOSHI_START_RACE, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return()
])
