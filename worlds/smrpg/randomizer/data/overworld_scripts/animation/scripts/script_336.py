#A0336_SHIP_BARREL_PUZZLE_BUTTON
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
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(1, identifier="ACTION_336_pause_5"),
	A_JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_336_pause_5"]),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=1, destinations=["ACTION_336_pause_5"]),
	A_JmpIfObjectWithinRange(comparing_npc=NPC_0, usually=208, tiles=0, destinations=["ACTION_336_pause_5"]),
	A_Dec(TEMP_70AE),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ReturnQueue()
])
