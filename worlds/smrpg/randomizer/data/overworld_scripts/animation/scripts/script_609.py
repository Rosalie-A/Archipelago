#A0609_MINES_LONG_TRACK_ROOM_SHY_GUY
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
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_Pause(1, identifier="ACTION_609_pause_3"),
	A_JmpIfBitClear(TEMP_7044_7, ["ACTION_609_pause_3"]),
	A_ResetProperties(),
	A_FaceSouthwest(),
	A_SequenceLoopingOff(),
	A_SequencePlaybackOff(),
	A_TransferToObjectXY(NPC_1),
	A_TransferXYZFPixels(x=0, y=0, z=11, direction=EAST),
	A_SetWalkingSpeed(FAST),
	A_VisibilityOn(),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	A_ShiftZUpPixels(1, identifier="ACTION_609_shift_z_up_pixels_14"),
	A_Pause(2),
	A_ShiftZDownPixels(1),
	A_Pause(2),
	A_JmpIfObjectInSpecificLevel(NPC_1, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, ["ACTION_609_shift_z_up_pixels_14"]),
	A_VisibilityOff(),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_ReturnQueue()
])
