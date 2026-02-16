#A0921_SEQ_1_FALLING
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
	A_FloatingOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(1, identifier="ACTION_921_pause_5"),
	A_Jmp(["ACTION_921_pause_5"])
])
