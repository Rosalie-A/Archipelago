#A0744_STAR_HILL_1ST_ROOM_NORTH_GECKO
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SequenceLoopingOn(identifier="ACTION_744_sequence_looping_on_0"),
	A_ShadowOn(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestSteps(4),
	A_WalkSouthwestPixels(7),
	A_Pause(32),
	A_FaceNorthwest(),
	A_Pause(24),
	A_WalkNorthwestSteps(3),
	A_WalkNorthwestPixels(7),
	A_Pause(16),
	A_FaceNortheast(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthwestPixels(3),
	A_SetSequenceSpeed(SLOW),
	A_Pause(384),
	A_WalkNortheastPixels(3),
	A_FixedFCoordOff(),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepSouthwest(),
	A_WalkSoutheastSteps(8),
	A_WalkSoutheastPixels(5),
	A_SetSequenceSpeed(SLOW),
	A_Pause(32),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastSteps(4),
	A_WalkNortheastPixels(7),
	A_Pause(32),
	A_SequenceLoopingOff(),
	A_Pause(64),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkToXYCoords(x=12, y=71),
	A_Jmp(["ACTION_744_sequence_looping_on_0"])
])
