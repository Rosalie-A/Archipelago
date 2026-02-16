#A0101_MK_THRONE_HENCHMAN_BOUNCE
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
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_101_jmp_if_random_above_128_6"]),
	A_JmpIfRandom1of2(["ACTION_101_transfer_xyzf_pixels_4"]),
	A_TransferXYZFPixels(x=0, y=0, z=21, direction=EAST),
	A_Jmp(["ACTION_103_set_animation_speed_15"]),
	A_TransferXYZFPixels(x=0, y=0, z=14, direction=EAST, identifier="ACTION_101_transfer_xyzf_pixels_4"),
	A_Jmp(["ACTION_103_set_animation_speed_23"]),
	A_JmpIfRandom1of2(["ACTION_101_pause_9"], identifier="ACTION_101_jmp_if_random_above_128_6"),
	A_Pause(8),
	A_Jmp(["ACTION_103_clear_solidity_bits_0"]),
	A_Pause(20, identifier="ACTION_101_pause_9"),
	A_Jmp(["ACTION_103_clear_solidity_bits_0"])
])
