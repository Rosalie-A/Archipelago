#A0855_PLAYER_DIZZY_FROM_GARDENER
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
	A_OverwriteSolidity(),
	A_SetWalkingSpeed(SLOW),
	A_WalkToXYCoords(x=24, y=18),
	A_PlaySound(sound=SO031_SPINNING_FLOWER, channel=4),
	A_StartLoopNTimes(1),
	A_FaceSouthwest(),
	A_Pause(3),
	A_FaceWest(),
	A_Pause(3),
	A_FaceNorthwest(),
	A_Pause(3),
	A_FaceNorth(),
	A_Pause(3),
	A_FaceNortheast(),
	A_Pause(3),
	A_FaceEast(),
	A_Pause(3),
	A_FaceSoutheast(),
	A_Pause(3),
	A_FaceSouth(),
	A_Pause(3),
	A_EndLoop(),
	A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True),
	A_FaceSouth(),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_ReturnQueue()
])
