#A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA
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
	A_SequenceLoopingOn(identifier="ACTION_405_sequence_looping_on_0"),
	A_SetSequenceSpeed(NORMAL),
	A_JmpIfRandom1of2(["ACTION_405_walk_1_step_southeast_20"]),
	A_WalkNortheastSteps(2),
	A_Pause(8),
	A_Walk1StepSoutheast(),
	A_Pause(8),
	A_Walk1StepSouthwest(),
	A_Pause(8),
	A_Walk1StepSoutheast(),
	A_Pause(8),
	A_Walk1StepNortheast(),
	A_Pause(8),
	A_Walk1StepNorthwest(),
	A_Pause(8),
	A_WalkSouthwestSteps(2),
	A_Pause(8),
	A_Walk1StepNorthwest(),
	A_Pause(8),
	A_Jmp(["ACTION_405_sequence_looping_on_0"]),
	A_Walk1StepSoutheast(identifier="ACTION_405_walk_1_step_southeast_20"),
	A_Pause(8),
	A_Walk1StepNortheast(),
	A_Pause(8),
	A_Walk1StepNorthwest(),
	A_Pause(8),
	A_WalkSoutheastSteps(2),
	A_Pause(8),
	A_Walk1StepNortheast(),
	A_Pause(8),
	A_WalkNorthwestSteps(2),
	A_Pause(8),
	A_WalkSouthwestSteps(2),
	A_Pause(8),
	A_Jmp(["ACTION_405_sequence_looping_on_0"])
])
