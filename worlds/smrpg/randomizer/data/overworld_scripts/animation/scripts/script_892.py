#A0892_KNIFE_GUY_DEFAULT
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
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=0, looping=True, identifier="ACTION_892_set_sprite_sequence_2"),
	A_Pause(32),
	A_SetSpriteSequence(index=1, looping=True),
	A_Pause(32),
	A_Jmp(["ACTION_892_set_sprite_sequence_2"])
])
