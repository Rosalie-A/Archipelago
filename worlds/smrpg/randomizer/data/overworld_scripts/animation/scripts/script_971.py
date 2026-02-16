#A0971_ENDING_CREDITS_CASTLE_SHY_GUY
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
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_SetPriority(1),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	A_WalkNorthPixels(5),
	A_SetWalkingSpeed(SLOW),
	A_WalkToXYCoords(x=5, y=6),
	A_ShiftToXYCoords(x=5, y=8),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthPixels(15),
	A_WalkSouthwestPixels(20),
	A_SetWalkingSpeed(SLOW),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_WalkSouthwestSteps(3),
	A_WalkSouthwestPixels(8),
	A_Pause(8),
	A_UnknownCommand(bytearray(b' \x05')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x80\x01\x00\x01\x00\x00\x00\x04\x80')),
	A_Pause(511),
	A_ReturnQueue()
])
