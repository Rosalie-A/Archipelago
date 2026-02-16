# E3206_SEA_PIPE_TO_SHIP
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
	SetVarToConst(X_COORD_2, 4),
	SetVarToConst(Y_COORD_2, 38),
	SetBit(MAP_SUNKEN_SHIP),
	SetBit(MAP_DIRECTIONAL_SEA_SUNKEN_SHIP),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R160_SUNKEN_SHIP_AREA_01, face_direction=SOUTH, x=4, y=18, z=8, run_entrance_event=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_JumpToHeight(height=0, silent=True)
	]),
	Return()
])
