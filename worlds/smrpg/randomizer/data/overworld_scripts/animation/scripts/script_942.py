#A0942_HINOPIO_IN_DOORWAY
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_942_set_700C_to_pressed_button_36"]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_VisibilityOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkSoutheastPixels(7),
	A_WalkNortheastPixels(3),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
	A_Walk1StepNortheast(),
	A_UnknownCommand(bytearray(b'\xc8\x07')),
	A_CopyVarToVar(from_var=X_COORD_2, to_var=SECONDARY_TEMP_7024),
	A_CopyVarToVar(from_var=Y_COORD_2, to_var=TEMP_7026),
	A_Pause(100, identifier="ACTION_942_pause_13"),
	A_VisibilityOn(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_Walk1StepSouthwest(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SequenceLoopingOn(),
	A_FixedFCoordOff(),
	A_StartLoopNTimes(254),
	A_FaceMario(),
	A_Pause(4),
	A_EndLoop(),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[0]),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_Walk1StepNortheast(),
	A_VisibilityOff(),
	A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=X_COORD_2),
	A_CopyVarToVar(from_var=TEMP_7026, to_var=Y_COORD_2),
	A_TransferTo70167018(),
	A_Pause(900),
	A_Jmp(["ACTION_942_pause_13"]),
	A_Set700CToPressedButton(identifier="ACTION_942_set_700C_to_pressed_button_36"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_942_db_42"]),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x00\x03\x80')),
	A_Pause(1, identifier="ACTION_942_pause_40"),
	A_Jmp(["ACTION_942_pause_40"]),
	A_UnknownCommand(bytearray(b' \x04'), identifier="ACTION_942_db_42"),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x03\x00\x01\x00\x00\x00\x03\x80')),
	A_Pause(1, identifier="ACTION_942_pause_44"),
	A_Jmp(["ACTION_942_pause_44"])
])
