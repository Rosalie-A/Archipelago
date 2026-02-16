# E0244_CHEST_4_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_244_set_var_to_const_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_244_set_var_to_const_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_244_jmp_to_event_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_244_jmp_to_event_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_244_set_var_to_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_244_jmp_to_event_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_244_jmp_to_event_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_244_set_var_to_const_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_244_jmp_to_event_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_244_jmp_to_event_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_244_jmp_to_event_24"]),
	Return(),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_244_set_var_to_const_12"),
	JmpToEvent(E3403_COIN_CHEST_MULTI_HIT_4),
	SetVarToConst(ITEM_ID, StarGunItem, identifier="EVENT_244_set_var_to_const_14"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_244_jmp_to_event_16"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_jmp_to_event_17"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_244_set_var_to_const_18"),
	JmpToEvent(E3403_COIN_CHEST_MULTI_HIT_4),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_244_jmp_to_event_20"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_244_jmp_to_event_21"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_jmp_to_event_22"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_jmp_to_event_23"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_jmp_to_event_24")
])
