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
script = AnimationScriptBlock(expected_size=40, expected_beginning=0x3A8192, script=[
	ResetTargetMappingMemory(identifier="command_0x3A8192"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=72, y=144, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A819C"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=88, y=152, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A81A6"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=104, y=160, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A81B0"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=120, y=168, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
