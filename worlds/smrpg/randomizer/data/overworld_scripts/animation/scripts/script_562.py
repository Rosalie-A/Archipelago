#A0562_SONG_HINT_TADPOLE_SUMMONING
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
	A_SetBit(TEMP_7043_6),
	A_ShiftToXYCoords(x=29, y=60),
	A_VisibilityOn(),
	A_SetSequenceSpeed(FAST),
	A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(12),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetWalkingSpeed(FAST),
	A_WalkSouthwestSteps(1),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestPixels(8),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestPixels(5),
	A_Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
