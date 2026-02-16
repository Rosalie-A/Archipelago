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
script = AnimationScriptBlock(expected_size=168, expected_beginning=0x3AC148, script=[
	RunSubroutine(["command_0x3A773F"], identifier="command_0x3AC148"),
	RemoveObject(),
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=236, y=46, z=0, set_x=True, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0331_BANDANA_BLUE, sequence=0, priority=2, vram_address=0x7A00, palette_row=12, overwrite_vram=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	SummonMonster(monster=WATERCRYSTALEnemy, position=6, bit_7=True),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=216, y=56, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=186, y=71, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=128),
	PauseScriptUntil(condition=UNKNOWN_PAUSE_1),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=136, y=96, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=352),
	PauseScriptUntil(condition=UNKNOWN_PAUSE_1),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=30),
	SpriteSequence(sequence=0, looping_off=True, mirror=True),
	RunSubroutine(["command_0x3A7374"]),
	UnknownCommand(bytearray(b'\x16'), identifier="command_0x3AC1A2"),
	Pause1Frame(),
	SetAMEM8BitTo7E1x(0x67, 0x7EE003),
	JmpIfAMEMBitsSet(0x67, [0], ["command_0x3AC1EA"]),
	Pause1Frame(),
	SetAMEMToRandomByte(amem=0x68, upper_bound=100),
	JmpIfAMEM8BitEqualsConst(0x68, 0, ["command_0x3AC1CE"]),
	JmpIfAMEM8BitEqualsConst(0x68, 1, ["command_0x3AC1D8"]),
	JmpIfAMEM8BitEqualsConst(0x68, 2, ["command_0x3AC1DE"]),
	JmpIfAMEM8BitEqualsConst(0x68, 3, ["command_0x3AC1E4"]),
	SpriteSequence(sequence=0, looping_off=True, mirror=True),
	Jmp(["command_0x3AC1A2"]),
	SpriteSequence(sequence=0, looping_on=True, mirror=True, identifier="command_0x3AC1CE"),
	RunSubroutine(["command_0x3A7390"]),
	SpriteSequence(sequence=0, looping_off=True, mirror=True),
	Jmp(["command_0x3AC1A2"]),
	SpriteSequence(sequence=2, mirror=True, identifier="command_0x3AC1D8"),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["command_0x3AC1A2"]),
	SpriteSequence(sequence=3, mirror=True, identifier="command_0x3AC1DE"),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["command_0x3AC1A2"]),
	SpriteSequence(sequence=4, mirror=True, identifier="command_0x3AC1E4"),
	PauseScriptUntilSpriteSequenceDone(),
	Jmp(["command_0x3AC1A2"]),
	Pause1Frame(identifier="command_0x3AC1EA"),
	SpriteSequence(sequence=0, looping_off=True, mirror=True),
	Jmp(["command_0x3AC1EA"])
])
