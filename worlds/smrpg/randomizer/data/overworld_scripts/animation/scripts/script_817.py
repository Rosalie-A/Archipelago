#A0817_LANDS_END_CANNON_AT_REST
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
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_817_set_sprite_sequence_6"]),
	A_SetPriority(3),
	A_SequenceLoopingOff(),
	A_FixedFCoordOn(),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="ACTION_817_set_sprite_sequence_6"),
	A_SequenceLoopingOff(),
	A_FixedFCoordOn(),
	A_ReturnQueue()
])
