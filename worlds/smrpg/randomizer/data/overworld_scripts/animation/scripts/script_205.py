#A0205_CASINO_SLOT_MACHINE_ROLLER
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
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetPriority(3),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="ACTION_205_set_sprite_sequence_2"),
	A_SetVarToConst(FACTORY_FALL_2, 2),
	A_JmpIfBitSet(DIRECTIONAL_7045_0, ["ACTION_205_pause_8"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_1, ["ACTION_205_pause_10"]),
	A_Pause(7),
	A_Jmp(["ACTION_205_set_sprite_sequence_11"]),
	A_Pause(4, identifier="ACTION_205_pause_8"),
	A_Jmp(["ACTION_205_set_sprite_sequence_11"]),
	A_Pause(9, identifier="ACTION_205_pause_10"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="ACTION_205_set_sprite_sequence_11"),
	A_SetVarToConst(FACTORY_FALL_2, 1),
	A_JmpIfBitSet(DIRECTIONAL_7045_0, ["ACTION_205_pause_17"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_1, ["ACTION_205_pause_19"]),
	A_Pause(7),
	A_Jmp(["ACTION_205_set_sprite_sequence_20"]),
	A_Pause(4, identifier="ACTION_205_pause_17"),
	A_Jmp(["ACTION_205_set_sprite_sequence_20"]),
	A_Pause(9, identifier="ACTION_205_pause_19"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="ACTION_205_set_sprite_sequence_20"),
	A_SetVarToConst(FACTORY_FALL_2, 0),
	A_JmpIfBitSet(DIRECTIONAL_7045_0, ["ACTION_205_pause_26"]),
	A_JmpIfBitSet(DIRECTIONAL_7045_1, ["ACTION_205_pause_28"]),
	A_Pause(7),
	A_Jmp(["ACTION_205_set_sprite_sequence_2"]),
	A_Pause(4, identifier="ACTION_205_pause_26"),
	A_Jmp(["ACTION_205_set_sprite_sequence_2"]),
	A_Pause(9, identifier="ACTION_205_pause_28"),
	A_Jmp(["ACTION_205_set_sprite_sequence_2"])
])
