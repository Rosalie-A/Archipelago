#A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER
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
	A_SetVarToConst(TEMP_7034, 1),
	A_UnknownCommand(bytearray(b'\xc7\x07')),
	A_StartLoopNTimes(2),
	A_AddConstToVar(TEMP_7034, 1),
	A_AddConstToVar(Z_COORD_1, 8),
	A_CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_7"]),
	A_Pause(2),
	A_EndLoop(identifier="ACTION_976_end_loop_7"),
	A_SetVarToConst(TEMP_7034, 1),
	A_UnknownCommand(bytearray(b'\xc7\x07')),
	A_StartLoopNTimes(2),
	A_AddConstToVar(TEMP_7034, 1),
	A_AddConstToVar(Z_COORD_1, 8),
	A_CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_15"]),
	A_Pause(2),
	A_EndLoop(identifier="ACTION_976_end_loop_15"),
	A_ReturnQueue()
])
