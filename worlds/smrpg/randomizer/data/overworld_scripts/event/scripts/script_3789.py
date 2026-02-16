# E3789_BEAN_VALLEY_WEST_VINE_ROOM_PLATFORM
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
	EnterArea(room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02, face_direction=SOUTHWEST, x=3, y=58, z=26),
	JmpIfObjectNotInSpecificLevel(NPC_1, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["EVENT_3789_action_queue_4"]),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(6),
		A_SetWalkingSpeed(NORMAL),
		A_DecZCoord1Step(),
		A_FloatingOn()
	], identifier="EVENT_3789_action_queue_4"),
	Pause(2),
	FadeInFromBlack(sync=False),
	Return()
])
