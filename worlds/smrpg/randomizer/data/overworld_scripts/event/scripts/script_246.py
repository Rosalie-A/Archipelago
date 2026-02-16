# E0246_CHEST_2_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 31, ["EVENT_246_jmp_to_event_51"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 60, ["EVENT_246_jmp_to_event_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 78, ["EVENT_246_jmp_to_event_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_246_set_var_to_const_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 87, ["EVENT_246_jmp_to_event_56"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_246_jmp_to_event_57"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 94, ["EVENT_246_jmp_to_event_57"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 100, ["EVENT_246_jmp_to_event_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 114, ["EVENT_246_jmp_to_event_59"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_246_jmp_to_event_60"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_246_jmp_to_event_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_246_set_var_to_const_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 132, ["EVENT_246_jmp_to_event_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 138, ["EVENT_246_jmp_to_event_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_246_set_var_to_const_66"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 175, ["EVENT_246_set_var_to_const_68"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 184, ["EVENT_246_jmp_to_event_70"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_246_jmp_to_event_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 203, ["EVENT_246_set_var_to_const_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 204, ["EVENT_246_jmp_to_event_74"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_246_jmp_to_event_75"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_246_set_var_to_const_76"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 252, ["EVENT_246_jmp_to_event_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 262, ["EVENT_246_jmp_to_event_79"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 270, ["EVENT_246_jmp_to_event_80"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 288, ["EVENT_246_jmp_to_event_81"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 301, ["EVENT_246_jmp_to_event_82"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_246_jmp_to_event_83"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 331, ["EVENT_246_jmp_to_event_84"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 335, ["EVENT_246_jmp_to_event_85"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 349, ["EVENT_246_jmp_to_event_86"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 355, ["EVENT_246_jmp_to_event_87"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 366, ["EVENT_246_jmp_to_event_88"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 372, ["EVENT_246_jmp_to_event_89"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 373, ["EVENT_246_jmp_to_event_90"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 384, ["EVENT_246_set_var_to_const_91"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 405, ["EVENT_246_jmp_to_event_93"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 410, ["EVENT_246_jmp_to_event_94"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 419, ["EVENT_246_jmp_to_event_95"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_246_jmp_to_event_96"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_246_set_var_to_const_97"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_246_jmp_to_event_99"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_246_set_var_to_const_66"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 451, ["EVENT_246_jmp_to_event_100"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_246_jmp_to_event_101"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_246_jmp_to_event_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_246_jmp_to_event_103"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 475, ["EVENT_246_jmp_to_event_104"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_246_jmp_to_event_105"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 498, ["EVENT_246_jmp_to_event_59"]),
	Return(),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_51"),
	JmpToEvent(E3124_MIMIC_1_CHEST, identifier="EVENT_246_jmp_to_event_52"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_53"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_54"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_56"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_57"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_58"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_59"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_60"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_61"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_62"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_64"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_65"),
	SetVarToConst(ITEM_ID, SuperSlapItem, identifier="EVENT_246_set_var_to_const_66"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_68"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3126_MIMIC_2_CHEST, identifier="EVENT_246_jmp_to_event_70"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_71"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_72"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_74"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_75"),
	SetVarToConst(ITEM_ID, SonicCymbalItem, identifier="EVENT_246_set_var_to_const_76"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_78"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_79"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_80"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_81"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_82"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_83"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_84"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_85"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_86"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_87"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_88"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_89"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_90"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_91"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_93"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_94"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_95"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_96"),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_set_var_to_const_97"),
	JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_99"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_100"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_101"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_102"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_103"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_jmp_to_event_104"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_jmp_to_event_105")
])
