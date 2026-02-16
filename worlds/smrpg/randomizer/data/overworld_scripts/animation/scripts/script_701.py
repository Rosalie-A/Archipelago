#A0701_BOOSTER_PASS_SECRET_SPINY
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
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSoutheastPixels(2),
	A_WalkSouthwestPixels(9),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_701_face_southeast_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_701_face_southeast_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_701_face_southeast_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_701_face_southeast_11"]),
	A_FaceSouthwest(),
	A_ReturnQueue(),
	A_FaceSoutheast(identifier="ACTION_701_face_southeast_11"),
	A_ReturnQueue()
])
