#A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1
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
	A_TransferToXYZF(x=16, y=77, z=0, direction=EAST),
	A_WalkEastPixels(16),
	A_FaceNortheast(),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_WalkNortheastSteps(4),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JumpToHeight(108),
	A_Walk1StepNortheast(),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkNortheastPixels(4),
	A_StartLoopNTimes(2),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_Walk1StepNorthwest(),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JumpToHeight(108),
	A_Walk1StepNorthwest(),
	A_EndLoop(),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkNorthwestPixels(4),
	A_WalkSouthwestSteps(5),
	A_VisibilityOff(),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_ReturnQueue()
])
