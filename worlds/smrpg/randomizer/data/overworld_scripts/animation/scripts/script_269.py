#A0269_BLOOBER_TAIL
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
	A_SetMovementsBits(bit_0=True, cant_walk_under=True),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Pause(20),
	A_SetPriority(3),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_269_set_animation_speed_4"),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_269_set_sprite_sequence_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_269_set_sprite_sequence_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_269_set_sprite_sequence_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_269_set_sprite_sequence_12"]),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	A_Jmp(["ACTION_269_shift_z_down_steps_13"]),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_269_set_sprite_sequence_12"),
	A_ShiftZDownSteps(5, identifier="ACTION_269_shift_z_down_steps_13"),
	A_CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_269_set_sprite_sequence_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_269_set_sprite_sequence_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_269_set_sprite_sequence_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_269_set_sprite_sequence_22"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
	A_Jmp(["ACTION_269_clear_solidity_bits_23"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_269_set_sprite_sequence_22"),
	A_ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_269_clear_solidity_bits_23"),
	A_SetWalkingSpeed(FAST),
	A_SetSolidityBits(cant_pass_walls=True),
	A_StartLoopNTimes(39),
	A_ShiftZUpPixels(2),
	A_WalkFDirectionPixels(1),
	A_EndLoop(),
	A_Jmp(["ACTION_269_set_animation_speed_4"])
])
