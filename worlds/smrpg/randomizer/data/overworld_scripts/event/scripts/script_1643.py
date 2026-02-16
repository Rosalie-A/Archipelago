# E1643_PURTEND_STORE
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1643_run_dialog_5"]),
    JmpIfBitSet(PURTEND_STORE_CHECK_DONE, ["EVENT_1643_store_checked"]),
	JmpIfBitSet(CARBO_COOKIE_GIVEN, ["EVENT_1643_purtend_store_check_allowed"]),
	StoreItemAmountTo7000(FireworksItem),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_purtend_store_check_allowed"]),
	StoreItemAmountTo7000(ShinyStoneItem),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_purtend_store_check_allowed"]),
	StoreItemAmountTo7000(CarboCookieItem),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_purtend_store_check_allowed"]),
    Jmp(["EVENT_1643_run_dialog_30"]),
    SetBit(PURTEND_STORE_CHECK_DONE, identifier="EVENT_1643_purtend_store_check_allowed"),
    RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
    Return(),
	RunDialog(dialog_id=DI1160_PURTEND_STORE_DISABLED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_store_checked"),
	Return(),
	RunDialog(dialog_id=DI1124_PURTEND_STORE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_5"),
	JmpIfDialogOptionBSelected(["EVENT_1643_pause_26"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_run_dialog_23"]),
	StoreItemAmountTo7000(FireworksItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_run_dialog_30"]),
	RunDialog(dialog_id=DI1295_PURTEND_STORE_PROMPT_TO_TRADE_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1643_pause_26"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FireworksItem),
	RunDialog(dialog_id=DI1154_PURTEND_STORE_THANKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, ShinyStoneItem),
	SetVarToConst(PRIMARY_TEMP_7000, 1155),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	Return(),
	RunDialog(dialog_id=DI1153_PURTEND_STORE_SOLD_OUT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_23"),
	RunDialogForDuration(dialog_id=DI1154_PURTEND_STORE_THANKS, duration=1, sync=False),
	Return(),
	Pause(10, identifier="EVENT_1643_pause_26"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1154_PURTEND_STORE_THANKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1296_PURTEND_STORE_NEED_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_30"),
	Return()
])
