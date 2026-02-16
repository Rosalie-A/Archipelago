# E2065_DOJO_LOADER_FIRST_TIME_ANIMATION
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
	Pause(1, identifier="EVENT_2065_pause_0"),
	Pause(1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_Pause(15),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_ResetProperties(),
		A_FixedFCoordOff()
	]),
	Jmp(["EVENT_2065_set_bit_5"]),
	SetBit(INITIAL_DOJO_CUTSCENE_COMPLETED, identifier="EVENT_2065_set_bit_5"),
	Return()
])
