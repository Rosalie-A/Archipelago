#A0886_NIMBUS_FORKIES
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
	A_ClearBit(TEMP_7043_0, identifier="ACTION_886_clear_bit_0"),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 410, ["ACTION_886_clear_bit_34"]),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_JmpIfRandom1of2(["ACTION_886_pause_6"]),
	A_Pause(8),
	A_Pause(4, identifier="ACTION_886_pause_6"),
	A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(6),
	A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetBit(TEMP_7043_0),
	A_Pause(2),
	A_JmpIfRandom1of2(["ACTION_886_set_sprite_sequence_29"]),
	A_Pause(4),
	A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_886_set_sprite_sequence_29"),
	A_Pause(30),
	A_JmpIfRandom1of2(["ACTION_886_clear_bit_0"]),
	A_Pause(60),
	A_Jmp(["ACTION_886_clear_bit_0"]),
	A_ClearBit(TEMP_7043_0, identifier="ACTION_886_clear_bit_34"),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_JmpIfRandom1of2(["ACTION_886_pause_38"]),
	A_Pause(8),
	A_Pause(4, identifier="ACTION_886_pause_38"),
	A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
	A_Pause(6),
	A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetBit(TEMP_7043_0),
	A_Pause(2),
	A_JmpIfRandom1of2(["ACTION_886_set_sprite_sequence_61"]),
	A_Pause(4),
	A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_886_set_sprite_sequence_61"),
	A_Pause(2),
	A_Pause(10),
	A_JmpIfRandom1of2(["ACTION_886_clear_bit_34"]),
	A_Pause(30),
	A_Jmp(["ACTION_886_clear_bit_34"])
])
