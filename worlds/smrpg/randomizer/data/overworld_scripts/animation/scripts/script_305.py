#A0305_OUTER_SEA_BUBBLE
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
	A_Mem700CAndConst(0x0006),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_305_pause_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_305_pause_10"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_305_pause_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_305_jmp_to_subroutine_12"]),
	A_Pause(80, identifier="ACTION_305_pause_9"),
	A_Pause(80, identifier="ACTION_305_pause_10"),
	A_Pause(80, identifier="ACTION_305_pause_11"),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"], identifier="ACTION_305_jmp_to_subroutine_12"),
	A_TransferXYZFSteps(x=2, y=4, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	A_TransferXYZFSteps(x=253, y=254, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	A_TransferXYZFSteps(x=1, y=254, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_Jmp(["ACTION_305_jmp_to_subroutine_12"])
])
