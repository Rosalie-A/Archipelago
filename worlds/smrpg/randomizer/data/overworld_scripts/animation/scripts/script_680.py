#A0680_MUSHROOM_DERBY_UNKNOWN
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
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(8, identifier="ACTION_680_pause_2"),
	A_SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_ResetProperties(),
	A_Pause(1, identifier="ACTION_680_pause_6"),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_680_ret_11"]),
	A_JmpIfMarioInAir(["ACTION_680_pause_6"]),
	A_Pause(30),
	A_Jmp(["ACTION_680_pause_2"]),
	A_ReturnQueue(identifier="ACTION_680_ret_11")
])
