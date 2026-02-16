#A0293_MINES_FINAL_BOSS_ROOM_HENCHMAN_BASE
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
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6], identifier="ACTION_293_object_memory_modify_bits_0"),
	A_FaceMario(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkFDirectionSteps(2),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_AddConstToVar(PRIMARY_TEMP_700C, 4),
	A_Mem700CAndConst(0x0007),
	A_FaceEast7C(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_WalkFDirectionSteps(2),
	A_ReturnQueue()
])
