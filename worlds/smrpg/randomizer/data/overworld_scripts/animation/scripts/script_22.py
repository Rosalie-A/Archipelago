#A0022_SLOW_REPEATED_JUMPING
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
	A_JumpToHeight(height=80, silent=True, identifier="ACTION_22_jump_to_height_silent_0"),
	A_Pause(1, identifier="ACTION_22_pause_1"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_22_pause_1"]),
	A_Jmp(["ACTION_22_jump_to_height_silent_0"])
])
