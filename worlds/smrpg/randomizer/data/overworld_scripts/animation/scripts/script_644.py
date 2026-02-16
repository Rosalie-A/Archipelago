#A0644_MIDAS_2ND_TUNNELS_FLOWER
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
	A_Pause(1, identifier="ACTION_644_pause_0"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_0"]),
	A_SetPriority(3),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	A_Pause(1, identifier="ACTION_644_pause_5"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_5"]),
	A_Pause(26),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_Pause(1, identifier="ACTION_644_pause_10"),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_644_pause_10"]),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_SetWalkingSpeed(FAST),
	A_SetPriority(3),
	A_JumpToHeight(153),
	A_SetVRAMPriority(PRIORITY_3),
	A_BounceToXYWithHeight(x=17, y=58, height=0),
	A_SetWalkingSpeed(VERY_FAST),
	A_AddZCoord1Step(),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	A_Pause(1, identifier="ACTION_644_pause_21"),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_644_pause_21"]),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(48),
	A_WalkNortheastSteps(3),
	A_Pause(1, identifier="ACTION_644_pause_26"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_26"]),
	A_JumpToHeight(80),
	A_Pause(17),
	A_FloatingOff(),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	A_Pause(1, identifier="ACTION_644_pause_32"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_32"]),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	A_Pause(1, identifier="ACTION_644_pause_35"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_35"]),
	A_Pause(13),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_JumpToHeight(16),
	A_Pause(14),
	A_FloatingOff(),
	A_Pause(10),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	A_Pause(1, identifier="ACTION_644_pause_44"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_44"]),
	A_Pause(13),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_JumpToHeight(96),
	A_JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_1, ["ACTION_644_shift_southwest_steps_63"]),
	A_WalkSoutheastSteps(2),
	A_Pause(20),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	A_PlaySound(sound=SO085_FLOWER, channel=4),
	A_StartLoopNTimes(7),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_SetBit(MIDAS_RIVER_TUNNEL_2_BIT_1),
	A_SetBit(TEMP_7043_4),
	A_ReturnQueue(),
	A_WalkSouthwestSteps(2, identifier="ACTION_644_shift_southwest_steps_63"),
	A_SetWalkingSpeed(NORMAL),
	A_Walk1StepSouth(),
	A_Walk1StepSouthwest(),
	A_Walk1StepSouth(),
	A_VisibilityOff(),
	A_ClearBit(TEMP_7043_4),
	A_ReturnQueue()
])
