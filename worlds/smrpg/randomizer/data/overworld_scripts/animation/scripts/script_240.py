#A0240_SMITHY_COMPONENT
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
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_Pause(45),
	A_PlaySound(sound=SO145_BLACKSMITH_HAMMER_STRIKE, channel=4),
	A_SetBit(TEMP_7044_6),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_ReturnQueue()
])
