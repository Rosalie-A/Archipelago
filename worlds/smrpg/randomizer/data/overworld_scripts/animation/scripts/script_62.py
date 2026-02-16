#A0062_SEWER_RAT_NEAR_PROGRESSION_PIPE
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_62_object_memory_set_bit_0"),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(2),
	A_WalkNortheastSteps(2),
	A_Jmp(["ACTION_62_object_memory_set_bit_0"])
])
