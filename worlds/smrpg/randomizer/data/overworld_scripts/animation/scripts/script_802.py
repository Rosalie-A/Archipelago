#A0802_MUSHROOM_DERBY_UNKNOWN
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
	A_SequenceLoopingOn(),
	A_JmpIfRandom1of2(["ACTION_802_fixed_f_coord_off_18"]),
	A_WalkNortheastPixels(8),
	A_SequenceLoopingOff(),
	A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthwestPixels(8),
	A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True),
	A_Pause(30),
	A_ResetProperties(),
	A_SetWalkingSpeed(FAST),
	A_Pause(10),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Pause(30),
	A_ResetProperties(),
	A_FixedFCoordOff(identifier="ACTION_802_fixed_f_coord_off_18"),
	A_Walk1StepEast(),
	A_Walk1StepNorth(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkNortheastSteps(4),
	A_WalkNortheastPixels(4),
	A_WalkNorthwestSteps(4),
	A_SequenceLoopingOff(),
	A_FaceSouthwest(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ReturnQueue()
])
