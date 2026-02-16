#A0239_ENDING_CREDITS_CROCO
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
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="bandits_way_ascript_recoil"),
	A_Pause(18),
	A_ResetProperties(),
	A_Pause(10),
	A_FaceSoutheast(),
	A_Pause(2),
	A_FaceNortheast(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(10),
	A_FaceNorthwest(),
	A_Pause(90),
	A_WalkNortheastSteps(6),
	A_ReturnQueue()
])
