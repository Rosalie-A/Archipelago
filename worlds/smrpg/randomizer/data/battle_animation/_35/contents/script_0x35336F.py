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
script = AnimationScriptBlock(expected_size=189, expected_beginning=0x35336F, script=[
	ClearAMEM8Bit(0x68, identifier="command_0x35336F"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [0]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x35337D"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [1]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x35338B"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [2]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x353399"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [3]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x3533A7"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [4]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x3533B5"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [5]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x3533C3"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [6]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68, identifier="command_0x3533D1"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	SetAMEMBits(0x68, [7]),
	Set7E1xToAMEM8Bit(0x7EE01B, 0x68),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533DF"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3533DF"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533EA"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [1], ["command_0x3533EA"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3533F5"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [2], ["command_0x3533F5"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x353400"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [3], ["command_0x353400"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x35340B"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [4], ["command_0x35340B"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x353416"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [5], ["command_0x353416"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x353421"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01B),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x353421"]),
	ReturnSubroutine()
])
