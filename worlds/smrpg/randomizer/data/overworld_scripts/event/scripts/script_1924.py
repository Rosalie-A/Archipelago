# E1924_WORLD_MAP_INNER_FACTORY
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
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	JmpIfBitClear(FAST_TRAVEL_ENABLED, ["EVENT_1924_jmp_if_bit_set_3"]),
	SetBit(MAP_INNER_FACTORY),
	JmpIfBitSet(INNER_FACTORY_ROOM_1_COMPLETED, ["EVENT_1924_enter_area_6"], identifier="EVENT_1924_jmp_if_bit_set_3"),
	EnterArea(room_id=R469_FACTORY_GROUNDS_AREA_01, face_direction=NORTHWEST, x=15, y=55, z=5, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, face_direction=NORTHWEST, x=15, y=55, z=5, run_entrance_event=True, identifier="EVENT_1924_enter_area_6"),
	Return()
])
