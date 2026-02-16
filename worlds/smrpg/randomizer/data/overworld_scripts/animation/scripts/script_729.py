#A0729_EXPLODING_MICROBOMB
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
	A_VisibilityOff(identifier="ACTION_729_visibility_off_0"),
	A_Pause(1),
	A_JmpIfBitClear(TEMP_7043_4, ["ACTION_729_visibility_off_0"]),
	A_VisibilityOn(),
	A_SequenceLoopingOn(),
	A_PlaySound(sound=SO089_LIT_FUSE, channel=4),
	A_SequencePlaybackOn(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_Pause(60),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
	A_Pause(20),
	A_VisibilityOff(),
	A_UnknownCommand(bytearray(b'\xc7\x07')),
	A_StartLoopNTimes(2),
	A_AddConstToVar(Z_COORD_1, 32),
	A_JmpToSubroutine(["ACTION_729_pause_42"]),
	A_CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	A_AddConstToVar(Z_COORD_1, 32),
	A_AddConstToVar(X_COORD_1, 64),
	A_Pause(10),
	A_JmpToSubroutine(["ACTION_729_pause_42"]),
	A_CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	A_AddConstToVar(Z_COORD_1, 32),
	A_AddConstToVar(X_COORD_1, 65408),
	A_Pause(11),
	A_JmpToSubroutine(["ACTION_729_pause_42"]),
	A_CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	A_AddConstToVar(Z_COORD_1, 32),
	A_AddConstToVar(Y_COORD_1, 64),
	A_Pause(9),
	A_JmpToSubroutine(["ACTION_729_pause_42"]),
	A_CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	A_AddConstToVar(Z_COORD_1, 32),
	A_AddConstToVar(Y_COORD_1, 65472),
	A_AddConstToVar(X_COORD_1, 64),
	A_Pause(11),
	A_JmpToSubroutine(["ACTION_729_pause_42"]),
	A_CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	A_Pause(10, identifier="ACTION_729_pause_38"),
	A_EndLoop(),
	A_SetBit(TEMP_7043_5),
	A_ReturnQueue(),
	A_Pause(1, identifier="ACTION_729_pause_42"),
	A_JmpIfBitSet(BAMBINO_BOMB_UNKNOWN, ["ACTION_729_pause_42"]),
	A_ReturnQueue()
])
