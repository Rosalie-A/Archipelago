#A0781_PLAYER_SPINS_ON_FLOWER
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
	A_JmpIfBitSet(SPINNING_FLOWER_1, ["ACTION_781_play_sound_12"]),
	A_SetBit(TEMP_7043_0),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetVRAMPriority(PRIORITY_3),
	A_UnknownCommand(bytearray(b'\xc8\x91')),
	A_SetWalkingSpeed(SLOW),
	A_WalkTo70167018(),
	A_SetWalkingSpeed(NORMAL),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_ClearBit(TEMP_7043_0),
	A_ReturnQueue(),
	A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4, identifier="ACTION_781_play_sound_12"),
	A_JumpToHeight(height=48, silent=True),
	A_WalkTo70167018(),
	A_ReturnQueue()
])
