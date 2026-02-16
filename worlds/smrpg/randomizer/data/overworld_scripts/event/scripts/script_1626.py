# E1626_MOLEVILLE_CARBO_COOKIE_TRADER
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
	JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1626_store_item_amount_7000_6"]),
    JmpIfBitSet(COOKIE_TRADER_CHECKED, ["EVENT_1626_run_dialog_8"]),
	JmpIfBitSet(CARBO_COOKIE_GIVEN, ["EVENT_1626_purtend_store_check_allowed"]),
	StoreItemAmountTo7000(ShinyStoneItem),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_purtend_store_check_allowed"]),
	StoreItemAmountTo7000(CarboCookieItem),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_purtend_store_check_allowed"]),
    Jmp(["EVENT_1626_store_item_amount_7000_6"]),
    SetBit(COOKIE_TRADER_CHECKED, identifier="EVENT_1626_purtend_store_check_allowed"),
    RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
    Return(),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1626_store_item_amount_7000_6"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_10"]),
	RunDialog(dialog_id=DI1156_BEAN_VALLEY_PLATFORM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_8"),
	Return(),
	RunDialog(dialog_id=DI1159_ASK_TO_TRADE_COOKIE_FOR_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_10"),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_18"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(ShinyStoneItem),
	SetVarToConst(ITEM_ID, CarboCookieItem),
	RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
    JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["traded_stone_for_cookie"]),
	ApplySolidityModToLevel(permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0),
	RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
	Return(identifier="traded_stone_for_cookie"),
	Pause(10, identifier="EVENT_1626_pause_18"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
