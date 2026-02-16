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
script = AnimationScriptBlock(expected_size=488, expected_beginning=0x3A7333, script=[
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=384, identifier="command_0x3A7333"),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A733E"),
	MoveObject(speed=1, start_position=-769, end_position=-769, apply_to_z=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	ResetObjectMappingMemory(),
	MoveObject(speed=1, start_position=768, end_position=768, apply_to_z=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	ResetObjectMappingMemory(),
	MoveObject(speed=1, start_position=-769, end_position=-769, apply_to_z=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	ResetObjectMappingMemory(),
	MoveObject(speed=1, start_position=768, end_position=768, apply_to_z=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A7374"),
	MoveObject(speed=81, start_position=-1281, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ResetObjectMappingMemory(),
	MoveObject(speed=81, start_position=0, end_position=1280, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A7390"),
	MoveObject(speed=129, start_position=-2049, end_position=0, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ResetObjectMappingMemory(),
	MoveObject(speed=129, start_position=0, end_position=2048, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x3A73AC"),
	MoveObject(speed=1, start_position=-1025, end_position=-1025, apply_to_y=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	ResetObjectMappingMemory(),
	MoveObject(speed=1, start_position=1024, end_position=1024, apply_to_y=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	ResetObjectMappingMemory(),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01F),
	JmpIfAMEMBitsClear(0x68, [0], ["command_0x3A73AC"]),
	ReturnSubroutine()
])
