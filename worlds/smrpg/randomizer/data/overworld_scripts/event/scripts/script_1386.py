# E1386_VISTA_HILL_LOADER_CONTINUED
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
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=0, y=2, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkNortheastPixels(1),
		A_FaceNorthwest(),
		A_SequencePlaybackOff()
	]),
	FadeInFromBlack(sync=True, duration=130),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkEastSteps(1)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkWestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkEastSteps(1)
	]),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOn(),
		A_JumpToHeight(108),
		A_Pause(40),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(1),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(6),
		A_VisibilityOff(),
		A_Pause(20)
	]),
	FadeOutToBlack(sync=False, duration=70),
	ExitToWorldMap(area=OW03_VISTA_HILL, bit_6=True, bit_7=True),
	Return()
])
