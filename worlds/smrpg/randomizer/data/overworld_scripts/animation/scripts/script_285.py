#A0285_KEEP_BULLET_BILL
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
	A_Pause(100),
	A_SetPriority(3),
	A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65512),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(180),
	A_EndLoop(),
	A_TransferToXYZF(x=25, y=35, z=19, direction=EAST),
	A_VisibilityOn(),
	A_FaceSouthwest(identifier="ACTION_285_face_southwest_11"),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownSteps(9),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetWalkingSpeed(NORMAL),
	A_WalkToXYCoords(x=5, y=75),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpSteps(9),
	A_SetWalkingSpeed(NORMAL),
	A_FaceNortheast(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_WalkToXYCoords(x=25, y=35),
	A_Jmp(["ACTION_285_face_southwest_11"])
])
