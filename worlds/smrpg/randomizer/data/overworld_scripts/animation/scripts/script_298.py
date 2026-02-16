#A0298_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH_BASE
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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True, identifier="ACTION_298_clear_solidity_bits_0"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetBit(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_SetSpriteSequence(index=2, looping=False),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_FAST),
	A_AddZCoord1Step(),
	A_Pause(24),
	A_VisibilityOff(),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_ReturnQueue()
])
