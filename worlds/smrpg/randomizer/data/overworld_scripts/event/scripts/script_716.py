# E0716_ENTER_JUMPING_KIDS_HOUSE
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
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["jumping_kids_house_mk_not_liberated_yet"]),
    JmpIfBitClear(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED, ["jumping_kid_load_occupied_house"]),
    JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED, ["jumping_kid_load_normal_house"]),
    JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["jumping_kid_load_normal_house"], identifier="jumping_kids_house_mk_not_liberated_yet"),
    EnterArea(R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, NORTHWEST, 6, 24, 2, run_entrance_event=True, identifier="jumping_kid_load_occupied_house"),
    Return(),
    EnterArea(R488_MUSHROOM_KINGDOM_JUMPING_KIDS_HOUSE_1F, NORTHWEST, 6, 24, 2, run_entrance_event=True, identifier="jumping_kid_load_normal_house"),
    Return()
])
