#A0048_SEWERS_1ST_WATER_ROOM_RAT
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_48_object_memory_set_bit_0"),
	A_SetAllSpeeds(FAST),
	A_WalkNortheastSteps(3),
	A_Pause(8),
	A_FaceNorthwest(),
	A_Pause(8),
	A_FaceSoutheast(),
	A_Pause(8),
	A_JmpIfRandom1of2(["ACTION_48_shift_southwest_steps_27"]),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNortheastSteps(3),
	A_Pause(8),
	A_WalkNortheastSteps(4),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(2),
	A_Pause(8),
	A_Walk1StepNorthwest(),
	A_WalkSouthwestSteps(4),
	A_Pause(8),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(8),
	A_WalkSouthwestSteps(4),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(12),
	A_Walk1StepNorthwest(),
	A_Pause(8),
	A_Jmp(["ACTION_48_object_memory_set_bit_0"]),
	A_WalkSouthwestSteps(5, identifier="ACTION_48_shift_southwest_steps_27"),
	A_Walk1StepSoutheast(),
	A_Pause(8),
	A_FaceSouthwest(),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(12),
	A_Walk1StepSouthwest(),
	A_Pause(8),
	A_WalkSouthwestSteps(5),
	A_FaceNorthwest(),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(16),
	A_JmpIfRandom1of2(["ACTION_48_pause_52"]),
	A_WalkNortheastSteps(3),
	A_FaceNorthwest(),
	A_JumpToHeight(height=72, silent=True),
	A_Pause(8),
	A_Walk1StepNorthwest(),
	A_WalkNortheastSteps(4),
	A_Pause(8),
	A_JumpToHeight(height=72, silent=True),
	A_Pause(8),
	A_Walk1StepNortheast(),
	A_Pause(8),
	A_Jmp(["ACTION_48_object_memory_set_bit_0"]),
	A_Pause(8, identifier="ACTION_48_pause_52"),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(16),
	A_Walk1StepSoutheast(),
	A_Walk1StepSouthwest(),
	A_Walk1StepNorthwest(),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestSteps(2),
	A_FaceNortheast(),
	A_JumpToHeight(height=72, silent=True),
	A_Pause(8),
	A_Walk1StepNortheast(),
	A_Pause(4),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(4),
	A_Pause(8),
	A_JumpToHeight(height=88, silent=True),
	A_WalkNortheastSteps(2),
	A_Pause(8),
	A_Jmp(["ACTION_48_object_memory_set_bit_0"])
])
