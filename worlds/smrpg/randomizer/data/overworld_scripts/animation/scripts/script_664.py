#A0664_ROSE_TOWN_OCCUPIED_WATER_GUY
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
	A_TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_VisibilityOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	A_Walk1StepSoutheast(),
	A_FaceNorthwest(),
	A_Pause(60),
	A_SetSolidityBits(cant_walk_through=True),
	A_WalkSoutheastSteps(4),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkSouthwestSteps(2),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_WalkSouthwestSteps(3),
	A_FaceNorthwest(),
	A_Pause(60),
	A_Walk1StepNortheast(),
	A_FaceNorthwest(),
	A_FixedFCoordOn(),
	A_StartLoopNTimes(2),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(6),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZDownPixels(6),
	A_Pause(30),
	A_EndLoop(),
	A_FixedFCoordOff(),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepSouthwest(),
	A_FaceNorthwest(),
	A_Pause(60),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(3),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkNortheastSteps(2),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_WalkNorthwestSteps(4),
	A_Pause(30),
	A_ClearBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	A_ClearSolidityBits(cant_walk_through=True),
	A_Walk1StepNorthwest(),
	A_VisibilityOff(),
	A_TransferToXYZF(x=22, y=77, z=0, direction=EAST),
	A_ReturnQueue()
])
