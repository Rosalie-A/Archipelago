# E0243_CHEST_5_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_243_set_var_to_const_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_243_set_var_to_const_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_243_jmp_to_event_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_243_set_var_to_const_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_243_jmp_to_event_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_243_jmp_to_event_13"]),
	Return(),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_243_set_var_to_const_7"),
	JmpToEvent(E3404_COIN_CHEST_MULTI_HIT_5),
	SetVarToConst(ITEM_ID, RockCandyItem, identifier="EVENT_243_set_var_to_const_9"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_243_jmp_to_event_11"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_243_jmp_to_event_12"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_243_jmp_to_event_13")
])
