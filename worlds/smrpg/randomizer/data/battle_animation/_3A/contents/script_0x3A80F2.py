# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *
script = AnimationScriptBlock(expected_size=10, expected_beginning=0x3A80F2, script=[
	ResetTargetMappingMemory(identifier="command_0x3A80F2"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=40, y=160, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
