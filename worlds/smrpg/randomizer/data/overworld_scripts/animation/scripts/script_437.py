#A0437_ROSE_WAY_SWINGING_PLATFORM_1
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
	A_ShiftXYPixels(x=16, y=248),
	A_ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x07')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00@\x00\x01\x00\x00\x00\x02\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00 \x00\x01\x00\x00\x00\x02\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x0c\x00\x01\x00\x00\x00\x04\x80')),
	A_Pause(1, identifier="ACTION_437_pause_7"),
	A_Jmp(["ACTION_437_pause_7"])
])
