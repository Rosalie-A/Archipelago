# E0252_NPC_QUEST_2_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_252_set_var_to_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_252_jmp_to_event_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 75, ["EVENT_252_set_var_to_const_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 108, ["EVENT_252_jmp_to_event_ss"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 143, ["EVENT_252_set_var_to_const_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_252_jmp_to_event_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 189, ["EVENT_252_set_var_to_const_free1"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_252_set_var_to_const_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_252_set_var_to_const_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_252_set_var_to_const_tower"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 206, ["EVENT_252_set_var_to_const_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_252_dojo_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 328, ["EVENT_252_set_var_to_const_34"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 336, ["EVENT_252_jmp_to_event_36"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 346, ["EVENT_252_set_var_to_const_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 351, ["EVENT_252_set_var_to_const_131"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 397, ["EVENT_252_set_var_to_const_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 399, ["EVENT_252_set_var_to_const_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 414, ["EVENT_252_set_var_to_const_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 483, ["EVENT_252_set_var_to_const_32"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 491, ["EVENT_252_set_var_to_const_32"]),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 3, identifier="EVENT_252_set_var_to_const_18"),
	JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
	JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT, identifier="EVENT_252_jmp_to_event_22"),
	SetVarToConst(PRIMARY_TEMP_7000, 10, identifier="EVENT_252_set_var_to_const_23"),
	JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
	SetVarToConst(ITEM_ID, FlowerJarItem, identifier="EVENT_252_set_var_to_const_25"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	JmpToEvent(E3933_GET_RING, identifier="EVENT_252_jmp_to_event_27"),
	SetVarToConst(ITEM_ID, Stella023Item, identifier="EVENT_252_set_var_to_const_tower"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	JmpToEvent(E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS, identifier="EVENT_252_jmp_to_event_ss"),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="EVENT_252_set_var_to_const_free1"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FlowerTabItem, identifier="EVENT_252_set_var_to_const_28"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, WalletItem, identifier="EVENT_252_set_var_to_const_30"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, TeamworkBandItem, identifier="EVENT_252_dojo_postgame"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CricketPieItem, identifier="EVENT_252_set_var_to_const_32"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FlowerTabItem, identifier="EVENT_252_set_var_to_const_34"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT, identifier="EVENT_252_jmp_to_event_36"),
	SetVarToConst(ITEM_ID, RedEssenceItem, identifier="EVENT_252_set_var_to_const_37"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CrystalShardItem, identifier="EVENT_252_set_var_to_const_131"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SuperSuitItem, identifier="EVENT_252_set_var_to_const_39"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, GhostMedalItem, identifier="EVENT_252_set_var_to_const_41"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CastleKey1Item, identifier="EVENT_252_set_var_to_const_43"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
