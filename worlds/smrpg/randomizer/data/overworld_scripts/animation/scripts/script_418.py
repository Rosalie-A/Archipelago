#A0418_GOOMBA_THUMPIN_RIGHT_PIPE
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
	A_SetWalkingSpeed(SLOW),
	A_VisibilityOff(),
	A_TransferToXYZF(x=7, y=118, z=1, direction=EAST),
	A_JmpIfBitClear(TEMP_7049_6, ["ACTION_418_set_700C_to_pressed_button_5"]),
	A_SetWalkingSpeed(NORMAL),
	A_Set700CToPressedButton(identifier="ACTION_418_set_700C_to_pressed_button_5"),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 25),
	A_JmpIfComparisonResultIsLesser(["ACTION_418_shift_z_up_pixels_16"]),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 29),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_418_transfer_xyzf_pixels_28"]),
	A_JmpIfBitSet(TEMP_7049_6, ["ACTION_418_set_animation_speed_14"]),
	A_SetWalkingSpeed(NORMAL),
	A_Pause(6),
	A_Jmp(["ACTION_418_shift_z_up_pixels_16"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_418_set_animation_speed_14"),
	A_Pause(3),
	A_ShiftZUpPixels(6, identifier="ACTION_418_shift_z_up_pixels_16"),
	A_ResetProperties(),
	A_VisibilityOn(),
	A_ShiftZUpPixels(10),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Pause(40),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Pause(4),
	A_ShiftZDownPixels(10),
	A_VisibilityOff(),
	A_BounceToXYWithHeight(x=7, y=118, height=1),
	A_Jmp(["ACTION_418_transfer_to_xyzf_47"]),
	A_TransferXYZFPixels(x=254, y=0, z=0, direction=EAST, identifier="ACTION_418_transfer_xyzf_pixels_28"),
	A_JmpIfBitSet(TEMP_7049_6, ["ACTION_418_pause_31"]),
	A_Pause(1),
	A_Pause(1, identifier="ACTION_418_pause_31"),
	A_ShiftZUpPixels(4),
	A_ResetProperties(),
	A_VisibilityOn(),
	A_ShiftZUpPixels(10),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Pause(28),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Pause(2),
	A_ShiftZDownPixels(10),
	A_VisibilityOff(),
	A_BounceToXYWithHeight(x=7, y=118, height=1),
	A_JmpIfBitSet(TEMP_7049_6, ["ACTION_418_pause_45"]),
	A_Pause(1),
	A_Pause(1, identifier="ACTION_418_pause_45"),
	A_Jmp(["ACTION_418_transfer_to_xyzf_47"]),
	A_TransferToXYZF(x=8, y=60, z=0, direction=EAST, identifier="ACTION_418_transfer_to_xyzf_47"),
	A_ClearBit(TEMP_7044_2),
	A_ReturnQueue()
])
