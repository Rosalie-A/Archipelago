# E0245_CHEST_3_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 31, ["EVENT_245_jmp_to_event_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_245_set_var_to_const_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_245_jmp_to_event_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_245_jmp_to_event_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 132, ["EVENT_245_jmp_to_event_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_245_set_var_to_const_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_245_jmp_to_event_31"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_245_jmp_to_event_32"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_245_jmp_to_event_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 301, ["EVENT_245_set_var_to_const_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_245_jmp_to_event_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 331, ["EVENT_245_jmp_to_event_34"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 405, ["EVENT_245_jmp_to_event_42"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_245_jmp_to_event_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_245_jmp_to_event_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_245_jmp_to_event_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_245_set_var_to_const_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_245_jmp_to_event_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_245_jmp_to_event_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_245_jmp_to_event_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 512, ["EVENT_245_set_var_to_const_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_245_set_var_to_const_37"]),
	Return(),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_23"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_245_set_var_to_const_24"),
	JmpToEvent(E3402_COIN_CHEST_MULTI_HIT_3),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_26"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_27"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_28"),
	SetVarToConst(ITEM_ID, DrillClawItem, identifier="EVENT_245_set_var_to_const_29"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_31"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_32"),
	JmpToEvent(E3081_YOU_MISSED, identifier="EVENT_245_jmp_to_event_33"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_34"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_245_set_var_to_const_35"),
	JmpToEvent(E3402_COIN_CHEST_MULTI_HIT_3),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_245_set_var_to_const_37"),
	JmpToEvent(E3402_COIN_CHEST_MULTI_HIT_3),
	SetVarToConst(ITEM_ID, CricketJamItem, identifier="EVENT_245_set_var_to_const_39"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_245_jmp_to_event_41"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_245_jmp_to_event_42"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_43"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_44"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_245_jmp_to_event_45"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_245_jmp_to_event_46"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_245_jmp_to_event_47"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_245_jmp_to_event_48")
])
