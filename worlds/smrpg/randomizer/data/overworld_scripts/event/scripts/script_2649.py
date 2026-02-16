# E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER
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
	SetVarToRandom(PRIMARY_TEMP_7000, 255),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2649_set_var_to_const_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2649_set_var_to_const_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2649_set_var_to_const_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2649_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2649_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2649_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2649_set_var_to_const_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2649_set_var_to_const_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2649_set_var_to_const_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2649_set_var_to_const_38"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2649_set_var_to_const_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2649_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2649_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2649_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2649_set_var_to_const_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2649_set_var_to_const_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2649_set_var_to_const_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2649_set_var_to_const_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2649_set_var_to_const_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2649_set_var_to_const_58"]),
	Jmp(["EVENT_2649_set_var_to_const_43"]),
	SetVarToConst(ITEM_ID, RockCandyItem, identifier="EVENT_2649_set_var_to_const_23"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, RoyalSyrupItem, identifier="EVENT_2649_set_var_to_const_28"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, RedEssenceItem, identifier="EVENT_2649_set_var_to_const_33"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, KerokeroColaItem, identifier="EVENT_2649_set_var_to_const_38"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="EVENT_2649_set_var_to_const_43"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, WiltShroomItem, identifier="EVENT_2649_set_var_to_const_48"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, RottenMushItem, identifier="EVENT_2649_set_var_to_const_53"),
	Jmp(["EVENT_2649_ret_62"]),
	SetVarToConst(ITEM_ID, MoldyMushItem, identifier="EVENT_2649_set_var_to_const_58"),
	Return(identifier="EVENT_2649_ret_62")
])
