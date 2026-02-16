#A0522_TOWER_SNIFIT_VIEWING_PORTRAITS
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
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_522_set_animation_speed_0"),
	A_SetSequenceSpeed(NORMAL),
	A_WalkNorthwestSteps(2),
	A_Pause(10),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_FaceNorthwest(),
	A_Pause(20),
	A_WalkNorthwestSteps(2),
	A_Pause(10),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_FaceNorthwest(),
	A_Pause(20),
	A_WalkNorthwestSteps(2),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_FaceNorthwest(),
	A_Pause(30),
	A_WalkNorthwestSteps(2),
	A_FaceNortheast(),
	A_Pause(30),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(FAST),
	A_WalkSouthwestPixels(16),
	A_FixedFCoordOff(),
	A_Pause(60),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastPixels(16),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_WalkNorthwestSteps(2),
	A_Pause(10),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_FaceSoutheast(),
	A_Pause(60),
	A_WalkSoutheastSteps(2),
	A_Pause(10),
	A_FaceNortheast(),
	A_Pause(30),
	A_FaceSoutheast(),
	A_Pause(15),
	A_WalkSoutheastSteps(2),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_FaceSoutheast(),
	A_Pause(20),
	A_WalkSoutheastSteps(2),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(30),
	A_FaceSoutheast(),
	A_Pause(10),
	A_WalkSoutheastSteps(2),
	A_FaceNortheast(),
	A_Pause(60),
	A_JumpToHeight(64),
	A_Pause(30),
	A_JumpToHeight(64),
	A_Pause(90),
	A_FaceSoutheast(),
	A_Pause(10),
	A_WalkSoutheastSteps(2),
	A_FaceNortheast(),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_Pause(60),
	A_Jmp(["ACTION_522_set_animation_speed_0"]),
	A_ReturnQueue()
])
