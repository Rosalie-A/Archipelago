#A0340_SHIP_PUZZLE_HINT_VANISH
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
	A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_JumpToHeight(height=160, silent=True),
	A_Pause(13),
	A_FloatingOff(),
	A_StartLoopNTimes(7),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
