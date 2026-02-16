#A0643_MIDAS_2ND_TUNNELS_FISH
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
	A_SetPriority(3),
	A_SetWalkingSpeed(SLOW),
	A_JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_643_shift_southeast_steps_24"]),
	A_Pause(173),
	A_StartLoopNTimes(4),
	A_WalkSoutheastSteps(2),
	A_WalkNorthwestSteps(2),
	A_EndLoop(),
	A_StartLoopNTimes(3),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(3),
	A_EndLoop(),
	A_WalkSoutheastSteps(6),
	A_JumpToHeight(120),
	A_SetAllSpeeds(FAST),
	A_FixedFCoordOn(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkNortheastSteps(2),
	A_Pause(7),
	A_FloatingOff(),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetBit(TEMP_7043_3),
	A_ReturnQueue(),
	A_WalkSoutheastSteps(2, identifier="ACTION_643_shift_southeast_steps_24"),
	A_WalkNorthwestSteps(2),
	A_Jmp(["ACTION_643_shift_southeast_steps_24"])
])
