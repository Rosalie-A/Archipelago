#A0519_TOWER_BOSS_PEEKING_BEHIND_ENTRANCE
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
	A_Pause(1, identifier="ACTION_519_pause_0"),
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_Pause(120),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthPixels(15),
	A_Pause(120),
	A_Pause(120),
	A_Pause(120),
	A_Pause(120),
	A_WalkNorthPixels(15),
	A_Pause(60),
	A_Jmp(["ACTION_519_pause_0"]),
	A_VisibilityOff(),
	A_ReturnQueue()
])
