# E3781_BEAN_VALLEY_EAST_VINE_ROOM_EXIT_TO_NIMBUS_MEZZANINE
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
	JmpIfMarioInAir(["EVENT_3584_ret_0"]),
	EnterArea(room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, face_direction=NORTHEAST, x=24, y=25, z=0),
	UnknownCommand(bytearray(b'\xfdI')),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(132),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(20),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3781_pause_5"),
	JmpIfMarioInAir(["EVENT_3781_pause_5"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3781_ret_11"]),
	RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3781_ret_11")
])
