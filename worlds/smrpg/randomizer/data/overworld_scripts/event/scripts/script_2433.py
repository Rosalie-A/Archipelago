# E2433_FOREST_MAZE_TRANSITION
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
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2433_clear_bit_23"]),
	JmpIfBitSet(DIRECTIONAL_7045_6, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_7, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7046_0, ["EVENT_2433_clear_bit_26"]),
	JmpIfBitSet(DIRECTIONAL_7046_1, ["EVENT_2433_set_bit_9"]),
	SetBit(DIRECTIONAL_7045_6, identifier="EVENT_2433_set_bit_9"),
	Jmp(["EVENT_2433_clear_bit_12"]),
	ClearBit(DIRECTIONAL_7045_6, identifier="EVENT_2433_clear_bit_11"),
	ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2433_clear_bit_12"),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	SetBit(DIRECTIONAL_7045_5),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	ClearBit(DIRECTIONAL_7046_1),
	EnterArea(room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, face_direction=NORTHWEST, x=8, y=61, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_4, identifier="EVENT_2433_clear_bit_23"),
	EnterArea(room_id=R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, face_direction=NORTHWEST, x=16, y=40, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7046_0, identifier="EVENT_2433_clear_bit_26"),
	EnterArea(room_id=R231_FOREST_MAZE_SECRET_ENTRANCE, face_direction=NORTHWEST, x=21, y=76, z=0, run_entrance_event=True),
	Return()
])
