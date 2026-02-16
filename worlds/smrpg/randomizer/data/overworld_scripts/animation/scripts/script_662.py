#A0662_ROSE_TOWN_LIBERATED_WATER_GUY
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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	A_FaceSoutheast(),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(2),
	A_SetSolidityBits(cant_walk_through=True),
	A_Walk1StepNortheast(),
	A_FaceSouthwest(),
	A_SetSequenceSpeed(SLOW),
	A_SetBit(TEMP_7043_7),
	A_ReturnQueue()
])
