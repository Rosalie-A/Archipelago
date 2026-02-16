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
script = AnimationScriptBlock(expected_size=12, expected_beginning=0x3A8674, script=[
	Pause1Frame(identifier="command_0x3A8674"),
	SetAMEM8BitToAMEM(amem=0x68, source_amem=0x68, upper=0x60),
	JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x3A8674"]),
	ReturnSubroutine()
])
