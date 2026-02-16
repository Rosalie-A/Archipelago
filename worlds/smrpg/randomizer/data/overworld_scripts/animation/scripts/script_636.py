#A0636_54_VELOCITY_SINGLE_JUMP
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
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JumpToHeight(height=64, silent=True),
	A_Pause(1, identifier="ACTION_636_pause_3"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_636_pause_3"]),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_ReturnQueue()
])
