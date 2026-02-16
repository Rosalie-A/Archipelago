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
script = AnimationScriptBlock(expected_size=165, expected_beginning=0x357FF8, script=[
	ResetTargetMappingMemory(identifier="command_0x357FF8"),
	MoveObject(speed=1, start_position=-137, end_position=0, apply_to_x=True, should_set_speed=True),
	MoveObject(speed=1, start_position=80, end_position=0, apply_to_y=True, should_set_speed=True),
	MoveObject(speed=17, start_position=-257, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	MoveObject(speed=17, start_position=256, end_position=-257, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	MoveObject(speed=17, start_position=-257, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	MoveObject(speed=17, start_position=256, end_position=-257, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x35803B"),
	MoveObject(speed=1, start_position=-129, end_position=0, apply_to_x=True, should_set_speed=True),
	MoveObject(speed=1, start_position=64, end_position=0, apply_to_y=True, should_set_speed=True),
	MoveObject(speed=17, start_position=-257, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	MoveObject(speed=17, start_position=256, end_position=-257, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	MoveObject(speed=17, start_position=-257, end_position=256, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	ResetObjectMappingMemory(),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358072"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358086"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=12, y=-6, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1664, arch_height=0),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine()
])
