#A0169_BANDITS_WAY_GOOMBA
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
	A_Pause(2),
	A_EndLoop(),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_169_set_animation_speed_6"),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_Walk1StepSouthwest(),
	A_Pause(9),
	A_ResetProperties(),
	A_Pause(9),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_StartLoopNTimes(2),
	A_TurnClockwise45DegreesNTimes(6),
	A_Walk1StepFDirection(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_EndLoop(),
	A_Pause(15),
	A_FaceSoutheast(),
	A_Pause(15),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_Walk1StepSoutheast(),
	A_Pause(9),
	A_ResetProperties(),
	A_Pause(9),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_StartLoopNTimes(2),
	A_TurnClockwise45DegreesNTimes(2),
	A_Walk1StepFDirection(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_EndLoop(),
	A_Pause(15),
	A_FaceSouthwest(),
	A_Pause(15),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	A_Jmp(["ACTION_169_set_animation_speed_6"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_169_set_animation_speed_39"),
	A_SetSequenceSpeed(VERY_FAST),
	A_StartLoopNTimes(1),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_EndLoop(),
	A_Jmp(["ACTION_169_set_animation_speed_6"])
])
