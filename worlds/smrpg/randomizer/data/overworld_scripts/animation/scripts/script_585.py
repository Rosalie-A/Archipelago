#A0585_SEASIDE_OCCUPIED_SHOPKEEPER
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
	A_FaceSoutheast(),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestSteps(2, identifier="ACTION_585_shift_southwest_steps_5"),
	A_WalkNortheastSteps(3),
	A_WalkSouthwestSteps(1),
	A_Jmp(["ACTION_585_shift_southwest_steps_5"])
])
