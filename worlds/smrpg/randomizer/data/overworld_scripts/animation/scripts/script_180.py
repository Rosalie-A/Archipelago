#A0180_FOREST_1ST_UNDERGROUND_RAT
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
	A_SequenceLoopingOn(identifier="ACTION_180_sequence_looping_on_0"),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(6),
	A_Pause(24),
	A_FaceSouthwest(),
	A_Pause(24),
	A_FaceNortheast(),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(8),
	A_Walk1StepNortheast(),
	A_WalkNorthwestSteps(8),
	A_WalkSouthwestSteps(3),
	A_Pause(24),
	A_FaceNorthwest(),
	A_Pause(24),
	A_FaceSoutheast(),
	A_Pause(24),
	A_WalkNortheastSteps(4),
	A_WalkSoutheastSteps(10),
	A_Jmp(["ACTION_180_sequence_looping_on_0"])
])
