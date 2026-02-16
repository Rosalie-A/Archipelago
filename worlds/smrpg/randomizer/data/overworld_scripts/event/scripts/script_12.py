# E0012_SET_70A7_TO_RANDOM_TIER_4_EQUIP
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_12_set_var_to_const_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_12_set_var_to_const_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_12_set_var_to_const_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_12_set_var_to_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_12_set_var_to_const_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_12_set_var_to_const_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_12_set_var_to_const_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_12_set_var_to_const_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_12_set_var_to_const_28"]),
	SetVarToConst(ITEM_ID, MasherItem),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SuperSuitItem, identifier="EVENT_12_set_var_to_const_12"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LazyShellItem2, identifier="EVENT_12_set_var_to_const_14"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, AttackScarfItem, identifier="EVENT_12_set_var_to_const_16"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LazyShellItem, identifier="EVENT_12_set_var_to_const_18"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, QuartzCharmItem, identifier="EVENT_12_set_var_to_const_20"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SafetyRingItem, identifier="EVENT_12_set_var_to_const_22"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FryingPanItem, identifier="EVENT_12_set_var_to_const_24"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, JinxBeltItem, identifier="EVENT_12_set_var_to_const_26"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ExpBoosterItem, identifier="EVENT_12_set_var_to_const_28"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
