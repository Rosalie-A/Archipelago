# E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER
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
	StoreItemAmountTo7000(MysteryEggItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_set_var_to_const_15"]),
	StoreItemAmountTo7000(LambsLureItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_set_var_to_const_12"]),
	StoreItemAmountTo7000(SheepAttackItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_set_var_to_const_8"]),
	SetVarToConst(ITEM_ID, MysteryEggItem),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, SheepAttackItem, identifier="EVENT_3397_set_var_to_const_8"),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, SheepAttackItem, identifier="EVENT_3397_set_var_to_const_12"),
	RemoveOneOfItemFromInventory(LambsLureItem),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, LambsLureItem, identifier="EVENT_3397_set_var_to_const_15"),
	RemoveOneOfItemFromInventory(MysteryEggItem),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM)
])
