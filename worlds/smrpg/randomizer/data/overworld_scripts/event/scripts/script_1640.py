# E1640_INITIATE_MINECART_FREEPLAY
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
	JmpIfBitSet(PAID_FOR_MINECART, ["EVENT_1640_run_dialog_46"]),
	RunDialog(dialog_id=DI1126_MINECART_PAYMENT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 10),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1640_store_coin_amount_7000_9"]),
	RunDialog(dialog_id=DI1129_MINECART_NO_COIN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	StoreCoinCountTo7000(identifier="EVENT_1640_store_coin_amount_7000_9"),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsLesser(["EVENT_1640_store_7000_minecart_timer_18"]),
	JmpIfBitClear(TEMP_7042_2, ["EVENT_1640_store_7000_minecart_timer_18"]),
	Set7000ToMinecartTimer(),
	RunDialogForDuration(dialog_id=DI1101_MINECART_HIGH_SCORE, duration=0, sync=False),
	RunDialogForDuration(dialog_id=DI1173_TROLLEY_RIDE_PAY_PROMPT, duration=1, sync=False),
	JmpIfDialogOptionBOrCSelected(['EVENT_1640_set_var_to_const_33', 'EVENT_1640_ret_45']),
	Jmp(["EVENT_1640_set_var_to_const_30"]),
	Set7000ToMinecartTimer(identifier="EVENT_1640_store_7000_minecart_timer_18"),
	RunDialogForDuration(dialog_id=DI1127_MINECART_CONFIRM, duration=1, sync=False),
	JmpIfDialogOptionBSelected(["EVENT_1640_pause_43"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetBit(TEMP_7042_2),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsLesser(["EVENT_1640_set_var_to_const_30"]),
	RunDialog(dialog_id=DI1130_WAGER_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	RunDialogForDuration(dialog_id=DI1131_WAGER_CHOICE, duration=1, sync=False, identifier="EVENT_1640_run_dialog_duration_28"),
	JmpIfDialogOptionBOrCSelected(['EVENT_1640_set_var_to_const_33', 'EVENT_1640_run_dialog_41']),
	SetVarToConst(PRIMARY_TEMP_7000, 10, identifier="EVENT_1640_set_var_to_const_30"),
	ClearBit(MINECART_INITIATE_FREEPLAY),
	Jmp(["EVENT_1640_run_dialog_35"]),
	SetVarToConst(PRIMARY_TEMP_7000, 30, identifier="EVENT_1640_set_var_to_const_33"),
	SetBit(MINECART_INITIATE_FREEPLAY),
	RunDialog(dialog_id=DI1132_MINECART_PAYMENT_CONFIRM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1640_run_dialog_35"),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	Dec7000FromCoins(),
	SetBit(TEMP_7044_5),
	SetBit(PAID_FOR_MINECART),
	Return(),
	RunDialog(dialog_id=DI1133_WAGER_EXPLANATION, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_1640_run_dialog_41"),
	Jmp(["EVENT_1640_run_dialog_duration_28"]),
	Pause(10, identifier="EVENT_1640_pause_43"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(identifier="EVENT_1640_ret_45"),
	RunDialog(dialog_id=DI1134_MINECART_ALREADY_PAID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1640_run_dialog_46"),
	SetBit(TEMP_7044_5),
	Return()
])
