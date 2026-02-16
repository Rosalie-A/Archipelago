# E3849_WORLD_MAP_ROSE_WAY
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
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	UnknownCommand(bytearray(b'\xfdE')),
	JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 18, ["EVENT_3849_set_var_to_const_8"]),
	SetVarToConst(UNKNOWN_7036, 0),
	EnterArea(room_id=R079_ROSE_WAY_MAIN_AREA, face_direction=NORTHEAST, x=4, y=56, z=0, run_entrance_event=True),
	Return(),
	SetVarToConst(UNKNOWN_7036, 4493, identifier="EVENT_3849_set_var_to_const_8"),
	EnterArea(room_id=R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED, face_direction=SOUTHWEST, x=26, y=77, z=0, run_entrance_event=True),
	Return()
])
