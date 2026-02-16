#A0876_MONSTRO_MIMIC
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
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_876_set_sprite_sequence_0"),
	A_Pause(170),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(5),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(120),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(3),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_876_set_sprite_sequence_0"])
])
