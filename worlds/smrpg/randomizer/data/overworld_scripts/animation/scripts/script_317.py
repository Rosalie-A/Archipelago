#A0317_COIN_SNAKE_HEAD_BASE
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
	A_SetSolidityBits(bit_0=True, cant_pass_walls=True, identifier="ACTION_317_set_solidity_bits_0"),
	A_SetVarToConst(TEMP_70AE, 21),
	A_Walk1StepNorthwest(),
	A_AddZCoord1Step(),
	A_WalkNorthwestSteps(2),
	A_Inc(TEMP_70AE),
	A_Walk1StepSouthwest(),
	A_DecZCoord1Step(),
	A_Walk1StepSouthwest(),
	A_Inc(TEMP_70AE),
	A_Walk1StepSouthwest(),
	A_DecZCoord1Step(),
	A_Walk1StepSouthwest(),
	A_Inc(TEMP_70AE),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(2),
	A_ShiftZUpSteps(3),
	A_WalkNorthwestSteps(2),
	A_Inc(TEMP_70AE),
	A_WalkSouthwestSteps(4),
	A_Inc(TEMP_70AE),
	A_WalkSouthwestSteps(2),
	A_ShiftZDownSteps(2),
	A_Inc(TEMP_70AE),
	A_WalkSouthwestSteps(2),
	A_AddZCoord1Step(),
	A_Walk1StepSouthwest(),
	A_Inc(TEMP_70AE),
	A_Walk1StepSoutheast(),
	A_DecZCoord1Step(),
	A_WalkSoutheastSteps(2),
	A_Inc(TEMP_70AE),
	A_WalkSoutheastSteps(2),
	A_DecZCoord1Step(),
	A_Walk1StepSoutheast(),
	A_Inc(TEMP_70AE),
	A_Walk1StepSoutheast(),
	A_AddZCoord1Step(),
	A_WalkNortheastSteps(2),
	A_Inc(TEMP_70AE),
	A_WalkNortheastSteps(2),
	A_ShiftZUpSteps(2),
	A_Walk1StepNortheast(),
	A_Inc(TEMP_70AE),
	A_WalkNortheastSteps(2),
	A_Inc(TEMP_70AE),
	A_Walk1StepNortheast(),
	A_Walk1StepSoutheast(),
	A_DecZCoord1Step(),
	A_Inc(TEMP_70AE),
	A_WalkSoutheastSteps(2),
	A_AddZCoord1Step(),
	A_Walk1StepSoutheast(),
	A_Inc(TEMP_70AE),
	A_Walk1StepNortheast(),
	A_ShiftZDownSteps(2),
	A_WalkNortheastSteps(2),
	A_Inc(TEMP_70AE),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
