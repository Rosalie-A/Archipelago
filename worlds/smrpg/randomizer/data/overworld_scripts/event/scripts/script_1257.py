# E1257_CHECKERBOARD_ROOM_COIN_CLONE
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
    CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_7, ["EVENT_1257_jump_to_freestanding_5_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_8, ["EVENT_1257_jump_to_freestanding_6_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_9, ["EVENT_1257_jump_to_freestanding_7_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_10, ["EVENT_1257_jump_to_freestanding_8_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_11, ["EVENT_1257_jump_to_freestanding_9_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_12, ["EVENT_1257_jump_to_freestanding_10_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_13, ["EVENT_1257_jump_to_freestanding_11_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_14, ["EVENT_1257_jump_to_freestanding_12_grant"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, NPC_15, ["EVENT_1257_jump_to_freestanding_13_grant"]),
    Return(),
    JmpToEvent(E0237_FREESTANDING_5_GRANT, identifier="EVENT_1257_jump_to_freestanding_5_grant"),
    JmpToEvent(E0236_FREESTANDING_6_GRANT, identifier="EVENT_1257_jump_to_freestanding_6_grant"),
    JmpToEvent(E0235_FREESTANDING_7_GRANT, identifier="EVENT_1257_jump_to_freestanding_7_grant"),
    JmpToEvent(E0234_FREESTANDING_8_GRANT, identifier="EVENT_1257_jump_to_freestanding_8_grant"),
    JmpToEvent(E0233_FREESTANDING_9_GRANT, identifier="EVENT_1257_jump_to_freestanding_9_grant"),
    JmpToEvent(E0232_FREESTANDING_10_GRANT, identifier="EVENT_1257_jump_to_freestanding_10_grant"),
    JmpToEvent(E0231_FREESTANDING_11_GRANT, identifier="EVENT_1257_jump_to_freestanding_11_grant"),
    JmpToEvent(E0230_FREESTANDING_12_GRANT, identifier="EVENT_1257_jump_to_freestanding_12_grant"),
    JmpToEvent(E0229_FREESTANDING_13_GRANT, identifier="EVENT_1257_jump_to_freestanding_13_grant"),
])
