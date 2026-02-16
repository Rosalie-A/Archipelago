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
script = AnimationScriptBlock(expected_size=80, expected_beginning=0x357951, script=[
	ReturnSubroutine(identifier="command_0x357951"),
	ResetTargetMappingMemory(identifier="command_0x357952"),
	ResetObjectMappingMemory(),
	MoveObject(speed=257, start_position=1024, end_position=2048, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=BUTTON_PRESSED),
	ResetObjectMappingMemory(),
	PlaySound(sound=S0170_SUBMERGED_UNDER),
	ClearAMEM8Bit(0x68),
	SetAMEM16BitToConst(0x60, 11),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	UnknownCommand(bytearray(b'Z')),
	VisibilityOff(unknown_byte=0x01),
	RunSubroutine(["command_0x352552"]),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray(b'D`')),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=768, arch_height=0),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	SetAMEM60ToCurrentTarget(),
	ClearAMEM8Bit(0x68),
	SetAMEM16BitToConst(0x60, 11),
	UseObjectQueueAtOffsetWithAMEM60PointerOffset(index=0, destinations=["command_0x355F1D"]),
	VisibilityOn(unknown_byte=0x01),
	PlaySound(sound=S0170_SUBMERGED_UNDER),
	MoveObject(speed=257, start_position=-1025, end_position=-2049, apply_to_z=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
	UnknownCommand(bytearray(b'Y')),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x352552"]),
	ReturnSubroutine()
])
