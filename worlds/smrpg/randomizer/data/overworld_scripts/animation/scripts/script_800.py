#A0800_MUSHROOM_DERBY_UNKNOWN
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
	A_Pause(10, identifier="ACTION_800_pause_0"),
	A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkNortheastPixels(1),
	A_StartLoopNTimes(29),
	A_WalkSouthwestPixels(2),
	A_WalkNortheastPixels(2),
	A_EndLoop(),
	A_WalkSouthwestPixels(1),
	A_SetWalkingSpeed(FAST),
	A_Pause(16),
	A_ResetProperties(),
	A_FaceNorthwest(),
	A_ReturnQueue()
])
