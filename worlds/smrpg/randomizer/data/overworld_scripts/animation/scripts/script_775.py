#A0775_PLAYER_FALLS_IN_KEEP_LAVA
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
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_775_set_var_to_const_11"]),
	A_PlaySound(sound=SO105_SURPRISE, channel=4),
	A_SetAllSpeeds(VERY_FAST),
	A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
	A_JumpToHeight(height=112, silent=True, identifier="ACTION_775_jump_to_height_silent_5"),
	A_WalkSouthwestPixels(1),
	A_WalkWestPixels(4, identifier="ACTION_775_shift_west_pixels_7"),
	A_JmpIfMarioInAir(["ACTION_775_shift_west_pixels_7"]),
	A_PlaySound(sound=SO084_SMOKED, channel=4),
	A_Jmp(["ACTION_775_jump_to_height_silent_5"]),
	A_SetVarToConst(TEMP_7034, 65535, identifier="ACTION_775_set_var_to_const_11"),
	A_UnknownCommand(bytearray(b'\xc7\x00')),
	A_CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["ACTION_775_pause_14"]),
	A_Pause(6, identifier="ACTION_775_pause_14"),
	A_Jmp(["ACTION_775_set_var_to_const_11"])
])
