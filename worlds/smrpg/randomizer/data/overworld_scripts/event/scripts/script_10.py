# E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP
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
	SetVarToRandom(PRIMARY_TEMP_7000, 20),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_10_set_var_to_const_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_10_set_var_to_const_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_10_set_var_to_const_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_10_set_var_to_const_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_10_set_var_to_const_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_10_set_var_to_const_32"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_10_set_var_to_const_34"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_10_set_var_to_const_36"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_10_set_var_to_const_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_10_set_var_to_const_40"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_10_set_var_to_const_42"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["EVENT_10_set_var_to_const_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_10_set_var_to_const_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_10_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["EVENT_10_set_var_to_const_50"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_10_set_var_to_const_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_10_set_var_to_const_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_10_set_var_to_const_56"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 18, ["EVENT_10_set_var_to_const_58"]),
	SetVarToConst(ITEM_ID, DoublePunchItem),
	Return(),
	SetVarToConst(ITEM_ID, SafetyBadgeItem, identifier="EVENT_10_set_var_to_const_22"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, TroopaPinItem, identifier="EVENT_10_set_var_to_const_24"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireDressItem, identifier="EVENT_10_set_var_to_const_26"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FirePantsItem, identifier="EVENT_10_set_var_to_const_28"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireShirtItem, identifier="EVENT_10_set_var_to_const_30"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ParasolItem, identifier="EVENT_10_set_var_to_const_32"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, RibbitStickItem, identifier="EVENT_10_set_var_to_const_34"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, TroopaShellItem, identifier="EVENT_10_set_var_to_const_36"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, GhostMedalItem, identifier="EVENT_10_set_var_to_const_38"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HandCannonItem, identifier="EVENT_10_set_var_to_const_40"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, DrillClawItem, identifier="EVENT_10_set_var_to_const_42"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FuzzyDressItem, identifier="EVENT_10_set_var_to_const_44"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FuzzyPantsItem, identifier="EVENT_10_set_var_to_const_46"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FuzzyShirtItem, identifier="EVENT_10_set_var_to_const_48"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, StarCapeItem, identifier="EVENT_10_set_var_to_const_50"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SlapGloveItem, identifier="EVENT_10_set_var_to_const_52"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SuperHammerItem, identifier="EVENT_10_set_var_to_const_54"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, WhompGloveItem, identifier="EVENT_10_set_var_to_const_56"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, AmuletItem, identifier="EVENT_10_set_var_to_const_58"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
