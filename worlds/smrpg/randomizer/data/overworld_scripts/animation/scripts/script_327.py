#A0327_MARRYMORE_ELDERLY_GUEST_LEAVES
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
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_FaceSouthwest(),
	A_TransferToXYZF(x=7, y=59, z=3, direction=EAST),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_WalkSouthwestSteps(3),
	A_SetSequenceSpeed(SLOW),
	A_FaceNorthwest(),
	A_Pause(60),
	A_SetSequenceSpeed(NORMAL),
	A_Walk1StepSouthwest(),
	A_FaceSoutheast(),
	A_SetBit(TEMP_7044_3),
	A_Pause(1),
	A_ClearBit(TEMP_7044_3),
	A_Pause(29),
	A_Walk1StepSoutheast(),
	A_TransferToXYZF(x=6, y=88, z=0, direction=EAST),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_SetBit(EMPLOYMENT_704C_2),
	A_ReturnQueue()
])
