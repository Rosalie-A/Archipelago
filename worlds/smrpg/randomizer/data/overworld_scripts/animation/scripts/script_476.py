#A0476_BANDITS_WAY_SPINY
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
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_SetAllSpeeds(NORMAL, identifier="ACTION_476_set_animation_speed_6"),
	A_StartLoopNTimes(2),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(5),
	A_EndLoop(),
	A_Pause(16),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	A_Walk1StepFDirection(),
	A_Pause(16),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	A_Jmp(["ACTION_476_set_animation_speed_6"]),
	A_SetAllSpeeds(FAST, identifier="ACTION_476_set_animation_speed_17"),
	A_StartLoopNTimes(1),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_EndLoop(),
	A_Jmp(["ACTION_476_set_animation_speed_6"])
])
