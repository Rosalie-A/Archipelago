#A0056_SEWER_WATER_DRAIN
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
	A_Set700CToCurrentLevel(identifier="ACTION_56_set_700C_to_current_level_0"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 302, ["ACTION_56_set_vram_priority_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 303, ["ACTION_56_set_vram_priority_9"]),
	A_Pause(1),
	A_JmpIfBitClear(SEWER_WATER_LEVEL, ["ACTION_56_set_700C_to_current_level_0"]),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_ClearSolidityBits(cant_walk_through=True, bit_7=True),
	A_ReturnQueue(),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES, identifier="ACTION_56_set_vram_priority_9"),
	A_JmpIfBitSet(SEWER_BOSS_DEFEATED, ["ACTION_56_set_solidity_bits_14"]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_Pause(1),
	A_Jmp(["ACTION_56_set_vram_priority_9"]),
	A_SetSolidityBits(cant_walk_through=True, bit_7=True, identifier="ACTION_56_set_solidity_bits_14"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
	A_Pause(1),
	A_ReturnQueue()
])
