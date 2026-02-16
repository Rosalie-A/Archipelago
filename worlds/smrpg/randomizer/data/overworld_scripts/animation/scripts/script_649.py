#A0649_MOLEVILLE_WOMAN_ON_MOUNTAIN
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
	A_FaceSouthwest(),
	A_FixedFCoordOn(),
	A_SetAllSpeeds(VERY_FAST, identifier="ACTION_649_set_animation_speed_2"),
	A_Walk1StepSouthwest(),
	A_SequenceLoopingOn(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=8, destinations=["ACTION_649_start_loop_n_times_8"]),
	A_Pause(30),
	A_Jmp(["ACTION_649_set_animation_speed_14"]),
	A_StartLoopNTimes(4, identifier="ACTION_649_start_loop_n_times_8"),
	A_PlaySound(sound=SO058_INSERT, channel=4),
	A_Pause(2),
	A_PlaySound(sound=SO058_INSERT, channel=4),
	A_Pause(4),
	A_EndLoop(),
	A_SetAllSpeeds(SLOW, identifier="ACTION_649_set_animation_speed_14"),
	A_Walk1StepNortheast(),
	A_SequenceLoopingOff(),
	A_Pause(20),
	A_Jmp(["ACTION_649_set_animation_speed_2"])
])
