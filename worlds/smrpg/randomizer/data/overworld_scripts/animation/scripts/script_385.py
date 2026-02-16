#A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST
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
	A_FaceSouth(),
	A_Pause(2),
	A_FaceSouthwest(),
	A_Pause(2),
	A_FaceWest(),
	A_Pause(2),
	A_FaceNorthwest(),
	A_Pause(2),
	A_FaceNorth(),
	A_Pause(2),
	A_FaceNortheast(),
	A_Pause(2),
	A_FaceEast(),
	A_Pause(2),
	A_FaceSoutheast(),
	A_Pause(6),
	A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
	A_Pause(64),
	A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
	A_FaceSouth(),
	A_ResetProperties(),
	A_ReturnQueue()
])
