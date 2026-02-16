#A0102_MK_THRONE_HENCHMAN_BOUNCE
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
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_102_jmp_if_random_above_128_6"]),
	A_JmpIfRandom2of3(['ACTION_103_clear_solidity_bits_0', 'ACTION_102_transfer_xyzf_pixels_4']),
	A_TransferXYZFPixels(x=0, y=0, z=9, direction=EAST),
	A_Jmp(["ACTION_103_set_animation_speed_5"]),
	A_TransferXYZFPixels(x=0, y=0, z=17, direction=EAST, identifier="ACTION_102_transfer_xyzf_pixels_4"),
	A_Jmp(["ACTION_103_set_animation_speed_9"]),
	A_JmpIfRandom1of2(["ACTION_101_pause_9"], identifier="ACTION_102_jmp_if_random_above_128_6"),
	A_Pause(30),
	A_Jmp(["ACTION_103_clear_solidity_bits_0"]),
	A_Pause(10),
	A_Jmp(["ACTION_103_clear_solidity_bits_0"])
])
