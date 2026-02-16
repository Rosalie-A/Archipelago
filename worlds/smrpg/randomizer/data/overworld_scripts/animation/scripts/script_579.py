#A0579_CURTAIN_GAME_HENCHMAN_SPIN
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
	A_SetSequenceSpeed(FAST, identifier="ACTION_579_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_FaceSouthwest(),
	A_Pause(24),
	A_FaceNorthwest(),
	A_Pause(24),
	A_FaceNortheast(),
	A_Pause(30),
	A_FaceNorthwest(),
	A_Pause(44),
	A_FaceSouthwest(),
	A_Pause(19),
	A_FaceNorthwest(),
	A_Pause(45),
	A_FaceNortheast(),
	A_Pause(36),
	A_FaceNorthwest(),
	A_Pause(20),
	A_Jmp(["ACTION_579_set_animation_speed_0"])
])
