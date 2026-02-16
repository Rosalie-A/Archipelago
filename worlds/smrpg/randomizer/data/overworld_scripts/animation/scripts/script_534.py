#A0534_MUSHROOM_WAY_GUARD_GOOMBA
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
	A_FaceSouthwest(identifier="ACTION_534_face_southwest_0"),
	A_Pause(40),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_Pause(90),
	A_SequenceLoopingOff(),
	A_Pause(40),
	A_FaceSoutheast(),
	A_Pause(20),
	A_Jmp(["ACTION_534_face_southwest_0"]),
	A_ReturnQueue()
])
