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
script = AnimationScriptBlock(expected_size=75, expected_beginning=0x35240C, script=[
	ClearAMEM8Bit(0x6F, identifier="command_0x35240C"),
	SetAMEM16BitToConst(0x60, 17),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	AttackTimerBegins(),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x6F, identifier="command_0x35241B"),
	SetAMEM16BitToConst(0x60, 18),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	AttackTimerBegins(),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x6F, identifier="command_0x35242A"),
	SetAMEM16BitToConst(0x60, 19),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	AttackTimerBegins(),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x6F, identifier="command_0x352439"),
	SetAMEM16BitToConst(0x60, 20),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	AttackTimerBegins(),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x6F, identifier="command_0x352448"),
	SetAMEM16BitToConst(0x60, 21),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	AttackTimerBegins(),
	ReturnSubroutine()
])
