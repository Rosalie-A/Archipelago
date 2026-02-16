#A0092_BRIDGE_TADPOLE
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
	A_SetSequenceSpeed(FAST),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_92_visibility_on_3"]),
	A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	A_VisibilityOn(identifier="ACTION_92_visibility_on_3"),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(10),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(5),
	A_SetWalkingSpeed(FAST),
	A_WalkNorthwestPixels(9),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestPixels(11),
	A_SetWalkingSpeed(SLOW),
	A_WalkNorthwestPixels(9),
	A_Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
