# E3818_WORLD_MAP_MUSHROOM_WAY
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
	JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 10, ["EVENT_3818_jmp_if_bit_clear_4"]),
	EnterArea(room_id=R203_MUSHROOM_WAY_AREA_01, face_direction=SOUTHEAST, x=3, y=28, z=0, run_entrance_event=True, identifier="EVENT_3818_enter_area_2"),
	Return(),
	JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_3818_enter_area_2"], identifier="EVENT_3818_jmp_if_bit_clear_4"),
	EnterArea(room_id=R205_MUSHROOM_WAY_AREA_03, face_direction=SOUTHWEST, x=28, y=89, z=0, run_entrance_event=True),
	Return()
])
