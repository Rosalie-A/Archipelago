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
script = AnimationScriptBlock(expected_size=141, expected_beginning=0x357AE5, script=[
	ResetTargetMappingMemory(identifier="command_0x357AE5"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray(b'D@')),
	PlaySound(sound=S0134_BOO_DISAPPEARS),
	ClearAMEM8Bit(0x6F),
	SetAMEM16BitToConst(0x60, 12),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	VisibilityOff(unknown_byte=0x01),
	UnknownCommand(bytearray(b'Z')),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=512, arch_height=0),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ClearAMEM8Bit(0x6F),
	SetAMEM16BitToConst(0x60, 12),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	PlaySound(sound=S0135_BOO_APPEARS),
	VisibilityOn(unknown_byte=0x01),
	UnknownCommand(bytearray(b'Y')),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
	PlaySound(sound=S0136_BOO_APPROACHES),
	MoveObject(speed=1, start_position=-257, end_position=0, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=-65, end_position=0, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	MoveObject(speed=1, start_position=-193, end_position=0, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=192, end_position=0, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	MoveObject(speed=1, start_position=-257, end_position=0, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=-65, end_position=0, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	MoveObject(speed=1, start_position=-193, end_position=0, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=192, end_position=0, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ResetObjectMappingMemory(),
	ReturnSubroutine()
])
