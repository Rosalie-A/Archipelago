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
script = AnimationScriptBlock(expected_size=62, expected_beginning=0x3A711F, script=[
	ResetTargetMappingMemory(identifier="command_0x3A711F"),
	SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1536, arch_height=80),
	PauseScriptUntil(condition=UNKNOWN_PAUSE_7),
	ResetObjectMappingMemory(),
	ResetSpriteSequence(),
	ReturnSubroutine(),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1024, arch_height=0, identifier="command_0x3A7135"),
	SetAMEM16BitToConst(0x60, 0),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=6, destinations=["command_0x3A8AC0"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	VisibilityOff(unknown_byte=0x01),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=6, destinations=["command_0x3A8AC0"]),
	VisibilityOn(unknown_byte=0x01),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE, identifier="shift_sprite_and_remap"),
	ResetObjectMappingMemory(),
	ReturnSubroutine()
])
