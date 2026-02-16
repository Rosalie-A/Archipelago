#A0938_UNUSED
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
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthSteps(4),
	A_WalkSouthPixels(8),
	A_SetBit(TEMP_7044_7),
	A_StartLoopNTimes(4),
	A_WalkNorthPixels(4),
	A_WalkSouthPixels(4),
	A_EndLoop(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_JumpToHeight(height=256, silent=True),
	A_Pause(20),
	A_SetBit(TEMP_7043_6),
	A_ReturnQueue()
])
