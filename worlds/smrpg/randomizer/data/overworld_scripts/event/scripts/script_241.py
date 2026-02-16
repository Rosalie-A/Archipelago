# E0241_FREESTANDING_1_GRANT
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_241_jmp_to_event_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_241_jmp_to_event_36"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 72, ["EVENT_241_jmp_to_event_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 73, ["EVENT_241_jmp_to_event_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 79, ["EVENT_241_jmp_to_event_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 101, ["EVENT_241_jmp_to_event_40"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_241_jmp_to_event_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_241_jmp_to_event_42"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 163, ["EVENT_241_jmp_to_event_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 166, ["EVENT_241_jmp_to_event_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 167, ["EVENT_241_jmp_to_event_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 168, ["EVENT_241_set_var_to_const_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 172, ["EVENT_241_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 176, ["EVENT_241_jmp_to_event_50"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 187, ["EVENT_241_jmp_to_event_51"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 195, ["EVENT_241_set_var_to_const_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 197, ["EVENT_241_set_var_to_const_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 200, ["EVENT_241_set_var_to_const_56"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 207, ["EVENT_241_jmp_to_event_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 286, ["EVENT_241_jmp_to_event_59"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 316, ["EVENT_241_set_var_to_const_60"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_241_jmp_to_event_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 324, ["EVENT_241_set_var_to_const_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 345, ["EVENT_241_set_var_to_const_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 358, ["EVENT_241_jmp_to_event_67"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 361, ["EVENT_241_jmp_to_event_68"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 378, ["EVENT_241_jmp_to_event_69"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_241_jmp_to_event_70"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 380, ["EVENT_241_jmp_to_event_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 381, ["EVENT_241_jmp_to_event_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 383, ["EVENT_241_jmp_to_event_73"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_241_jmp_to_event_74"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_241_jmp_to_event_75"]),
	Return(),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_35"),
	JmpToEvent(E1294_COLLECT_FREESTANDING_SMALL_FROG_COIN, identifier="EVENT_241_jmp_to_event_36"),
	JmpToEvent(E2816_ASYNC_NO_ANIMATION_FROG_COIN, identifier="EVENT_241_jmp_to_event_37"),
	JmpToEvent(E2817_ASYNC_NO_ANIMATION_FLOWER, identifier="EVENT_241_jmp_to_event_38"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_241_jmp_to_event_39"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_241_jmp_to_event_40"),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_241_jmp_to_event_41"),
	JmpToEvent(E3938_FREESTANDING_CROWN, identifier="EVENT_241_jmp_to_event_42"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_241_jmp_to_event_43"),
	JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM, identifier="EVENT_241_jmp_to_event_44"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_241_jmp_to_event_45"),
	SetVarToConst(ITEM_ID, RoyalSyrupItem, identifier="EVENT_241_set_var_to_const_46"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="EVENT_241_set_var_to_const_48"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM, identifier="EVENT_241_jmp_to_event_50"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_51"),
	SetVarToConst(ITEM_ID, ElderKeyItem, identifier="EVENT_241_set_var_to_const_52"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	SetVarToConst(ITEM_ID, MasherItem, identifier="EVENT_241_set_var_to_const_54"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	SetVarToConst(ITEM_ID, ChompItem, identifier="EVENT_241_set_var_to_const_56"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_241_jmp_to_event_58"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_59"),
	SetVarToConst(ITEM_ID, ShedKeyItem, identifier="EVENT_241_set_var_to_const_60"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_241_jmp_to_event_62"),
	SetVarToConst(ITEM_ID, TempleKeyItem, identifier="EVENT_241_set_var_to_const_63"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	SetVarToConst(ITEM_ID, SignalRingItem, identifier="EVENT_241_set_var_to_const_65"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_67"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_68"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_69"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_70"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_241_jmp_to_event_71"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_241_jmp_to_event_72"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_241_jmp_to_event_73"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_241_jmp_to_event_74"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_241_jmp_to_event_75")
])
