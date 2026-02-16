#A0658_PIPE_VAULT_THWOMP_ROOM_SHAKE_CAMERA
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
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthPixels(8),
	A_SetBit(TEMP_7043_2),
	A_WalkNorthPixels(16),
	A_WalkSouthPixels(16),
	A_WalkNorthPixels(12),
	A_WalkSouthPixels(8),
	A_ClearBit(TEMP_7043_2),
	A_WalkNorthPixels(8),
	A_WalkSouthPixels(6),
	A_WalkNorthPixels(4),
	A_WalkSouthPixels(4),
	A_WalkNorthPixels(2),
	A_ReturnQueue()
])
