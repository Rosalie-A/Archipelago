#A0157_MELODY_BAY_TADPOLES
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
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_157_set_sprite_sequence_3"]),
	A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True, identifier="ACTION_157_set_sprite_sequence_3"),
	A_Pause(12),
	A_VisibilityOff(),
	A_ReturnQueue()
])
