# E2272_MOLEVILLE_TREASURE_SHOP
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
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_2272_jmp_if_bit_clear_57"]),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_2272_jmp_if_bit_clear_22"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_6"]),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2915_TREASURE_SELLER_2ND_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_21"], identifier="EVENT_2272_jmp_if_bit_set_6"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_21"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_19"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Jmp(["EVENT_2272_jmp_21"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_19"),
	Jmp(["EVENT_2272_jmp_21"]),
	Jmp(["EVENT_2272_jmp_if_bit_set_108"], identifier="EVENT_2272_jmp_21"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_27"], identifier="EVENT_2272_jmp_if_bit_clear_22"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_27"]),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2905_TREASURE_SELLER_3RD_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_42"], identifier="EVENT_2272_jmp_if_bit_set_27"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_42"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_40"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Jmp(["EVENT_2272_jmp_if_bit_set_42"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_40"),
	Jmp(["EVENT_2272_jmp_if_bit_set_42"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_108"], identifier="EVENT_2272_jmp_if_bit_set_42"),
	RunDialog(dialog_id=DI2908_TREASURE_SELLER_ITEM_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_108"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_40"]),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_2_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Jmp(["EVENT_2272_jmp_if_bit_set_108"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2272_jmp_if_bit_set_108"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_63"], identifier="EVENT_2272_jmp_if_bit_clear_57"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_63"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2272_jmp_if_bit_set_63"]),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2902_TREASURE_SELLER_ALL_ITEMS_UNLOCKED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_78"], identifier="EVENT_2272_jmp_if_bit_set_63"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_78"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_76"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(LuckyJewelItem),
	Jmp(["EVENT_2272_jmp_if_bit_set_78"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_76"),
	Jmp(["EVENT_2272_jmp_if_bit_set_78"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_93"], identifier="EVENT_2272_jmp_if_bit_set_78"),
	RunDialog(dialog_id=DI2908_TREASURE_SELLER_ITEM_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_93"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_91"]),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_2_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Jmp(["EVENT_2272_jmp_if_bit_set_93"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_91"),
	Jmp(["EVENT_2272_jmp_if_bit_set_93"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2272_jmp_if_bit_set_108"], identifier="EVENT_2272_jmp_if_bit_set_93"),
	RunDialog(dialog_id=DI2914_TREASURE_SELLER_ITEM_3, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_108"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 300),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_106"]),
	SetVarToConst(PRIMARY_TEMP_7000, 300),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_3_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	Jmp(["EVENT_2272_jmp_if_bit_set_108"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_106"),
	Jmp(["EVENT_2272_jmp_if_bit_set_108"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2272_run_dialog_113"], identifier="EVENT_2272_jmp_if_bit_set_108"),
	JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_run_dialog_113"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_run_dialog_113"]),
	RunDialog(dialog_id=DI2907_TREASURE_SELLER_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2909_TREASURE_SELLER_ALL_IVE_GOT_FOR_NOW, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_113"),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_2272_run_dialog_118"]),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_2272_run_dialog_120"]),
	RunDialog(dialog_id=DI2915_TREASURE_SELLER_2ND_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2902_TREASURE_SELLER_ALL_ITEMS_UNLOCKED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_118"),
	Return(),
	RunDialog(dialog_id=DI2905_TREASURE_SELLER_3RD_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_120"),
	Return()
])
