#A0920_STATIC_DRY_BONES_COLLAPSE
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
	A_PlaySound(sound=SO117_SPINNING_MONSTER, channel=4),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_920_set_sprite_sequence_14"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_920_set_sprite_sequence_14"]),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Pause(240),
	A_PlaySound(sound=SO117_SPINNING_MONSTER, channel=4),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(36),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_920_set_sprite_sequence_14"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Pause(120),
	A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
	A_Pause(36),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ReturnQueue()
])
