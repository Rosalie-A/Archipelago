#A0635_ROSE_TOWN_ARROW
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
	A_JmpIfBitSet(TEMP_7043_3, ["ACTION_635_transfer_to_xyzf_8"]),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_635_transfer_to_xyzf_11"]),
	A_JmpIfBitSet(TEMP_7043_5, ["ACTION_635_transfer_to_xyzf_14"]),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_635_transfer_to_xyzf_20"]),
	A_JmpIfBitSet(TEMP_7044_1, ["ACTION_635_transfer_to_xyzf_17"]),
	A_TransferToXYZF(x=10, y=59, z=0, direction=SOUTHEAST),
	A_SetPriority(3),
	A_Jmp(["ACTION_635_visibility_on_22"]),
	A_TransferToXYZF(x=7, y=45, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_8"),
	A_SetPriority(3),
	A_Jmp(["ACTION_635_visibility_on_22"]),
	A_TransferToXYZF(x=13, y=34, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_11"),
	A_SetPriority(2),
	A_Jmp(["ACTION_635_visibility_on_22"]),
	A_TransferToXYZF(x=14, y=43, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_14"),
	A_SetPriority(3),
	A_Jmp(["ACTION_635_visibility_on_22"]),
	A_TransferToXYZF(x=17, y=59, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_17"),
	A_SetPriority(3),
	A_Jmp(["ACTION_635_visibility_on_22"]),
	A_TransferToXYZF(x=12, y=44, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_20"),
	A_SetPriority(3),
	A_VisibilityOn(identifier="ACTION_635_visibility_on_22"),
	A_ShadowOff(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x00h\xff')),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastPixels(4),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastPixels(12),
	A_BPL262728(),
	A_ShadowOn(),
	A_Pause(1, identifier="ACTION_635_pause_32"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_635_pause_32"]),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_StartLoopNTimes(2),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_VisibilityOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_TransferToXYZF(x=21, y=79, z=0, direction=EAST),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_ClearBit(TEMP_7043_3),
	A_ClearBit(TEMP_7043_4),
	A_ClearBit(TEMP_7043_5),
	A_ClearBit(TEMP_7043_6),
	A_ClearBit(TEMP_7043_7),
	A_ClearBit(TEMP_7044_1),
	A_SetBit(TEMP_7044_5),
	A_ReturnQueue()
])
