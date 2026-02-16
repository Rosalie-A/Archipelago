#A0289_MARIO_DISMOUNT_YOSHI
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
	A_SetSequenceSpeed(SLOW),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ClearBit(TEMP_7044_0),
	A_ClearBit(TEMP_7044_1),
	A_ClearBit(TEMP_7044_2),
	A_ClearBit(TEMP_7044_3),
	A_ClearBit(TEMP_7044_5),
	A_Pause(12),
	A_SetSequenceSpeed(SLOW),
	A_SetWalkingSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_SetSolidityBits(cant_walk_through=True),
	A_ClearSolidityBits(cant_pass_npcs=True),
	A_CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_ReturnQueue()
])
