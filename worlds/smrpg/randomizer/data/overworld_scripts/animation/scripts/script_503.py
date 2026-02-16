#A0503_MUSHROOM_DERBY_PLAYER_WHEN_COOKIE_USED
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
	A_BPL262728(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNortheastSteps(3),
	A_SetBit(TEMP_7043_2),
	A_ClearBit(TEMP_7043_4),
	A_Jmp(["ACTION_500_db_0"])
])
