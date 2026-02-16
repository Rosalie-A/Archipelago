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
script = AnimationScriptBlock(expected_size=64, expected_beginning=0x02F461, script=[
	ReturnSubroutine(identifier="command_0x02F461"),
	InitializeBonusMessageSequence(identifier="command_0x02F462"),
	DisplayBonusMessage(message=BM_ATTACK, x=0, y=-32),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
	DisplayBonusMessage(message=BM_UP, x=2, y=-24),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F473"),
	DisplayBonusMessage(message=BM_DEFENSE, x=0, y=-32),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
	DisplayBonusMessage(message=BM_UP, x=2, y=-24),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F484"),
	DisplayBonusMessage(message=BM_HPMAX, x=4, y=-32),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F48C"),
	DisplayBonusMessage(message=BM_ONCE, x=0, y=-32),
	DisplayBonusMessage(message=BM_AGAIN, x=4, y=-24),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine(),
	InitializeBonusMessageSequence(identifier="command_0x02F499"),
	DisplayBonusMessage(message=BM_LUCKY, x=2, y=-32),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
