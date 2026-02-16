# E3615_CLIMB_UP_VALLEY_BEANSTALK_INTO_VINE_CLOUDS
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
	EnterArea(room_id=R378_BEAN_VALLEY_BEANSTALKS_AREA_01, face_direction=NORTHWEST, x=6, y=123, z=0),
	UnknownCommand(bytearray(b'\xfdI')),
	SetBit(NOTE_DIRECTION),
	SetSyncActionScript(NPC_0, A0977_NOTE_WITHOUT_KNIFE),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(132),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(20),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3615_pause_6"),
	JmpIfMarioInAir(["EVENT_3615_pause_6"]),
	Return()
])
