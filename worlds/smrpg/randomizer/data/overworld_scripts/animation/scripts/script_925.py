#A0925_SPINNING_STATIC_COIN
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
	A_SetPriority(2, identifier="ACTION_925_set_priority_0"),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 79, ["ACTION_925_set_priority_4"]),
	A_SetSequenceSpeed(SLOW),
	A_SetPriority(3, identifier="ACTION_925_set_priority_4"),
	A_WalkSouthPixels(3),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(1, identifier="ACTION_925_pause_7"),
	A_Jmp(["ACTION_925_pause_7"])
])
