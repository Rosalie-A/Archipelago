# E0290_MUSHROOM_KINGDOM_SHOP_LOGIC
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
	JmpIfBitSet(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, ["EVENT_290_jmp_if_bit_clear_4"]),
	SetBit(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return(),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_290_jmp_to_event_7"], identifier="EVENT_290_jmp_if_bit_clear_4"),
    JmpIfBitSet(RARE_FROG_COIN_EXCHANGED, ["EVENT_290_jmp_to_event_7"]),
	StoreItemAmountTo7000(RareFrogCoinItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_290_remove_one_from_inventory_8"]),
	JmpToEvent(E0284_OPEN_MUSHROOM_KINGDOM_SHOP, identifier="EVENT_290_jmp_to_event_7"),
	RemoveOneOfItemFromInventory(RareFrogCoinItem, identifier="EVENT_290_remove_one_from_inventory_8"),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
    SetBit(RARE_FROG_COIN_EXCHANGED),
    RunEventAsSubroutine(E1254_UNLOCK_SEWER_BY_RFC),
	Return()
])
