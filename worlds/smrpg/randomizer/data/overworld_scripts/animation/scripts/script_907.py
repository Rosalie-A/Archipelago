#A0907_MUSHROOM_THROWN_SOUTHWEST
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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetSolidityBits(cant_pass_walls=True, cant_jump_through=True),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_JumpToHeight(height=48, silent=True),
	A_FloatingOn(),
	A_FaceSoutheast(),
	A_JmpIfBitSet(TEMP_7044_7, ["ACTION_907_set_object_memory_bits_9"]),
	A_FaceSouthwest(),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[0], identifier="ACTION_907_set_object_memory_bits_9"),
	A_Walk1StepFDirection(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Walk1StepFDirection(),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_WalkFDirectionSteps(6),
	A_StartLoopNTimes(7),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_VisibilityOff(),
	A_ReturnQueue()
])
