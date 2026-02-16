#A0529_MUSHROOM_WAY_1_GOOMBA
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
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FASTER),
	A_WalkSouthwestSteps(1, identifier="ACTION_529_shift_southwest_steps_2"),
	A_WalkSoutheastSteps(4),
	A_WalkSouthwestSteps(6),
	A_WalkNorthwestSteps(1),
	A_WalkSouthwestSteps(3),
	A_WalkNorthwestSteps(8),
	A_WalkSouthwestSteps(1),
	A_WalkNorthwestSteps(6),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(7),
	A_VisibilityOff(),
	A_ShiftToXYCoords(x=12, y=11),
	A_VisibilityOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkSouthwestSteps(4),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(1),
	A_WalkSoutheastSteps(4),
	A_WalkSouthwestSteps(1),
	A_WalkSoutheastSteps(4),
	A_WalkNortheastSteps(1),
	A_SetSolidityBits(cant_pass_walls=True),
	A_WalkSoutheastSteps(6),
	A_Jmp(["ACTION_529_shift_southwest_steps_2"])
])
