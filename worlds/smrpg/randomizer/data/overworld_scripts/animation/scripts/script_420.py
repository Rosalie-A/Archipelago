#A0420_GOOMBA_THUMPIN_BONK
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
	A_JmpToSubroutine(["ACTION_420_set_sprite_sequence_2"]),
	A_Jmp(["ACTION_416_transfer_to_xyzf_47"]),
	A_SetSpriteSequence(index=1, is_mold=True, looping=True, identifier="ACTION_420_set_sprite_sequence_2"),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ShiftZDownPixels(4),
	A_VisibilityOff(),
	A_ResetProperties(),
	A_ReturnQueue()
])
