#A1016_FREESTANDING_FLOWER_PICKED_UP
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
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetPriority(3),
	A_PlaySound(sound=SO014_FLOWER, channel=4),
	A_StartLoopNTimes(4),
	A_VisibilityOn(),
	A_Pause(7),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_ReturnQueue()
])
