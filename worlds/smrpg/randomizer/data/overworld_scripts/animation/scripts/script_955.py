#A0955_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES
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
	A_SetWalkingSpeed(SLOW),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkToXYCoords(x=7, y=75),
	A_WalkNortheastPixels(11),
	A_UnknownCommand(bytearray(b' \x03')),
	A_UnknownCommand(bytearray(b'$\xc0\x01\xa0\x02')),
	A_Pause(5),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_BPL262728(),
	A_WalkSoutheastSteps(16),
	A_ShiftToXYCoords(x=8, y=35),
	A_WalkSoutheastSteps(5),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_Jmp(["ACTION_953_set_animation_speed_0"])
])
