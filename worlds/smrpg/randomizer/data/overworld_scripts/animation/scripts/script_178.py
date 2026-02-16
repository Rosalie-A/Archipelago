#A0178_FOREST_ARROW
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
	A_VisibilityOff(),
	A_SetPriority(3),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 255, identifier="ACTION_178_set_var_to_random_2"),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_JmpIfRandom2of3(['ACTION_178_transfer_to_xyzf_19', 'ACTION_178_transfer_to_xyzf_31']),
	A_TransferToXYZF(x=11, y=52, z=17, direction=EAST),
	A_VisibilityOn(),
	A_OverwriteSolidity(bit_4=True, cant_walk_through=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x80\xfb\x00\x01')),
	A_UnknownCommand(bytearray(b'%\x00\x00`\xff')),
	A_Pause(16),
	A_UnknownCommand(bytearray(b'$\xe0\xff\x80\x00')),
	A_Pause(9),
	A_BPL262728(),
	A_OverwriteSolidity(),
	A_Jmp(["ACTION_178_play_sound_42"]),
	A_TransferToXYZF(x=3, y=48, z=17, direction=EAST, identifier="ACTION_178_transfer_to_xyzf_19"),
	A_VisibilityOn(),
	A_OverwriteSolidity(bit_4=True, cant_walk_through=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x80\x03\x00\x04')),
	A_UnknownCommand(bytearray(b'%\x00\x00`\xff')),
	A_Pause(16),
	A_UnknownCommand(bytearray(b'$ \x00\x80\x00')),
	A_Pause(9),
	A_BPL262728(),
	A_OverwriteSolidity(),
	A_Jmp(["ACTION_178_play_sound_42"]),
	A_TransferToXYZF(x=10, y=66, z=0, direction=SOUTH, identifier="ACTION_178_transfer_to_xyzf_31"),
	A_VisibilityOn(),
	A_OverwriteSolidity(bit_4=True, cant_walk_through=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x80\xfe\x80\xfe')),
	A_UnknownCommand(bytearray(b'%\x00\x00`\xff')),
	A_Pause(38),
	A_UnknownCommand(bytearray(b'$\xe0\xff\x00\xff')),
	A_Pause(9),
	A_BPL262728(),
	A_OverwriteSolidity(),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6, identifier="ACTION_178_play_sound_42"),
	A_SetSpriteSequence(index=0, looping=False),
	A_Pause(80),
	A_StartLoopNTimes(3),
	A_VisibilityOff(),
	A_Pause(3),
	A_VisibilityOn(),
	A_Pause(3),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ShiftToXYCoords(x=14, y=122),
	A_Jmp(["ACTION_178_set_var_to_random_2"])
])
