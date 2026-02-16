# E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT
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
	StoreItemAmountTo7000(FireworksItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3100_set_var_to_const_12"]),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3100_set_var_to_const_8"]),
	SetVarToConst(FIREWORKS_COUNTER, 5),
	SetVarToConst(ITEM_ID, FireworksItem),
	JmpToEvent(E0883_CHEST_ITEM_BAG_PACKET),
	Return(),
	SetVarToConst(ITEM_ID, CarboCookieItem, identifier="EVENT_3100_set_var_to_const_8"),
	ApplySolidityModToLevel(permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0),
	RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
	RemoveOneOfItemFromInventory(ShinyStoneItem),
	JmpToEvent(E0893_CHEST_COOKIE_PACKET),
	Return(),
	SetVarToConst(ITEM_ID, ShinyStoneItem, identifier="EVENT_3100_set_var_to_const_12"),
	RemoveOneOfItemFromInventory(FireworksItem),
	JmpToEvent(E0951_CRYSTAL_CHEST_PACKET),
	Return()
])
