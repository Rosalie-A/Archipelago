#A0481_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_Pause(128),
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
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_StartLoopNTimes(2),
	A_UnknownCommand(bytearray(b'$\xc0\x00\xa0\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_EndLoop(),
	A_StartLoopNTimes(1, identifier="ACTION_481_start_loop_n_times_21"),
	A_UnknownCommand(bytearray(b'$\xa0\xff@\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_UnknownCommand(bytearray(b'$\xa0\xff\xc0\xff')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_UnknownCommand(bytearray(b'$`\x00\xc0\xff')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_UnknownCommand(bytearray(b'$`\x00@\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(30),
	A_EndLoop(),
	A_Jmp(["ACTION_481_start_loop_n_times_21"])
])
