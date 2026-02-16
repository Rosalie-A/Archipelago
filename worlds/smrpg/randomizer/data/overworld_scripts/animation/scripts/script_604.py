#A0604_MIDAS_1ST_TUNNEL_SPINY
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
	A_SetPriority(3, identifier="ACTION_604_set_priority_0"),
	A_SetAllSpeeds(NORMAL),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_Pause(20),
	A_SetAllSpeeds(FAST),
	A_Walk1StepEast(),
	A_Pause(13),
	A_Jmp(["ACTION_604_set_priority_0"])
])
