#A0256_NIMBUS_SHY_GUY_LEFT
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_256_reset_properties_8"]),
	A_ResetProperties(),
	A_FaceNortheast(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkToXYCoords(x=5, y=109),
	A_ReturnQueue(),
	A_ResetProperties(identifier="ACTION_256_reset_properties_8"),
	A_FaceNortheast(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkToXYCoords(x=25, y=78),
	A_FaceNortheast(),
	A_ReturnQueue()
])
