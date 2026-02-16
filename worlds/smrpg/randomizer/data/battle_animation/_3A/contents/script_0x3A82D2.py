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
script = AnimationScriptBlock(expected_size=20, expected_beginning=0x3A82D2, script=[
	ResetTargetMappingMemory(identifier="command_0x3A82D2"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=136, y=112, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A82DC"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=152, y=120, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
