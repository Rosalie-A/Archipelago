#A0111_MK_HALL_REPEATING_HENCHMEN_STARTING
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
	A_ClearSolidityBits(bit_4=True, identifier="ACTION_111_clear_solidity_bits_0"),
	A_ClearSolidityBits(cant_walk_through=True),
	A_VisibilityOff(),
	A_Pause(60),
	A_FaceSoutheast(),
	A_VisibilityOn(),
	A_SetSolidityBits(bit_4=True),
	A_SetSolidityBits(cant_walk_through=True),
	A_StartLoopNTimes(4),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Walk1StepSoutheast(),
	A_WalkSoutheastPixels(11),
	A_BPL262728(),
	A_Pause(2),
	A_EndLoop(),
	A_Walk1StepSoutheast(),
	A_VisibilityOff(),
	A_ClearSolidityBits(bit_4=True),
	A_ClearSolidityBits(cant_walk_through=True),
	A_TransferToXYZF(x=8, y=32, z=4, direction=EAST),
	A_Pause(240),
	A_FaceNorthwest(),
	A_VisibilityOn(),
	A_SetSolidityBits(bit_4=True),
	A_SetSolidityBits(cant_walk_through=True),
	A_StartLoopNTimes(4),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Walk1StepNorthwest(),
	A_WalkNorthwestPixels(11),
	A_BPL262728(),
	A_Pause(2),
	A_EndLoop(),
	A_Walk1StepNorthwest(),
	A_VisibilityOff(),
	A_ClearSolidityBits(bit_4=True),
	A_ClearSolidityBits(cant_walk_through=True),
	A_TransferToXYZF(x=3, y=23, z=4, direction=EAST),
	A_Pause(180),
	A_SetBit(TEMP_7043_1),
	A_Jmp(["ACTION_111_clear_solidity_bits_0"])
])
