#A0737_TOWER_EARLY_CIRCLING_BOMB
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
	A_SequenceLoopingOn(identifier="ACTION_737_sequence_looping_on_0"),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(2),
	A_Walk1StepNortheast(),
	A_WalkNorthwestSteps(2),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_737_sequence_looping_on_0"])
])
