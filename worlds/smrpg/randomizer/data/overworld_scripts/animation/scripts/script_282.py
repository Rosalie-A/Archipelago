#A0282_KEEP_BALL_SOLITAIRE_BALL
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
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
	A_IncPaletteRowBy(1),
	A_SetPriority(3),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkSouthwestPixels(10),
	A_ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetWalkingSpeed(NORMAL),
	A_ReturnQueue()
])
