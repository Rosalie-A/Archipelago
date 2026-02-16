#A0648_MOLEVILLE_WOMAN_NEAR_MOUNTAIN
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
	A_SequenceLoopingOn(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(4),
	A_EndLoop(),
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_648_set_animation_speed_6"),
	A_StartLoopNTimes(3),
	A_ShiftZUpPixels(4),
	A_ShiftZDownPixels(4),
	A_EndLoop(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_648_face_northwest_15"]),
	A_FaceSoutheast(),
	A_Jmp(["ACTION_648_set_animation_speed_16"]),
	A_FaceNorthwest(identifier="ACTION_648_face_northwest_15"),
	A_SetSequenceSpeed(VERY_FAST, identifier="ACTION_648_set_animation_speed_16"),
	A_Pause(32),
	A_FaceNortheast(),
	A_Jmp(["ACTION_648_set_animation_speed_6"]),
	A_ReturnQueue()
])
