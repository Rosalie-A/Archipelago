# E3786_BEAN_VALLEY_WEST_VINE_ROOM_EXIT_TO_UPPER_CHEST_ROOM
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
	EnterArea(room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, face_direction=NORTHEAST, x=17, y=104, z=6),
	UnknownCommand(bytearray(b'\xfdI')),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(128),
		A_WalkNortheastPixels(8),
		A_FloatingOn(),
		A_Walk1StepNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Walk1StepNortheast()
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3786_pause_5"),
	JmpIfMarioInAir(["EVENT_3786_pause_5"]),
	Return()
])
