#A0590_KEEP_FINAL_ROOM_CHANDELIER_STRING
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
	A_FixedFCoordOn(),
	A_WalkSouthPixels(1, identifier="ACTION_590_shift_south_pixels_1"),
	A_WalkNorthPixels(1),
	A_WalkSouthPixels(1),
	A_WalkNorthPixels(1),
	A_Pause(40),
	A_JmpIfRandom2of3(['ACTION_590_pause_9', 'ACTION_590_pause_11']),
	A_Pause(50),
	A_Jmp(["ACTION_590_shift_south_pixels_1"]),
	A_Pause(120, identifier="ACTION_590_pause_9"),
	A_Jmp(["ACTION_590_shift_south_pixels_1"]),
	A_Pause(100, identifier="ACTION_590_pause_11"),
	A_WalkSouthPixels(1),
	A_WalkNorthPixels(1),
	A_Pause(90),
	A_JmpIfRandom1of2(["ACTION_590_pause_9"]),
	A_Jmp(["ACTION_590_shift_south_pixels_1"])
])
