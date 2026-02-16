#A0351_OERLIKONS_AND_3D_MAZE
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
	A_JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_351_set_animation_speed_10"]),
	A_UnknownCommand(bytearray(b'\xc8\x00')),
	A_TransferTo70167018(),
	A_SetPriority(3),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_VisibilityOn(identifier="ACTION_351_visibility_on_5"),
	A_Pause(30),
	A_VisibilityOff(),
	A_Pause(30),
	A_Jmp(["ACTION_351_visibility_on_5"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_351_set_animation_speed_10"),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepFDirection(),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_351_set_animation_speed_10"]),
	A_FaceMario(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(VERY_FAST),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_351_set_animation_speed_10"])
])
