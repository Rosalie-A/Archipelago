#A0745_STAR_HILL_1ST_ROOM_SOUTH_GECKO
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
	A_SequenceLoopingOn(identifier="ACTION_745_sequence_looping_on_0"),
	A_ShadowOn(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(3),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_WalkSoutheastSteps(4),
	A_WalkSoutheastPixels(8),
	A_Pause(24),
	A_FaceSouthwest(),
	A_Pause(24),
	A_WalkSouthwestSteps(8),
	A_Pause(24),
	A_FaceNorthwest(),
	A_Pause(24),
	A_WalkNorthwestSteps(8),
	A_Pause(24),
	A_FaceNortheast(),
	A_Pause(24),
	A_WalkNortheastSteps(3),
	A_WalkNortheastPixels(4),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_WalkSoutheastSteps(3),
	A_WalkSoutheastPixels(8),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_WalkToXYCoords(x=10, y=107),
	A_Jmp(["ACTION_745_sequence_looping_on_0"])
])
