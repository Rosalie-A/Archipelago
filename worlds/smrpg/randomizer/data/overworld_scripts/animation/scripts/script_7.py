#A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED
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
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x03\x80\xff')),
	A_Pause(8),
	A_BPL262728(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_Pause(24),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%@\x00\x80\xff')),
	A_Pause(8),
	A_BPL262728(),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
