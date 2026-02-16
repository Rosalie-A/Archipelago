#A0856_GARDENER_RUNS_IN_CIRCLES
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
	A_SetWalkingSpeed(VERY_FAST),
	A_Walk1StepSoutheast(identifier="ACTION_856_walk_1_step_southeast_1"),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(2),
	A_WalkNortheastSteps(2),
	A_Walk1StepSoutheast(),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_856_face_northeast_8"]),
	A_Jmp(["ACTION_856_walk_1_step_southeast_1"]),
	A_FaceNortheast(identifier="ACTION_856_face_northeast_8"),
	A_SetWalkingSpeed(NORMAL),
	A_SetBit(TEMP_7043_1),
	A_ReturnQueue()
])
