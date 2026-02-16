#A0127_BAG_APPEARS_BRIEFLY_THEN_POOFS
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
	A_ShadowOn(),
	A_FloatingOff(),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_VisibilityOff(),
	A_SequenceLoopingOn(),
	A_Pause(6),
	A_VisibilityOn(),
	A_Pause(26),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
	A_Pause(24),
	A_VisibilityOff(),
	A_ReturnQueue()
])
