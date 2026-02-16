#A0144_FROGFUCIUS
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
	A_Pause(120, identifier="ACTION_144_pause_0"),
	A_Pause(120),
	A_SetSpriteSequence(index=6, is_mold=True, looping=True),
	A_Pause(120),
	A_Pause(30),
	A_ResetProperties(),
	A_Pause(60),
	A_SetSpriteSequence(index=6, is_mold=True, looping=True),
	A_Pause(6),
	A_ResetProperties(),
	A_Pause(12),
	A_SetSpriteSequence(index=6, is_mold=True, looping=True),
	A_Pause(6),
	A_ResetProperties(),
	A_Pause(20),
	A_Pause(120),
	A_Pause(120),
	A_Pause(120),
	A_Pause(120),
	A_Jmp(["ACTION_144_pause_0"])
])
