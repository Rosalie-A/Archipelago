#A0674_ROSE_TOWN_LIBERATED_WATER_KID
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
	A_Pause(64),
	A_JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	A_FaceNorthwest(),
	A_SequenceLoopingOff(),
	A_Pause(32),
	A_StartLoopNTimes(2),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZDownPixels(8),
	A_EndLoop(),
	A_SetWalkingSpeed(SLOW),
	A_Pause(30),
	A_JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	A_Pause(30),
	A_SetBit(TEMP_7044_0),
	A_ReturnQueue()
])
