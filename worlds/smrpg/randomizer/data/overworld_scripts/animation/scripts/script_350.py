#A0350_SHIP_BULLET
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
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetAllSpeeds(FAST),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_350_create_packet_at_npc_coords_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_350_pause_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_350_pause_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_350_pause_17"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_350_pause_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_350_pause_15"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_350_pause_14"]),
	A_Pause(20),
	A_Pause(20, identifier="ACTION_350_pause_14"),
	A_Pause(20, identifier="ACTION_350_pause_15"),
	A_Pause(20, identifier="ACTION_350_pause_16"),
	A_Pause(20, identifier="ACTION_350_pause_17"),
	A_Pause(20, identifier="ACTION_350_pause_18"),
	A_Pause(20, identifier="ACTION_350_pause_19"),
	A_CreatePacketAtObjectCoords(packet=P024_REGULAR_SOUND_EXPLOSION, target_npc=DUMMY_0X07, destinations=["ACTION_350_visibility_on_21"], identifier="ACTION_350_create_packet_at_npc_coords_20"),
	A_VisibilityOn(identifier="ACTION_350_visibility_on_21"),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(7),
	A_Walk1StepFDirection(),
	A_ShadowOff(),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Pause(128),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_350_transfer_to_xyzf_39"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_350_transfer_to_xyzf_41"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 28, ["ACTION_350_transfer_to_xyzf_43"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 29, ["ACTION_350_transfer_to_xyzf_45"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_350_transfer_to_xyzf_47"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 31, ["ACTION_350_transfer_to_xyzf_49"]),
	A_TransferToXYZF(x=23, y=59, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_39"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	A_TransferToXYZF(x=21, y=63, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_41"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	A_TransferToXYZF(x=30, y=63, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_43"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	A_TransferToXYZF(x=28, y=59, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_45"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	A_TransferToXYZF(x=22, y=61, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_47"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	A_TransferToXYZF(x=29, y=61, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_49"),
	A_Jmp(["ACTION_350_create_packet_at_npc_coords_20"])
])
