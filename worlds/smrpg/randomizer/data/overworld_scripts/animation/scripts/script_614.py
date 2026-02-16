#A0614_ROSE_WAY_LAKITU_SHY_GUY
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
	A_VisibilityOff(identifier="ACTION_614_visibility_off_0"),
	A_ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	A_SetPriority(3),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
	A_Pause(1),
	A_JmpIfVarNotEqualsConst(TEMP_70AE, 24, ["ACTION_614_visibility_off_0"]),
	A_VisibilityOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SequenceLoopingOn(),
	A_WalkSoutheastPixels(18),
	A_ShiftZDownSteps(3),
	A_FaceMario(identifier="ACTION_614_face_mario_11"),
	A_Pause(1),
	A_Jmp(["ACTION_614_face_mario_11"])
])
