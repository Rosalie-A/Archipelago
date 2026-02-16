#A0757_STAR_HILL_2ND_ROOM_EAST_GECKO
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
	A_SequenceLoopingOn(identifier="ACTION_757_sequence_looping_on_0"),
	A_ShadowOn(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(3),
	A_WalkNortheastPixels(8),
	A_Pause(16),
	A_FaceNorthwest(),
	A_Pause(16),
	A_WalkNorthwestSteps(4),
	A_Pause(16),
	A_FaceNortheast(),
	A_Pause(16),
	A_WalkNortheastSteps(8),
	A_Pause(16),
	A_FaceSoutheast(),
	A_Pause(16),
	A_WalkSoutheastSteps(8),
	A_Pause(16),
	A_FaceSouthwest(),
	A_Pause(16),
	A_WalkSouthwestSteps(8),
	A_Pause(16),
	A_FaceSoutheast(),
	A_Pause(16),
	A_WalkSoutheastSteps(4),
	A_Pause(16),
	A_FaceSouthwest(),
	A_Pause(16),
	A_WalkSouthwestSteps(4),
	A_Pause(16),
	A_FaceNorthwest(),
	A_Pause(16),
	A_WalkToXYCoords(x=21, y=39),
	A_Jmp(["ACTION_757_sequence_looping_on_0"])
])
