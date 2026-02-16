#A0406_STAR_HILL_3RD_ROOM_MUKU
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
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True, identifier="ACTION_406_clear_solidity_bits_0"),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_ShiftToXYCoords(x=26, y=93),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(160),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_SetSpriteSequence(index=9, looping=False),
	A_Pause(292),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_ShiftToXYCoords(x=0, y=0),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_Pause(48),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(1),
	A_ShiftToXYCoords(x=22, y=101),
	A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
	A_Pause(160),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_SetSpriteSequence(index=9, looping=False, mirror_sprite=True),
	A_Pause(292),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOff(),
	A_Pause(48),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(1),
	A_ShiftToXYCoords(x=20, y=121),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
	A_Pause(160),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_SetSpriteSequence(index=9, looping=False, mirror_sprite=True),
	A_Pause(292),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOff(),
	A_Pause(48),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_ShiftToXYCoords(x=26, y=117),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(160),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_SetSpriteSequence(index=9, looping=False),
	A_Pause(292),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOff(),
	A_Pause(48),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(1),
	A_ShiftToXYCoords(x=20, y=73),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(160),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_SetSpriteSequence(index=9, looping=False),
	A_Pause(292),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOff(),
	A_Pause(48),
	A_Jmp(["ACTION_406_clear_solidity_bits_0"])
])
