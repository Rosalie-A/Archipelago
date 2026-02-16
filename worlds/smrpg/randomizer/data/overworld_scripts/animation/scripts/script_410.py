#A0410_FOREST_MAZE_AREA_BEE
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
	A_SetPriority(3),
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_UnknownCommand(bytearray(b' \x07')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x04\x80')),
	A_Pause(1, identifier="ACTION_410_pause_7"),
	A_Jmp(["ACTION_410_pause_7"])
])
