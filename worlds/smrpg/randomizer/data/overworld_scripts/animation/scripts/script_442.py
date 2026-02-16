#A0442_ROSE_WAY_CROOK
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
	A_Pause(25, identifier="ACTION_442_pause_0"),
	A_FaceMario(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_442_set_animation_speed_4"]),
	A_Jmp(["ACTION_442_pause_0"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_442_set_animation_speed_4"),
	A_SequencePlaybackOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_WalkFDirectionSteps(2),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_SequencePlaybackOff(),
	A_Jmp(["ACTION_442_pause_0"])
])
