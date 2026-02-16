#A0227_ENDING_CUTSCENE_EFFECT
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
	A_SetSequenceSpeed(VERY_SLOW),
	A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=True),
	A_Pause(98),
	A_SetSequenceSpeed(SLOW),
	A_Pause(162),
	A_SetSequenceSpeed(NORMAL),
	A_Pause(162),
	A_SetSequenceSpeed(FAST),
	A_Pause(214),
	A_SetSequenceSpeed(FASTER),
	A_Pause(216),
	A_SetSequenceSpeed(VERY_FAST),
	A_Pause(384),
	A_SetWalkingSpeed(VERY_SLOW),
	A_AddZCoord1Step(),
	A_ReturnQueue()
])
