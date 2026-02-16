#A0798_MUSHROOM_DERBY_UNKNOWN
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
	A_JmpIfRandom2of3(['ACTION_799_set_animation_speed_0', 'ACTION_800_pause_0']),
	A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True),
	A_JumpToHeight(height=80, silent=True),
	A_Pause(1, identifier="ACTION_798_pause_3"),
	A_JmpIfMarioInAir(["ACTION_798_pause_3"]),
	A_JumpToHeight(height=80, silent=True),
	A_Pause(1, identifier="ACTION_798_pause_6"),
	A_JmpIfMarioInAir(["ACTION_798_pause_6"]),
	A_JumpToHeight(height=80, silent=True),
	A_Pause(1, identifier="ACTION_798_pause_9"),
	A_JmpIfMarioInAir(["ACTION_798_pause_9"]),
	A_ResetProperties(),
	A_FaceNorthwest(),
	A_ReturnQueue()
])
