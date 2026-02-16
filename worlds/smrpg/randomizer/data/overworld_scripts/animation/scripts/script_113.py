#A0113_HENCHMAN_BOUNCING_IN_PLACE
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
	A_JmpIfBitSet(TEMP_7043_3, ["ACTION_113_shift_west_pixels_4"], identifier="ACTION_113_jmp_if_bit_set_0"),
	A_FaceNortheast(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FASTEST),
	A_WalkWestPixels(1, identifier="ACTION_113_shift_west_pixels_4"),
	A_Pause(1),
	A_WalkEastPixels(1),
	A_Pause(1),
	A_Jmp(["ACTION_113_shift_west_pixels_4"])
])
