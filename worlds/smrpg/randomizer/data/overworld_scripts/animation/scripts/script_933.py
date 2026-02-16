#A0933_ERUPT
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
	A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_VisibilityOff(),
	A_FloatingOff(),
	A_TransferToObjectXY(NPC_0),
	A_TransferXYZFPixels(x=254, y=4, z=18, direction=SOUTHEAST),
	A_Pause(52),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 8),
	A_FaceEast7C(),
	A_JmpIfRandom1of2(["ACTION_933_jump_to_height_silent_23"]),
	A_JmpIfRandom1of2(["ACTION_933_jump_to_height_silent_19"]),
	A_JumpToHeight(height=128, silent=True),
	A_WalkFDirectionSteps(4),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Jmp(["ACTION_727_jmp_if_var_equals_const_0"]),
	A_JumpToHeight(height=80, silent=True, identifier="ACTION_933_jump_to_height_silent_19"),
	A_WalkFDirectionSteps(2),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Jmp(["ACTION_727_jmp_if_var_equals_const_0"]),
	A_JumpToHeight(height=160, silent=True, identifier="ACTION_933_jump_to_height_silent_23"),
	A_WalkFDirectionSteps(6),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Jmp(["ACTION_727_jmp_if_var_equals_const_0"])
])
