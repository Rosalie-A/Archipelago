#A0878_MONSTRO_GOOMBETTE
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
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_878_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
	A_FaceSouthwest7D(arg=0x00),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_878_face_east_7C_8"]),
	A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(identifier="ACTION_878_face_east_7C_8"),
	A_Pause(1),
	A_Jmp(["ACTION_878_set_animation_speed_0"])
])
