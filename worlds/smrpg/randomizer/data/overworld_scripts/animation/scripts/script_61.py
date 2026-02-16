#A0061_SEWER_RATS_IN_A_LINE
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
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_61_object_memory_set_bit_0"),
	A_SetPriority(2),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_61_pause_8"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_61_pause_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_61_pause_10"]),
	A_Pause(3),
	A_Pause(3, identifier="ACTION_61_pause_8"),
	A_Pause(3, identifier="ACTION_61_pause_9"),
	A_Pause(3, identifier="ACTION_61_pause_10"),
	A_WalkFDirectionSteps(2),
	A_Pause(5),
	A_TurnClockwise45DegreesNTimes(4),
	A_JmpIfRandom1of2(["ACTION_61_object_memory_set_bit_0"]),
	A_Pause(8),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_61_object_memory_set_bit_0"])
])
