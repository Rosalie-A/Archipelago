#A0049_SEWERS_3RD_WATER_ROOM_RATS
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_49_object_memory_set_bit_0"),
	A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	A_Pause(13),
	A_Inc(TEMP_702C),
	A_Walk1StepSouthwest(),
	A_Walk1StepSoutheast(),
	A_WalkSouthwestSteps(3),
	A_WalkNorthwestSteps(3),
	A_JmpIfRandom1of2(["ACTION_49_shift_southeast_steps_13"]),
	A_WalkNortheastSteps(3),
	A_WalkSoutheastSteps(2),
	A_Walk1StepNortheast(),
	A_Jmp(["ACTION_49_object_memory_set_bit_0"]),
	A_WalkSoutheastSteps(2, identifier="ACTION_49_shift_southeast_steps_13"),
	A_WalkNortheastSteps(4),
	A_Jmp(["ACTION_49_object_memory_set_bit_0"])
])
