#A0471_BANDITS_WAY_2_CHEST_ROOM_CHEST
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
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetPriority(3),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_FixedFCoordOff(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ObjectMemorySetBit(arg_1=0x09, bits=[7]),
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_SetAllSpeeds(VERY_FAST),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_471_transfer_to_xyzf_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_471_transfer_to_xyzf_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_471_transfer_to_xyzf_24"]),
	A_TransferToXYZF(x=18, y=46, z=0, direction=EAST),
	A_FaceNorthwest(),
	A_Jmp(["ACTION_471_visibility_on_26"]),
	A_TransferToXYZF(x=17, y=47, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_18"),
	A_FaceNorthwest(),
	A_Jmp(["ACTION_471_visibility_on_26"]),
	A_TransferToXYZF(x=3, y=36, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_21"),
	A_FaceNortheast(),
	A_Jmp(["ACTION_471_visibility_on_26"]),
	A_TransferToXYZF(x=3, y=37, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_24"),
	A_FaceNortheast(),
	A_VisibilityOn(identifier="ACTION_471_visibility_on_26"),
	A_WalkFDirectionSteps(15),
	A_Jmp(["ACTION_714_turn_clockwise_45_degrees_12"])
])
