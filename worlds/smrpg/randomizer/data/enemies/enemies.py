from smrpgpatchbuilder.datatypes.enemies.classes import (
    Enemy as EnemyBase,
    EnemyCollection)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    HitSound,
    FlowerBonusType,
    CoinSprite,
    EntranceStyle)
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status
from smrpgpatchbuilder.datatypes.items.classes import RegularItem
from ..items import *
from ...types.enemy import Enemy

class TERRAPINEnemy(Enemy):
    """TERRAPIN enemy class"""
    _monster_id: int = 0
    _name: str = "TERRAPIN"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 1
    _defense: int = 8
    _magic_attack: int = 0
    _magic_defense: int = 1
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Yo! What’s going on?[await]"


class SPIKEYEnemy(Enemy):
    """SPIKEY enemy class"""
    _monster_id: int = 1
    _name: str = "SPIKEY"

    _hp: int = 20
    _fp: int = 100
    _attack: int = 6
    _defense: int = 11
    _magic_attack: int = 4
    _magic_defense: int = 2
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 1
    _coins: int = 2
    _yoshi_cookie_item = BracerItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Just try and jump on me![await]"


class SKYTROOPAEnemy(Enemy):
    """SKY TROOPA enemy class"""
    _monster_id: int = 2
    _name: str = "SKY TROOPA"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 4
    _defense: int = 16
    _magic_attack: int = 6
    _magic_defense: int = 4
    _speed: int = 18
    _evade: int = 8
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 1
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " What a gorgeous day![await]"

    _remake_name = "PARATROOPA"


class MADMALLETEnemyStatic(Enemy):
    """MAD MALLET enemy class"""
    _monster_id: int = 3
    _name: str = "MAD MALLET"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 34
    _magic_defense: int = 85
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 1
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Work, work, work...[await]"


class SHAMANEnemy(Enemy):
    """SHAMAN enemy class"""
    _monster_id: int = 4
    _name: str = "SHAMAN"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 92
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 17
    _coins: int = 4
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = MapleSyrupItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’m losing this fight![await]"


class CROOKEnemyStatic(Enemy):
    """CROOK enemy class"""
    _monster_id: int = 5
    _name: str = "CROOK"

    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " You can’t run away! Ha![await]"


class GOOMBAEnemy(Enemy):
    """GOOMBA enemy class"""
    _monster_id: int = 6
    _name: str = "GOOMBA"

    _hp: int = 16
    _fp: int = 100
    _attack: int = 3
    _defense: int = 3
    _magic_attack: int = 1
    _magic_defense: int = 1
    _speed: int = 13
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 1
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Goomba gumba...phew![await]"


class PIRANHAPLANTEnemyStatic(Enemy):
    """PIRANHA PLANT enemy class"""
    _monster_id: int = 7
    _name: str = "PIRANHA PLANT"

    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 5
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Pretty boring nowadays.[await]"


class AMANITAEnemy(Enemy):
    """AMANITA enemy class"""
    _monster_id: int = 8
    _name: str = "AMANITA"

    _hp: int = 52
    _fp: int = 100
    _attack: int = 35
    _defense: int = 30
    _magic_attack: int = 31
    _magic_defense: int = 18
    _speed: int = 12
    _evade: int = 10
    _magic_evade: int = 10
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 3
    _coins: int = 0
    _yoshi_cookie_item = BadMushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Gotta work on my tan![await]"


class GOBYEnemy(Enemy):
    """GOBY enemy class"""
    _monster_id: int = 9
    _name: str = "GOBY"

    _hp: int = 40
    _fp: int = 100
    _attack: int = 22
    _defense: int = 14
    _magic_attack: int = 2
    _magic_defense: int = 10
    _speed: int = 12
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 10
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Blub blub blub...[await]"

    _remake_name = "CHEEP CHEEP"


class BLOOBEREnemyStatic(Enemy):
    """BLOOBER enemy class"""
    _monster_id: int = 10
    _name: str = "BLOOBER"

    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love floating around.[await]"

    _remake_name = "BLOOPER"


class BANDANAREDEnemy(Enemy):
    """BANDANA RED enemy class"""
    _monster_id: int = 11
    _name: str = "BANDANA RED"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 10
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love the color RED![await]"


class LAKITUEnemy(Enemy):
    """LAKITU enemy class"""
    _monster_id: int = 12
    _name: str = "LAKITU"

    _hp: int = 124
    _fp: int = 100
    _attack: int = 45
    _defense: int = 43
    _magic_attack: int = 35
    _magic_defense: int = 40
    _speed: int = 28
    _evade: int = 13
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = MidMushroomItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 3
    _psychopath_message: str = " Why do people hate me?[await]"


class BIRDYEnemyStatic(Enemy):
    """BIRDY enemy class"""
    _monster_id: int = 13
    _name: str = "BIRDY"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I HATE Valentina.[await]"


class PINWHEELEnemy(Enemy):
    """PINWHEEL enemy class"""
    _monster_id: int = 14
    _name: str = "PINWHEEL"

    _hp: int = 99
    _fp: int = 100
    _attack: int = 120
    _defense: int = 90
    _magic_attack: int = 70
    _magic_defense: int = 66
    _speed: int = 32
    _evade: int = 35
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 23
    _coins: int = 0
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 3
    _psychopath_message: str = " What a day it’s been...[await]"


class RATFUNKEnemy(Enemy):
    """RAT FUNK enemy class"""
    _monster_id: int = 15
    _name: str = "RAT FUNK"

    _hp: int = 32
    _fp: int = 100
    _attack: int = 20
    _defense: int = 14
    _magic_attack: int = 0
    _magic_defense: int = 6
    _speed: int = 21
    _evade: int = 30
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 2
    _coins: int = 6
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Squeek, squeek...[await]"


class K9Enemy(Enemy):
    """K-9 enemy class"""
    _monster_id: int = 16
    _name: str = "K-9"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 13
    _defense: int = 13
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " May I take a BITE?[await]"


class MAGMITEEnemy(Enemy):
    """MAGMITE enemy class"""
    _monster_id: int = 17
    _name: str = "MAGMITE"

    _hp: int = 26
    _fp: int = 100
    _attack: int = 45
    _defense: int = 70
    _magic_attack: int = 3
    _magic_defense: int = 1
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 1
    _yoshi_cookie_item = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Got a thorn in my foot.[await]"


class THEBIGBOOEnemy(Enemy):
    """THE BIG BOO enemy class"""
    _monster_id: int = 18
    _name: str = "THE BIG BOO"

    _hp: int = 43
    _fp: int = 12
    _attack: int = 18
    _defense: int = 0
    _magic_attack: int = 18
    _magic_defense: int = 24
    _speed: int = 17
    _evade: int = 40
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.FEAR]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = FrightBombItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Stop staring at me![await]"

    _remake_name = "BOO"


class DRYBONESEnemy(Enemy):
    """DRY BONES enemy class"""
    _monster_id: int = 19
    _name: str = "DRY BONES"

    _hp: int = 0
    _fp: int = 100
    _attack: int = 74
    _defense: int = 0
    _magic_attack: int = 7
    _magic_defense: int = 0
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m sick of gettin’ hit![await]"


class GREAPEREnemy(Enemy):
    """GREAPER enemy class"""
    _monster_id: int = 20
    _name: str = "GREAPER"

    _hp: int = 148
    _fp: int = 100
    _attack: int = 72
    _defense: int = 50
    _magic_attack: int = 40
    _magic_defense: int = 20
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 13
    _coins: int = 0
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 1
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Any reaping to be done?[await]"


class SPARKYEnemy(Enemy):
    """SPARKY enemy class"""
    _monster_id: int = 21
    _name: str = "SPARKY"

    _hp: int = 120
    _fp: int = 12
    _attack: int = 40
    _defense: int = 1
    _magic_attack: int = 38
    _magic_defense: int = 50
    _speed: int = 19
    _evade: int = 6
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Fire EVERYWHERE![await]"

    _remake_name = "LAVA BUBBLE"


class CHOMPEnemy(Enemy):
    """CHOMP enemy class"""
    _monster_id: int = 22
    _name: str = "CHOMP"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 65
    _magic_attack: int = 5
    _magic_defense: int = 31
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = BracerItem
    _common_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Workin’ on a chain gang.[await]"

    _remake_name = "CHAIN CHOMP"


class PANDORITEEnemy(Enemy):
    """PANDORITE enemy class"""
    _monster_id: int = 23
    _name: str = "PANDORITE"

    _hp: int = 300
    _fp: int = 50
    _attack: int = 30
    _defense: int = 20
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " I’m trying to sleep, OK?[await]"

    _remake_name = "HUHWHAT"


class SHYRANGEREnemy(Enemy):
    """SHY RANGER enemy class"""
    _monster_id: int = 24
    _name: str = "SHY RANGER"

    _hp: int = 300
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 43
    _evade: int = 50
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _xp: int = 60
    _coins: int = 1
    _yoshi_cookie_item = KerokeroColaItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Transmitting information.[await]\n Over and out.[await]"


class BOBOMBEnemyStatic(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 25
    _name: str = "BOB-OMB"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 4
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ouch. HEY! Watch it![await]"


class SPOOKUMEnemy(Enemy):
    """SPOOKUM enemy class"""
    _monster_id: int = 26
    _name: str = "SPOOKUM"

    _hp: int = 98
    _fp: int = 100
    _attack: int = 50
    _defense: int = 45
    _magic_attack: int = 32
    _magic_defense: int = 5
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 8
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 10
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Que pasa?[await]"

    _remake_name = "SNIFIT"


class HAMMERBROEnemy(Enemy):
    """HAMMER BRO enemy class"""
    _monster_id: int = 27
    _name: str = "HAMMER BRO"

    _hp: int = 50
    _fp: int = 1
    _attack: int = 6
    _defense: int = 13
    _magic_attack: int = 6
    _magic_defense: int = 8
    _speed: int = 10
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 3
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I love my hammer![await]"


class BUZZEREnemy(Enemy):
    """BUZZER enemy class"""
    _monster_id: int = 28
    _name: str = "BUZZER"

    _hp: int = 43
    _fp: int = 100
    _attack: int = 37
    _defense: int = 15
    _magic_attack: int = 4
    _magic_defense: int = 1
    _speed: int = 25
    _evade: int = 30
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Buzzzzz...[await]"


class AMEBOIDEnemy(Enemy):
    """AMEBOID enemy class"""
    _monster_id: int = 29
    _name: str = "AMEBOID"

    _hp: int = 220
    _fp: int = 100
    _attack: int = 130
    _defense: int = 1
    _magic_attack: int = 30
    _magic_defense: int = 120
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 50
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MaxMushroomItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_FROM_MIDDLE
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Get outta my face.[await]"


class GECKOEnemy(Enemy):
    """GECKO enemy class"""
    _monster_id: int = 30
    _name: str = "GECKO"

    _hp: int = 92
    _fp: int = 100
    _attack: int = 68
    _defense: int = 46
    _magic_attack: int = 9
    _magic_defense: int = 32
    _speed: int = 22
    _evade: int = 14
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = FroggieDrinkItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Red? What about Green?[await]"


class WIGGLEREnemy(Enemy):
    """WIGGLER enemy class"""
    _monster_id: int = 31
    _name: str = "WIGGLER"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 40
    _defense: int = 25
    _magic_attack: int = 18
    _magic_defense: int = 20
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 6
    _coins: int = 10
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 3
    _psychopath_message: str = " I’m just a helpless wiggler...[await]"


class CRUSTYEnemy(Enemy):
    """CRUSTY enemy class"""
    _monster_id: int = 32
    _name: str = "CRUSTY"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 100
    _defense: int = 100
    _magic_attack: int = 12
    _magic_defense: int = 35
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 25
    _coins: int = 7
    _yoshi_cookie_item = BracerItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " Look at THIS![await]"


class KAMEKEnemy(Enemy):
    """KAMEK enemy class"""
    _monster_id: int = 33
    _name: str = "MAGIKOOPA"

    _hp: int = 1600
    _fp: int = 250
    _attack: int = 100
    _defense: int = 60
    _magic_attack: int = 120
    _magic_defense: int = 100
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON]
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " That’s...my child?[await]"

    _remake_name = "WIZAKOOPA"


class LEUKOEnemy(Enemy):
    """LEUKO enemy class"""
    _monster_id: int = 34
    _name: str = "LEUKO"

    _hp: int = 220
    _fp: int = 100
    _attack: int = 65
    _defense: int = 50
    _magic_attack: int = 42
    _magic_defense: int = 60
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 3
    _yoshi_cookie_item = MegalixirItem
    _rare_item_drop = MidMushroomItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Floating’s a bad habit.[await]"


class JAWFULEnemy(Enemy):
    """JAWFUL enemy class"""
    _monster_id: int = 35
    _name: str = "JAWFUL"

    _hp: int = 278
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.FEAR]
    _xp: int = 27
    _coins: int = 0
    _yoshi_cookie_item = RockCandyItem
    _rare_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Huh?[await]"


class ENIGMAEnemy(Enemy):
    """ENIGMA enemy class"""
    _monster_id: int = 36
    _name: str = "ENIGMA"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 55
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _speed: int = 25
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 10
    _coins: int = 5
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " Gather around! Watch it![await]"


class BLASTEREnemy(Enemy):
    """BLASTER enemy class"""
    _monster_id: int = 37
    _name: str = "BLASTER"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 70
    _defense: int = 70
    _magic_attack: int = 0
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = FrightBombItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Wanna join me?[await]"


class GUERRILLAEnemy(Enemy):
    """GUERRILLA enemy class"""
    _monster_id: int = 38
    _name: str = "GUERRILLA"

    _hp: int = 135
    _fp: int = 100
    _attack: int = 42
    _defense: int = 32
    _magic_attack: int = 1
    _magic_defense: int = 5
    _speed: int = 7
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 4
    _cursor_y: int = 5
    _psychopath_message: str = " Don’t confuse me[await]\n with someone else![await]"


class BIRDYEnemyHenchman(Enemy):
    """BIRDY enemy class"""
    _monster_id: int = 39
    _name: str = "BIRDY"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I HATE Valentina.[await]"


class HOBGOBLINEnemy(Enemy):
    """HOBGOBLIN enemy class"""
    _monster_id: int = 40
    _name: str = "HOBGOBLIN"

    _hp: int = 50
    _fp: int = 8
    _attack: int = 22
    _defense: int = 22
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item = PureWaterItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " Havin’ a blast today![await]"


class REACHEREnemy(Enemy):
    """REACHER enemy class"""
    _monster_id: int = 41
    _name: str = "REACHER"

    _hp: int = 184
    _fp: int = 100
    _attack: int = 95
    _defense: int = 75
    _magic_attack: int = 8
    _magic_defense: int = 0
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " Hope you’ll stay close.[await]"


class SHOGUNEnemy(Enemy):
    """SHOGUN enemy class"""
    _monster_id: int = 42
    _name: str = "SHOGUN"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 1
    _magic_defense: int = 32
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 24
    _coins: int = 10
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Do as you like.[await]"


class ORBUSEREnemy(Enemy):
    """ORB USER enemy class"""
    _monster_id: int = 43
    _name: str = "ORB USER"

    _hp: int = 8
    _fp: int = 20
    _attack: int = 42
    _defense: int = 80
    _magic_attack: int = 28
    _magic_defense: int = 40
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 5
    _coins: int = 2
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " I hate Kinklinks![await]"


class HEAVYTROOPAEnemy(Enemy):
    """HEAVY TROOPA enemy class"""
    _monster_id: int = 44
    _name: str = "HEAVY TROOPA"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 1
    _magic_defense: int = 50
    _speed: int = 3
    _evade: int = 2
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 32
    _coins: int = 4
    _yoshi_cookie_item = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " I’ll make ya beautiful![await]"

    _remake_name = "HEAVY TROOPA"


class SHADOWEnemy(Enemy):
    """SHADOW enemy class"""
    _monster_id: int = 45
    _name: str = "SHADOW"

    _hp: int = 85
    _fp: int = 14
    _attack: int = 24
    _defense: int = 5
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 18
    _evade: int = 10
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = HoneySyrupItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " You’re a model, right?[await]"


class CLUSTEREnemy(Enemy):
    """CLUSTER enemy class"""
    _monster_id: int = 46
    _name: str = "CLUSTER"

    _hp: int = 60
    _fp: int = 100
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 21
    _magic_defense: int = 10
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I’ll psyche you out![await]"


class BAHAMUTTEnemy(Enemy):
    """BAHAMUTT enemy class"""
    _monster_id: int = 47
    _name: str = "BAHAMUTT"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _disable_auto_death: bool = True
    _psychopath_message: str = " Give me a chance, here.[await]"


class OCTOLOTEnemy(Enemy):
    """OCTOLOT enemy class"""
    _monster_id: int = 48
    _name: str = "OCTOLOT"

    _hp: int = 99
    _fp: int = 100
    _attack: int = 38
    _defense: int = 27
    _magic_attack: int = 25
    _magic_defense: int = 30
    _speed: int = 3
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 6
    _coins: int = 4
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " Check out my legs![await]"


class FROGOGEnemy(Enemy):
    """FROGOG enemy class"""
    _monster_id: int = 49
    _name: str = "FROGOG"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 15
    _defense: int = 8
    _magic_attack: int = 0
    _magic_defense: int = 8
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 3
    _coins: int = 4
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " This bright sunlight[await]\n better not fry me![await]"


class CLERKEnemy(Enemy):
    """CLERK enemy class"""
    _monster_id: int = 50
    _name: str = "CLERK"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 47
    _magic_defense: int = 60
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 5
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _psychopath_message: str = " 10 years I’ve been here![await]"


class GUNYOLKEnemy(Enemy):
    """GUNYOLK enemy class"""
    _monster_id: int = 51
    _name: str = "GUNYOLK"

    _hp: int = 1500
    _fp: int = 100
    _attack: int = 200
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 80
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE, Element.THUNDER]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 100
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 5
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " If we’re beaten, the boss is alone![await]"


class BOOMEREnemy(Enemy):
    """BOOMER enemy class"""
    _monster_id: int = 52
    _name: str = "BOOMER"

    _hp: int = 2000
    _fp: int = 200
    _attack: int = 200
    _defense: int = 140
    _magic_attack: int = 35
    _magic_defense: int = 26
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 55
    _coins: int = 9
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " It’s all over now...[await]"


class REMOCONEnemy(Enemy):
    """REMO CON enemy class"""
    _monster_id: int = 53
    _name: str = "REMO CON"

    _hp: int = 88
    _fp: int = 100
    _attack: int = 56
    _defense: int = 52
    _magic_attack: int = 25
    _magic_defense: int = 10
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 8
    _coins: int = 7
    _yoshi_cookie_item = PickMeUpItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " The world is history.[await]"

    _remake_name = "DOLLOX"


class SNAPDRAGONEnemy(Enemy):
    """SNAPDRAGON enemy class"""
    _monster_id: int = 54
    _name: str = "SNAPDRAGON"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 28
    _defense: int = 25
    _magic_attack: int = 31
    _magic_defense: int = 25
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item = SleepyBombItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I did a lot in my youth.[await]"


class STUMPETEnemy(Enemy):
    """STUMPET enemy class"""
    _monster_id: int = 55
    _name: str = "STUMPET"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 6
    _magic_defense: int = 60
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 70
    _coins: int = 15
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = FrightBombItem
    _common_item_drop = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " Express yourself![await]"


class DODOEnemy(Enemy):
    """DODO enemy class"""
    _monster_id: int = 56
    _name: str = "DODO"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m starved...later![await]"


class JESTEREnemy(Enemy):
    """JESTER enemy class"""
    _monster_id: int = 57
    _name: str = "JESTER"

    _hp: int = 151
    _fp: int = 12
    _attack: int = 48
    _defense: int = 35
    _magic_attack: int = 22
    _magic_defense: int = 35
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 80
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " I’ve failed my King...[await]"


class ARTICHOKEREnemy(Enemy):
    """ARTICHOKER enemy class"""
    _monster_id: int = 58
    _name: str = "ARTICHOKER"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 50
    _defense: int = 54
    _magic_attack: int = 27
    _magic_defense: int = 24
    _speed: int = 7
    _evade: int = 0
    _magic_evade: int = 20
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Relax a little, okay?[await]"


class ARACHNEEnemy(Enemy):
    """ARACHNE enemy class"""
    _monster_id: int = 59
    _name: str = "ARACHNE"

    _hp: int = 82
    _fp: int = 100
    _attack: int = 35
    _defense: int = 35
    _magic_attack: int = 6
    _magic_defense: int = 0
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 6
    _coins: int = 6
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " ♪Day-o...[await]"


class CARROBOSCISEnemy(Enemy):
    """CARROBOSCIS enemy class"""
    _monster_id: int = 60
    _name: str = "CARROBOSCIS"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 55
    _defense: int = 44
    _magic_attack: int = 28
    _magic_defense: int = 22
    _speed: int = 30
    _evade: int = 13
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 10
    _coins: int = 4
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " I ALWAYS eat my vegetables![await]"


class HIPPOPOEnemy(Enemy):
    """HIPPOPO enemy class"""
    _monster_id: int = 61
    _name: str = "HIPPOPO"

    _hp: int = 400
    _fp: int = 100
    _attack: int = 150
    _defense: int = 110
    _magic_attack: int = 85
    _magic_defense: int = 53
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 15
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 80
    _coins: int = 50
    _yoshi_cookie_item = MegalixirItem
    _common_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 5
    _cursor_y: int = 4
    _psychopath_message: str = " This is a drag...[await]"


class MASTADOOMEnemy(Enemy):
    """MASTADOOM enemy class"""
    _monster_id: int = 62
    _name: str = "MASTADOOM"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 90
    _defense: int = 65
    _magic_attack: int = 30
    _magic_defense: int = 50
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = CrystallineItem
    _rare_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " Phew, I’m FREEZING..[await]"


class CORKPEDITEEnemy(Enemy):
    """CORKPEDITE enemy class"""
    _monster_id: int = 63
    _name: str = "CORKPEDITE"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 20
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item = CrystallineItem
    _rare_item_drop = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _psychopath_message: str = " Off! FORGET IT![await]"

    _remake_name = "STOMPILLAR"


class TERRACOTTAEnemy(Enemy):
    """TERRA COTTA enemy class"""
    _monster_id: int = 64
    _name: str = "TERRA COTTA"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 120
    _defense: int = 85
    _magic_attack: int = 36
    _magic_defense: int = 35
    _speed: int = 23
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Oh, Mr.Bowser~~[await]"


class SPIKESTEREnemy(Enemy):
    """SPIKESTER enemy class"""
    _monster_id: int = 65
    _name: str = "SPIKESTER"

    _hp: int = 50
    _fp: int = 100
    _attack: int = 48
    _defense: int = 60
    _magic_attack: int = 12
    _magic_defense: int = 4
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 6
    _coins: int = 2
    _yoshi_cookie_item = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Why, you’re AFRAID of me![await]"


class MALAKOOPAEnemy(Enemy):
    """MALAKOOPA enemy class"""
    _monster_id: int = 66
    _name: str = "MALAKOOPA"

    _hp: int = 95
    _fp: int = 100
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 47
    _magic_defense: int = 98
    _speed: int = 35
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 23
    _coins: int = 3
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Just call me “General!”[await]"


class POUNDEREnemyStatic(Enemy):
    """POUNDER enemy class"""
    _monster_id: int = 67
    _name: str = "POUNDER"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 130
    _defense: int = 70
    _magic_attack: int = 45
    _magic_defense: int = 60
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 24
    _coins: int = 2
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Wham bam SLAM![await]"


class POUNDETTEEnemyStatic(Enemy):
    """POUNDETTE enemy class"""
    _monster_id: int = 68
    _name: str = "POUNDETTE"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 28
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Love conquers ALL.[await]"


class SACKITEnemy(Enemy):
    """SACKIT enemy class"""
    _monster_id: int = 69
    _name: str = "SACKIT"

    _hp: int = 152
    _fp: int = 100
    _attack: int = 70
    _defense: int = 53
    _magic_attack: int = 13
    _magic_defense: int = 20
    _speed: int = 26
    _evade: int = 20
    _magic_evade: int = 0
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item = MaxMushroomItem
    _rare_item_drop = MaxMushroomItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " This is just how I am.[await]"


class GUGOOMBAEnemy(Enemy):
    """GU GOOMBA enemy class"""
    _monster_id: int = 70
    _name: str = "GU GOOMBA"

    _hp: int = 132
    _fp: int = 100
    _attack: int = 115
    _defense: int = 66
    _magic_attack: int = 13
    _magic_defense: int = 66
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 50
    _xp: int = 15
    _coins: int = 1
    _yoshi_cookie_item = FroggieDrinkItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Hey, maybe I CAN win![await]"

    _remake_name = "PRO GOOMBA"


class CHEWYEnemy(Enemy):
    """CHEWY enemy class"""
    _monster_id: int = 71
    _name: str = "CHEWY"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 110
    _defense: int = 82
    _magic_attack: int = 70
    _magic_defense: int = 52
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 50
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 14
    _coins: int = 0
    _yoshi_cookie_item = BadMushroomItem
    _common_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’m just a fresh flower.[await]"


class FIREBALLEnemy(Enemy):
    """FIREBALL enemy class"""
    _monster_id: int = 72
    _name: str = "FIREBALL"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 55
    _defense: int = 16
    _magic_attack: int = 30
    _magic_defense: int = 16
    _speed: int = 42
    _evade: int = 50
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.ICE, Element.JUMP]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 8
    _coins: int = 0
    _yoshi_cookie_item = FireBombItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Blurb blurb blurb...[await]"

    _remake_name = "LAVA BLUBBLE"


class MRKIPPEREnemy(Enemy):
    """MR.KIPPER enemy class"""
    _monster_id: int = 73
    _name: str = "MR.KIPPER"

    _hp: int = 133
    _fp: int = 100
    _attack: int = 75
    _defense: int = 45
    _magic_attack: int = 14
    _magic_defense: int = 10
    _speed: int = 23
    _evade: int = 13
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 8
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " I’m a fresh little fish.[await]"


class FACTORYCHIEFEnemy(Enemy):
    """FACTORY CHIEF enemy class"""
    _monster_id: int = 74
    _name: str = "FACTORY CHIEF"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 70
    _magic_defense: int = 90
    _speed: int = 45
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 80
    _coins: int = 90
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Who DARES to fight ME?![await]"


class BANDANABLUEEnemy(Enemy):
    """BANDANA BLUE enemy class"""
    _monster_id: int = 75
    _name: str = "BANDANA BLUE"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 80
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 30
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Color me Blue, mates!![await]"


class MANAGEREnemy(Enemy):
    """MANAGER enemy class"""
    _monster_id: int = 76
    _name: str = "MANAGER"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 170
    _defense: int = 110
    _magic_attack: int = 60
    _magic_defense: int = 70
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 60
    _coins: int = 40
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " 25 years of working, sigh.[await]"


class BLUEBIRDEnemyStatic(Enemy):
    """BLUEBIRD enemy class"""
    _monster_id: int = 77
    _name: str = "BLUEBIRD"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _speed: int = 29
    _evade: int = 8
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item = BracerItem
    _common_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " You are... magnificent[await]"



class GENOCLONESEnemy(Enemy):
    """GENO CLONE S enemy class"""
    _monster_id: int = 78
    _name: str = "GENO CLONE S"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 220
    _defense: int = 170
    _magic_attack: int = 180
    _magic_defense: int = 60
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE, Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 39
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Truth is...[await]\nI don't care one bit about Star Pieces.[await]"



class ALLEYRATEnemy(Enemy):
    """ALLEY RAT enemy class"""
    _monster_id: int = 79
    _name: str = "ALLEY RAT"

    _hp: int = 105
    _fp: int = 100
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 13
    _magic_defense: int = 12
    _speed: int = 21
    _evade: int = 15
    _magic_evade: int = 0
    _xp: int = 9
    _coins: int = 3
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Don’t pity me, Mario![await]"


class CHOWEnemy(Enemy):
    """CHOW enemy class"""
    _monster_id: int = 80
    _name: str = "CHOW"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 82
    _defense: int = 77
    _magic_attack: int = 8
    _magic_defense: int = 28
    _speed: int = 27
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _xp: int = 15
    _coins: int = 3
    _yoshi_cookie_item = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Hey, I fought you already![await]"


class MAGMUSEnemy(Enemy):
    """MAGMUS enemy class"""
    _monster_id: int = 81
    _name: str = "MAGMUS"

    _hp: int = 50
    _fp: int = 100
    _attack: int = 110
    _defense: int = 140
    _magic_attack: int = 3
    _magic_defense: int = 25
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 18
    _coins: int = 3
    _yoshi_cookie_item = BracerItem
    _rare_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Clobber me for good life![await]"


class LILBOOEnemy(Enemy):
    """LI’L BOO enemy class"""
    _monster_id: int = 82
    _name: str = "LI’L BOO"

    _hp: int = 66
    _fp: int = 100
    _attack: int = 120
    _defense: int = 20
    _magic_attack: int = 74
    _magic_defense: int = 120
    _speed: int = 27
    _evade: int = 50
    _magic_evade: int = 20
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 28
    _coins: int = 0
    _yoshi_cookie_item = FreshenUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Beep pa doodle-dee!♪[await]"

    _remake_name = "HIGH BOO"


class VOMEREnemy(Enemy):
    """VOMER enemy class"""
    _monster_id: int = 83
    _name: str = "VOMER"

    _hp: int = 0
    _fp: int = 100
    _attack: int = 110
    _defense: int = 0
    _magic_attack: int = 9
    _magic_defense: int = 0
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 5
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 19
    _coins: int = 0
    _yoshi_cookie_item = PureWaterItem
    _rare_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Nobody, NOBODY likes me.[await]"


class GLUMREAPEREnemy(Enemy):
    """GLUM REAPER enemy class"""
    _monster_id: int = 84
    _name: str = "GLUM REAPER"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 120
    _defense: int = 55
    _magic_attack: int = 60
    _magic_defense: int = 80
    _speed: int = 35
    _evade: int = 20
    _magic_evade: int = 10
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 35
    _coins: int = 3
    _yoshi_cookie_item = PureWaterItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 1
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Comin’ through...[await]"


class PYROSPHEREEnemy(Enemy):
    """PYROSPHERE enemy class"""
    _monster_id: int = 85
    _name: str = "PYROSPHERE"

    _hp: int = 167
    _fp: int = 100
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _speed: int = 24
    _evade: int = 7
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Vroom, VROOM!![await]"

    _remake_name = "LAVA BABBLE"


class CHOMPCHOMPEnemy(Enemy):
    """CHOMP CHOMP enemy class"""
    _monster_id: int = 86
    _name: str = "CHOMP CHOMP"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 100
    _defense: int = 92
    _magic_attack: int = 14
    _magic_defense: int = 30
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Hey, let’s PLAY![await]"


class HIDONEnemy(Enemy):
    """HIDON enemy class"""
    _monster_id: int = 87
    _name: str = "HIDON"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 110
    _defense: int = 90
    _magic_attack: int = 60
    _magic_defense: int = 30
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 50
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " You wanna run, huh?![await]"

    _remake_name = "WHUHOH"


class SLINGSHYEnemy(Enemy):
    """SLING SHY enemy class"""
    _monster_id: int = 88
    _name: str = "SLING SHY"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 108
    _defense: int = 80
    _magic_attack: int = 42
    _magic_defense: int = 21
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 3
    _coins: int = 20
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Hear my song.[await]"


class ROBOMBEnemy(Enemy):
    """ROB-OMB enemy class"""
    _monster_id: int = 89
    _name: str = "ROB-OMB"

    _hp: int = 42
    _fp: int = 100
    _attack: int = 54
    _defense: int = 63
    _magic_attack: int = 1
    _magic_defense: int = 20
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 6
    _coins: int = 1
    _yoshi_cookie_item = PickMeUpItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Disappear? Maybe later![await]"


class SHYGUYEnemyStatic(Enemy):
    """SHY GUY enemy class"""
    _monster_id: int = 90
    _name: str = "SHY GUY"

    _hp: int = 78
    _fp: int = 100
    _attack: int = 29
    _defense: int = 30
    _magic_attack: int = 20
    _magic_defense: int = 6
    _speed: int = 14
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 2
    _coins: int = 1
    _yoshi_cookie_item = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Hold still, okay?![await]"


class NINJAEnemy(Enemy):
    """NINJA enemy class"""
    _monster_id: int = 91
    _name: str = "NINJA"

    _hp: int = 235
    _fp: int = 100
    _attack: int = 130
    _defense: int = 76
    _magic_attack: int = 51
    _magic_defense: int = 67
    _speed: int = 28
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 32
    _coins: int = 6
    _yoshi_cookie_item = PowerBlastItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 70
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Wooo HOOO! I’m a FOO![await]"


class STINGEREnemy(Enemy):
    """STINGER enemy class"""
    _monster_id: int = 92
    _name: str = "STINGER"

    _hp: int = 65
    _fp: int = 100
    _attack: int = 78
    _defense: int = 80
    _magic_attack: int = 23
    _magic_defense: int = 10
    _speed: int = 33
    _evade: int = 25
    _magic_evade: int = 0
    _xp: int = 13
    _coins: int = 1
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Strike the pose![await]"


class GOOMBETTEEnemy(Enemy):
    """GOOMBETTE enemy class"""
    _monster_id: int = 93
    _name: str = "GOOMBETTE"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 90
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 30
    _speed: int = 16
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 1
    _psychopath_message: str = " Me speak soft, BIG STICK![await]"

    _remake_name = "MINI GOOMBA"


class GECKITEnemy(Enemy):
    """GECKIT enemy class"""
    _monster_id: int = 94
    _name: str = "GECKIT"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 84
    _defense: int = 63
    _magic_attack: int = 20
    _magic_defense: int = 8
    _speed: int = 25
    _evade: int = 14
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Geck...Geck...GOCK?[await]"


class JABITEnemy(Enemy):
    """JABIT enemy class"""
    _monster_id: int = 95
    _name: str = "JABIT"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 120
    _defense: int = 95
    _magic_attack: int = 27
    _magic_defense: int = 34
    _speed: int = 13
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = BracerItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " This is the pits![await]"


class STARCRUSTEREnemy(Enemy):
    """STAR CRUSTER enemy class"""
    _monster_id: int = 96
    _name: str = "STAR CRUSTER"

    _hp: int = 72
    _fp: int = 100
    _attack: int = 135
    _defense: int = 145
    _magic_attack: int = 16
    _magic_defense: int = 53
    _speed: int = 11
    _evade: int = 0
    _magic_evade: int = 10
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 36
    _coins: int = 30
    _yoshi_cookie_item = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " I’M NOT A CRAB!![await]"


class TeamGaugeEnemy(Enemy):
    """Team Gauge enemy class"""
    _monster_id: int = 97
    _name: str = "Team Gauge"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 255
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "[await]"


class MUCKLEEnemy(Enemy):
    """MUCKLE enemy class"""
    _monster_id: int = 98
    _name: str = "MUCKLE"

    _hp: int = 320
    _fp: int = 100
    _attack: int = 90
    _defense: int = 44
    _magic_attack: int = 90
    _magic_defense: int = 44
    _speed: int = 2
    _evade: int = 1
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 6
    _coins: int = 3
    _yoshi_cookie_item = IceBombItem
    _common_item_drop = IceBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Gotta know your limits.[await]"


class FORKIESEnemy(Enemy):
    """FORKIES enemy class"""
    _monster_id: int = 99
    _name: str = "FORKIES"

    _hp: int = 350
    _fp: int = 100
    _attack: int = 170
    _defense: int = 120
    _magic_attack: int = 45
    _magic_defense: int = 128
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 32
    _coins: int = 7
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Shikashikashika~~![await]"

    _remake_name = "FORKIE"


class GORGONEnemy(Enemy):
    """GORGON enemy class"""
    _monster_id: int = 100
    _name: str = "GORGON"

    _hp: int = 140
    _fp: int = 100
    _attack: int = 86
    _defense: int = 73
    _magic_attack: int = 24
    _magic_defense: int = 52
    _speed: int = 16
    _evade: int = 11
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I just wanna go home.[await]"

    _remake_name = "ENIGMAX"


class BIGBERTHAEnemy(Enemy):
    """BIG BERTHA enemy class"""
    _monster_id: int = 101
    _name: str = "BIG BERTHA"

    _hp: int = 350
    _fp: int = 100
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 35
    _coins: int = 7
    _yoshi_cookie_item = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Adabing, ADABANG![await]"

    _remake_name = "BIG BLASTER"


class CHAINEDKONGEnemy(Enemy):
    """CHAINED KONG enemy class"""
    _monster_id: int = 102
    _name: str = "CHAINED KONG"

    _hp: int = 355
    _fp: int = 100
    _attack: int = 150
    _defense: int = 80
    _magic_attack: int = 22
    _magic_defense: int = 50
    _speed: int = 17
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 35
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " A tad warm, isn’t it?![await]"


class FAUTSOEnemy(Enemy):
    """FAUTSO enemy class"""
    _monster_id: int = 103
    _name: str = "FAUTSO"

    _hp: int = 420
    _fp: int = 100
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 60
    _magic_defense: int = 60
    _speed: int = 14
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 3
    _cursor_y: int = 6
    _disable_auto_death: bool = True
    _psychopath_message: str = " Thanks to you I’m free![await]"

    _remake_name = "JINNIE"


class STRAWHEADEnemy(Enemy):
    """STRAW HEAD enemy class"""
    _monster_id: int = 104
    _name: str = "STRAW HEAD"

    _hp: int = 131
    _fp: int = 100
    _attack: int = 80
    _defense: int = 63
    _magic_attack: int = 18
    _magic_defense: int = 12
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 17
    _coins: int = 12
    _yoshi_cookie_item = PureWaterItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " Gotta press this shirt![await]"


class BLUEBIRDEnemyHenchman(Enemy):
    """BLUEBIRD enemy class"""
    _monster_id: int = 105
    _name: str = "BLUEBIRD"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _speed: int = 29
    _evade: int = 8
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item = BracerItem
    _common_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " You are... magnificent[await]"


class ARMOREDANTEnemy(Enemy):
    """ARMORED ANT enemy class"""
    _monster_id: int = 106
    _name: str = "ARMORED ANT"

    _hp: int = 230
    _fp: int = 100
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 30
    _coins: int = 5
    _yoshi_cookie_item = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Do one good turn a day![await]"


class ORBISONEnemy(Enemy):
    """ORBISON enemy class"""
    _monster_id: int = 107
    _name: str = "ORBISON"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 113
    _defense: int = 140
    _magic_attack: int = 63
    _magic_defense: int = 65
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = RoyalSyrupItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " Don’t jump on me![await]"


class TUBOTROOPAEnemy(Enemy):
    """TUB-O-TROOPA enemy class"""
    _monster_id: int = 108
    _name: str = "TUB-O-TROOPA"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 200
    _defense: int = 80
    _magic_attack: int = 7
    _magic_defense: int = 34
    _speed: int = 5
    _evade: int = 1
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 40
    _coins: int = 11
    _yoshi_cookie_item = ElixirItem
    _common_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " My shell’s shot![await]"

    _remake_name = "GRAND TROOPA"


class DOPPELEnemy(Enemy):
    """DOPPEL enemy class"""
    _monster_id: int = 109
    _name: str = "DOPPEL"

    _hp: int = 333
    _fp: int = 100
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 44
    _magic_defense: int = 50
    _speed: int = 40
    _evade: int = 19
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 40
    _coins: int = 12
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " This’s been a bad year![await]"


class PULSAREnemy(Enemy):
    """PULSAR enemy class"""
    _monster_id: int = 110
    _name: str = "PULSAR"

    _hp: int = 69
    _fp: int = 100
    _attack: int = 75
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 35
    _speed: int = 8
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 15
    _coins: int = 12
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 90
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I’m a mini-pulsar.[await]"


class BOBOMBEnemyHenchman(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 111
    _name: str = "BOB-OMB"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 4
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = "[await]"


class OCTOVADEREnemy(Enemy):
    """OCTOVADER enemy class"""
    _monster_id: int = 112
    _name: str = "OCTOVADER"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 63
    _magic_defense: int = 50
    _speed: int = 5
    _evade: int = 9
    _magic_evade: int = 8
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item = FroggieDrinkItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 6
    _psychopath_message: str = " I’m a part-time typist![await]"


class RIBBITEEnemy(Enemy):
    """RIBBITE enemy class"""
    _monster_id: int = 113
    _name: str = "RIBBITE"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 115
    _defense: int = 20
    _magic_attack: int = 31
    _magic_defense: int = 29
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 22
    _coins: int = 8
    _yoshi_cookie_item = ElixirItem
    _common_item_drop = ElixirItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 6
    _psychopath_message: str = " My dad says, “Hello.”[await]"


class DIRECTOREnemy(Enemy):
    """DIRECTOR enemy class"""
    _monster_id: int = 114
    _name: str = "DIRECTOR"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 190
    _defense: int = 120
    _magic_attack: int = 57
    _magic_defense: int = 80
    _speed: int = 35
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 70
    _coins: int = 80
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 5
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _psychopath_message: str = " I just lost EVERYTHING.[await]"


class SNIFITEnemyHenchman(Enemy):
    """SNIFIT enemy class"""
    _monster_id: int = 115
    _name: str = "SNIFIT"

    _hp: int = 200
    _fp: int = 32
    _attack: int = 60
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 26
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Minimum wage for THIS?![await]"

    _remake_name = "SNIFSTER"


class POUNDEREnemyHenchman(Enemy):
    """Pounder henchman class to not interfere with overworld enemy in factory encounters, etc"""
    _monster_id: int = 116
    _name: str = "POUNDER"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 130
    _defense: int = 70
    _magic_attack: int = 45
    _magic_defense: int = 60
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 24
    _coins: int = 2
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


class PUPPOXEnemy(Enemy):
    """PUPPOX enemy class"""
    _monster_id: int = 117
    _name: str = "PUPPOX"

    _hp: int = 300
    _fp: int = 100
    _attack: int = 145
    _defense: int = 110
    _magic_attack: int = 20
    _magic_defense: int = 32
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item = RockCandyItem
    _rare_item_drop = FreshenUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " What does it all MEAN?[await]"


class FINKFLOWEREnemy(Enemy):
    """FINK FLOWER enemy class"""
    _monster_id: int = 118
    _name: str = "FINK FLOWER"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 95
    _defense: int = 32
    _magic_attack: int = 63
    _magic_defense: int = 90
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 12
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 20
    _coins: int = 2
    _yoshi_cookie_item = MaxMushroomItem
    _rare_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " Gimme your best shot![await]"


class CROOKEnemyHenchman(Enemy):
    """CROOK enemy class"""
    _monster_id: int = 119
    _name: str = "CROOK"

    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " You can’t run away! Ha![await]"


class SPRINGEREnemy(Enemy):
    """SPRINGER enemy class"""
    _monster_id: int = 120
    _name: str = "SPRINGER"

    _hp: int = 122
    _fp: int = 100
    _attack: int = 155
    _defense: int = 110
    _magic_attack: int = 100
    _magic_defense: int = 79
    _speed: int = 16
    _evade: int = 30
    _magic_evade: int = 0
    _xp: int = 29
    _coins: int = 2
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " What’s going on here?[await]"



class APPRENTICEEnemyHenchman(Enemy):
    """APPRENTICE enemy class"""
    _monster_id: int = 121
    _name: str = "APPRENTICE"

    _hp: int = 120
    _fp: int = 32
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’ve had ENOUGH.[await]"


class KRIFFIDEnemy(Enemy):
    """KRIFFID enemy class"""
    _monster_id: int = 122
    _name: str = "KRIFFID"

    _hp: int = 320
    _fp: int = 100
    _attack: int = 95
    _defense: int = 100
    _magic_attack: int = 50
    _magic_defense: int = 40
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 35
    _coins: int = 6
    _yoshi_cookie_item = CrystallineItem
    _common_item_drop = BadMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Aloe~ there![await]"


class SPINTHRAEnemy(Enemy):
    """SPINTHRA enemy class"""
    _monster_id: int = 123
    _name: str = "SPINTHRA"

    _hp: int = 230
    _fp: int = 100
    _attack: int = 110
    _defense: int = 70
    _magic_attack: int = 4
    _magic_defense: int = 32
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 4
    _yoshi_cookie_item = PowerBlastItem
    _rare_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Oh! I’m gonna poison ya![await]"


class BANDANAREDEnemyHenchman(Enemy):
    """BANDANA RED enemy class"""
    _monster_id: int = 124
    _name: str = "BANDANA RED"

    _hp: int = 124
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 10
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love the color RED![await]"


class BOWSERCOPYSEnemy(Enemy):
    """BOWSER COPY S enemy class"""
    _monster_id: int = 125
    _name: str = "BOWSER COPY S"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 230
    _defense: int = 180
    _magic_attack: int = 142
    _magic_defense: int = 30
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 99
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 2
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "What a rrrrrrollicking good time![await]"


class BLOOBEREnemyHenchman(Enemy):
    """BLOOBER enemy class"""
    _monster_id: int = 126
    _name: str = "BLOOBER"

    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love floating around.[await]"

    _remake_name = "BLOOPER"


class BOOSTERDUMMY(Enemy):
    """booster 2 enemy class"""
    _monster_id: int = 127
    _name: str = ""

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 255
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = "[await]"


class APPRENTICEEnemyStatic(Enemy):
    """APPRENTICE enemy class"""
    _monster_id: int = 128
    _name: str = "APPRENTICE"

    _hp: int = 120
    _fp: int = 32
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’ve had ENOUGH.[await]"


class TOADSTOOL3Enemy(Enemy):
    """TOADSTOOL 3 enemy class"""
    _monster_id: int = 129
    _name: str = "TOADSTOOL 3"

    _hp: int = 240
    _fp: int = 180
    _attack: int = 190
    _defense: int = 155
    _magic_attack: int = 152
    _magic_defense: int = 100
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Hey, Chancellor.[await]\n I'm the pretty one, right?[await]"


class PIRANHAPLANTEnemyHenchman(Enemy):
    """PIRANHA PLANT enemy class"""
    _monster_id: int = 130
    _name: str = "PIRANHA PLANT"

    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 5
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Pretty boring nowadays.[await]"


class MARIOCLONESEnemy(Enemy):
    """MARIO CLONE S enemy class"""
    _monster_id: int = 131
    _name: str = "MARIO CLONE S"

    _hp: int = 400
    _fp: int = 100
    _attack: int = 200
    _defense: int = 170
    _magic_attack: int = 163
    _magic_defense: int = 80
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 9
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " ![await]"


class POUNDETTEEnemyHenchman(Enemy):
    """POUNDETTE henchman class to not interfere with overworld enemy in factory, etc"""
    _monster_id: int = 132
    _name: str = "POUNDETTE"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 28
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


class MADMALLETEnemyHenchman(Enemy):
    """MAD MALLET henchman class to not interfere with overworld enemy in factory, etc"""
    _monster_id: int = 133
    _name: str = "MAD MALLET"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 34
    _magic_defense: int = 85
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 1
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


class BOXBOYEnemy(Enemy):
    """BOX BOY enemy class"""
    _monster_id: int = 134
    _name: str = "BOX BOY"

    _hp: int = 900
    _fp: int = 100
    _attack: int = 180
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 40
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 100
    _coins: int = 150
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " Been waitin’ 100 years![await]"

    _remake_name = "PLEASENO"


class SHELLYEnemy(Enemy):
    """SHELLY enemy class"""
    _monster_id: int = 135
    _name: str = "SHELLY"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 0
    _defense: int = 80
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Slow down![await]"


class PUNCHINELLO2Enemy(Enemy):
    """PUNCHINELLO enemy class"""
    _monster_id: int = 136
    _name: str = "PUNCHINELLO 2"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 235
    _defense: int = 215
    _magic_attack: int = 235
    _magic_defense: int = 255
    _speed: int = 99
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Everyone is even MORE chic now![await]\n You've really leveled up your game![await]"


class DODOEnemySolo(Enemy):
    """DODO enemy class"""
    _monster_id: int = 137
    _name: str = "DODO"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 70
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m STARVED![await]"


class OERLIKONEnemy(Enemy):
    """OERLIKON enemy class"""
    _monster_id: int = 138
    _name: str = "OERLIKON"

    _hp: int = 85
    _fp: int = 100
    _attack: int = 120
    _defense: int = 125
    _magic_attack: int = 17
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 22
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " I live to eat.[await]"

    _remake_name = "URSPIKE"


class CHESTEREnemy(Enemy):
    """CHESTER enemy class"""
    _monster_id: int = 139
    _name: str = "CHESTER"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 120
    _magic_defense: int = 80
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 150
    _coins: int = 200
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " I love my job!♥[await]"

    _remake_name = "COMEON"


class BODYEnemy(Enemy):
    """BODY enemy class"""
    _monster_id: int = 140
    _name: str = "BODY"

    _hp: int = 300
    _fp: int = 100
    _attack: int = 100
    _defense: int = 99
    _magic_attack: int = 6
    _magic_defense: int = 1
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " ••••••[await]"


class STRONGBOBOMB1Enemy(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 141
    _name: str = "BOB-OMB S"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 255
    _defense: int = 68
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " How many times do I need to say,[await]\n “Watch out.  I'm gonna explode.”[await]\n before you get it?[await]"


class TORTEEnemy(Enemy):
    """TORTE enemy class"""
    _monster_id: int = 142
    _name: str = "TORTE"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 50
    _magic_attack: int = 8
    _magic_defense: int = 27
    _speed: int = 99
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.TORTE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Cake! Vatch zee CAKE.[await]"


class SHYAWAYEnemy(Enemy):
    """SHY AWAY enemy class"""
    _monster_id: int = 143
    _name: str = "SHY AWAY"

    _hp: int = 140
    _fp: int = 100
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 39
    _magic_defense: int = 73
    _speed: int = 25
    _evade: int = 40
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 30
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " La Dee Dah~ Ha Ha.[await]"

    _remake_name = "BEEZO"


class JINXCLONEEnemy(Enemy):
    """JINX CLONE enemy class"""
    _monster_id: int = 144
    _name: str = "JINX CLONE"

    _hp: int = 320
    _fp: int = 0
    _attack: int = 180
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 35
    _speed: int = 22
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m the REAL thing![await]"


class MACHINEMADEBodyguardEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 145
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 250
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 90
    _magic_defense: int = 65
    _speed: int = 36
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"


class MACHINEMADEDrillbitEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 146
    _name: str = "MACHINE MADE"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 130
    _defense: int = 82
    _magic_attack: int = 31
    _magic_defense: int = 69
    _speed: int = 24
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Look out, LOSERS![await]"


class FORMLESSEnemy(Enemy):
    """FORMLESS enemy class"""
    _monster_id: int = 147
    _name: str = "FORMLESS"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 50
    _magic_defense: int = 0
    _speed: int = 2
    _evade: int = 100
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I have a secret![await]"


class MOKURAEnemy(Enemy):
    """MOKURA enemy class"""
    _monster_id: int = 148
    _name: str = "MOKURA"

    _hp: int = 620
    _fp: int = 100
    _attack: int = 120
    _defense: int = 75
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 25
    _evade: int = 20
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 90
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _common_item_drop = KerokeroColaItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _psychopath_message: str = " Mwa ha ha...[await]"

    _remake_name = "GASSOX"


class FIRECRYSTALEnemy(Enemy):
    """FIRE CRYSTAL enemy class"""
    _monster_id: int = 149
    _name: str = "FIRE CRYSTAL"

    _hp: int = 2500
    _fp: int = 250
    _attack: int = 0
    _defense: int = 100
    _magic_attack: int = 130
    _magic_defense: int = 60
    _speed: int = 10
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " I gotta vacuum tonight![await]"


class WATERCRYSTALEnemy(Enemy):
    """WATER CRYSTAL enemy class"""
    _monster_id: int = 150
    _name: str = "WATER CRYSTAL"

    _hp: int = 1800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 50
    _speed: int = 12
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Get me back underground![await]"


class EARTHCRYSTALEnemy(Enemy):
    """EARTH CRYSTAL enemy class"""
    _monster_id: int = 151
    _name: str = "EARTH CRYSTAL"

    _hp: int = 3200
    _fp: int = 250
    _attack: int = 0
    _defense: int = 70
    _magic_attack: int = 80
    _magic_defense: int = 33
    _speed: int = 1
    _evade: int = 5
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " I hate being awakened![await]"


class WINDCRYSTALEnemy(Enemy):
    """WIND CRYSTAL enemy class"""
    _monster_id: int = 152
    _name: str = "WIND CRYSTAL"

    _hp: int = 800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 200
    _magic_attack: int = 60
    _magic_defense: int = 88
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Whhhhhhooooo...[await]"


class MARIOCLONEEnemy(Enemy):
    """MARIO CLONE enemy class"""
    _monster_id: int = 153
    _name: str = "MARIO CLONE"

    _hp: int = 200
    _fp: int = 25
    _attack: int = 100
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " ••••••[await]"


class TOADSTOOL2Enemy(Enemy):
    """TOADSTOOL 2 enemy class"""
    _monster_id: int = 154
    _name: str = "TOADSTOOL 2"

    _hp: int = 120
    _fp: int = 180
    _attack: int = 90
    _defense: int = 60
    _magic_attack: int = 62
    _magic_defense: int = 70
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 1
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " It’s tough to be pretty![await]"


class BOWSERCLONEEnemy(Enemy):
    """BOWSER CLONE enemy class"""
    _monster_id: int = 155
    _name: str = "BOWSER CLONE"

    _hp: int = 300
    _fp: int = 1
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 12
    _magic_defense: int = 0
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 100
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 2
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Grr...my castle...[await]"


class GENOCLONEEnemy(Enemy):
    """GENO CLONE enemy class"""
    _monster_id: int = 156
    _name: str = "GENO CLONE"

    _hp: int = 250
    _fp: int = 40
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 30
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Star Pieces...Star...[await]"


class MALLOWCLONEEnemy(Enemy):
    """MALLOW CLONE enemy class"""
    _monster_id: int = 157
    _name: str = "MALLOW CLONE"

    _hp: int = 150
    _fp: int = 80
    _attack: int = 80
    _defense: int = 65
    _magic_attack: int = 70
    _magic_defense: int = 80
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ma? Pa? Where are ya?[await]"


class SHYSTEREnemy(Enemy):
    """SHYSTER enemy class"""
    _monster_id: int = 158
    _name: str = "SHYSTER"

    _hp: int = 30
    _fp: int = 2
    _attack: int = 20
    _defense: int = 26
    _magic_attack: int = 18
    _magic_defense: int = 10
    _speed: int = 18
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = HoneySyrupItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"

    _remake_name = "SHYMORE"


class STRONGBOBOMB2Enemy(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 159
    _name: str = "BOB-OMB S"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 255
    _defense: int = 68
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " How many times do I need to say,[await]\n “Watch out.  I'm gonna explode.”[await]\n before you get it?[await]"


class STRONGBOBOMB3Enemy(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 160
    _name: str = "BOB-OMB S"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 255
    _defense: int = 68
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " How many times do I need to say,[await]\n “Watch out.  I'm gonna explode.”[await]\n before you get it?[await]"


class HANGINSHYEnemy(Enemy):
    """HANGIN’ SHY enemy class"""
    _monster_id: int = 161
    _name: str = "HANGIN' SHY"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _ohko_immune: bool = True
    _psychopath_message: str = " Minimum wage for THIS?![await]"


class SMELTEREnemy(Enemy):
    """SMELTER enemy class"""
    _monster_id: int = 162
    _name: str = "SMELTER"

    _hp: int = 1500
    _fp: int = 100
    _attack: int = 0
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 100
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I brush after each meal![await]"


class MACHINEMADEMackEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 163
    _name: str = "MACHINE MADE"

    _hp: int = 300
    _fp: int = 250
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 95
    _magic_defense: int = 40
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 120
    _coins: int = 30
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Mario! I’m BAAAAAAAACK![await]"


class MACHINEMADEBowyerEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 164
    _name: str = "MACHINE MADE"

    _hp: int = 1000
    _fp: int = 250
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 90
    _magic_defense: int = 80
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 150
    _coins: int = 40
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = IceBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Nya! I’ll SNUFF ya! NYA![await]"


class MACHINEMADEYaridovichEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 165
    _name: str = "MACHINE MADE"

    _hp: int = 800
    _fp: int = 250
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 90
    _magic_defense: int = 50
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 180
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " My promotion’s at stake![await]"


class MACHINEMADEAxemPinkEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 166
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 200
    _attack: int = 95
    _defense: int = 90
    _magic_attack: int = 40
    _magic_defense: int = 100
    _speed: int = 35
    _evade: int = 25
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Oh! My makeup![await]"


class MACHINEMADEAxemBlackEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 167
    _name: str = "MACHINE MADE"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 120
    _defense: int = 110
    _magic_attack: int = 4
    _magic_defense: int = 40
    _speed: int = 55
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Will I make the team?[await]"


class MACHINEMADEAxemRedEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 168
    _name: str = "MACHINE MADE"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 45
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Gotta fight for evil![await]"


class MACHINEMADEAxemYellowEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 169
    _name: str = "MACHINE MADE"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 140
    _defense: int = 130
    _magic_attack: int = 16
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " I’m STARVED![await]"


class MACHINEMADEAxemGreenEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 170
    _name: str = "MACHINE MADE"

    _hp: int = 80
    _fp: int = 250
    _attack: int = 105
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 120
    _speed: int = 40
    _evade: int = 0
    _magic_evade: int = 20
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Whew! Vertigo![await]"


class BAHAMUTTEnemy2(Enemy):
    """BAHAMUTT enemy class"""
    _monster_id: int = 171
    _name: str = "BAHAMUTT"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _disable_auto_death: bool = True
    _psychopath_message: str = "[await]"



class MALLOWCOPYSEnemy(Enemy):
    """MALLOW COPY S enemy class"""
    _monster_id: int = 172
    _name: str = "MALLOW COPY S"

    _hp: int = 300
    _fp: int = 80
    _attack: int = 180
    _defense: int = 160
    _magic_attack: int = 190
    _magic_defense: int = 110
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "I'm afraid to go[await]\n to the bathroom at night.[await]"


class STRONGBOBOMB4Enemy(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 173
    _name: str = "BOB-OMB S"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 255
    _defense: int = 68
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " How many times do I need to say,[await]\n “Watch out.  I'm gonna explode.”[await]\n before you get it?[await]"



class CULEX3DEnemy(Enemy):
    """CULEX 3D enemy class"""
    _monster_id: int = 174
    _name: str = "CULEX 3D"

    _hp: int = 9999
    _fp: int = 255
    _attack: int = 255
    _defense: int = 135
    _magic_attack: int = 110
    _magic_defense: int = 100
    _speed: int = 50
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 732
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 1
    _cursor_x: int = 6
    _cursor_y: int = 7
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You shall bear witness to...[await]\n...the power of post-game content![await]"



class JOHNNYEnemy2(Enemy):
    """JOHNNY 2 enemy class"""
    _monster_id: int = 175
    _name: str = "JOHNNY 2"

    _hp: int = 2000
    _fp: int = 200
    _attack: int = 170
    _defense: int = 50
    _magic_attack: int = 135
    _magic_defense: int = 180
    _speed: int = 255
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 90
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Mario sure is amazing.  I'm a lucky[await]\n guy to get a rematch with him.[await]"



class STARSLAPEnemy(Enemy):
    """STARSLAP enemy class"""
    _monster_id: int = 176
    _name: str = "STARSLAP"

    _hp: int = 62
    _fp: int = 100
    _attack: int = 25
    _defense: int = 24
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 2
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " They think I’m goofy...[await]"


class MUKUMUKUEnemy(Enemy):
    """MUKUMUKU enemy class"""
    _monster_id: int = 177
    _name: str = "MUKUMUKU"

    _hp: int = 108
    _fp: int = 100
    _attack: int = 60
    _defense: int = 47
    _magic_attack: int = 22
    _magic_defense: int = 30
    _speed: int = 11
    _evade: int = 0
    _magic_evade: int = 80
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 8
    _coins: int = 1
    _yoshi_cookie_item = MukuCookieItem
    _rare_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.READY_TO_ATTACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Ya trying to bug me?![await]"

    _remake_name = "THROPHER"


class ZEOSTAREnemy(Enemy):
    """ZEOSTAR enemy class"""
    _monster_id: int = 178
    _name: str = "ZEOSTAR"

    _hp: int = 90
    _fp: int = 4
    _attack: int = 75
    _defense: int = 60
    _magic_attack: int = 28
    _magic_defense: int = 20
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item = SleepyBombItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Oh, I can’t stand him![await]"


class JAGGEREnemy(Enemy):
    """JAGGER enemy class"""
    _monster_id: int = 179
    _name: str = "JAGGER"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 0
    _magic_defense: int = 50
    _speed: int = 30
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Oh! I’m so excited![await]"


class JINXEnemy4(Enemy):
    """JINX enemy class"""
    _monster_id: int = 180
    _name: str = "JINX 4"

    _hp: int = 4000
    _fp: int = 0
    _attack: int = 200
    _defense: int = 50
    _magic_attack: int = 0
    _magic_defense: int = 140
    _speed: int = 35
    _evade: int = 30
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "Sensei!  Please instruct me![await]"



class SMITHYTankEnemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 181
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 30
    _attack: int = 250
    _defense: int = 130
    _magic_attack: int = 10
    _magic_defense: int = 50
    _speed: int = 50
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Don’t shock me! DON’T![await]"


class SMITHYSafeEnemy2(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 182
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 120
    _attack: int = 40
    _defense: int = 150
    _magic_attack: int = 70
    _magic_defense: int = 100
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.THUNDER, Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 4
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Nothin’ can hurt me![await]"



class FIRECRYS3DEnemy(Enemy):
    """FIRE CRYS 3D enemy class"""
    _monster_id: int = 183
    _name: str = "FIRE CRYS 3D"

    _hp: int = 3500
    _fp: int = 250
    _attack: int = 0
    _defense: int = 110
    _magic_attack: int = 140
    _magic_defense: int = 80
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Master Culex has certainly...[await]\n ...grown impressive.[await]"




class MICROBOMBEnemy(Enemy):
    """MICROBOMB enemy class"""
    _monster_id: int = 184
    _name: str = "MICROBOMB"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 42
    _defense: int = 30
    _magic_attack: int = 6
    _magic_defense: int = 10
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 1
    _disable_auto_death: bool = True
    _psychopath_message: str = " Small is as small does.[await]"


class WATERCRYS3DEnemy(Enemy):
    """WATER CRYS 3D enemy class"""
    _monster_id: int = 185
    _name: str = "WATER CRYS 3D"

    _hp: int = 2800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 140
    _magic_attack: int = 130
    _magic_defense: int = 70
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " I continue to hate how dry it is.[await]"


class PYROSPHEREEnemyHenchman(Enemy):
    """PYROSPHERE enemy class"""
    _monster_id: int = 186
    _name: str = "PYROSPHERE"

    _hp: int = 167
    _fp: int = 100
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _speed: int = 24
    _evade: int = 7
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Vroom, VROOM!![await]"

    _remake_name = "LAVA BABBLE"


class NEOSQUIDEnemy(Enemy):
    """NEOSQUID enemy class"""
    _monster_id: int = 187
    _name: str = "NEOSQUID"

    _hp: int = 800
    _fp: int = 200
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 86
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m so utterly alone...[await]"


class YARIDOVICHMirageEnemy(Enemy):
    """YARIDOVICH enemy class"""
    _monster_id: int = 188
    _name: str = "YARIDOVICH"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 100
    _defense: int = 40
    _magic_attack: int = 60
    _magic_defense: int = 10
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m not the real McCoy![await]"

    _remake_name = "SPEARDOVICH"


class HELIOEnemy(Enemy):
    """HELIO enemy class"""
    _monster_id: int = 189
    _name: str = "HELIO"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 140
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.WAIT_THEN_APPEAR
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 1
    _psychopath_message: str = " I’m burnin’ up inside![await]"


class RIGHTEYEEnemy(Enemy):
    """RIGHT EYE enemy class"""
    _monster_id: int = 190
    _name: str = "RIGHT EYE"

    _hp: int = 500
    _fp: int = 200
    _attack: int = 128
    _defense: int = 100
    _magic_attack: int = 82
    _magic_defense: int = 36
    _speed: int = 17
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’ve got an astigmatism![await]"


class LEFTEYEEnemy(Enemy):
    """LEFT EYE enemy class"""
    _monster_id: int = 191
    _name: str = "LEFT EYE"

    _hp: int = 300
    _fp: int = 200
    _attack: int = 153
    _defense: int = 130
    _magic_attack: int = 47
    _magic_defense: int = 80
    _speed: int = 21
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I can’t see a thing![await]"


class KNIFEGUYEnemy(Enemy):
    """KNIFE GUY enemy class"""
    _monster_id: int = 192
    _name: str = "KNIFE GUY"

    _hp: int = 700
    _fp: int = 35
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 20
    _magic_defense: int = 10
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 40
    _coins: int = 15
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Happiness is hip![await]"


class GRATEGUYEnemy(Enemy):
    """GRATE GUY enemy class"""
    _monster_id: int = 193
    _name: str = "GRATE GUY"

    _hp: int = 900
    _fp: int = 50
    _attack: int = 60
    _defense: int = 40
    _magic_attack: int = 25
    _magic_defense: int = 40
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Peace is just a dream.[await]"


class BUNDTEnemy(Enemy):
    """BUNDT enemy class"""
    _monster_id: int = 194
    _name: str = "BUNDT"

    _hp: int = 900
    _fp: int = 100
    _attack: int = 65
    _defense: int = 10
    _magic_attack: int = 25
    _magic_defense: int = 50
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Congratulations.[await]"


class JINX1Enemy(Enemy):
    """JINX 1 enemy class"""
    _monster_id: int = 195
    _name: str = "JINX 1"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 0
    _magic_defense: int = 80
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You’re just a beginner![await]"


class JINX2Enemy(Enemy):
    """JINX 2 enemy class"""
    _monster_id: int = 196
    _name: str = "JINX 2"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 90
    _speed: int = 32
    _evade: int = 30
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Sympathy!? Not from me![await]"


class COUNTDOWNEnemy(Enemy):
    """COUNT DOWN enemy class"""
    _monster_id: int = 197
    _name: str = "COUNT DOWN"

    _hp: int = 2400
    _fp: int = 100
    _attack: int = 0
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 80
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 140
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " We’re into overtime![await]"


class DINGALINGEnemy(Enemy):
    """DING-A-LING enemy class"""
    _monster_id: int = 198
    _name: str = "DING-A-LING"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 180
    _defense: int = 120
    _magic_attack: int = 20
    _magic_defense: int = 50
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Wake up sleepy heads![await]"

    _remake_name = "RING-A-DING"


class BELOME1Enemy(Enemy):
    """BELOME 1 enemy class"""
    _monster_id: int = 199
    _name: str = "BELOME 1"

    _hp: int = 500
    _fp: int = 30
    _attack: int = 30
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 40
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.FLOPPING
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I just...wanna sleep.[await]"


class BELOME2Enemy(Enemy):
    """BELOME 2 enemy class"""
    _monster_id: int = 200
    _name: str = "BELOME 2"

    _hp: int = 1200
    _fp: int = 250
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 40
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 80
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.FLOPPING
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gotta yummy in my tummy![await]"


class BELOMEEnemy3(Enemy):
    """BELOME enemy class"""
    _monster_id: int = 201
    _name: str = "BELOME 3"

    _hp: int = 4600
    _fp: int = 250
    _attack: int = 210
    _defense: int = 0
    _magic_attack: int = 140
    _magic_defense: int = 0
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 84
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.FLOPPING
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "My throat's all scratchy.[await]\n Life would be better if it wasn't.[await]"



class SMILAXEnemy(Enemy):
    """SMILAX enemy class"""
    _monster_id: int = 202
    _name: str = "SMILAX"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Turn your eyes![await]"


class EARTHCRYS3DEnemy(Enemy):
    """EARTH CRYS 3D enemy class"""
    _monster_id: int = 203
    _name: str = "EARTH CRYS 3D"

    _hp: int = 4200
    _fp: int = 250
    _attack: int = 1
    _defense: int = 100
    _magic_attack: int = 105
    _magic_defense: int = 53
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = "Personally, I'd never felt the need...[await]\n...to become three-dimensional.[await]"


class MEGASMILAXEnemy(Enemy):
    """MEGASMILAX enemy class"""
    _monster_id: int = 204
    _name: str = "MEGASMILAX"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 140
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 80
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 120
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 3
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I was a water baby![await]"


class BIRDETTAEnemy(Enemy):
    """BIRDETTA enemy class"""
    _monster_id: int = 205
    _name: str = "BIRDO"

    _hp: int = 777
    _fp: int = 100
    _attack: int = 160
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 100
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 60
    _coins: int = 30
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I just love life![await]"


class EGGBERTEnemy(Enemy):
    """EGGBERT enemy class"""
    _monster_id: int = 206
    _name: str = "EGGBERT"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 210
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What a glorious day![await]"


class AXEMYELLOWEnemy(Enemy):
    """AXEM YELLOW enemy class"""
    _monster_id: int = 207
    _name: str = "AXEM YELLOW"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 60
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " We’re lookin’ GOOD![await]"


class PUNCHINELLOEnemy(Enemy):
    """PUNCHINELLO enemy class"""
    _monster_id: int = 208
    _name: str = "PUNCHINELLO"

    _hp: int = 1200
    _fp: int = 10
    _attack: int = 60
    _defense: int = 42
    _magic_attack: int = 22
    _magic_defense: int = 40
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Yeeha! I see we’re already famous![await]"


class TENTACLESEnemy(Enemy):
    """TENTACLES enemy class"""
    _monster_id: int = 209
    _name: str = "TENTACLES"

    _hp: int = 260
    _fp: int = 100
    _attack: int = 82
    _defense: int = 50
    _magic_attack: int = 35
    _magic_defense: int = 40
    _speed: int = 21
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.READY_TO_ATTACK_2
    _cursor_x: int = 2
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Keep me in cool![await]"

    _remake_name = "TENTACLE"


class AXEMREDEnemy(Enemy):
    """AXEM RED enemy class"""
    _monster_id: int = 210
    _name: str = "AXEM RED"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 150
    _defense: int = 100
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 30
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m all thumbs today![await]"


class AXEMGREENEnemy(Enemy):
    """AXEM GREEN enemy class"""
    _monster_id: int = 211
    _name: str = "AXEM GREEN"

    _hp: int = 450
    _fp: int = 200
    _attack: int = 110
    _defense: int = 60
    _magic_attack: int = 90
    _magic_defense: int = 120
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 20
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Are we done here?[await]"


class KINGBOMBEnemy(Enemy):
    """KING BOMB enemy class"""
    _monster_id: int = 212
    _name: str = "KING BOMB"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 0
    _defense: int = 130
    _magic_attack: int = 80
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I LIVE to explode![await]"


class MEZZOBOMBEnemy(Enemy):
    """MEZZO BOMB enemy class"""
    _monster_id: int = 213
    _name: str = "MEZZO BOMB"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 70
    _defense: int = 40
    _magic_attack: int = 0
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _disable_auto_death: bool = True
    _psychopath_message: str = " Look out![await]"



class BUNDT2Enemy(Enemy):
    """BUNDT enemy class"""
    _monster_id: int = 214
    _name: str = "FANCY BUNDT"

    _hp: int = 3900
    _fp: int = 100
    _attack: int = 230
    _defense: int = 110
    _magic_attack: int = 170
    _magic_defense: int = 100
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 75
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "Cong-ratu-lat-ions.[await]"


class RASPBERRYEnemy(Enemy):
    """RASPBERRY enemy class"""
    _monster_id: int = 215
    _name: str = "RASPBERRY"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 70
    _defense: int = 20
    _magic_attack: int = 30
    _magic_defense: int = 30
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Congratulations![await]"


class KINGCALAMARIEnemy(Enemy):
    """KING CALAMARI enemy class"""
    _monster_id: int = 216
    _name: str = "KING CALAMARI"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 40
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 100
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.DEEP_JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " The ship’s MINE! SCRAM![await]"


class TENTACLESEnemy2(Enemy):
    """TENTACLES enemy class"""
    _monster_id: int = 217
    _name: str = "TENTACLES"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 87
    _defense: int = 70
    _magic_attack: int = 35
    _magic_defense: int = 23
    _speed: int = 21
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.READY_TO_ATTACK_2
    _cursor_x: int = 5
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You wouldn’t...EAT me?![await]"

    _remake_name = "TENTACLE"


class JINX3Enemy(Enemy):
    """JINX 3 enemy class"""
    _monster_id: int = 218
    _name: str = "JINX 3"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 180
    _defense: int = 140
    _magic_attack: int = 0
    _magic_defense: int = 100
    _speed: int = 35
    _evade: int = 30
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ooh! I’m gonna hurt ya![await]"


class ZOMBONEEnemy(Enemy):
    """ZOMBONE enemy class"""
    _monster_id: int = 219
    _name: str = "ZOMBONE"

    _hp: int = 1800
    _fp: int = 100
    _attack: int = 190
    _defense: int = 60
    _magic_attack: int = 80
    _magic_defense: int = 100
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER, Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.WAIT_THEN_APPEAR
    _elevate: int = 2
    _cursor_x: int = 6
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Hey! We’re not done yet![await]"


class CZARDRAGONEnemy(Enemy):
    """CZAR DRAGON enemy class"""
    _monster_id: int = 220
    _name: str = "CZAR DRAGON"

    _hp: int = 1400
    _fp: int = 100
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 70
    _speed: int = 20
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 100
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 6
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Flamin’ hot, right at ya![await]"


class CLOAKEREnemy(Enemy):
    """CLOAKER enemy class"""
    _monster_id: int = 221
    _name: str = "CLOAKER"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I love cold hard steel![await]"


class DOMINOEnemy(Enemy):
    """DOMINO enemy class"""
    _monster_id: int = 222
    _name: str = "DOMINO"

    _hp: int = 900
    _fp: int = 250
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " MAGIC! DEAL with it![await]"


class MADADDEREnemy(Enemy):
    """MAD ADDER enemy class"""
    _monster_id: int = 223
    _name: str = "MAD ADDER"

    _hp: int = 1500
    _fp: int = 250
    _attack: int = 150
    _defense: int = 70
    _magic_attack: int = 90
    _magic_defense: int = 180
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 200
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 10
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m alive and kicking.[await]"


class MACKEnemy(Enemy):
    """MACK enemy class"""
    _monster_id: int = 224
    _name: str = "MACK"

    _hp: int = 480
    _fp: int = 28
    _attack: int = 22
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 24
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Boing, boing, boing.[await]"

    _remake_name = "CLAYMORTON"


class BODYGUARDEnemy(Enemy):
    """BODYGUARD enemy class"""
    _monster_id: int = 225
    _name: str = "BODYGUARD"

    _hp: int = 30
    _fp: int = 3
    _attack: int = 20
    _defense: int = 22
    _magic_attack: int = 19
    _magic_defense: int = 12
    _speed: int = 15
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"


class YARIDOVICHEnemy(Enemy):
    """YARIDOVICH enemy class"""
    _monster_id: int = 226
    _name: str = "YARIDOVICH"

    _hp: int = 1500
    _fp: int = 100
    _attack: int = 125
    _defense: int = 85
    _magic_attack: int = 70
    _magic_defense: int = 75
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 120
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " My promotion’s at stake![await]"

    _remake_name = "SPEARDOVICH"


class DRILLBITEnemy(Enemy):
    """DRILL BIT enemy class"""
    _monster_id: int = 227
    _name: str = "DRILL BIT"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " This is for Yaridovich![await]"


class AXEMPINKEnemy(Enemy):
    """AXEM PINK enemy class"""
    _monster_id: int = 228
    _name: str = "AXEM PINK"

    _hp: int = 400
    _fp: int = 200
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 100
    _speed: int = 25
    _evade: int = 25
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Red, WRONG POSITION![await]"


class AXEMBLACKEnemy(Enemy):
    """AXEM BLACK enemy class"""
    _monster_id: int = 229
    _name: str = "AXEM BLACK"

    _hp: int = 550
    _fp: int = 100
    _attack: int = 140
    _defense: int = 120
    _magic_attack: int = 4
    _magic_defense: int = 40
    _speed: int = 35
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 40
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You’re timing stinks![await]"


class BOWYEREnemy(Enemy):
    """BOWYER enemy class"""
    _monster_id: int = 230
    _name: str = "BOWYER"

    _hp: int = 720
    _fp: int = 250
    _attack: int = 50
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 60
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _common_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What’s with these folks?[await]"



class RASPBERRY2Enemy(Enemy):
    """RASPBERRY enemy class"""
    _monster_id: int = 231
    _name: str = "RASPBERRY 2"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 230
    _defense: int = 110
    _magic_attack: int = 170
    _magic_defense: int = 100
    _speed: int = 97
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Grrr![await]"




class TORTE2Enemy(Enemy):
    """TORTE enemy class"""
    _monster_id: int = 232
    _name: str = "TIRED TORTE"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 50
    _magic_attack: int = 8
    _magic_defense: int = 27
    _speed: int = 99
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.TORTE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _invincible: bool = True
    _psychopath_message: str = " I'm so sleepy...[await]"


class EXOREnemy(Enemy):
    """EXOR enemy class"""
    _monster_id: int = 233
    _name: str = "EXOR"

    _hp: int = 1800
    _fp: int = 0
    _attack: int = 0
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 80
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 100
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gotta mow the lawn soon.[await]"


class SMITHY1Enemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 234
    _name: str = "SMITHY"

    _hp: int = 2000
    _fp: int = 250
    _attack: int = 230
    _defense: int = 130
    _magic_attack: int = 100
    _magic_defense: int = 100
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Eh?! Not bad![await]"


class SHYPEREnemy(Enemy):
    """SHYPER enemy class"""
    _monster_id: int = 235
    _name: str = "SHYPER"

    _hp: int = 400
    _fp: int = 30
    _attack: int = 170
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _speed: int = 42
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_FROM_FRONT
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ooh! This’ll be fun![await]"


class SMITHYBodyEnemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 236
    _name: str = "SMITHY"

    _hp: int = 1000
    _fp: int = 50
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 60
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What a heavy head![await]"


class SMITHY2Enemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 237
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 50
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 50
    _speed: int = 40
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " This isn’t good at all![await]"


class SMITHYMageEnemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 238
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 250
    _attack: int = 135
    _defense: int = 50
    _magic_attack: int = 130
    _magic_defense: int = 150
    _speed: int = 35
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Good magic, bad defense.[await]"


class SMITHYChestEnemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 239
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 250
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 78
    _magic_defense: int = 80
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 4
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What’s hidden inside?![await]"


class CROCO1Enemy(Enemy):
    """CROCO 1 enemy class"""
    _monster_id: int = 240
    _name: str = "CROCO 1"

    _hp: int = 320
    _fp: int = 12
    _attack: int = 25
    _defense: int = 25
    _magic_attack: int = 30
    _magic_defense: int = 18
    _speed: int = 16
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.MUSHROOM, Status.SCARECROW]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerTabItem
    _common_item_drop = FlowerTabItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gosh, I’m good![await]"


class CROCO2Enemy(Enemy):
    """CROCO 2 enemy class"""
    _monster_id: int = 241
    _name: str = "CROCO 2"

    _hp: int = 750
    _fp: int = 12
    _attack: int = 52
    _defense: int = 50
    _magic_attack: int = 27
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.MUSHROOM, Status.SCARECROW]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 30
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ooh! I’m good![await]"


class WINDCRYS3DEnemy(Enemy):
    """WIND CRYS 3D enemy class"""
    _monster_id: int = 242
    _name: str = "WIND CRYS 3D"

    _hp: int = 1800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 150
    _magic_attack: int = 90
    _magic_defense: int = 108
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Whooooosh...  Swoooooosh...[await]"


class EARTHLINKEnemy(Enemy):
    """EARTH LINK enemy class"""
    _monster_id: int = 243
    _name: str = "EARTH LINK"

    _hp: int = 2500
    _fp: int = 100
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 5
    _magic_defense: int = 10
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 200
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 10
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What a royal pain![await]"

    _remake_name = "BAD ADDER"


class AEROEnemy(Enemy):
    """AERO enemy class"""
    _monster_id: int = 244
    _name: str = "AERO"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 4
    _psychopath_message: str = "[await]"


class AXEMRANGERSEnemy(Enemy):
    """AXEM RANGERS enemy class"""
    _monster_id: int = 245
    _name: str = "AXEM RANGERS"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 0
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 100
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 190
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " It’s a melee![await]"

    _remake_name = "THE BLADE"


class BOOSTEREnemy(Enemy):
    """BOOSTER enemy class"""
    _monster_id: int = 246
    _name: str = "BOOSTER"

    _hp: int = 800
    _fp: int = 2
    _attack: int = 75
    _defense: int = 55
    _magic_attack: int = 1
    _magic_defense: int = 40
    _speed: int = 24
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _psychopath_message: str = " This is like realizing[await]\n you’re outside without[await]\n your clothes on![await]"


class BOOSTEREnemy2(Enemy):
    """BOOSTER enemy class"""
    _monster_id: int = 247
    _name: str = "BOOSTER 2"

    _hp: int = 3800
    _fp: int = 100
    _attack: int = 75
    _defense: int = 120
    _magic_attack: int = 1
    _magic_defense: int = 80
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I feel like I just knocked my prized[await]\n Impossible Grade model off the[await]\n shelf while cleaning it.[await]"

class SNIFITEnemyStatic(Enemy):
    """SNIFIT enemy class to not interfere with overworld enemy in tower, etc"""
    _monster_id: int = 248
    _name: str = "SNIFIT"

    _hp: int = 200
    _fp: int = 32
    _attack: int = 60
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 26
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Minimum wage for THIS?![await]"

    _remake_name = "SNIFSTER"


class JOHNNYEnemy(Enemy):
    """JOHNNY enemy class"""
    _monster_id: int = 249
    _name: str = "JOHNNY"

    _hp: int = 820
    _fp: int = 100
    _attack: int = 85
    _defense: int = 80
    _magic_attack: int = 25
    _magic_defense: int = 60
    _speed: int = 13
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 90
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Whoa! It’s all over.[await]"

class SNIFIT2Enemy(Enemy):
    """SNIFIT enemy class"""
    _monster_id: int = 250
    _name: str = "STRONG SNIFIT"

    _hp: int = 2200
    _fp: int = 100
    _attack: int = 220
    _defense: int = 100
    _magic_attack: int = 180
    _magic_defense: int = 60
    _speed: int = 26
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " I don't get enough paid vacation.[await]\n I should get to cash it out[await]\n at the end of the year![await]"

    _remake_name = "SNIFSTER S"


class VALENTINAEnemy(Enemy):
    """VALENTINA enemy class"""
    _monster_id: int = 251
    _name: str = "VALENTINA"

    _hp: int = 2000
    _fp: int = 250
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 60
    _speed: int = 200
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 120
    _coins: int = 200
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLOW_DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I tell ya, he’s NOTHING![await]"


class CLOAKEREnemy2(Enemy):
    """CLOAKER enemy class"""
    _monster_id: int = 252
    _name: str = "CLOAKER"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 260
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I can’t think straight![await]"


class DOMINOEnemy2(Enemy):
    """DOMINO enemy class"""
    _monster_id: int = 253
    _name: str = "DOMINO"

    _hp: int = 900
    _fp: int = 250
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 260
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Sh...sho...shocked![await]"


class CANDLEEnemy(Enemy):
    """CANDLE enemy class"""
    _monster_id: int = 254
    _name: str = "CANDLE"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _psychopath_message: str = "[await]"


class CULEXEnemy(Enemy):
    """CULEX enemy class"""
    _monster_id: int = 255
    _name: str = "CULEX"

    _hp: int = 4096
    _fp: int = 200
    _attack: int = 250
    _defense: int = 100
    _magic_attack: int = 100
    _magic_defense: int = 80
    _speed: int = 50
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 600
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 1
    _cursor_x: int = 6
    _cursor_y: int = 7
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " A little off, eh?[await]"

# Enemy collection with all enemies instantiated in order of monster_id
ENEMIES = EnemyCollection([
    TERRAPINEnemy(),  # monster_id: 0
    SPIKEYEnemy(),  # monster_id: 1
    SKYTROOPAEnemy(),  # monster_id: 2
    MADMALLETEnemyStatic(),  # monster_id: 3
    SHAMANEnemy(),  # monster_id: 4
    CROOKEnemyStatic(),  # monster_id: 5
    GOOMBAEnemy(),  # monster_id: 6
    PIRANHAPLANTEnemyStatic(),  # monster_id: 7
    AMANITAEnemy(),  # monster_id: 8
    GOBYEnemy(),  # monster_id: 9
    BLOOBEREnemyStatic(),  # monster_id: 10
    BANDANAREDEnemy(),  # monster_id: 11
    LAKITUEnemy(),  # monster_id: 12
    BIRDYEnemyStatic(),  # monster_id: 13
    PINWHEELEnemy(),  # monster_id: 14
    RATFUNKEnemy(),  # monster_id: 15
    K9Enemy(),  # monster_id: 16
    MAGMITEEnemy(),  # monster_id: 17
    THEBIGBOOEnemy(),  # monster_id: 18
    DRYBONESEnemy(),  # monster_id: 19
    GREAPEREnemy(),  # monster_id: 20
    SPARKYEnemy(),  # monster_id: 21
    CHOMPEnemy(),  # monster_id: 22
    PANDORITEEnemy(),  # monster_id: 23
    SHYRANGEREnemy(),  # monster_id: 24
    BOBOMBEnemyStatic(),  # monster_id: 25
    SPOOKUMEnemy(),  # monster_id: 26
    HAMMERBROEnemy(),  # monster_id: 27
    BUZZEREnemy(),  # monster_id: 28
    AMEBOIDEnemy(),  # monster_id: 29
    GECKOEnemy(),  # monster_id: 30
    WIGGLEREnemy(),  # monster_id: 31
    CRUSTYEnemy(),  # monster_id: 32
    KAMEKEnemy(),  # monster_id: 33
    LEUKOEnemy(),  # monster_id: 34
    JAWFULEnemy(),  # monster_id: 35
    ENIGMAEnemy(),  # monster_id: 36
    BLASTEREnemy(),  # monster_id: 37
    GUERRILLAEnemy(),  # monster_id: 38
    BIRDYEnemyHenchman(),  # monster_id: 39
    HOBGOBLINEnemy(),  # monster_id: 40
    REACHEREnemy(),  # monster_id: 41
    SHOGUNEnemy(),  # monster_id: 42
    ORBUSEREnemy(),  # monster_id: 43
    HEAVYTROOPAEnemy(),  # monster_id: 44
    SHADOWEnemy(),  # monster_id: 45
    CLUSTEREnemy(),  # monster_id: 46
    BAHAMUTTEnemy(),  # monster_id: 47
    OCTOLOTEnemy(),  # monster_id: 48
    FROGOGEnemy(),  # monster_id: 49
    CLERKEnemy(),  # monster_id: 50
    GUNYOLKEnemy(),  # monster_id: 51
    BOOMEREnemy(),  # monster_id: 52
    REMOCONEnemy(),  # monster_id: 53
    SNAPDRAGONEnemy(),  # monster_id: 54
    STUMPETEnemy(),  # monster_id: 55
    DODOEnemy(),  # monster_id: 56
    JESTEREnemy(),  # monster_id: 57
    ARTICHOKEREnemy(),  # monster_id: 58
    ARACHNEEnemy(),  # monster_id: 59
    CARROBOSCISEnemy(),  # monster_id: 60
    HIPPOPOEnemy(),  # monster_id: 61
    MASTADOOMEnemy(),  # monster_id: 62
    CORKPEDITEEnemy(),  # monster_id: 63
    TERRACOTTAEnemy(),  # monster_id: 64
    SPIKESTEREnemy(),  # monster_id: 65
    MALAKOOPAEnemy(),  # monster_id: 66
    POUNDEREnemyStatic(),  # monster_id: 67
    POUNDETTEEnemyStatic(),  # monster_id: 68
    SACKITEnemy(),  # monster_id: 69
    GUGOOMBAEnemy(),  # monster_id: 70
    CHEWYEnemy(),  # monster_id: 71
    FIREBALLEnemy(),  # monster_id: 72
    MRKIPPEREnemy(),  # monster_id: 73
    FACTORYCHIEFEnemy(),  # monster_id: 74
    BANDANABLUEEnemy(),  # monster_id: 75
    MANAGEREnemy(),  # monster_id: 76
    BLUEBIRDEnemyStatic(),  # monster_id: 77
    GENOCLONESEnemy(),  # monster_id: 78
    ALLEYRATEnemy(),  # monster_id: 79
    CHOWEnemy(),  # monster_id: 80
    MAGMUSEnemy(),  # monster_id: 81
    LILBOOEnemy(),  # monster_id: 82
    VOMEREnemy(),  # monster_id: 83
    GLUMREAPEREnemy(),  # monster_id: 84
    PYROSPHEREEnemy(),  # monster_id: 85
    CHOMPCHOMPEnemy(),  # monster_id: 86
    HIDONEnemy(),  # monster_id: 87
    SLINGSHYEnemy(),  # monster_id: 88
    ROBOMBEnemy(),  # monster_id: 89
    SHYGUYEnemyStatic(),  # monster_id: 90
    NINJAEnemy(),  # monster_id: 91
    STINGEREnemy(),  # monster_id: 92
    GOOMBETTEEnemy(),  # monster_id: 93
    GECKITEnemy(),  # monster_id: 94
    JABITEnemy(),  # monster_id: 95
    STARCRUSTEREnemy(),  # monster_id: 96
    TeamGaugeEnemy(),  # monster_id: 97
    MUCKLEEnemy(),  # monster_id: 98
    FORKIESEnemy(),  # monster_id: 99
    GORGONEnemy(),  # monster_id: 100
    BIGBERTHAEnemy(),  # monster_id: 101
    CHAINEDKONGEnemy(),  # monster_id: 102
    FAUTSOEnemy(),  # monster_id: 103
    STRAWHEADEnemy(),  # monster_id: 104
    BLUEBIRDEnemyHenchman(),  # monster_id: 105
    ARMOREDANTEnemy(),  # monster_id: 106
    ORBISONEnemy(),  # monster_id: 107
    TUBOTROOPAEnemy(),  # monster_id: 108
    DOPPELEnemy(),  # monster_id: 109
    PULSAREnemy(),  # monster_id: 110
    BOBOMBEnemyHenchman(),  # monster_id: 111
    OCTOVADEREnemy(),  # monster_id: 112
    RIBBITEEnemy(),  # monster_id: 113
    DIRECTOREnemy(),  # monster_id: 114
    SNIFITEnemyHenchman(),  # monster_id: 115
    POUNDEREnemyHenchman(),  # monster_id: 116
    PUPPOXEnemy(),  # monster_id: 117
    FINKFLOWEREnemy(),  # monster_id: 118
    CROOKEnemyHenchman(),  # monster_id: 119
    SPRINGEREnemy(),  # monster_id: 120
    APPRENTICEEnemyHenchman(),  # monster_id: 121
    KRIFFIDEnemy(),  # monster_id: 122
    SPINTHRAEnemy(),  # monster_id: 123
    BANDANAREDEnemyHenchman(),  # monster_id: 124
    BOWSERCOPYSEnemy(),  # monster_id: 125
    BLOOBEREnemyHenchman(),  # monster_id: 126
    BOOSTERDUMMY(),  # monster_id: 127
    APPRENTICEEnemyStatic(),  # monster_id: 128
    TOADSTOOL3Enemy(),  # monster_id: 129
    PIRANHAPLANTEnemyHenchman(),  # monster_id: 130
    MARIOCLONESEnemy(),  # monster_id: 131
    POUNDETTEEnemyHenchman(),  # monster_id: 132
    MADMALLETEnemyHenchman(),  # monster_id: 133
    BOXBOYEnemy(),  # monster_id: 134
    SHELLYEnemy(),  # monster_id: 135
    PUNCHINELLO2Enemy(),  # monster_id: 136
    DODOEnemySolo(),  # monster_id: 137
    OERLIKONEnemy(),  # monster_id: 138
    CHESTEREnemy(),  # monster_id: 139
    BODYEnemy(),  # monster_id: 140
    STRONGBOBOMB1Enemy(),  # monster_id: 141
    TORTEEnemy(),  # monster_id: 142
    SHYAWAYEnemy(),  # monster_id: 143
    JINXCLONEEnemy(),  # monster_id: 144
    MACHINEMADEBodyguardEnemy(),  # monster_id: 145
    MACHINEMADEDrillbitEnemy(),  # monster_id: 146
    FORMLESSEnemy(),  # monster_id: 147
    MOKURAEnemy(),  # monster_id: 148
    FIRECRYSTALEnemy(),  # monster_id: 149
    WATERCRYSTALEnemy(),  # monster_id: 150
    EARTHCRYSTALEnemy(),  # monster_id: 151
    WINDCRYSTALEnemy(),  # monster_id: 152
    MARIOCLONEEnemy(),  # monster_id: 153
    TOADSTOOL2Enemy(),  # monster_id: 154
    BOWSERCLONEEnemy(),  # monster_id: 155
    GENOCLONEEnemy(),  # monster_id: 156
    MALLOWCLONEEnemy(),  # monster_id: 157
    SHYSTEREnemy(),  # monster_id: 158
    STRONGBOBOMB2Enemy(),  # monster_id: 159
    STRONGBOBOMB3Enemy(),  # monster_id: 160
    HANGINSHYEnemy(),  # monster_id: 161
    SMELTEREnemy(),  # monster_id: 162
    MACHINEMADEMackEnemy(),  # monster_id: 163
    MACHINEMADEBowyerEnemy(),  # monster_id: 164
    MACHINEMADEYaridovichEnemy(),  # monster_id: 165
    MACHINEMADEAxemPinkEnemy(),  # monster_id: 166
    MACHINEMADEAxemBlackEnemy(),  # monster_id: 167
    MACHINEMADEAxemRedEnemy(),  # monster_id: 168
    MACHINEMADEAxemYellowEnemy(),  # monster_id: 169
    MACHINEMADEAxemGreenEnemy(),  # monster_id: 170
    BAHAMUTTEnemy2(),  # monster_id: 171
    MALLOWCOPYSEnemy(),  # monster_id: 172
    STRONGBOBOMB4Enemy(),  # monster_id: 173
    CULEX3DEnemy(),  # monster_id: 174
    JOHNNYEnemy2(),  # monster_id: 175
    STARSLAPEnemy(),  # monster_id: 176
    MUKUMUKUEnemy(),  # monster_id: 177
    ZEOSTAREnemy(),  # monster_id: 178
    JAGGEREnemy(),  # monster_id: 179
    JINXEnemy4(),  # monster_id: 180
    SMITHYTankEnemy(),  # monster_id: 181
    SMITHYSafeEnemy2(),  # monster_id: 182
    FIRECRYS3DEnemy(),  # monster_id: 183
    MICROBOMBEnemy(),  # monster_id: 184
    WATERCRYS3DEnemy(),  # monster_id: 185
    PYROSPHEREEnemyHenchman(),  # monster_id: 186
    NEOSQUIDEnemy(),  # monster_id: 187
    YARIDOVICHMirageEnemy(),  # monster_id: 188
    HELIOEnemy(),  # monster_id: 189
    RIGHTEYEEnemy(),  # monster_id: 190
    LEFTEYEEnemy(),  # monster_id: 191
    KNIFEGUYEnemy(),  # monster_id: 192
    GRATEGUYEnemy(),  # monster_id: 193
    BUNDTEnemy(),  # monster_id: 194
    JINX1Enemy(),  # monster_id: 195
    JINX2Enemy(),  # monster_id: 196
    COUNTDOWNEnemy(),  # monster_id: 197
    DINGALINGEnemy(),  # monster_id: 198
    BELOME1Enemy(),  # monster_id: 199
    BELOME2Enemy(),  # monster_id: 200
    BELOMEEnemy3(),  # monster_id: 201
    SMILAXEnemy(),  # monster_id: 202
    EARTHCRYS3DEnemy(),  # monster_id: 203
    MEGASMILAXEnemy(),  # monster_id: 204
    BIRDETTAEnemy(),  # monster_id: 205
    EGGBERTEnemy(),  # monster_id: 206
    AXEMYELLOWEnemy(),  # monster_id: 207
    PUNCHINELLOEnemy(),  # monster_id: 208
    TENTACLESEnemy(),  # monster_id: 209
    AXEMREDEnemy(),  # monster_id: 210
    AXEMGREENEnemy(),  # monster_id: 211
    KINGBOMBEnemy(),  # monster_id: 212
    MEZZOBOMBEnemy(),  # monster_id: 213
    BUNDT2Enemy(),  # monster_id: 214
    RASPBERRYEnemy(),  # monster_id: 215
    KINGCALAMARIEnemy(),  # monster_id: 216
    TENTACLESEnemy2(),  # monster_id: 217
    JINX3Enemy(),  # monster_id: 218
    ZOMBONEEnemy(),  # monster_id: 219
    CZARDRAGONEnemy(),  # monster_id: 220
    CLOAKEREnemy(),  # monster_id: 221
    DOMINOEnemy(),  # monster_id: 222
    MADADDEREnemy(),  # monster_id: 223
    MACKEnemy(),  # monster_id: 224
    BODYGUARDEnemy(),  # monster_id: 225
    YARIDOVICHEnemy(),  # monster_id: 226
    DRILLBITEnemy(),  # monster_id: 227
    AXEMPINKEnemy(),  # monster_id: 228
    AXEMBLACKEnemy(),  # monster_id: 229
    BOWYEREnemy(),  # monster_id: 230
    RASPBERRY2Enemy(),  # monster_id: 231
    TORTE2Enemy(),  # monster_id: 232
    EXOREnemy(),  # monster_id: 233
    SMITHY1Enemy(),  # monster_id: 234
    SHYPEREnemy(),  # monster_id: 235
    SMITHYBodyEnemy(),  # monster_id: 236
    SMITHY2Enemy(),  # monster_id: 237
    SMITHYMageEnemy(),  # monster_id: 238
    SMITHYChestEnemy(),  # monster_id: 239
    CROCO1Enemy(),  # monster_id: 240
    CROCO2Enemy(),  # monster_id: 241
    WINDCRYS3DEnemy(),  # monster_id: 242
    EARTHLINKEnemy(),  # monster_id: 243
    AEROEnemy(),  # monster_id: 244
    AXEMRANGERSEnemy(),  # monster_id: 245
    BOOSTEREnemy(),  # monster_id: 246
    BOOSTEREnemy2(),  # monster_id: 247
    SNIFITEnemyStatic(),  # monster_id: 248
    JOHNNYEnemy(),  # monster_id: 249
    SNIFIT2Enemy(),  # monster_id: 250
    VALENTINAEnemy(),  # monster_id: 251
    CLOAKEREnemy2(),  # monster_id: 252
    DOMINOEnemy2(),  # monster_id: 253
    CANDLEEnemy(),  # monster_id: 254
    CULEXEnemy(),  # monster_id: 255
])
