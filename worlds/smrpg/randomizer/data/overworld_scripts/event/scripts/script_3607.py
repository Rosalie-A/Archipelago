# E3607_COIN_DIFFERENTIATOR_NPC_8_THROUGH_15
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
	JmpIfVarEqualsConst(ACTIVE_NPC, 28, ["EVENT_3607_jmp_to_event_9"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3607_jmp_to_event_10"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 30, ["EVENT_3607_jmp_to_event_11"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3607_jmp_to_event_12"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 32, ["EVENT_3607_jmp_to_event_13"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 33, ["EVENT_3607_jmp_to_event_14"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 34, ["EVENT_3607_jmp_to_event_15"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 35, ["EVENT_3607_jmp_to_event_16"]),
	JmpToEvent(E0237_FREESTANDING_5_GRANT),
	JmpToEvent(E0236_FREESTANDING_6_GRANT, identifier="EVENT_3607_jmp_to_event_9"),
	JmpToEvent(E0235_FREESTANDING_7_GRANT, identifier="EVENT_3607_jmp_to_event_10"),
	JmpToEvent(E0234_FREESTANDING_8_GRANT, identifier="EVENT_3607_jmp_to_event_11"),
	JmpToEvent(E0233_FREESTANDING_9_GRANT, identifier="EVENT_3607_jmp_to_event_12"),
	JmpToEvent(E0232_FREESTANDING_10_GRANT, identifier="EVENT_3607_jmp_to_event_13"),
	JmpToEvent(E0231_FREESTANDING_11_GRANT, identifier="EVENT_3607_jmp_to_event_14"),
	JmpToEvent(E0230_FREESTANDING_12_GRANT, identifier="EVENT_3607_jmp_to_event_15"),
	JmpToEvent(E0229_FREESTANDING_13_GRANT, identifier="EVENT_3607_jmp_to_event_16")
])
