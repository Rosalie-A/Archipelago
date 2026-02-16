#A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM
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
	A_Pause(1, identifier="ACTION_823_pause_0"),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 2176),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_823_pause_0"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 9216),
	A_JmpIfComparisonResultIsLesser(["ACTION_823_object_memory_modify_bits_13"]),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 13056),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_823_object_memory_modify_bits_13"]),
	A_SetPriority(0),
	A_ShadowOn(),
	A_Jmp(["ACTION_823_pause_0"]),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6], identifier="ACTION_823_object_memory_modify_bits_13"),
	A_ShadowOff(),
	A_Jmp(["ACTION_823_pause_0"])
])
