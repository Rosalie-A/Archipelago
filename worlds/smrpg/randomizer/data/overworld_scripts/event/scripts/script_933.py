# E0933_FAT_YOSHI_PRESENT_GENERATOR
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
	PlaySound(sound=SO130_BIG_BABY_YOSHI, channel=6),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_932_enable_controls_until_return_36"]),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
	StoreItemAmountTo7000(YoshiCookieItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_933_close_dialog_55"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	RunDialog(dialog_id=DI2372_PROMPT_TO_FEED_BABY_YOSHI, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_933_close_dialog_55"]),
	SetBit(TEMP_7042_0),
	JmpToSubroutine(["EVENT_930_enable_controls_until_return_85"]),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	RemoveOneOfItemFromInventory(YoshiCookieItem),
	EndLoop(),
	CopyVarToVar(from_var=FED_COOKIES, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(SECONDARY_TEMP_7024),
	CompareVarToConst(PRIMARY_TEMP_7000, 50),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_933_action_queue_47"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=FED_COOKIES),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 20),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_933_action_queue_29"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 10),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_933_action_queue_38"]),
	Jmp(["EVENT_933_close_dialog_55"]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	], identifier="EVENT_933_action_queue_29"),
	Pause(10),
	JmpToSubroutine(["EVENT_933_action_queue_63"]),
	Pause(10),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunEventAsSubroutine(E0008_SET_70A7_TO_RANDOM_TIER_4_CONSUMABLE),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Jmp(["EVENT_933_close_dialog_55"]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	], identifier="EVENT_933_action_queue_38"),
	Pause(10),
	JmpToSubroutine(["EVENT_933_action_queue_63"]),
	Pause(10),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunEventAsSubroutine(E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Jmp(["EVENT_933_close_dialog_55"]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	], identifier="EVENT_933_action_queue_47"),
	Pause(10),
	JmpToSubroutine(["EVENT_933_action_queue_63"]),
	Pause(10),
	AddFrogCoins(1),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(FED_COOKIES, 0),
	CloseDialog(identifier="EVENT_933_close_dialog_55"),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	Return(),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequencePlaybackOff(),
		A_SequenceLoopingOff()
	], identifier="EVENT_933_action_queue_63"),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False, mirror_sprite=True),
		A_Pause(110),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequencePlaybackOn(),
		A_SequenceLoopingOn()
	]),
	Return()
])
