# E0239_FREESTANDING_3_GRANT
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_239_jmp_to_event_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 79, ["EVENT_239_jmp_to_event_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_239_jmp_to_event_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 187, ["EVENT_239_jmp_to_event_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 207, ["EVENT_239_jmp_to_event_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_239_jmp_to_event_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 378, ["EVENT_239_jmp_to_event_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_239_jmp_to_event_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 380, ["EVENT_239_jmp_to_event_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 381, ["EVENT_239_jmp_to_event_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_239_jmp_to_event_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_239_jmp_to_event_25"]),
	Return(),
	JmpToEvent(E1294_COLLECT_FREESTANDING_SMALL_FROG_COIN, identifier="EVENT_239_jmp_to_event_14"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_15"),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_239_jmp_to_event_16"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_239_jmp_to_event_17"),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_239_jmp_to_event_18"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_19"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_20"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_21"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_22"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_23"),
	JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_239_jmp_to_event_24"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_239_jmp_to_event_25")
])
