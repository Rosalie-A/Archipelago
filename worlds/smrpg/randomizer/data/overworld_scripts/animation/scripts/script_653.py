#A0653_SLOW_ROTATING_PLATFORM
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 455, ["ACTION_653_set_700C_to_pressed_button_6"]),
	A_Set700CToPressedButton(),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 30),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_653_set_vram_priority_11"]),
	A_Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_6"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65534),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	A_UnknownCommand(bytearray(b'\x97\x10')),
	A_Jmp(["ACTION_653_set_700C_to_pressed_button_6"]),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES, identifier="ACTION_653_set_vram_priority_11"),
	A_Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_12"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65534),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	A_TransferToObjectXY(MEM_70A8),
	A_Jmp(["ACTION_653_set_700C_to_pressed_button_12"])
])
