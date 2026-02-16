#A0605_MIDAS_1ST_TUNNEL_TROOPA
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
	A_SetPriority(3, identifier="ACTION_605_set_priority_0"),
	A_WalkFDirectionSteps(3),
	A_SetAllSpeeds(FAST),
	A_ShiftZUpPixels(8),
	A_DecZCoord1Step(),
	A_AddZCoord1Step(),
	A_ShiftZDownPixels(8),
	A_SetAllSpeeds(NORMAL),
	A_TurnClockwise45DegreesNTimes(4),
	A_WalkFDirectionSteps(3),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_605_set_priority_0"])
])
