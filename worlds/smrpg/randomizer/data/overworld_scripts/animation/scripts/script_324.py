#A0324_INVISIBLE_ITEM_SHIFT_1
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
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(3),
	A_JmpIfRandom1of2(["ACTION_324_walk_1_step_southeast_16"]),
	A_WalkNortheastSteps(2),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkNortheastSteps(2),
	A_VisibilityOff(),
	A_Pause(180),
	A_FaceSouthwest(),
	A_VisibilityOn(),
	A_WalkSouthwestSteps(4),
	A_WalkSoutheastSteps(1),
	A_TransferToXYZF(x=6, y=88, z=0, direction=EAST, identifier="ACTION_324_transfer_to_xyzf_14"),
	A_ReturnQueue(),
	A_Walk1StepSoutheast(identifier="ACTION_324_walk_1_step_southeast_16"),
	A_Jmp(["ACTION_324_transfer_to_xyzf_14"])
])
