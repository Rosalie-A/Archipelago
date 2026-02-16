# E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE
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
	SetVarToRandom(PRIMARY_TEMP_7000, 21),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_2670_jmp_if_bit_set_31"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_set_var_to_const_7"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_set_var_to_const_9"]),
	SetVarToConst(ITEM_ID, WiltShroomItem),
	Return(),
	SetVarToConst(ITEM_ID, RottenMushItem, identifier="EVENT_2670_set_var_to_const_7"),
	Return(),
	SetVarToConst(ITEM_ID, MoldyMushItem, identifier="EVENT_2670_set_var_to_const_9"),
	Return(),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_put_inventory_27"], identifier="EVENT_2670_jmp_if_bit_set_31"),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_put_inventory_29"]),
	SetVarToConst(ITEM_ID, MushroomItem),
	Return(),
	SetVarToConst(ITEM_ID, MidMushroomItem, identifier="EVENT_2670_put_inventory_27"),
	Return(),
	SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="EVENT_2670_put_inventory_29"),
	Return(),
])
