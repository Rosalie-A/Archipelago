#A0386_TOWER_SHOOT_BULLET_BILLS
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
	A_FaceSoutheast(),
	A_Pause(18),
	A_FaceSouthwest(),
	A_Pause(18),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_386_set_sprite_sequence_4"),
	A_Pause(4),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
	A_Pause(16),
	A_SetBit(TEMP_7043_3),
	A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
	A_Pause(24),
	A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_Jmp(["ACTION_386_set_sprite_sequence_4"])
])
