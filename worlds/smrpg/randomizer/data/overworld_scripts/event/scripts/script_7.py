# E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE
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
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_7_set_var_to_const_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_7_set_var_to_const_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_7_set_var_to_const_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_7_set_var_to_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_7_set_var_to_const_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_7_set_var_to_const_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_7_set_var_to_const_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_7_set_var_to_const_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_7_set_var_to_const_28"]),
	SetVarToConst(ITEM_ID, MaxMushroomItem),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, RoyalSyrupItem, identifier="EVENT_7_set_var_to_const_12"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, YoshiAdeItem, identifier="EVENT_7_set_var_to_const_14"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireBombItem, identifier="EVENT_7_set_var_to_const_16"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, IceBombItem, identifier="EVENT_7_set_var_to_const_18"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FlowerJarItem, identifier="EVENT_7_set_var_to_const_20"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MukuCookieItem, identifier="EVENT_7_set_var_to_const_22"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MegalixirItem, identifier="EVENT_7_set_var_to_const_24"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CrystallineItem, identifier="EVENT_7_set_var_to_const_26"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, PowerBlastItem, identifier="EVENT_7_set_var_to_const_28"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
