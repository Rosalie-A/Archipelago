#A0312_SHIP_TROOPA_PUZZLE_CANNONBALL
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
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
	A_IncPaletteRowBy(3),
	A_SetPriority(3),
	A_Pause(1, identifier="ACTION_312_pause_3"),
	A_JmpIfObjectWithinRange(comparing_npc=NPC_0, usually=48, tiles=0, destinations=["ACTION_312_set_700C_to_object_coord_6"]),
	A_Jmp(["ACTION_312_pause_3"]),
	A_Set700CToObjectCoord(target_npc=NPC_0, coord=COORD_F, identifier="ACTION_312_set_700C_to_object_coord_6"),
	A_JmpIfVarEqualsConst(TEMP_70AE, 1, ["ACTION_312_jmp_if_var_not_equals_const_11"]),
	A_JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_312_jmp_if_var_not_equals_const_20"]),
	A_JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_312_jmp_if_var_not_equals_const_35"]),
	A_JmpIfVarEqualsConst(TEMP_70AE, 4, ["ACTION_312_jmp_if_var_not_equals_const_49"]),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_312_pause_3"], identifier="ACTION_312_jmp_if_var_not_equals_const_11"),
	A_FixedFCoordOn(),
	A_FloatingOn(),
	A_Walk1StepSoutheast(),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(10),
	A_FloatingOff(),
	A_SetBit(TEMP_7043_0),
	A_ReturnQueue(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_312_pause_3"], identifier="ACTION_312_jmp_if_var_not_equals_const_20"),
	A_FixedFCoordOn(),
	A_FloatingOn(),
	A_Walk1StepNortheast(),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(8),
	A_SetBit(TEMP_7044_7),
	A_Pause(1, identifier="ACTION_312_pause_29"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_29"]),
	A_WalkNortheastSteps(2),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_312_pause_3"], identifier="ACTION_312_jmp_if_var_not_equals_const_35"),
	A_FixedFCoordOn(),
	A_FloatingOn(),
	A_Walk1StepSouthwest(),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(8),
	A_SetBit(TEMP_7044_7),
	A_Pause(1, identifier="ACTION_312_pause_43"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_43"]),
	A_WalkSouthwestSteps(3),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_312_pause_3"], identifier="ACTION_312_jmp_if_var_not_equals_const_49"),
	A_FixedFCoordOn(),
	A_FloatingOn(),
	A_Walk1StepNorthwest(),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(8),
	A_SetBit(TEMP_7044_7),
	A_Pause(1, identifier="ACTION_312_pause_58"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_58"]),
	A_WalkNorthwestSteps(2),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
