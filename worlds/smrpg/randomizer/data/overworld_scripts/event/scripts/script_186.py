# E0186_PARTY_JOIN_LOGIC
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, ["EVENT_186_jmp_to_event_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R205_MUSHROOM_WAY_AREA_03, ["EVENT_186_jmp_to_event_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, ["EVENT_186_jmp_to_event_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM, ["EVENT_186_jmp_to_event_9"]),
	Return(),
	JmpToEvent(E0197_TOADSTOOL_JOINS_CONTAINER, identifier="EVENT_186_jmp_to_event_6"),
	JmpToEvent(E0194_MALLOW_JOINS_CONTAINER, identifier="EVENT_186_jmp_to_event_7"),
	JmpToEvent(E0195_GENO_JOINS_CONTAINER, identifier="EVENT_186_jmp_to_event_8"),
	JmpToEvent(E0196_BOWSER_JOINS_CONTAINER, identifier="EVENT_186_jmp_to_event_9")
])
