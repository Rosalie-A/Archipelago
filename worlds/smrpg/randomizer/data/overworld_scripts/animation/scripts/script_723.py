#A0723_MINES_RECRUITABLE_CHARACTER
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
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SequencePlaybackOn(),
	A_SequenceLoopingOn(),
	A_WalkNortheastPixels(3),
	A_FaceSouthwest(identifier="ACTION_723_face_southwest_5"),
	A_FixedFCoordOn(),
	A_StartLoopNTimes(3),
	A_WalkWestPixels(1),
	A_Pause(1),
	A_WalkEastPixels(1),
	A_Pause(1),
	A_EndLoop(),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastPixels(8),
	A_Pause(80),
	A_JmpIfRandom1of2(["ACTION_723_face_southwest_23"]),
	A_FixedFCoordOff(),
	A_FaceNorthwest(),
	A_JumpToHeight(40),
	A_Pause(16),
	A_JumpToHeight(40),
	A_Pause(64),
	A_FaceSouthwest(identifier="ACTION_723_face_southwest_23"),
	A_FixedFCoordOn(),
	A_WalkSouthwestPixels(8),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_723_face_southwest_5"])
])
