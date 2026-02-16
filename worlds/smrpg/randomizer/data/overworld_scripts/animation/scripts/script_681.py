#A0681_MUSHROOM_DERBY_UNKNOWN
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
	A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, identifier="ACTION_681_set_sprite_sequence_0"),
	A_JumpToHeight(height=108, silent=True),
	A_Pause(1, identifier="ACTION_681_pause_2"),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_681_ret_7"]),
	A_JmpIfMarioInAir(["ACTION_681_pause_2"]),
	A_Pause(30),
	A_Jmp(["ACTION_681_set_sprite_sequence_0"]),
	A_ReturnQueue(identifier="ACTION_681_ret_7")
])
