#A0917_SEQ_0_FALLING
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
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_VisibilityOff(identifier="ACTION_917_default"),
	A_Pause(2, identifier="ACTION_917_pause_2"),
	A_SetPriority(3),
	A_VisibilityOn(),
	A_FloatingOn(),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(1, identifier="ACTION_917_pause_8"),
	A_Jmp(["ACTION_917_pause_8"])
])
