#A0170_MIDAS_BARRELS_WATER_SPLASH
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
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetPriority(3),
	A_SequenceLoopingOn(),
	A_AddConstToVar(Z_COORD_2, 2),
	A_UnknownCommand(bytearray(b'\x9a')),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkEastPixels(4),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[3]),
	A_VisibilityOn(),
	A_ReturnQueue()
])
