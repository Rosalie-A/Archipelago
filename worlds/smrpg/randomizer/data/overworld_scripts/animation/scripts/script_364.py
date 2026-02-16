#A0364_BOOSTER_HILL_LEFTOVER_FLOWERS
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
	A_SetPriority(2),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FAST),
	A_JmpIfRandom1of2(["ACTION_364_transfer_to_xyzf_6"]),
	A_TransferToXYZF(x=1, y=50, z=0, direction=EAST),
	A_Jmp(["ACTION_364_visibility_on_9"]),
	A_TransferToXYZF(x=2, y=48, z=0, direction=EAST, identifier="ACTION_364_transfer_to_xyzf_6"),
	A_Jmp(["ACTION_364_visibility_on_9"]),
	A_TransferToXYZF(x=3, y=46, z=0, direction=EAST),
	A_VisibilityOn(identifier="ACTION_364_visibility_on_9"),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_Walk1StepSoutheast(identifier="ACTION_364_walk_1_step_southeast_12"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	A_JmpIfComparisonResultIsLesser(["ACTION_364_walk_1_step_southeast_12"]),
    A_VisibilityOff(),
	A_ReturnQueue()
])
