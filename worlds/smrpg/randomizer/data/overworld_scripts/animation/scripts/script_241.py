#A0241_SMITHY_COMPONENT
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
	A_Pause(5),
	A_SequenceLoopingOn(),
	A_SetAllSpeeds(FAST),
	A_WalkSouthwestPixels(2),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastPixels(2),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastPixels(1),
	A_SetSequenceSpeed(SLOW),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthPixels(2),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_Pause(15),
	A_WalkSouthwestPixels(1),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthPixels(2),
	A_Pause(7),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_ReturnQueue()
])
