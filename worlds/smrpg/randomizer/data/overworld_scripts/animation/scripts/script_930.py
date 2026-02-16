#A0930_DONUT_LIFT_FALL
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
	A_FixedFCoordOn(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_930_set_sprite_sequence_5"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Jmp(["ACTION_930_start_loop_n_times_6"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_930_set_sprite_sequence_5"),
	A_StartLoopNTimes(47, identifier="ACTION_930_start_loop_n_times_6"),
	A_Pause(1),
	A_JmpIfMarioInAir(["ACTION_930_ret_23"]),
	A_EndLoop(),
	A_StartLoopNTimes(11),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(2),
	A_ShiftZUpPixels(2),
	A_JmpIfMarioInAir(["ACTION_930_ret_23"]),
	A_EndLoop(),
	A_JumpToHeight(height=0, silent=True),
	A_FloatingOn(),
	A_Pause(1, identifier="ACTION_930_pause_18"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_930_pause_18"]),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue(identifier="ACTION_930_ret_23")
])
