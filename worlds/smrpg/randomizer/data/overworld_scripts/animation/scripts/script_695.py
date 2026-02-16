#A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2
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
	A_SequenceLoopingOn(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_TransferToXYZF(x=13, y=71, z=16, direction=EAST),
	A_WalkEastPixels(16),
	A_FaceNortheast(),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_WalkNortheastSteps(5),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(2),
	A_Walk1StepSoutheast(),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkSoutheastPixels(6),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JumpToHeight(0),
	A_WalkSoutheastPixels(10),
	A_EndLoop(),
	A_Pause(16),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(8),
	A_JumpToHeight(0),
	A_Walk1StepSouthwest(),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkSouthwestSteps(2),
	A_WalkSouthwestPixels(8),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_VisibilityOff(),
	A_ReturnQueue()
])
