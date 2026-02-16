#A0040_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_WATER_DROPLETS
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
	A_StartLoopNTimes(2),
	A_Pause(1, identifier="ACTION_40_pause_1"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_40_pause_1"]),
	A_SetVarToConst(X_COORD_2, 15104),
	A_SetVarToConst(Y_COORD_2, 3712),
	A_SetVarToConst(Z_COORD_2, 0),
	A_UnknownCommand(bytearray(b'\x99')),
	A_VisibilityOn(),
	A_SequenceLoopingOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(15),
	A_VisibilityOff(),
	A_EndLoop(),
	A_ReturnQueue()
])
