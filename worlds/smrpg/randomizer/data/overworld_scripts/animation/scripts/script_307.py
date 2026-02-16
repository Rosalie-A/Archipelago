#A0307_WHIRLPOOL
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
	A_VisibilityOff(),
	A_WalkSoutheastPixels(8),
	A_SetSequenceSpeed(VERY_SLOW),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_307_jmp_to_subroutine_6"]),
	A_Pause(80),
	A_JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_307_jmp_to_subroutine_6"),
	A_TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	A_Pause(40),
	A_Jmp(["ACTION_307_jmp_to_subroutine_6"])
])
