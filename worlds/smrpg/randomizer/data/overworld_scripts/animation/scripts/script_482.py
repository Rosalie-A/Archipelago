#A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND
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
	A_ClearBit(DIRECTIONAL_7047_0),
	A_Pause(32),
	A_OverwriteSolidity(),
	A_SetPriority(3),
	A_ShadowOn(),
	A_FaceSouth(),
	A_JmpIfBitSet(DIRECTIONAL_7047_4, ["ACTION_482_clear_bit_18"]),
	A_SetSpriteSequence(index=0, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x00\x00\xb0\x00')),
	A_UnknownCommand(bytearray(b'%\x80\t\x80\xff')),
	A_Pause(16),
	A_ShadowOff(),
	A_Pause(24),
	A_BPL262728(),
	A_UnknownCommand(bytearray(b'\xfd\x9c:')),
	A_ReturnQueue(),
	A_ClearBit(DIRECTIONAL_7047_4, identifier="ACTION_482_clear_bit_18"),
	A_FaceSouthwest(),
	A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x00\x00\xb0\x00')),
	A_UnknownCommand(bytearray(b'%\x80\t\x80\xff')),
	A_Pause(16),
	A_ShadowOff(),
	A_Pause(24),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_UnknownCommand(bytearray(b'$\x00\x00\x00\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_Pause(30),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_UnknownCommand(bytearray(b'%\x80\x04\x80\xff')),
	A_Pause(20),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_UnknownCommand(bytearray(b'%@\x02\x80\xff')),
	A_Pause(10),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_BPL262728(),
	A_Pause(16),
	A_Jmp(["ACTION_384_sequence_looping_on_0"])
])
