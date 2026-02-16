#A0507_SPARKLE_LINE_LOOPED
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
	A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_507_set_sprite_sequence_0"),
	A_Pause(8),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_Jmp(["ACTION_507_set_sprite_sequence_0"])
])
