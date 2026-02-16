#A0931_STUMPET
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
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_931_transfer_xyzf_pixels_8"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_931_transfer_xyzf_pixels_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_931_set_vram_priority_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_931_set_vram_priority_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_931_set_vram_priority_26"]),
	A_ReturnQueue(),
	A_TransferXYZFPixels(x=16, y=16, z=0, direction=EAST, identifier="ACTION_931_transfer_xyzf_pixels_8"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	A_ReturnQueue(),
	A_TransferXYZFPixels(x=16, y=48, z=0, direction=EAST, identifier="ACTION_931_transfer_xyzf_pixels_12"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	A_ReturnQueue(),
	A_SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_16"),
	A_TransferXYZFPixels(x=224, y=21, z=0, direction=EAST),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	A_ReturnQueue(),
	A_SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_21"),
	A_TransferXYZFPixels(x=224, y=53, z=0, direction=EAST),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
	A_ReturnQueue(),
	A_SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_26"),
	A_TransferXYZFPixels(x=0, y=37, z=0, direction=EAST),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	A_ReturnQueue()
])
