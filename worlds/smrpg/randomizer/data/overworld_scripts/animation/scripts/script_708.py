#A0708_BOOSTER_HILL_BARREL
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
	A_SetPriority(2),
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SetAllSpeeds(FASTER),
	A_TransferToXYZF(x=1, y=50, z=0, direction=EAST),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 30),
	A_Inc(PRIMARY_TEMP_700C),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_JmpIfBitSet(TEMP_7044_4, ["ACTION_708_shift_southwest_pixels_14"]),
	A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
	A_WalkSouthwestPixels(8, identifier="ACTION_708_shift_southwest_pixels_14"),
	A_JmpIfObjectWithinRange(comparing_npc=NPC_3, usually=0, tiles=3, destinations=["ACTION_708_set_bit_19"], identifier="ACTION_708_jmp_if_object_within_range_15"),
	A_JumpToHeight(24),
	A_Walk1StepSoutheast(),
	A_Jmp(["ACTION_708_jmp_if_object_within_range_15"]),
	A_SetBit(TEMP_7043_0, identifier="ACTION_708_set_bit_19"),
	A_JumpToHeight(24, identifier="ACTION_708_jump_to_height_20"),
	A_Walk1StepSoutheast(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_708_jump_to_height_20"]),
	A_ReturnQueue()
])
