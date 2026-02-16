#A0891_MARRYMORE_BELLHOP_AFTER_PAYING_FOR_OVERSTAY
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
	A_Pause(144),
	A_FixedFCoordOn(),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNorthwest(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(48),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepSoutheast(),
	A_SetSequenceSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_ReturnQueue()
])
