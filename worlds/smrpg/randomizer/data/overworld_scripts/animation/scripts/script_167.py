#A0167_SPAWN_AT_7016_701A_CALCULATED
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
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_FloatingOff(),
	A_UnknownCommand(bytearray(b'\xc8\x00')),
	A_AddConstToVar(X_COORD_2, 62848),
	A_AddConstToVar(Y_COORD_2, 1280),
	A_SetVarToConst(Z_COORD_2, 144),
	A_UnknownCommand(bytearray(b'\x99')),
	A_SetWalkingSpeed(FAST),
	A_WalkNortheastSteps(4),
	A_VisibilityOn(),
	A_SequenceLoopingOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(15),
	A_VisibilityOff(),
	A_ReturnQueue()
])
