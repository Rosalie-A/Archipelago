#A0272_VOLCANO_DRY_BONES
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
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_272_set_animation_speed_0"),
	A_SetSequenceSpeed(FAST),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_272_set_sprite_sequence_30"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_272_set_sprite_sequence_30"]),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_VarShiftLeft(PRIMARY_TEMP_700C, 255),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_Pause(4, identifier="ACTION_272_pause_14"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=128, tiles=1, destinations=["ACTION_272_play_sound_17"]),
	A_Jmp(["ACTION_272_pause_14"]),
	A_PlaySound(sound=SO117_SPINNING_MONSTER, channel=4, identifier="ACTION_272_play_sound_17"),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(18),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(1, identifier="ACTION_272_start_loop_n_times_22"),
	A_FaceMario(),
	A_WalkFDirectionSteps(2),
	A_EndLoop(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_272_start_loop_n_times_22"]),
	A_Pause(8),
	A_JmpIfRandom1of2(["ACTION_272_start_loop_n_times_22"]),
	A_Jmp(["ACTION_272_set_animation_speed_0"]),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_272_set_sprite_sequence_30"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_VarShiftLeft(PRIMARY_TEMP_700C, 255),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_Pause(4, identifier="ACTION_272_pause_39"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_272_play_sound_42"]),
	A_Jmp(["ACTION_272_pause_39"]),
	A_PlaySound(sound=SO117_SPINNING_MONSTER, channel=4, identifier="ACTION_272_play_sound_42"),
	A_SetSpriteSequence(index=8, looping=False),
	A_Pause(18),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_Jmp(["ACTION_272_start_loop_n_times_22"])
])
