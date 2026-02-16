# E0869_TEST_SCRIPT_3
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
from ....spells.spells import *

script = EventScript([
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSequenceSpeed(FASTER),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSequenceSpeed(FASTEST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_MaximizeSequenceSpeed(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_MaximizeSequenceSpeed86(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False),
		A_Pause(120),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Return()
])
