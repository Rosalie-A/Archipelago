#A0457_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_ShadowOn(),
	A_SequenceLoopingOn(),
	A_WalkSouthwestSteps(2),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x00\x00\x80\x01')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x80\xfe\x00\x00'), identifier="ACTION_457_db_15"),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x00\xff\x00\x01')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_BPL262728(),
	A_Pause(16),
	A_ResetProperties(),
	A_Pause(16),
	A_WalkToXYCoords(x=20, y=95),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$0\x01\x00\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x00\x01\x00\xff')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_BPL262728(),
	A_Pause(16),
	A_ResetProperties(),
	A_Pause(16),
	A_WalkToXYCoords(x=21, y=88),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_Jmp(["ACTION_457_db_15"])
])
