# E0251_NPC_QUEST_3_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_251_set_var_to_const_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 34, ["EVENT_251_set_var_to_const_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_251_jmp_to_event_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_251_jmp_to_event_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 189, ["EVENT_252_set_var_to_const_free2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_251_jmp_to_event_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_251_jmp_to_event_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 336, ["EVENT_251_set_var_to_const_15"]),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 5, identifier="EVENT_251_set_var_to_const_8"),
	JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
	SetVarToConst(ITEM_ID, YoshiCookieItem, identifier="EVENT_251_set_var_to_const_10"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT, identifier="EVENT_251_jmp_to_event_12"),
	JmpToEvent(E3931_GET_SHOES, identifier="EVENT_251_jmp_to_event_13"),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="EVENT_252_set_var_to_const_free2"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	JmpToEvent(E0157_NPC_QUEST_GRANT_1_FROG_COIN, identifier="EVENT_251_jmp_to_event_14"),
	SetVarToConst(ITEM_ID, FryingPanItem, identifier="EVENT_251_set_var_to_const_15"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
