# E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1
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
	JmpIfRandom1of2(["EVENT_622_ret_10"]),
	JmpIfRandom2of3(['EVENT_622_set_var_to_const_5', 'EVENT_622_set_var_to_const_8']),
	SetVarToConst(PRIMARY_TEMP_7000, 30),
	JmpToEvent(E0159_NPC_QUEST_GRANT_COINS),
	Return(),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="EVENT_622_set_var_to_const_5"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	SetVarToConst(ITEM_ID, MidMushroomItem, identifier="EVENT_622_set_var_to_const_8"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(identifier="EVENT_622_ret_10")
])
