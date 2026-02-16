#A0309_SHIP_EARLY_GREAPERS
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
	A_VisibilityOff(identifier="ACTION_309_visibility_off_0"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_309_jmp_if_random_above_128_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_309_pause_10"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_309_pause_9"]),
	A_Pause(3),
	A_Pause(3, identifier="ACTION_309_pause_9"),
	A_Pause(3, identifier="ACTION_309_pause_10"),
	A_JmpIfRandom1of2(["ACTION_309_add_z_coord_1_step_15"], identifier="ACTION_309_jmp_if_random_above_128_11"),
	A_DecZCoord1Step(identifier="ACTION_309_dec_z_coord_1_step_12"),
	A_JmpIfRandom1of2(["ACTION_309_dec_z_coord_1_step_12"]),
	A_Jmp(["ACTION_309_set_700C_to_object_coord_17"]),
	A_AddZCoord1Step(identifier="ACTION_309_add_z_coord_1_step_15"),
	A_JmpIfRandom1of2(["ACTION_309_add_z_coord_1_step_15"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True, identifier="ACTION_309_set_700C_to_object_coord_17"),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 8),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_309_visibility_off_0"]),
	A_FaceMario(),
	A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	A_StartLoopNTimes(3),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOn(),
	A_SequenceLoopingOn(identifier="ACTION_309_sequence_looping_on_31"),
	A_WalkFDirectionSteps(2),
	A_JmpIfRandom1of2(["ACTION_309_sequence_looping_on_31"]),
	A_StartLoopNTimes(3),
	A_TurnRandomDirection(),
	A_Pause(16),
	A_EndLoop(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(3),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_Jmp(["ACTION_309_visibility_off_0"])
])
