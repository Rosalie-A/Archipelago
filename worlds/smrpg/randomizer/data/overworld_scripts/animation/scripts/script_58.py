#A0058_SEWER_STAIR_MOST_RATS
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
	A_Set700CToPressedButton(),
	A_SetVarToConst(TEMP_702C, 20),
	A_DecVarFrom700C(TEMP_702C),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_58_pause_15"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_58_pause_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_58_pause_17"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_58_pause_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_58_pause_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_58_pause_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_58_pause_21"]),
	A_Pause(1),
	A_Pause(1, identifier="ACTION_58_pause_15"),
	A_Pause(1, identifier="ACTION_58_pause_16"),
	A_Pause(1, identifier="ACTION_58_pause_17"),
	A_Pause(1, identifier="ACTION_58_pause_18"),
	A_Pause(1, identifier="ACTION_58_pause_19"),
	A_Pause(1, identifier="ACTION_58_pause_20"),
	A_Pause(1, identifier="ACTION_58_pause_21"),
	A_VisibilityOff(identifier="ACTION_58_visibility_off_22"),
	A_Pause(8),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=192, tiles=2, destinations=["ACTION_58_visibility_on_26"]),
	A_Jmp(["ACTION_58_visibility_off_22"]),
	A_VisibilityOn(identifier="ACTION_58_visibility_on_26"),
	A_SetAllSpeeds(FAST),
	A_WalkSouthwestSteps(2),
	A_Pause(32),
	A_WalkNorthwestSteps(2),
	A_Pause(32),
	A_Walk1StepNortheast(),
	A_Pause(16),
	A_WalkSoutheastSteps(4),
	A_Pause(16),
	A_WalkSouthwestSteps(2),
	A_Pause(32),
	A_WalkNorthwestSteps(2),
	A_WalkNortheastSteps(3),
	A_Jmp(["ACTION_58_visibility_off_22"])
])
