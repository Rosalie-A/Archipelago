#A0126_CANNON_GECKIT
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
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_Pause(1, identifier="ACTION_126_pause_4"),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65511),
	A_AddConstToVar(PRIMARY_TEMP_700C, 25),
	A_JmpIfMem704XAt700CBitClear(["ACTION_126_pause_4"]),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65511),
	A_Mem700CAndConst(0x0003),
	A_AddConstToVar(PRIMARY_TEMP_700C, 21),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AA),
	A_UnknownCommand(bytearray(b'\x97\x12')),
	A_JmpIfBitSet(TEMP_7044_1, ["ACTION_126_pause_4"]),
	A_SetBit(TEMP_7044_1),
	A_SetAllSpeeds(FASTER),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_SetVarToConst(TEMP_7034, 61166),
	A_CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=DUMMY_0X07, destinations=["ACTION_126_jump_to_height_20"]),
	A_JumpToHeight(188, identifier="ACTION_126_jump_to_height_20"),
	A_Pause(1),
	A_VisibilityOn(),
	A_ClearBit(TEMP_7044_1),
	A_WalkNorthwestSteps(6),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Pause(1, identifier="ACTION_126_pause_27"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_126_pause_27"]),
	A_SetAllSpeeds(NORMAL),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_Pause(20),
	A_StartLoopNTimes(7),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(2),
	A_EndLoop(),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(2),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Pause(1, identifier="ACTION_126_pause_41"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_126_pause_41"]),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_Walk1StepSoutheast(),
	A_FloatingOn(),
	A_Pause(1, identifier="ACTION_126_pause_47"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_126_pause_47"]),
	A_WalkSoutheastSteps(4),
	A_Walk1StepNortheast(),
	A_WalkNorthwestSteps(3),
	A_Walk1StepSouthwest(),
	A_WalkSoutheastSteps(3),
	A_WalkNortheastPixels(2),
	A_FixedFCoordOn(),
	A_Pause(10),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(108),
	A_Walk1StepEast(),
	A_Pause(6),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_Pause(2),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_FixedFCoordOff(),
	A_VisibilityOff(),
	A_Pause(1, identifier="ACTION_126_pause_66"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_126_pause_66"]),
	A_Pause(6),
	A_Jmp(["ACTION_126_pause_4"])
])
