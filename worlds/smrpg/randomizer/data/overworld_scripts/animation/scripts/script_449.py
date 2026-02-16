#A0449_FACTORY_FOUR_SCREW_ROOM_GLUM_REAPER
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
	A_ShadowOn(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(NORMAL),
	A_WalkSoutheastSteps(8, identifier="ACTION_449_shift_southeast_steps_3"),
	A_Pause(24),
	A_WalkNorthwestSteps(8),
	A_Pause(24),
	A_Jmp(["ACTION_449_shift_southeast_steps_3"])
])
