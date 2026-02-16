# E0604_MARRYMORE_INN_BRIGHT_CARD_ENTHUSIAST
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
	StoreItemAmountTo7000(BrightCardItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_604_run_dialog_5"]),
	JmpIfBitSet(BRIGHT_CARD_SOLD, ["EVENT_604_run_dialog_39"]),
	RunDialog(dialog_id=DI2057_BRIGHT_CARD_SALE_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2054_PROMPT_TO_SELL_BRIGHT_CARD, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_604_run_dialog_5"),
	JmpIfDialogOptionBSelected(["EVENT_604_set_action_script_17"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	PlaySound(sound=SO013_COIN, channel=6),
	AddCoins(100),
	RemoveOneOfItemFromInventory(BrightCardItem, identifier="EVENT_604_remove_one_from_inventory_11"),
	SetBit(BRIGHT_CARD_SOLD),
	RunDialog(dialog_id=DI2077_BRIGHT_CARD_BUYER, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI2468_BRIGHT_CARD_BUYER, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	RunDialog(dialog_id=DI2469_BRIGHT_CARD_BUYER, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_604_set_action_script_17"),
	Pause(10),
	RunDialog(dialog_id=DI2108_BRIGHT_CARD_HAGGLE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_604_set_action_script_26"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	AddFrogCoins(5),
	Jmp(["EVENT_604_remove_one_from_inventory_11"]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_604_set_action_script_26"),
	Pause(10),
	RunDialog(dialog_id=DI2307_BRIGHT_CARD_HAGGLE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_604_set_action_script_35"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	AddFrogCoins(10),
	Jmp(["EVENT_604_remove_one_from_inventory_11"]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_604_set_action_script_35"),
	Pause(10),
	RunDialog(dialog_id=DI2308_BRIGHT_CARD_HAGGLE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2329_BRIGHT_CARD_BUY_BACK_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_604_run_dialog_39"),
	JmpIfDialogOptionBSelected(["EVENT_604_run_dialog_53"]),
	StoreFrogCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 15),
	JmpIfComparisonResultIsLesser(["EVENT_604_run_dialog_51"]),
	RunDialog(dialog_id=DI2334_BRIGHT_CARD_BUY_BACK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(PRIMARY_TEMP_7000, 15),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	Dec7000FromFrogCoins(),
	AddToInventory(BrightCardItem),
	ClearBit(BRIGHT_CARD_SOLD),
	Return(),
	RunDialog(dialog_id=DI2380_LITTLE_SHORT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_604_run_dialog_51"),
	Return(),
	RunDialog(dialog_id=DI2335_BRIGHT_CARD_DECLINE_BUY_BACK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_604_run_dialog_53"),
	Return()
])
