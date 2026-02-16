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
script = AnimationScriptBlock(expected_size=85, expected_beginning=0x352D13, script=[
	SetAMEMToRandomShort(amem=0x60, upper_bound=7, identifier="command_0x352D13"),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x352D1B"]),
	ReturnSubroutine(),
	DefineObjectQueue(["command_0x352D29", "command_0x352D32", "command_0x352D3B", "command_0x352D44", "command_0x352D4D", "command_0x352D56", "command_0x352D5F"], identifier="command_0x352D1B"),
	MoveObject(speed=17, start_position=512, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D29"),
	ReturnSubroutine(),
	MoveObject(speed=17, start_position=640, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D32"),
	ReturnSubroutine(),
	MoveObject(speed=17, start_position=768, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D3B"),
	ReturnSubroutine(),
	MoveObject(speed=17, start_position=896, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D44"),
	ReturnSubroutine(),
	MoveObject(speed=17, start_position=1024, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D4D"),
	ReturnSubroutine(),
	MoveObject(speed=17, start_position=1152, end_position=128, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D56"),
	ReturnSubroutine(),
	MoveObject(speed=1, start_position=0, end_position=0, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True, identifier="command_0x352D5F"),
	ReturnSubroutine()
])
