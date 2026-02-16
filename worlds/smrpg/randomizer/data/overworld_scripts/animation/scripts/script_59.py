#A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 463, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 464, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 465, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 466, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 467, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 468, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
	A_FaceSouthwest(),
	A_SetWalkingSpeed(FAST, identifier="ACTION_59_set_animation_speed_10"),
	A_WalkFDirectionSteps(2),
	A_Pause(32),
	A_WalkFDirectionSteps(2),
	A_Pause(32),
	A_WalkFDirectionSteps(2),
	A_Pause(32),
	A_WalkFDirectionSteps(2),
	A_Pause(32),
	A_JumpToHeight(height=60, silent=True),
	A_WalkFDirectionSteps(2),
	A_TurnRandomDirection(),
	A_Jmp(["ACTION_59_set_animation_speed_10"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, identifier="ACTION_59_set_700C_to_object_coord_23"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_59_set_sprite_sequence_32"]),
	A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_59_set_sprite_sequence_32"),
	A_Pause(8),
	A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue()
])
