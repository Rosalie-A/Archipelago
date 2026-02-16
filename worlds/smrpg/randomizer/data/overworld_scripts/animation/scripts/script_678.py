#A0678_SAMUS
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_678_set_sprite_sequence_7"]),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_Pause(32),
	A_SetSequenceSpeed(SLOW),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_678_set_sprite_sequence_7"),
	A_Pause(40),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_Jmp(["ACTION_678_set_sprite_sequence_7"])
])
