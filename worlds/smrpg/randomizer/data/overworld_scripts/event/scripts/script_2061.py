# E2061_MONSTRO_TOWN_STAR
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
	FadeOutMusicToVolume(duration=0, volume=0),
	Pause(15),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Pause(5),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(3),
		A_PlaySound(sound=SO038_TADPOLE_POND_STAFF_MI, channel=6),
		A_Pause(20),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_WalkSoutheastPixels(3),
		A_PlaySound(sound=SO039_TADPOLE_POND_STAFF_FA, channel=6),
		A_Pause(10),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(3),
		A_PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6),
		A_Pause(20),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_WalkSoutheastPixels(3),
		A_PlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=6),
		A_Pause(10),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(1),
		A_JumpToHeight(37),
		A_Pause(5),
		A_PlaySound(sound=SO037_TADPOLE_POND_STAFF_RE, channel=6),
		A_Pause(24),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6),
		A_Pause(30),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=6),
		A_Pause(30),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO042_TADPOLE_POND_STAFF_TI, channel=6),
		A_Pause(30)
	], identifier="starfish_dance_hint"),
	FadeOutMusicToVolume(duration=5, volume=100),
	Return()
])
