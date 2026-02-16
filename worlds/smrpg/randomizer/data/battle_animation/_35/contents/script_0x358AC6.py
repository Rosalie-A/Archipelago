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
script = AnimationScriptBlock(expected_size=145, expected_beginning=0x358AC6, script=[
	PauseScriptUntilAMEMBitsClear(0x6B, [2, 4, 5]),
	ResetObjectMappingMemory(),
	JmpIfAMEM8BitEqualsConst(0x66, 0, ["command_0x358AD3"]),
	PauseScriptUntilAMEMBitsSet(0x67, [0]),
	ClearAMEM16Bit(0x60, identifier="command_0x358AD3"),
	UnknownCommand(bytearray(b'\xdbk')),
	UnknownCommand(bytearray(b'\x81')),
	Pause1Frame(),
	Jmp(["command_0x358AE4"]),
	ClearAMEM16Bit(0x60, identifier="command_0x358ADC"),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray(b'\xdbo')),
	UnknownCommand(bytearray(b'\x82')),
	Pause1Frame(),
	SetAMEM8BitTo7E1x(0x6F, 0x7EE020, identifier="command_0x358AE4"),
	JmpIfAMEM8BitNotEqualsConst(0x6F, 0, ["command_0x358AFB"]),
	SetAMEM8BitToConst(0x6F, 1),
	Set7E1xToAMEM8Bit(0x7EE025, 0x6F),
	UseSpriteQueue(field_object=0, destinations=["command_0x35F72A"], character_slot=True, bit_5=True),
	AttackTimerBegins(identifier="command_0x358AFB"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray(b'<\x00\x08')),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["fix_sprite_after_attack"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358B15"),
	ResetObjectMappingMemory(),
	SetOMEM60To072C(),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C992"]),
	SpriteSequence(sequence=0, looping_off=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358B22"),
	ResetObjectMappingMemory(),
	RunSubroutine(["command_0x358086"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0018_BOWSER_NONPROTAGONIST_6, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray(b'm')),
	ReturnSubroutine(),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x358B41"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x358ADC"])
])
