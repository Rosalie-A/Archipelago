#A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP
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
	A_SetVarToConst(SECONDARY_TEMP_7024, 20),
	A_SetWalkingSpeed(NORMAL),
	A_Set700CToPressedButton(),
	A_DecVarFrom700C(SECONDARY_TEMP_7024),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_36_load_mem_11"]),
	A_UnknownCommand(bytearray(b'\xc8\x07')),
	A_AddConstToVar(Z_COORD_2, 128),
	A_AddConstToVar(X_COORD_2, 64),
	A_UnknownCommand(bytearray(b'\x99')),
	A_Jmp(["ACTION_36_visibility_on_16"]),
	A_LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_36_load_mem_11"),
	A_Pause(8),
	A_EndLoop(),
	A_Pause(1),
	A_SetSequenceSpeed(FAST),
	A_VisibilityOn(identifier="ACTION_36_visibility_on_16"),
	A_SetPriority(3),
	A_WalkNorthwestSteps(4),
	A_Jmp(["ACTION_32_shift_z_up_steps_20"]),
	A_ReturnQueue()
])
