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
script = AnimationScriptBlock(expected_size=872, expected_beginning=0x350202, script=[
	DefineObjectQueue([
        "monster_sprite_behaviour_0_no_movement_for_escape", # terrapin
		"monster_sprite_behaviour_0_no_movement_for_escape", # spikey
		"monster_sprite_behaviour_5_sprite_shadow", # skytroopa
		"monster_sprite_behaviour_0_no_movement_for_escape", # madmallet static
		"monster_sprite_behaviour_0_no_movement_for_escape", # shaman
		"monster_sprite_behaviour_0_no_movement_for_escape", # crook
		"monster_sprite_behaviour_0_no_movement_for_escape", # goomba
		"monster_sprite_behaviour_0_no_movement_for_escape", # piranha plant
		"monster_sprite_behaviour_0_no_movement_for_escape", # amanita
		"monster_sprite_behaviour_5_sprite_shadow", # goby
		"monster_sprite_behaviour_6_floating_sprite_shadow", # bloober
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana red
		"monster_sprite_behaviour_5_sprite_shadow", # lakitu
		"monster_sprite_behaviour_5_sprite_shadow", # birdy
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pinwheel
		"monster_sprite_behaviour_0_no_movement_for_escape", # rat funk
		"monster_sprite_behaviour_0_no_movement_for_escape", # k9
		"monster_sprite_behaviour_0_no_movement_for_escape", # magmite
		"monster_sprite_behaviour_5_sprite_shadow", # big boo
		"monster_sprite_behaviour_0_no_movement_for_escape", # drybones
		"monster_sprite_behaviour_5_sprite_shadow", # greaper
		"monster_sprite_behaviour_6_floating_sprite_shadow", # sparky
		"monster_sprite_behaviour_0_no_movement_for_escape", # chomp
		"monster_sprite_behaviour_0_no_movement_for_escape", # pandorite
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy ranger
		"monster_sprite_behaviour_0_no_movement_for_escape", # bobomb static
		"monster_sprite_behaviour_0_no_movement_for_escape", # spookum
		"monster_sprite_behaviour_11_fade_out_death", # hammer bro
		"monster_sprite_behaviour_5_sprite_shadow", # buzzer
		"monster_sprite_behaviour_0_no_movement_for_escape", # ameboid
		"monster_sprite_behaviour_0_no_movement_for_escape", # gecko
		"monster_sprite_behaviour_0_no_movement_for_escape", # wiggler
		"monster_sprite_behaviour_0_no_movement_for_escape", # crusty
		"monster_sprite_behaviour_11_fade_out_death", # kamek
		"monster_sprite_behaviour_6_floating_sprite_shadow", # leuko
		"monster_sprite_behaviour_0_no_movement_for_escape", # jawful
		"monster_sprite_behaviour_5_sprite_shadow", # enigma
		"monster_sprite_behaviour_0_no_movement_for_escape", # blaster
		"monster_sprite_behaviour_0_no_movement_for_escape", # guerrilla
		"monster_sprite_behaviour_5_sprite_shadow", # birdy henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # hobgoblin
		"monster_sprite_behaviour_0_no_movement_for_escape", # reacher
		"monster_sprite_behaviour_0_no_movement_for_escape", # shogun
		"monster_sprite_behaviour_0_no_movement_for_escape", # orb user
		"monster_sprite_behaviour_5_sprite_shadow", # heavy troopa
		"monster_sprite_behaviour_6_floating_sprite_shadow", # shadow
		"monster_sprite_behaviour_6_floating_sprite_shadow", # cluster
		"monster_sprite_behaviour_0_no_movement_for_escape", # bahamutt (kamek)
		"monster_sprite_behaviour_6_floating_sprite_shadow", # octolot
		"monster_sprite_behaviour_0_no_movement_for_escape", # frogog
		"monster_sprite_behaviour_0_no_movement_for_escape", # clerk
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # gunyolk
		"monster_sprite_behaviour_0_no_movement_for_escape", # boomer
		"monster_sprite_behaviour_0_no_movement_for_escape", # remo con
		"monster_sprite_behaviour_0_no_movement_for_escape", # snapdragon
		"monster_sprite_behaviour_0_no_movement_for_escape", # stumpet
		"monster_sprite_behaviour_0_no_movement_for_escape", # dodo 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # jester
		"monster_sprite_behaviour_0_no_movement_for_escape", # artichoker
		"monster_sprite_behaviour_0_no_movement_for_escape", # arachne
		"monster_sprite_behaviour_6_floating_sprite_shadow", # carroboscis
		"monster_sprite_behaviour_0_no_movement_for_escape", # hippopo
		"monster_sprite_behaviour_0_no_movement_for_escape", # mastadoom
		"monster_sprite_behaviour_0_no_movement_for_escape", # corkpedite
		"monster_sprite_behaviour_0_no_movement_for_escape", # terra cotta
		"monster_sprite_behaviour_0_no_movement_for_escape", # spikester
		"monster_sprite_behaviour_5_sprite_shadow", # malakoopa
		"monster_sprite_behaviour_0_no_movement_for_escape", # pounder static
		"monster_sprite_behaviour_0_no_movement_for_escape", # poundette static
		"monster_sprite_behaviour_0_no_movement_for_escape", # sackit
		"monster_sprite_behaviour_0_no_movement_for_escape", # gu goomba
		"monster_sprite_behaviour_0_no_movement_for_escape", # chewy
		"monster_sprite_behaviour_6_floating_sprite_shadow", # fireball
		"monster_sprite_behaviour_5_sprite_shadow", # mr kipper
		"monster_sprite_behaviour_5_sprite_shadow", # factory chief
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana blue
		"monster_sprite_behaviour_5_sprite_shadow", # manager
		"monster_sprite_behaviour_5_sprite_shadow", # bluebird
		"monster_sprite_behaviour_1_slide_backward_when_hit", # geno clone S
		"monster_sprite_behaviour_0_no_movement_for_escape", # alley rat
		"monster_sprite_behaviour_0_no_movement_for_escape", # chow
		"monster_sprite_behaviour_0_no_movement_for_escape", # magmus
		"monster_sprite_behaviour_5_sprite_shadow", # lil boo
		"monster_sprite_behaviour_0_no_movement_for_escape", # vomer
		"monster_sprite_behaviour_5_sprite_shadow", # glum reaper
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pyrosphere
		"monster_sprite_behaviour_0_no_movement_for_escape", # chomp chomp
		"monster_sprite_behaviour_0_no_movement_for_escape", # hidon
		"monster_sprite_behaviour_5_sprite_shadow", # sling shy
		"monster_sprite_behaviour_0_no_movement_for_escape", # rob-omb
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy guy
		"monster_sprite_behaviour_0_no_movement_for_escape", # ninja
		"monster_sprite_behaviour_5_sprite_shadow", # stinger
		"monster_sprite_behaviour_0_no_movement_for_escape", # goombette
		"monster_sprite_behaviour_0_no_movement_for_escape", # geckit
		"monster_sprite_behaviour_0_no_movement_for_escape", # jabit
		"monster_sprite_behaviour_0_no_movement_for_escape", # star cruster
		"monster_sprite_behaviour_0_no_movement_for_escape", # team gauge
		"monster_sprite_behaviour_6_floating_sprite_shadow", # muckle
		"monster_sprite_behaviour_0_no_movement_for_escape", # forkies
		"monster_sprite_behaviour_5_sprite_shadow", # gorgon
		"monster_sprite_behaviour_0_no_movement_for_escape", # big bertha
		"monster_sprite_behaviour_0_no_movement_for_escape", # chained kong
		"monster_sprite_behaviour_10_fade_out_death_floating", # fautso
		"monster_sprite_behaviour_0_no_movement_for_escape", # straw head
		"monster_sprite_behaviour_5_sprite_shadow", # bluebird henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # armored ant
		"monster_sprite_behaviour_0_no_movement_for_escape", # orbison
		"monster_sprite_behaviour_6_floating_sprite_shadow", # tub o troopa
		"monster_sprite_behaviour_6_floating_sprite_shadow", # doppel
		"monster_sprite_behaviour_6_floating_sprite_shadow", # pulsar
		"monster_sprite_behaviour_0_no_movement_for_escape", # bobomb henchman
		"monster_sprite_behaviour_6_floating_sprite_shadow", # octovader
		"monster_sprite_behaviour_0_no_movement_for_escape", # ribbite
		"monster_sprite_behaviour_0_no_movement_for_escape", # director
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # pounder henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # puppox
		"monster_sprite_behaviour_0_no_movement_for_escape", # fink flower
		"monster_sprite_behaviour_0_no_movement_for_escape", # crook henchman
		"monster_sprite_behaviour_5_sprite_shadow", # springer
		"monster_sprite_behaviour_0_no_movement_for_escape", # apprentice henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # kriffid
		"monster_sprite_behaviour_0_no_movement_for_escape", # spinthra
		"monster_sprite_behaviour_0_no_movement_for_escape", # bandana red henchman
		"monster_sprite_behaviour_2_bowser_clone_sprite", # bowser clone S
		"monster_sprite_behaviour_6_floating_sprite_shadow", # BLOOBER HENCHMAN
		"monster_sprite_behaviour_0_no_movement_for_escape", # shy guy henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # apprentice
		"monster_sprite_behaviour_1_slide_backward_when_hit", # toadstool 3
		"monster_sprite_behaviour_0_no_movement_for_escape", # piranha plant henchman
		"monster_sprite_behaviour_3_mario_clone_sprite", # mario clone S
		"monster_sprite_behaviour_0_no_movement_for_escape", # poundette henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # mad mallet henchman
		"monster_sprite_behaviour_0_no_movement_for_escape", # box boy
		"monster_sprite_behaviour_4_no_reaction_when_hit", # shelly
		"monster_sprite_behaviour_12_fade_out_death_2", # punchinello 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # dodo 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # oerlikon
		"monster_sprite_behaviour_0_no_movement_for_escape", # chester
		"monster_sprite_behaviour_0_no_movement_for_escape", # body
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # torte
		"monster_sprite_behaviour_5_sprite_shadow", # shy away
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx clone
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made bodyguard
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made drill bit
		"monster_sprite_behaviour_8_floating_slide_backward_when_hit", # formless
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # mokura
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # fire crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # water crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # earth crystal
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # wind crystal
		"monster_sprite_behaviour_3_mario_clone_sprite", # mario clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # toadstool 2
		"monster_sprite_behaviour_2_bowser_clone_sprite", # bowser clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # geno clone
		"monster_sprite_behaviour_1_slide_backward_when_hit", # mallow clone
		"monster_sprite_behaviour_0_no_movement_for_escape", # shyster
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 3
		"monster_sprite_behaviour_0_no_movement_for_escape", # hangin shy
		"monster_sprite_behaviour_0_no_movement_for_escape", # smelter
		"monster_sprite_behaviour_11_fade_out_death", # machine made mack
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # machine made bowyer
		"monster_sprite_behaviour_11_fade_out_death", # machine made yaridovich
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem pink
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem black
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem red
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem yellow
		"monster_sprite_behaviour_0_no_movement_for_escape", # machine made axem green
		"monster_sprite_behaviour_0_no_movement_for_escape", # bahamutt (chester)
		"monster_sprite_behaviour_1_slide_backward_when_hit", # mallow clone s
		"monster_sprite_behaviour_0_no_movement_for_escape", # strong bobomb 4
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # culex 3D
		"monster_sprite_behaviour_11_fade_out_death", # johnny 2
		"monster_sprite_behaviour_5_sprite_shadow", # starslap
		"monster_sprite_behaviour_0_no_movement_for_escape", # mukumuku
		"monster_sprite_behaviour_5_sprite_shadow", # zeostar
		"monster_sprite_behaviour_0_no_movement_for_escape", # jagger
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 4
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy tank
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy safe
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # fire crystal 3d
		"monster_sprite_behaviour_0_no_movement_for_escape", # microbomb
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # water crystal 3d
		"monster_sprite_behaviour_6_floating_sprite_shadow", # grit
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # neosquid
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # yaridovich mirage
		"monster_sprite_behaviour_8_floating_slide_backward_when_hit", # helio
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # right eye
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # left eye
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # knife guy
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # grate guy
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bundt
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 2
		"monster_sprite_behaviour_17_no_reaction_when_hit_2", # count down
		"monster_sprite_behaviour_16_normal", # ding a ling
		"monster_sprite_behaviour_11_fade_out_death", # belome 1
		"monster_sprite_behaviour_11_fade_out_death", # belome 2
		"monster_sprite_behaviour_11_fade_out_death", # belome 3
		"monster_sprite_behaviour_7_floating", # smilax
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # earth crystal 3d
		"monster_sprite_behaviour_7_floating", # megasmilax
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # birdetta
		"monster_sprite_behaviour_0_no_movement_for_escape", # eggbert
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem yellow
		"monster_sprite_behaviour_12_fade_out_death_2", # punchinello
		"monster_sprite_behaviour_0_no_movement_for_escape", # tentacles
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem red
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem green
		"monster_sprite_behaviour_0_no_movement_for_escape", # king bomb
		"monster_sprite_behaviour_0_no_movement_for_escape", # mezzo bomb
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bundt 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # raspberry
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # king calamari
		"monster_sprite_behaviour_0_no_movement_for_escape", # tentacles
		"monster_sprite_behaviour_0_no_movement_for_escape", # jinx 3
		"monster_sprite_behaviour_10_fade_out_death_floating", # zombone
		"monster_sprite_behaviour_10_fade_out_death_floating", # czar dragon
		"monster_sprite_behaviour_5_sprite_shadow", # cloaker
		"monster_sprite_behaviour_5_sprite_shadow", # domino
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # mad adder
		"monster_sprite_behaviour_11_fade_out_death", # mack
		"monster_sprite_behaviour_0_no_movement_for_escape", # bodyguard
		"monster_sprite_behaviour_11_fade_out_death", # yaridovich
		"monster_sprite_behaviour_0_no_movement_for_escape", # drill bit
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem pink
		"monster_sprite_behaviour_0_no_movement_for_escape", # axem black
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # bowyer
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # raspberry 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # torte 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # exor
		"monster_sprite_behaviour_13_fade_out_death_smithy_spell_cast", # smithy 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # shyper
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy body
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy 2
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # smithy mage
		"monster_sprite_behaviour_14_fade_out_death_no_escape_movement", # smithy chest
		"monster_sprite_behaviour_0_no_movement_for_escape", # croco 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # croco 2
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # wind crystal 3d
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # earthlink
		"monster_sprite_behaviour_0_no_movement_for_escape", # aero
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # axem rangers
		"monster_sprite_behaviour_0_no_movement_for_escape", # booster 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # booster 2
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit static
		"monster_sprite_behaviour_11_fade_out_death", # johnny 1
		"monster_sprite_behaviour_0_no_movement_for_escape", # snifit 2
		"monster_sprite_behaviour_5_sprite_shadow", # valentina
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # cloaker
		"monster_sprite_behaviour_15_fade_out_death_no_escape_transition", # domino
		"monster_sprite_behaviour_0_no_movement_for_escape", # candle
		"monster_sprite_behaviour_9_floating_slide_backward_when_hit_2", # culex
    ], identifier="monster_sprite_behaviour_pointers"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x350488", "command_0x3504AB", "command_0x3504CE", "command_0x3504F1", "command_0x350502"], identifier="command_0x350402"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x35048F", "command_0x3504B2", "command_0x3504D5", "command_0x3504F1", "command_0x350502"], identifier="command_0x350412"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x350496", "command_0x3504B9", "command_0x3504DC", "command_0x3504F1", "command_0x350502"], identifier="command_0x350422"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x35049D", "command_0x3504C0", "command_0x3504E3", "command_0x3504F1", "command_0x350502"], identifier="command_0x350432"),
	DefineObjectQueue(["command_0x350462", "command_0x350468", "command_0x350484", "command_0x3504A4", "command_0x3504C7", "command_0x3504EA", "command_0x3504F1", "command_0x350502"], identifier="command_0x350442"),
	UnknownCommand(bytearray(b'\x16'), identifier="command_0x350462"),
	UnknownCommand(bytearray(b'\x14'), identifier="command_0x350463"),
	Pause1Frame(),
	Jmp(["command_0x350463"]),
	ResetTargetMappingMemory(identifier="command_0x350468"),
	ResetObjectMappingMemory(),
	UnknownCommand(bytearray(b'T')),
	UnknownCommand(bytearray(b'l')),
	UnknownCommand(bytearray(b'>')),
	UnknownCommand(bytearray(b'm')),
	UnknownCommand(bytearray(b'W')),
	UnknownCommand(bytearray(b';')),
	UnknownCommand(bytearray(b'U')),
	Pause1Frame(),
	UnknownCommand(bytearray(b';')),
	UnknownCommand(bytearray(b'V')),
	JmpIfTargetEnabled(["command_0x350480"]),
	SpriteSequence(sequence=7),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
	SpriteSequence(sequence=8, looping_off=True),
	Pause1Frame(),
	GameOverIfNoAlliesStanding(identifier="command_0x350480"),
	Jmp(["command_0x350463"]),
	UnknownCommand(bytearray(b'O'), identifier="command_0x350484"),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358916"], identifier="command_0x350488"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x3589D5"], identifier="command_0x35048F"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["bowser_weapon_wrapper"], identifier="command_0x350496"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358B57"], identifier="command_0x35049D"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358BEC"], identifier="command_0x3504A4"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358993"], identifier="command_0x3504AB"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358A2A"], identifier="command_0x3504B2"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358B15"], identifier="command_0x3504B9"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358BAA"], identifier="command_0x3504C0"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358C4D"], identifier="command_0x3504C7"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x3589A0"], identifier="command_0x3504CE"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358A37"], identifier="command_0x3504D5"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358B22"], identifier="command_0x3504DC"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358BB7"], identifier="command_0x3504E3"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	RunSubroutine(["command_0x358C5A"], identifier="command_0x3504EA"),
	UnknownCommand(bytearray(b'\x16')),
	Jmp(["command_0x350463"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=36, identifier="command_0x3504F1"),
	UnknownCommand(bytearray(b'l')),
	UnknownCommand(bytearray(b'm')),
	PauseScriptUntilAMEMBitsSet(0x60, [0], identifier="command_0x3504F7"),
	SpriteSequence(sequence=10),
	PauseScriptUntilSpriteSequenceDone(),
	ClearAMEM8Bit(0x60),
	Jmp(["command_0x3504F7"]),
	ResetTargetMappingMemory(identifier="command_0x350502"),
	ResetObjectMappingMemory(),
	SetAMEM8BitTo7E5x(0x60, 0x7E0040),
	JmpIfAMEMBitsSet(0x60, [1], ["command_0x350532"]),
	JmpIfAMEMBitsSet(0x60, [5, 6], ["command_0x350533"]),
	SetAMEM8BitTo7E5x(0x62, 0x7E0001),
	ClearAMEM8Bit(0x63),
	SpriteQueueReferenceEXPERIMENTAL(unknown_byte=2, destinations=["command_0x35053D"]),
	SetSequenceSpeed(3),
	MoveObject(speed=1, start_position=-801, end_position=-801, apply_to_x=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=1, start_position=400, end_position=400, apply_to_y=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=64),
	ActorExitBattleEXPERIMENTAL(identifier="command_0x350532"),
	SpriteSequence(sequence=1, identifier="command_0x350533"),
	UnknownCommand(bytearray(b'\xa2\x17\x04\x06\x04')),
	SetAMEMToRandomByte(amem=0x65, upper_bound=2),
	DefineObjectQueue(["command_0x350547", "command_0x35054E", "command_0x350555", "command_0x35055C", "command_0x350563"], identifier="command_0x35053D"),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0000_MARIO_WALKING_DOWN_LEFT, sequence=0, store_to_vram=True, looping=True, overlap_all_sprites=True, identifier="command_0x350547"),
	ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0007_TOADSTOOL_NONPROTAGONIST_1, sequence=0, store_to_vram=True, looping=True, overlap_all_sprites=True, identifier="command_0x35054E"),
	ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0013_BOWSER_NONPROTAGONIST_1, sequence=0, store_to_vram=True, looping=True, overlap_all_sprites=True, identifier="command_0x350555"),
	ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0025_GENO_NONPROTAGONIST_1, sequence=0, store_to_vram=True, looping=True, overlap_all_sprites=True, identifier="command_0x35055C"),
	ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0019_MALLOW_NONPROTAGONIST_1, sequence=0, store_to_vram=True, looping=True, overlap_all_sprites=True, identifier="command_0x350563"),
	ReturnSubroutine()

])
