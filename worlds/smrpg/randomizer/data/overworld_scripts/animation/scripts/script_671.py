#A0671_SHAKE_HEAD_NO
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
	A_JmpIf700CAnyBitsSet(bits=[0], destinations=["ACTION_671_jmp_if_bit_set_4"]),
	A_SetBit(TEMP_7049_6),
	A_JmpIfBitSet(TEMP_7049_2, ["ACTION_671_jmp_if_bit_set_6"], identifier="ACTION_671_jmp_if_bit_set_4"),
	A_SetSequenceSpeed(VERY_FAST),
	A_JmpIfBitSet(TEMP_7049_6, ["ACTION_671_copy_var_to_var_11"], identifier="ACTION_671_jmp_if_bit_set_6"),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 1, ["ACTION_671_set_sprite_sequence_19"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 3, ["ACTION_671_set_sprite_sequence_21"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 5, ["ACTION_671_set_sprite_sequence_23"]),
	A_JmpIfVarEqualsConst(ROSE_WAY_7038, 7, ["ACTION_671_set_sprite_sequence_25"]),
	A_CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C, identifier="ACTION_671_copy_var_to_var_11"),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AB),
	A_UnknownCommand(bytearray(b'\xfd$\x00\x13')),
	A_Mem700CAndConst(0x00C0),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_671_set_sprite_sequence_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["ACTION_671_set_sprite_sequence_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["ACTION_671_set_sprite_sequence_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["ACTION_671_set_sprite_sequence_25"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_671_set_sprite_sequence_19"),
	A_Jmp(["ACTION_671_set_bit_26"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, identifier="ACTION_671_set_sprite_sequence_21"),
	A_Jmp(["ACTION_671_set_bit_26"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, identifier="ACTION_671_set_sprite_sequence_23"),
	A_Jmp(["ACTION_671_set_bit_26"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_671_set_sprite_sequence_25"),
	A_SetBit(TEMP_7043_6, identifier="ACTION_671_set_bit_26"),
	A_Pause(4),
	A_StopSound(),
	A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
	A_Pause(32, identifier="ACTION_671_pause_31"),
	A_StopSound(),
	A_SequenceLoopingOff(),
	A_SetSequenceSpeed(NORMAL),
	A_ResetProperties(),
	A_CopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_ClearBit(TEMP_7049_6),
	A_ClearBit(TEMP_7049_2),
	A_ClearBit(UNKNOWN_704A_3),
	A_ClearBit(TEMP_7043_6),
	A_ReturnQueue()
])
