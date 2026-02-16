# E1872_FIREWORKS_HOUSE_BUY_ITEM
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
	JmpIfBitSet(FIREWORKS_HOUSE_ITEM_SOLD, ["EVENT_1872_run_dialog_44"]),
	JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1872_run_dialog_31"]),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1872_run_dialog_31"]),
	StoreItemAmountTo7000(FireworksItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1872_jmp_if_bit_set_9"]),
	RunDialog(dialog_id=DI1297_CANT_SELL_MORE_THAN_ONE_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(CARBO_COOKIE_GIVEN, ["EVENT_1872_run_dialog_10"], identifier="EVENT_1872_jmp_if_bit_set_9"),
	RunDialog(dialog_id=DI1289_FIREWORKS_GUY_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1872_run_dialog_10"),
	JmpIfDialogOptionBSelected(["EVENT_1872_pause_28"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 500),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1872_play_sound_19"]),
	RunDialog(dialog_id=DI1293_FIREWORKS_GUY_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1872_run_dialog_17"),
	Return(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6, identifier="EVENT_1872_play_sound_19"),
	SetVarToConst(PRIMARY_TEMP_7000, 500),
	Dec7000FromCoins(),
	JmpIfVarEqualsConst(FIREWORKS_COUNTER, 5, ["EVENT_1872_play_sound_24"]),
	Inc(FIREWORKS_COUNTER),
	PlaySound(sound=SO085_FLOWER, channel=6, identifier="EVENT_1872_play_sound_24"),
	RunDialog(dialog_id=DI1294_GOT_FIREWORKS, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(FireworksItem),
	Return(),
	Pause(10, identifier="EVENT_1872_pause_28"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(),
	RunDialog(dialog_id=DI1288_FIREWORKS_GUY_MYSTERY_ITEM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1872_run_dialog_31"),
	JmpIfDialogOptionBSelected(["EVENT_1872_pause_28"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 500),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1872_set_var_to_const_39"]),
	Jmp(["EVENT_1872_run_dialog_17"]),
	SetVarToConst(PRIMARY_TEMP_7000, 500, identifier="EVENT_1872_set_var_to_const_39"),
	Dec7000FromCoins(),
	SetBit(FIREWORKS_HOUSE_ITEM_SOLD),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return(),
	RunDialog(dialog_id=DI1287_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1872_run_dialog_44"),
	Return()
])
