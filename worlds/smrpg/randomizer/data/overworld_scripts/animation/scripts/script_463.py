#A0463_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_ShadowOn(),
	A_VisibilityOff(),
	A_Pause(64),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_WalkSouthwestSteps(6),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x00\x02\x00\x02')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x80\xfbp\xfe'), identifier="ACTION_463_db_18"),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x00\x01\x80\x03')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x80\xfcp\xfe')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=17, y=92),
	A_Pause(16),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x80\x03\x90\x01')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x00\xff\x00\xfd')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_UnknownCommand(bytearray(b'$\x80\x04\x90\x01')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(32),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=23, y=91),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_Jmp(["ACTION_463_db_18"])
])
