#A0509_PIPE_VAULT_FIREBALL
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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True, identifier="ACTION_509_clear_solidity_bits_0"),
	A_SetPriority(3),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(5),
	A_SetWalkingSpeed(FASTEST),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_PlaySound(sound=SO084_SMOKED, channel=6),
	A_AddZCoord1Step(),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_AddZCoord1Step(),
	A_SetWalkingSpeed(VERY_FAST),
	A_AddZCoord1Step(),
	A_SetWalkingSpeed(FASTER),
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(4),
	A_StartLoopNTimes(3),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
	A_Pause(4),
	A_EndLoop(),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(FASTER),
	A_ShiftZDownPixels(8),
	A_SetWalkingSpeed(VERY_FAST),
	A_DecZCoord1Step(),
	A_SetWalkingSpeed(FASTEST),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_DecZCoord1Step(),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_DecZCoord1Step(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(5),
	A_VisibilityOff(),
	A_Pause(90),
	A_Jmp(["ACTION_509_clear_solidity_bits_0"])
])
