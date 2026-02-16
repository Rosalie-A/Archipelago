# E3779_BEAN_VALLEY_1ST_VINE_ROOM_EXIT_TO_2ND_VINE_ROOM
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
	EnterArea(room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02, face_direction=NORTHWEST, x=7, y=59, z=0),
	UnknownCommand(bytearray(b'\xfdI')),
	JmpIfObjectNotInSpecificLevel(NPC_1, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["EVENT_3779_action_queue_6"]),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(132),
		A_WalkNorthwestPixels(20),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3779_action_queue_6"),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3779_pause_8"),
	JmpIfMarioInAir(["EVENT_3779_pause_8"]),
	Return()
])
