#A0050_SEWERS_3RD_WATER_ROOM_RATS
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_50_pause_26"]),
	A_Pause(4, identifier="ACTION_50_pause_4"),
	A_Walk1StepNorthwest(),
	A_Pause(1),
	A_Walk1StepSouthwest(),
	A_Pause(1),
	A_WalkSoutheastSteps(2),
	A_Pause(1),
	A_Walk1StepNortheast(),
	A_Pause(1),
	A_Inc(TEMP_702C),
	A_Walk1StepNorthwest(),
	A_Pause(1),
	A_WalkSouthwestSteps(2),
	A_Pause(1),
	A_Walk1StepNorthwest(),
	A_Pause(1),
	A_WalkNortheastSteps(3),
	A_Pause(1),
	A_Walk1StepSoutheast(),
	A_Pause(1),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_50_pause_4"]),
	A_Pause(3, identifier="ACTION_50_pause_26"),
	A_Walk1StepNorthwest(),
	A_Pause(1),
	A_WalkNortheastSteps(2),
	A_Pause(2),
	A_Walk1StepSoutheast(),
	A_WalkSouthwestSteps(3),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Walk1StepNorthwest(),
	A_JmpIfRandom1of2(["ACTION_50_pause_26"]),
	A_WalkNortheastSteps(2),
	A_Walk1StepSoutheast(),
	A_Pause(3),
	A_WalkNorthwestSteps(2),
	A_WalkSouthwestSteps(3),
	A_Walk1StepSoutheast(),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_50_pause_26"])
])
