#A0408_JUMP_ON_SAVE_BLOCK
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
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_408_set_sprite_sequence_10"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_408_set_sprite_sequence_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_408_set_sprite_sequence_14"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_408_set_sprite_sequence_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_408_set_sprite_sequence_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_408_set_sprite_sequence_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_408_set_sprite_sequence_22"]),
	A_SetSpriteSequence(index=4, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=2, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_408_set_sprite_sequence_10"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_408_set_sprite_sequence_12"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=0, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_408_set_sprite_sequence_14"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_408_set_sprite_sequence_16"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=2, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_408_set_sprite_sequence_18"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=4, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_408_set_sprite_sequence_20"),
	A_Jmp(["ACTION_408_ret_23"]),
	A_SetSpriteSequence(index=1, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_408_set_sprite_sequence_22"),
	A_ReturnQueue(identifier="ACTION_408_ret_23")
])
