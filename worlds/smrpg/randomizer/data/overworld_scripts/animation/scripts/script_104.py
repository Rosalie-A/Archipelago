#A0104_BASE_SOUTHWEST_MK_HENCHMAN_MOVEMENT
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
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_104_set_animation_speed_0"),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(11),
	A_BPL262728(),
	A_Pause(2),
	A_ReturnQueue()
])
