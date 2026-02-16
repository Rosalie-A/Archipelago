#A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS
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
	A_SequencePlaybackOn(identifier="ACTION_997_sequence_playback_on_0"),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(FAST),
	A_WalkNortheastSteps(13),
	A_JumpToHeight(height=21, silent=True),
	A_SequencePlaybackOff(),
	A_WalkNortheastSteps(3),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastSteps(1),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastSteps(1),
	A_Pause(15),
	A_FaceSouthwest(),
	A_Pause(15),
	A_SequencePlaybackOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthwestSteps(13),
	A_JumpToHeight(height=21, silent=True),
	A_SequencePlaybackOff(),
	A_WalkSouthwestSteps(3),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestSteps(1),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestSteps(1),
	A_Pause(15),
	A_FaceNortheast(),
	A_Pause(15),
	A_Jmp(["ACTION_997_sequence_playback_on_0"])
])
