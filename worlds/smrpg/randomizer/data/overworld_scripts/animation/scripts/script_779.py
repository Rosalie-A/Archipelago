#A0779_LANDS_END_MOVING_CHEST
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
	A_SetPriority(3),
	A_FixedFCoordOn(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepNortheast(identifier="ACTION_779_walk_1_step_northeast_5"),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_779_walk_1_step_northeast_5"])
])
