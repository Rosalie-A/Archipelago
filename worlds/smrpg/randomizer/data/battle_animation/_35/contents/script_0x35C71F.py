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
script = AnimationScriptBlock(expected_size=66, expected_beginning=0x35C71F, script=[
	SetAMEM8BitTo7E1x(0x67, 0x7EE011, identifier="command_0x35C71F"),
	IncAMEM8Bit(0x67),
	JmpIfAMEM8BitLessThanConst(0x67, 2, ["command_0x35C746"]),
	Pause1Frame(),
	ClearAMEM8Bit(0x67),
	Set7E1xToAMEM8Bit(0x7EE011, 0x67),
	SetAMEM8BitTo7E1x(0x67, 0x7EE010),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x67, 125, ["command_0x35C74A"]),
	Pause1Frame(),
	IncAMEM8Bit(0x67),
	Set7E1xToAMEM8Bit(0x7EE010, 0x67),
	Jmp(["command_0x35C74A"]),
	Set7E1xToAMEM8Bit(0x7EE011, 0x67, identifier="command_0x35C746"),
	ReturnSubroutine(identifier="command_0x35C74A"),
	Pause1Frame(identifier="command_0x35C74B"),
	SetAMEM8BitTo7E1x(0x67, 0x7EE013),
	JmpIfAMEM8BitGreaterOrEqualThanAMEM(amem=0x67, source_amem=0x6B, upper=0x60, destinations=["command_0x35C760"]),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x67, 100, ["command_0x35C760"]),
	Set7E1xToAMEM8Bit(0x7EE013, 0x6B),
	ReturnSubroutine(identifier="command_0x35C760")
])
