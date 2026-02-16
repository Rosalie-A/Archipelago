#A0284_IFRAME_BLINK
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
	A_UnknownCommand(bytearray(b'6')),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_JmpIfBitClear(TEMP_707C_1, ["ACTION_284_start_loop_n_times_4"]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(15, identifier="ACTION_284_start_loop_n_times_4"),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_EndLoop(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_UnknownCommand(bytearray(b'7')),
	A_ReturnQueue()
])
