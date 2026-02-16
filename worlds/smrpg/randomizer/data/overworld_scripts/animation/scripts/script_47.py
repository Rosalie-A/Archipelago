#A0047_SKY_BRIDGE_BULLET_BILL
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
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b'\xc8#')),
	A_AddConstToVar(X_COORD_2, 224),
	A_AddConstToVar(Y_COORD_2, 112),
	A_AddConstToVar(Z_COORD_2, 384),
	A_UnknownCommand(bytearray(b'\x99')),
	A_PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
	A_VisibilityOn(),
	A_SetVarToConst(TEMP_7034, 65535),
	A_CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=DUMMY_0X07, destinations=["ACTION_47_set_animation_speed_10"]),
	A_SetAllSpeeds(FAST, identifier="ACTION_47_set_animation_speed_10"),
	A_SetBit(TEMP_7044_5),
	A_WalkSoutheastSteps(2),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_WalkSoutheastSteps(15),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_WalkSoutheastSteps(12),
	A_VisibilityOff(),
	A_ReturnQueue()
])
