#A0577_CURTAIN_GAME_OPEN_CURTAIN
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
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_Pause(5),
	A_ResetProperties(),
	A_FaceNorthwest(),
	A_ReturnQueue()
])
