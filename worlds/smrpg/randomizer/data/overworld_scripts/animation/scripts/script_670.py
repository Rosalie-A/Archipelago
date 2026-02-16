#A0670_NOD_YES
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
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_7038),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 1, ["ACTION_670_start_loop_n_times_15"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 3, ["ACTION_670_start_loop_n_times_22"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 5, ["ACTION_670_start_loop_n_times_29"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 7, ["ACTION_670_start_loop_n_times_36"]),
	A_CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AB),
	A_UnknownCommand(bytearray(b'\xfd$\x00\x13')),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=PRIMARY_TEMP_7000),
	A_Mem700CAndConst(0x00C0),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_670_start_loop_n_times_15"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["ACTION_670_start_loop_n_times_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["ACTION_670_start_loop_n_times_29"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["ACTION_670_start_loop_n_times_36"]),
	A_StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_15"),
	A_SetSpriteSequence(index=6, is_mold=True, looping=True, mirror_sprite=True),
	A_Pause(5),
	A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
	A_Pause(5),
	A_EndLoop(),
	A_Jmp(["ACTION_670_reset_properties_42"]),
	A_StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_22"),
	A_SetSpriteSequence(index=6, is_mold=True, looping=True),
	A_Pause(5),
	A_SetSpriteSequence(index=0, is_mold=True, looping=True),
	A_Pause(5),
	A_EndLoop(),
	A_Jmp(["ACTION_670_reset_properties_42"]),
	A_StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_29"),
	A_SetSpriteSequence(index=3, is_mold=True, looping=True),
	A_Pause(5),
	A_SetSpriteSequence(index=7, is_mold=True, looping=True),
	A_Pause(5),
	A_EndLoop(),
	A_Jmp(["ACTION_670_reset_properties_42"]),
	A_StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_36"),
	A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
	A_Pause(5),
	A_SetSpriteSequence(index=7, is_mold=True, looping=True, mirror_sprite=True),
	A_Pause(5),
	A_EndLoop(),
	A_ResetProperties(identifier="ACTION_670_reset_properties_42"),
	A_CopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_ClearBit(TEMP_7044_7),
	A_ReturnQueue()
])
