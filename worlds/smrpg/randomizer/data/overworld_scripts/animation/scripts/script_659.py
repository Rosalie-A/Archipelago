#A0659_PIPE_VAULT_THWOMP_ROOM_GOOMBA
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_659_set_animation_speed_0"),
	A_SetSequenceSpeed(FAST),
	A_StartLoopNTimes(3),
	A_WalkNortheastSteps(2),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	A_EndLoop(),
	A_StartLoopNTimes(3),
	A_WalkSouthwestSteps(2),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	A_EndLoop(),
	A_Jmp(["ACTION_659_set_animation_speed_0"]),
	A_SetSequenceSpeed(VERY_FAST, identifier="ACTION_659_set_animation_speed_11"),
	A_SetWalkingSpeed(NORMAL),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_Jmp(["ACTION_659_set_animation_speed_0"])
])
