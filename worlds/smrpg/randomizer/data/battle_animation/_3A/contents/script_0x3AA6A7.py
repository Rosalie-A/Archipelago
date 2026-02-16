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
script = AnimationScriptBlock(expected_size=582, expected_beginning=0x3AA6A7, script=[
	DisplayMessage(ATTACK_NAME, 61, identifier="command_0x3AA845"),
	PauseScriptUntilDialogClosed(),
	RunSubroutine(["command_0x3A8160"]),
	PlaySound(sound=S0011_SWOOSH_RUN_AWAY),
	RunSubroutine(["command_0x3A72AA"]),
	PlaySound(sound=S0018_SUPER_JUMP_HIT_1),
	RunSubroutine(["command_0x3A756C"]),
	ResetTargetMappingMemory(),
	MoveObject(speed=1, start_position=256, end_position=256, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=-129, end_position=-129, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=49, start_position=-1537, end_position=1536, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	PauseScriptUntil(condition=BUTTON_PRESSED),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x3A773F"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	RunSubroutine(["command_0x3A71DA"]),
	RunSubroutine(["command_0x3A755E"]),
	ReturnSpriteQueue(),
	RunSubroutine(["command_0x3A7729"], identifier="command_0x3AA886"),
	SpriteSequence(sequence=3),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=0, looping_off=True),
	RunSubroutine(["command_0x3A771E"]),
	ReturnSpriteQueue(),
	DisplayMessage(ATTACK_NAME, 62, identifier="command_0x3AA892"),
	RunSubroutine(["command_0x3A733E"]),
	PauseScriptUntilDialogClosed(),
	SpriteSequence(sequence=8, looping_off=True, mirror=True),
	RunSubroutine(["command_0x3A756C"]),
	PlaySound(sound=S0004_JUMP),
	ResetTargetMappingMemory(),
	MoveObject(speed=1, start_position=256, end_position=256, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=-129, end_position=-129, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=81, start_position=-1025, end_position=1024, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	PauseScriptUntil(condition=BUTTON_PRESSED),
	ResetObjectMappingMemory(),
	PlaySound(sound=S0004_JUMP),
	ResetTargetMappingMemory(),
	MoveObject(speed=1, start_position=512, end_position=512, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=-257, end_position=-257, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=81, start_position=-2049, end_position=2048, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	PauseScriptUntil(condition=BUTTON_PRESSED),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x3A773F"]),
	RunSubroutine(["command_0x3A755E"]),
	ReturnSpriteQueue()
])
