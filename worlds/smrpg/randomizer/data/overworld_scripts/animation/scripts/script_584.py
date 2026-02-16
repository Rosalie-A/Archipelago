#A0584_SEASIDE_OCCUPIED_INNKEEPER_AFTER_SLEEP
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
	A_FaceNortheast(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_Pause(120),
	A_Pause(120),
	A_SetWalkingSpeed(FAST),
	A_SetWalkingSpeed(VERY_FAST),
	A_JumpToHeight(height=32, silent=True),
	A_WalkNorthwestSteps(4),
	A_WalkSouthwestSteps(2),
	A_VisibilityOff(),
	A_ReturnQueue()
])
