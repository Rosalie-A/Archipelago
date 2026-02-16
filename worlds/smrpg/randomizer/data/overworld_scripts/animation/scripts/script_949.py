#A0949_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_BEFORE_PAINT
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
	A_SetWalkingSpeed(SLOW),
	A_VisibilityOff(),
	A_WalkToXYCoords(x=16, y=49),
	A_ShiftToXYCoords(x=3, y=88),
	A_WalkSoutheastSteps(3),
	A_ShiftToXYCoords(x=6, y=28),
	A_VisibilityOn(),
	A_Jmp(["ACTION_948_shadow_on_0"])
])
