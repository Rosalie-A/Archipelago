# E3843_WORLD_MAP_MUSHROOM_KINGDOM
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
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_3843_jmp_if_bit_set_7"]),
	JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 9, ["EVENT_3843_enter_area_5"], identifier="EVENT_3843_jmp_if_var_equals_const_2"),
	EnterArea(room_id=R191_MUSHROOM_KINGDOM_OUTSIDE, face_direction=NORTHWEST, x=21, y=122, z=2, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R191_MUSHROOM_KINGDOM_OUTSIDE, face_direction=NORTHEAST, x=2, y=102, z=2, run_entrance_event=True, identifier="EVENT_3843_enter_area_5"),
	Return(),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_3843_jmp_if_var_equals_const_2"], identifier="EVENT_3843_jmp_if_bit_set_7"),
	JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 9, ["EVENT_3843_enter_area_11"]),
	EnterArea(room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, face_direction=NORTHWEST, x=21, y=122, z=2, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, face_direction=NORTHEAST, x=2, y=102, z=2, run_entrance_event=True, identifier="EVENT_3843_enter_area_11"),
	Return()
])
