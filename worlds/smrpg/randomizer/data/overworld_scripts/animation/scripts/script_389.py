#A0389_TOWER_BULLET_BILL_APPEARS
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
	A_ShiftToXYCoords(x=15, y=35),
	A_WalkSouthPixels(3),
	A_WalkNorthwestPixels(11),
	A_WalkSouthwestPixels(6),
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_VisibilityOn(),
	A_PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
	A_SequenceLoopingOn(),
	A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_WalkSouthwestSteps(10),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_VisibilityOff(),
	A_ReturnQueue()
])
