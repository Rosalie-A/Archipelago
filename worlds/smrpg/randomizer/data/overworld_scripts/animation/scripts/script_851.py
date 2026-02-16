#A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT
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
	A_FloatingOff(),
	A_ShadowOn(),
	A_SetPriority(3),
	A_OverwriteSolidity(),
	A_FaceSoutheast(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetSequenceSpeed(VERY_FAST),
	A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
	A_Pause(80),
	A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
	A_SetWalkingSpeed(FASTEST),
	A_WalkToXYCoords(x=23, y=76),
	A_VisibilityOff(),
	A_ReturnQueue()
])
