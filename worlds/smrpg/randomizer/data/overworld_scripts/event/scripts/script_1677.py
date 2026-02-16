# E1677_TEMPLE_PIPE_TO_MONSTRO
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
	JmpIfObjectInSpecificLevel(NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN, ["EVENT_1677_ret_15"]),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	RemoveObjectFromSpecificLevel(NPC_1, R317_LANDS_END_DESERT_AREA_01),
	RemoveObjectFromSpecificLevel(NPC_0, R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS),
	RemoveObjectFromSpecificLevel(NPC_0, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN),
	SetBit(MOUSE_RETURNED_TO_MONSTRO),
	SetVarToConst(X_COORD_2, 7470),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	SetBit(MAP_MONSTRO_TOWN),
	SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTH, x=2, y=47, z=16, show_banner=True),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	JmpToEvent(E2048_MONSTRO_TOWN_EXTERIOR_LOADER),
	Return(identifier="EVENT_1677_ret_15")
])
