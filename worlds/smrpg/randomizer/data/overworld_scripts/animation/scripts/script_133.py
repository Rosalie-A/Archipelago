#A0133_MK_OCCUPIED_EXTERIOR_REPEATING_HENCHMEN
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
	A_BPL262728(),
	A_TransferToXYZF(x=13, y=81, z=18, direction=EAST),
	A_Walk1StepSouthwest(),
	A_VisibilityOn(),
	A_WalkSouthwestPixels(12),
	A_SetSolidityBits(bit_4=True),
	A_SetSolidityBits(cant_walk_through=True),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(5),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(14),
	A_Pause(2),
	A_BPL262728(),
	A_EndLoop(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(1),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(14),
	A_Pause(2),
	A_BPL262728(),
	A_EndLoop(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_Pause(20),
	A_VisibilityOff(),
	A_ClearSolidityBits(bit_4=True),
	A_ClearSolidityBits(cant_walk_through=True),
	A_ReturnQueue()
])
