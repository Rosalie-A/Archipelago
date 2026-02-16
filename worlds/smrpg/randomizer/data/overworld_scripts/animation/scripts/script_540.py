#A0540_JUMPING_GOOMBA_MUSHROOM_WAY_2
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
	A_SetBit(TEMP_7044_4),
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_SetSolidityBits(cant_pass_walls=True),
	A_SetAllSpeeds(NORMAL),
	A_SequenceLoopingOn(),
	A_JumpToHeight(144),
	A_WalkSouthwestSteps(3),
	A_Pause(60),
	A_FixedFCoordOn(),
	A_SetAllSpeeds(NORMAL),
	A_WalkNortheastSteps(3),
	A_ClearBit(TEMP_7044_4),
	A_ReturnQueue()
])
