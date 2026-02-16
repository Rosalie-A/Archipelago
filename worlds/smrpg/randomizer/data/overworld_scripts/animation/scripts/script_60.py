#A0060_SEWER_WATER_SWITCH_BOOS
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
	A_SetPriority(3, identifier="ACTION_60_set_priority_0"),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_60_pause_7"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_60_pause_8"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_60_pause_9"]),
	A_Pause(3),
	A_Pause(3, identifier="ACTION_60_pause_7"),
	A_Pause(3, identifier="ACTION_60_pause_8"),
	A_Pause(3, identifier="ACTION_60_pause_9"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_VisibilityOff(),
	A_TurnRandomDirection(),
	A_SetWalkingSpeed(FAST),
	A_StartLoopNTimes(2),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	A_AddConstToVar(PRIMARY_TEMP_700C, 224),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True),
	A_Compare700CToVar(TEMP_7028),
	A_JmpIfLoadedMemoryIs0(["ACTION_60_jmp_24"]),
	A_JmpIfLoadedMemoryIsBelow0(["ACTION_60_shift_z_down_pixels_25"]),
	A_JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_60_shift_z_up_pixels_27"]),
	A_Jmp(["ACTION_60_walk_1_step_f_direction_28"], identifier="ACTION_60_jmp_24"),
	A_ShiftZDownPixels(8, identifier="ACTION_60_shift_z_down_pixels_25"),
	A_Jmp(["ACTION_60_walk_1_step_f_direction_28"]),
	A_ShiftZUpPixels(8, identifier="ACTION_60_shift_z_up_pixels_27"),
	A_Walk1StepFDirection(identifier="ACTION_60_walk_1_step_f_direction_28"),
	A_EndLoop(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ResetProperties(),
	A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	A_StartLoopNTimes(3),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_FaceMario(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_Mem700CAndConst(0x0006),
	A_Inc(PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_SequenceLoopingOn(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_60_set_sprite_sequence_50"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_60_set_sprite_sequence_52"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_60_set_sprite_sequence_52"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_60_set_sprite_sequence_50"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=False, mirror_sprite=True, identifier="ACTION_60_set_sprite_sequence_50"),
	A_Jmp(["ACTION_60_set_animation_speed_53"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=False, identifier="ACTION_60_set_sprite_sequence_52"),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_60_set_animation_speed_53"),
	A_WalkFDirectionSteps(3),
	A_SequenceLoopingOff(),
	A_PlaySound(sound=SO000_SILENCE, channel=6),
	A_StartLoopNTimes(3),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_VisibilityOff(),
	A_Jmp(["ACTION_60_set_priority_0"])
])
