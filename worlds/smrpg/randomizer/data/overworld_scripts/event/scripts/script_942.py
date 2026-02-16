# E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *

script = EventScript([
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_Pause(60),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(15)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_StartLoopNTimes(4),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_EndLoop()
	]),
	Return()
])
