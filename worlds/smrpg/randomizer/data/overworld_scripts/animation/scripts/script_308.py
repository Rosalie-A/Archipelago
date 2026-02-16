#A0308_SHIP_FIRST_WHIRLPOOL_ROOM_FISH
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
	A_SetMovementsBits(bit_0=True, cant_walk_under=True),
	A_SetWalkingSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x80\x00\x80')),
	A_TurnRandomDirection(identifier="ACTION_308_turn_random_direction_5"),
	A_WalkFDirectionSteps(2),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_TurnRandomDirection(),
	A_WalkFDirectionSteps(2),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_308_face_mario_13"]),
	A_Jmp(["ACTION_308_turn_random_direction_5"]),
	A_FaceMario(identifier="ACTION_308_face_mario_13"),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepFDirection(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_Jmp(["ACTION_308_turn_random_direction_5"])
])
