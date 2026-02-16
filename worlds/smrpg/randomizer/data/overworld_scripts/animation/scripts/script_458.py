#A0458_NIMBUS_POST_THRONE_BIRD
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
	A_SequenceLoopingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_458_set_animation_speed_3"),
	A_SetSequenceSpeed(FAST),
	A_StartLoopNTimes(1),
	A_FaceMario(),
	A_WalkFDirectionSteps(1),
	A_JmpIfRandom1of2(["ACTION_458_set_animation_speed_10"]),
	A_Pause(30),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_458_set_animation_speed_10"),
	A_SetSequenceSpeed(NORMAL),
	A_EndLoop(),
	A_Jmp(["ACTION_458_set_animation_speed_3"])
])
