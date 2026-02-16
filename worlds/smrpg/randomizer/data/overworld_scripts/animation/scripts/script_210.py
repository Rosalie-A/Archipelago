#A0210_GOOMBA_THUMPIN
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
	A_JumpToHeight(height=96, silent=True),
	A_SetWalkingSpeed(FAST),
	A_Pause(4),
	A_SetWalkingSpeed(NORMAL),
	A_Pause(1, identifier="ACTION_210_pause_4"),
	A_JmpIfMarioInAir(["ACTION_210_pause_4"]),
	A_SetWalkingSpeed(NORMAL),
	A_ReturnQueue()
])
