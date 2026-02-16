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
script = AnimationScriptBlock(expected_size=149, expected_beginning=0x358B57, script=[
	ResetTargetMappingMemory(identifier="command_0x358B57"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray(b'Dh')),
	SpriteSequence(sequence=0, looping_off=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM16Bit(0x61),
	ClearAMEM8Bit(0x63),
	ClearAMEM8Bit(0x66),
	SetAMEM8BitTo7E5x(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x358BD6"]),
	ClearAMEM8Bit(0x6F),
	PauseScriptUntilAMEMBitsSet(0x66, [0]),
	ClearAMEM16Bit(0x60),
	UnknownCommand(bytearray(b'\xdbk')),
	UnknownCommand(bytearray(b'\x81')),
	Pause1Frame(),
	Jmp(["command_0x358B98"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x358B8D"),
	PauseScriptUntilAMEMBitsSet(0x66, [0]),
	ClearAMEM16Bit(0x60),
	UnknownCommand(bytearray(b'\xdbo')),
	UnknownCommand(bytearray(b'\x82')),
	Pause1Frame(),
	AttackTimerBegins(identifier="command_0x358B98"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray(b'<\x00\x08')),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["fix_sprite_after_attack"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358BAA"),
	ResetObjectMappingMemory(),
	SetOMEM60To072C(),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C992"]),
	SpriteSequence(sequence=0, looping_off=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358BB7"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358086"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0030_GENO_NONPROTAGONIST_6, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x358BD6"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x358B8D"])
])
