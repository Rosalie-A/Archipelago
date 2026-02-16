# E0219_HILL_GRANT_LOGIC
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
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_213_get_flower"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_213_get_flower_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_213_get_flower_2"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_213_get_flower_3"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_213_get_flower_4"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_213_get_flower_5"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_213_get_flower_6"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_213_get_flower_7"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_213_get_flower_8"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_213_get_flower_9"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_213_get_flower_10"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["EVENT_213_get_flower_11"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_213_get_flower_12"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_213_get_flower_13"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["EVENT_213_get_flower_14"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_213_get_flower_15"]),
    Return(),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_1"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_2"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_3"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_4"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_5"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_6"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_7"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_8"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_9"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_10"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_11"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_12"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_13"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_14"),
    JmpToEvent(E0214_HILL_GET_FLOWER, identifier="EVENT_213_get_flower_15"),
])
