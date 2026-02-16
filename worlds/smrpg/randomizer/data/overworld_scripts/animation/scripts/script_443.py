#A0443_ROSE_WAY_SWINGING_PLATFORM_SHY_GUY
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
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_ShadowOn(),
	A_FaceMario(identifier="ACTION_443_face_mario_4"),
	A_StartLoopNTimes(7),
	A_Set700CToPressedButton(),
	A_Dec(PRIMARY_TEMP_700C),
	A_Dec(PRIMARY_TEMP_700C),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	A_UnknownCommand(bytearray(b'\xc8\x11')),
	A_AddConstToVar(Z_COORD_2, 192),
	A_AddConstToVar(X_COORD_2, 64),
	A_AddConstToVar(Y_COORD_2, 48),
	A_UnknownCommand(bytearray(b'\x99')),
	A_EndLoop(),
	A_Jmp(["ACTION_443_face_mario_4"])
])
