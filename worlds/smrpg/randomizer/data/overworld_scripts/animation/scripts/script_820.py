#A0820_JUMP_OFF_SPINNING_FLOWER
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
	A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
	A_JmpIfBitSet(SPINNING_FLOWER_2, ["ACTION_820_set_animation_speed_3"]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetWalkingSpeed(FASTER, identifier="ACTION_820_set_animation_speed_3"),
	A_JumpToHeight(height=136, silent=True),
	A_WalkFDirectionPixels(3, identifier="ACTION_820_shift_f_direction_pixels_5"),
	A_JmpIfMarioInAir(["ACTION_820_shift_f_direction_pixels_5"]),
	A_SetWalkingSpeed(NORMAL),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ReturnQueue()
])
