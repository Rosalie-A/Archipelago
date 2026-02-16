#A0533_MUSHROOM_WAY_1_TROOPA
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
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x06\x00\x01\x00\x00\x00\x04\x80')),
	A_SetSequenceSpeed(FAST, identifier="ACTION_533_set_animation_speed_2"),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastSteps(1),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastSteps(1),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSoutheastSteps(1),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(1),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestSteps(1),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkSouthwestSteps(1),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestSteps(1),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(SLOW),
	A_WalkNorthwestSteps(1),
	A_Jmp(["ACTION_533_set_animation_speed_2"])
])
