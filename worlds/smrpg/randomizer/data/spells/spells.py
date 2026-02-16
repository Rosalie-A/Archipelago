from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.spells.enums import (
    SpellType,
    EffectType,
    Element,
    Status,
    InflictFunction,
    TempStatBuff,
)
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    BUTTON_MASH,
    CHARGE_ONLY,
    MULTIPLE_BUTTON_PRESSES,
    ONE_PLUS_MORE_TARGETS_WITH_PRESSES,
    ONE_TIMING_FOR_125_DMG_ONLY,
    ONE_TIMING_FOR_125_OR_15X_DMG,
    ROTATE_1_TARGET_IF_TIMED_ALL,
    ROTATE_ONLY,
    TIMED_FOR_9999_SET_ENEMY_HP_0,
    TIMED_GIVES_TARGET_DEFENSE_UP_BUFF,
    TIMED_HEALS_ALL_HP_TO_FIRST_TARGET,
    TIMED_JUMPS,
    TIME_TO_ACTIVATE_HP_READ,
)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    NO_MODIFIERS,
    X00625_MODIFIER,
    X00625_MODIFIER_WITH_MULTI_TARGETING,
    X0125_MODIFIER_WITH_MULTI_TARGETING,
    X05_MODIFIER,
)
from ...types.spell import CharacterSpell, EnemySpell, palette_to_bytes


class JumpSpell(CharacterSpell):
    _index = 0
    _title = "Jump"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 25
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _inflict = InflictFunction.INC_JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Stomp foes! Press "Y" just before hit!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Jump"
        elif self.element == Element.ICE:
            return "Ice Jump"
        elif self.element == Element.THUNDER:
            return "Thunder Jump"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Stomp foes with\n fire! Press "Y"\n just before hit!'
        elif self.element == Element.ICE:
            return ' Stomp foes with\n ice! Press "Y"\n just before hit!'
        elif self.element == Element.THUNDER:
            return ' Stomp foes with\n thunder! Press\n "Y" just\n before hit!'
        else:
            return self._description


class FireOrbSpell(CharacterSpell):
    _index = 1
    _title = "Fire Orb"
    _prefix = ItemPrefix.STAR
    _fp = 5
    _power = 20
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X00625_MODIFIER
    _description = ' Fire orb!\n Push "Y"\n repeatedly!'

    _remake_name = "Fireball"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Orb"
        elif self.element == Element.ICE:
            return "Ice Orb"
        elif self.element == Element.THUNDER:
            return "Thunder Orb"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Ball"
        elif self.element == Element.ICE:
            return "Ice Ball"
        elif self.element == Element.THUNDER:
            return "Thunder Ball"
        else:
            return self._remake_name or self.title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Earth orb!\n Push "Y"\n repeatedly!'
        elif self.element == Element.ICE:
            return ' Ice orb!\n Push "Y"\n repeatedly!'
        elif self.element == Element.THUNDER:
            return ' Thunder orb!\n Push "Y"\n repeatedly!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x253000 + 30 * 408
        fade = 0x253000 + 30 * 392
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x80F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x008000,
                    0x78F800,
                    0xA8F800,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0xF8F8D0,
                    0x00F8F8,
                    0x00D0F8,
                    0x00A8F8,
                    0x0080F8,
                    0x0058F8,
                    0x0028F8,
                    0x0028F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xA0F8F8,
                    0x40F8F8,
                    0x38D0F8,
                    0x30A8F8,
                    0x1850F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.THUNDER:
            d[active] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F0F8,
                    0xB8E0F8,
                    0xB0E0F8,
                    0xA0D0F8,
                    0x80D0F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        return d


class SuperJumpSpell(CharacterSpell):
    _index = 2
    _title = "Super Jump"
    _prefix = ItemPrefix.STAR
    _fp = 7
    _power = 45
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X05_MODIFIER
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire S.Jump"
        elif self.element == Element.ICE:
            return "Ice S.Jump"
        elif self.element == Element.THUNDER:
            return "Thndr S.Jump"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Push "Y"\n prior to hit for\n FIRE DAMAGE!'
        elif self.element == Element.ICE:
            return ' Push "Y"\n prior to hit for\n ICE DAMAGE!'
        elif self.element == Element.THUNDER:
            return ' Push "Y"\n prior to hit for\n THUNDER\n DAMAGE!'
        else:
            return self._description


class SuperFlameSpell(CharacterSpell):
    _index = 3
    _title = "Super Flame"
    _prefix = ItemPrefix.STAR
    _fp = 9
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X00625_MODIFIER
    _description = ' Fire blast!\n Push "Y"\n repeatedly!'

    _remake_name = "SuperFireball"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Super Earth"
        elif self.element == Element.ICE:
            return "Super Ice"
        elif self.element == Element.THUNDER:
            return "SuperThunder"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.JUMP:
            return "S. EarthBall"
        elif self.element == Element.ICE:
            return "S. Ice Ball"
        elif self.element == Element.THUNDER:
            return "S. ThndrBall"
        else:
            return self._remake_name or self.title

    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Earth blast!\n Push "Y"\n repeatedly!'
        elif self.element == Element.ICE:
            return ' Ice blast!\n Push "Y"\n repeatedly!'
        elif self.element == Element.THUNDER:
            return ' Thunder blast!\n Push "Y"\n repeatedly!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x253000 + 30 * 817
        fade = 0x253000 + 30 * 815
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x80F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x008000,
                    0x78F800,
                    0xA8F800,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0xF8F8D0,
                    0x00F8F8,
                    0x00D0F8,
                    0x00A8F8,
                    0x0080F8,
                    0x0058F8,
                    0x0028F8,
                    0x0028F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xA0F8F8,
                    0x40F8F8,
                    0x38D0F8,
                    0x30A8F8,
                    0x1850F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.THUNDER:
            d[active] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F0F8,
                    0xB8E0F8,
                    0xB0E0F8,
                    0xA0D0F8,
                    0x80D0F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        return d


class UltraJumpSpell(CharacterSpell):
    _index = 4
    _title = "Ultra Jump"
    _prefix = ItemPrefix.STAR
    _fp = 11
    _power = 65
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers = X0125_MODIFIER_WITH_MULTI_TARGETING
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire U.Jump"
        elif self.element == Element.ICE:
            return "Ice U.Jump"
        elif self.element == Element.THUNDER:
            return "Thndr U.Jump"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Push "Y"\n prior to hit for\n FIRE DAMAGE!'
        elif self.element == Element.ICE:
            return ' Push "Y"\n prior to hit for\n ICE DAMAGE!'
        elif self.element == Element.THUNDER:
            return ' Push "Y"\n prior to hit for\n THUNDER\n DAMAGE!'
        else:
            return self._description


class UltraFlameSpell(CharacterSpell):
    _index = 5
    _title = "Ultra Flame"
    _prefix = ItemPrefix.STAR
    _fp = 14
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers = X00625_MODIFIER_WITH_MULTI_TARGETING
    _description = ' Fire orbs!\n Push "Y"\n repeatedly!'

    _remake_name = "UltraFireball"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Ultra Earth"
        elif self.element == Element.ICE:
            return "Ultra Ice"
        elif self.element == Element.THUNDER:
            return "Ultra Thunder"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.JUMP:
            return "U. EarthBall"
        elif self.element == Element.ICE:
            return "U. Ice Ball"
        elif self.element == Element.THUNDER:
            return "U. ThndrBall"
        else:
            return self._remake_name or self.title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Earth orbs!\n Push "Y"\n repeatedly!'
        elif self.element == Element.ICE:
            return ' Ice orbs!\n Push "Y"\n repeatedly!'
        elif self.element == Element.THUNDER:
            return ' Thunder orbs!\n Push "Y"\n repeatedly!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x253000 + 30 * 818
        fade = 0x253000 + 30 * 816
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x80F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x008000,
                    0x78F800,
                    0xA8F800,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0xF8F8D0,
                    0x00F8F8,
                    0x00D0F8,
                    0x00A8F8,
                    0x0080F8,
                    0x0058F8,
                    0x0028F8,
                    0x0028F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xA0F8F8,
                    0x40F8F8,
                    0x38D0F8,
                    0x30A8F8,
                    0x1850F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.THUNDER:
            d[active] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F0F8,
                    0xB8E0F8,
                    0xB0E0F8,
                    0xA0D0F8,
                    0x80D0F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        return d


class TherapySpell(CharacterSpell):
    _index = 6
    _title = "Therapy"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = " Heal\n HP & status$"


class GroupHugSpell(CharacterSpell):
    _index = 7
    _title = "Group Hug"
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = " Heal group!\n HP/status$"


class SleepyTimeSpell(CharacterSpell):
    _index = 8
    _title = "Sleepy Time"
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 0
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]
    _timing_modifiers = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers = NO_MODIFIERS
    _description = " Zonk 1 or\n more foes!"


class ComeBackSpell(CharacterSpell):
    _index = 9
    _title = "Come Back"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _inflict = InflictFunction.REVIVE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = True
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_HEALS_ALL_HP_TO_FIRST_TARGET
    _damage_modifiers = NO_MODIFIERS
    _description = " Revive one...\n or more pals!"


class MuteSpell(CharacterSpell):
    _index = 10
    _title = "Mute"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 0
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE]
    _timing_modifiers = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers = NO_MODIFIERS
    _description = " Halt magic\n attack(s)!"


class PsychBombSpell(CharacterSpell):
    _index = 11
    _title = "Psych Bomb"
    _prefix = ItemPrefix.STAR
    _fp = 15
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = " Make me mad\n and...BOOM!"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Bomb"
        elif self.element == Element.ICE:
            return "Ice Bomb"
        elif self.element == Element.THUNDER:
            return "Thunder Bomb"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Make me mad\n and my earth\n bomb will go...\n BOOM!'
        elif self.element == Element.ICE:
            return ' Make me mad\n and my ice\n bomb will go...\n BOOM!'
        elif self.element == Element.THUNDER:
            return ' Make me mad\n and my thunder\n bomb will go...\n BOOM!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        d = {}
        if self.element == Element.JUMP:
            d[0x3350EC] = bytearray([0x80, 0x05, 0xA0, 0x05, 0x40, 0x06, 0xC0, 0x06, 0x60, 0x07, 0xE0, 0x07, 0x60, 0x07, 0xC0, 0x06, 0x40, 0x06, 0xA0, 0x05, 0x80, 0x05, 0x40, 0x01])
        elif self.element == Element.ICE:
            d[0x3350EA] = bytearray([0xE1, 0x7F, 0x01, 0x30, 0x01, 0x34, 0x01, 0x48, 0x01, 0x58, 0x01, 0x6C, 0x01, 0x7C, 0x01, 0x6C, 0x01, 0x58, 0x01, 0x48, 0x01, 0x34, 0x01, 0x30, 0x00, 0x28, 0xE1, 0x7F, 0xE1, 0x7F, 0xE1, 0x7F])
        elif self.element == Element.FIRE:
            d[0x3350EC] = bytearray([0x8C, 0x05, 0xAD, 0x05, 0x52, 0x06, 0xD6, 0x06, 0x7B, 0x07, 0xFF, 0x07, 0x7B, 0x07, 0xD6, 0x06, 0x52, 0x06, 0xAD, 0x05, 0x8C, 0x05, 0x4A, 0x01])
        return d


class TerrorizeSpell(CharacterSpell):
    _index = 12
    _title = "Terrorize"
    _prefix = ItemPrefix.STAR
    _fp = 6
    _power = 10
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = " Scare 'em good!"


class PoisonGasSpell(CharacterSpell):
    _index = 13
    _title = "Poison Gas"
    _prefix = ItemPrefix.STAR
    _fp = 10
    _power = 20
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.POISON]
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = " Poison foes!"


class CrusherSpell(CharacterSpell):
    _index = 14
    _title = "Crusher"
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Rock slide!\n Hit "Y" prior\n to contact!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Crusher"
        elif self.element == Element.ICE:
            return "Ice Crusher"
        elif self.element == Element.THUNDER:
            return "ThndrCrusher"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Fire rock slide!\n Hit "Y" prior\n to contact!'
        elif self.element == Element.ICE:
            return ' Ice rock slide!\n Hit "Y" prior\n to contact!'
        elif self.element == Element.THUNDER:
            return ' Thunder rock\n slide! Hit "Y"\n prior to contact!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        d = {}
        if self.element == Element.JUMP:
            d[0x3350EC] = bytearray([0x80, 0x05, 0xA0, 0x05, 0x40, 0x06, 0xC0, 0x06, 0x60, 0x07, 0xE0, 0x07, 0x60, 0x07, 0xC0, 0x06, 0x40, 0x06, 0xA0, 0x05, 0x80, 0x05, 0x40, 0x01])
        elif self.element == Element.ICE:
            d[0x3350EA] = bytearray([0xE1, 0x7F, 0x01, 0x30, 0x01, 0x34, 0x01, 0x48, 0x01, 0x58, 0x01, 0x6C, 0x01, 0x7C, 0x01, 0x6C, 0x01, 0x58, 0x01, 0x48, 0x01, 0x34, 0x01, 0x30, 0x00, 0x28, 0xE1, 0x7F, 0xE1, 0x7F, 0xE1, 0x7F])
        elif self.element == Element.FIRE:
            d[0x3350EC] = bytearray([0x8C, 0x05, 0xAD, 0x05, 0x52, 0x06, 0xD6, 0x06, 0x7B, 0x07, 0xFF, 0x07, 0x7B, 0x07, 0xD6, 0x06, 0x52, 0x06, 0xAD, 0x05, 0x8C, 0x05, 0x4A, 0x01])
        return d


class BowserCrushSpell(CharacterSpell):
    _index = 15
    _title = "Bowser Crush"
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 58
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = " Bowser's\n ultimate weapon!"

    _remake_name = "Mecha Stomp"

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Crush"
        elif self.element == Element.ICE:
            return "Ice Crush"
        elif self.element == Element.THUNDER:
            return "ThunderCrush"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Stomp"
        elif self.element == Element.ICE:
            return "Ice Stomp"
        elif self.element == Element.THUNDER:
            return "ThunderStomp"
        else:
            return self._remake_name or self.title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return " Bowser's\n ultimate fire\n weapon!"
        elif self.element == Element.ICE:
            return " Bowser's\n ultimate ice\n weapon!"
        elif self.element == Element.THUNDER:
            return " Bowser's\n ultimate thunder\n weapon!"
        else:
            return self._description
        
    # honestly cant figure out where the colour is here


class GenoBeamSpell(CharacterSpell):
    _index = 16
    _title = "Geno Beam"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hold "Y" until\n just before\n discharge!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Beam"
        elif self.element == Element.THUNDER:
            return "Thunder Beam"
        elif self.element == Element.JUMP:
            return "Earth Beam"
        else:
            return self._title

    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' A fiery beam!\n Hold "Y" until\n just before\n discharge!'
        elif self.element == Element.THUNDER:
            return ' A thunderous beam!\n Hold "Y" until\n just before\n discharge!'
        elif self.element == Element.JUMP:
            return ' Earthen beam!\n Hold "Y" until\n just before\n discharge!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        # not sure if this will actually work...
        offset = 0x251158
        d = {}
        if self.element == Element.JUMP:
            d[offset] = bytearray([0x04])
        elif self.element == Element.THUNDER:
            d[offset] = bytearray([0x03])
        elif self.element == Element.FIRE:
            d[offset] = bytearray([0x01])
        return d


class GenoBoostSpell(CharacterSpell):
    _index = 17
    _title = "Geno Boost"
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4)]
    _timing_modifiers = TIMED_GIVES_TARGET_DEFENSE_UP_BUFF
    _damage_modifiers = NO_MODIFIERS
    _description = ' Attack up!\n Push "Y" just\n before end!'


class GenoWhirlSpell(CharacterSpell):
    _index = 18
    _title = "Geno Whirl"
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 45
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_FOR_9999_SET_ENEMY_HP_0
    _damage_modifiers = NO_MODIFIERS
    _description = ' Press "Y" prior\nto contact for\ncritical hit!'


class GenoBlastSpell(CharacterSpell):
    _index = 19
    _title = "Geno Blast"
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 50
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = " Beam hits\n all foes!\n Energize!"


class GenoFlashSpell(CharacterSpell):
    _index = 20
    _title = "Geno Flash"
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = " Build power!\n Beam hits\n all foes!"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Flash"
        elif self.element == Element.ICE:
            return "Ice Flash"
        elif self.element == Element.THUNDER:
            return "ThunderFlash"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Build power!\n Earth beam hits\n all foes!'
        elif self.element == Element.ICE:
            return ' Build power!\n Ice beam hits\n all foes!'
        elif self.element == Element.THUNDER:
            return ' Build power!\n Thunder beam hits\n all foes!'
        else:
            return self._description


class ThunderboltSpell(CharacterSpell):
    _index = 21
    _title = "Thunderbolt"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 15
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hit "Y" just\n before bolt\n ends!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Bolt"
        elif self.element == Element.ICE:
            return "Ice Bolt"
        elif self.element == Element.JUMP:
            return "Earth Bolt"
        else:
            return self._title

    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Hit "Y" just\n before fire bolt\n ends!'
        elif self.element == Element.ICE:
            return ' Hit "Y" just\n before ice bolt\n ends!'
        elif self.element == Element.JUMP:
            return ' Hit "Y" just\n before earth\n bolt ends!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x33CB1F
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes([0xF01880, 0x008008, 0x00C820, 0xC0F800])
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes([0xF01880, 0x0070A0, 0x00C8C8, 0x98F8F8])
        elif self.element == Element.FIRE:
            d[active] = palette_to_bytes([0xF01880, 0x880000, 0xC86000, 0xF8B800])
        return d


class HPRainSpell(CharacterSpell):
    _index = 22
    _title = "HP Rain"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 10
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' HP renewal!\n Hit "Y" just\n before shower\n ends! '


class PsychopathSpell(CharacterSpell):
    _index = 23
    _title = "Psychopath"
    _prefix = ItemPrefix.STAR
    _fp = 1
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.SCAN
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIME_TO_ACTIVATE_HP_READ
    _damage_modifiers = NO_MODIFIERS
    _description = " See foe's HP\n and...secrets!"

    _remake_name = "Thought Peek"


class ShockerSpell(CharacterSpell):
    _index = 24
    _title = "Shocker"
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hit "Y" just\n before bolt\n ends!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Shocker"
        elif self.element == Element.ICE:
            return "Ice Shocker"
        elif self.element == Element.JUMP:
            return "EarthShocker"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:   
            return ' Hit "Y" just\n before fire bolt\n ends!'
        elif self.element == Element.ICE:
            return ' Hit "Y" just\n before ice bolt\n ends!'
        elif self.element == Element.JUMP:
            return ' Hit "Y" just\n before earth\n bolt ends!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x330BB8
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xA0F8A0,
                    0x50F850,
                    0x00F800,
                    0x00F800,
                    0x00E800,
                    0x00C800,
                    0x00A800,
                    0x008000,
                    0x007800,
                    0x004000,
                    0x004800,
                    0x002000,
                    0x001010,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xF8E0E0,
                    0xC0F8F8,
                    0xA0F8F8,
                    0x80F8F8,
                    0x60F8F8,
                    0x48F8F8,
                    0x00B0B0,
                    0x008080,
                    0x007878,
                    0x004040,
                    0x004848,
                    0x002020,
                    0x001010,
                ]
            )
        elif self.element == Element.FIRE:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xF8E0E0,
                    0xF8C0C0,
                    0xF8A0A0,
                    0xF88080,
                    0xF86060,
                    0xF84848,
                    0xB00000,
                    0x800000,
                    0x780000,
                    0x400000,
                    0x480000,
                    0x200000,
                    0x100000,
                ]
            )
        return d


class SnowySpell(CharacterSpell):
    _index = 25
    _title = "Snowy"
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = " Snowman\n fells foes!"

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Firey"
        elif self.element == Element.THUNDER:
            return "Thundery"
        elif self.element == Element.JUMP:
            return "Earthy"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:   
            return ' Fiery snowman\n fells foes!'
        elif self.element == Element.THUNDER:
            return ' Thundery\n snowman fells\n foes!'
        elif self.element == Element.JUMP:
            return ' Earthy snowman\n fells foes!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        upper = 0x33C141
        lower = 0x33C400
        d = {}
        if self.element == Element.JUMP:
            d[upper] = palette_to_bytes([0x28A000, 0x00D000, 0x00A800, 0x008000])
            d[lower] = palette_to_bytes([0x000000, 0x00D000])
        elif self.element == Element.THUNDER:
            d[upper] = palette_to_bytes([0x28A000, 0xF8F8F8, 0xC0F8F8, 0x68F8F8])
            d[lower] = palette_to_bytes([0x000000, 0xF8F8F8])
        elif self.element == Element.FIRE:
            d[upper] = palette_to_bytes([0x28A000, 0xD8B000, 0xB86000, 0x980000])
            d[lower] = palette_to_bytes([0x000000, 0xD8B000])
        return d


class StarRainSpell(CharacterSpell):
    _index = 26
    _title = "Star Rain"
    _prefix = ItemPrefix.STAR
    _fp = 14
    _power = 55
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_JUMPS
    _damage_modifiers = X00625_MODIFIER
    _description = ' Star showers!\n Hit "Y" just\n upon contact!'


class DummySpell1(EnemySpell):
    _index = 27
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell2(EnemySpell):
    _index = 28
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.INVINCIBLE]
    _boosts = [TempStatBuff(3), TempStatBuff(4), TempStatBuff(5), TempStatBuff(6)]


class DummySpell3(EnemySpell):
    _index = 29
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell4(EnemySpell):
    _index = 30
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell5(EnemySpell):
    _index = 31
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell6(EnemySpell):
    _index = 32
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell7(EnemySpell):
    _index = 33
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 15
    _power = 60
    _hit_rate = 80
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell8(EnemySpell):
    _index = 34
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell9(EnemySpell):
    _index = 35
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell10(EnemySpell):
    _index = 36
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell11(EnemySpell):
    _index = 37
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell12(EnemySpell):
    _index = 38
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell13(EnemySpell):
    _index = 39
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell14(EnemySpell):
    _index = 40
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell15(EnemySpell):
    _index = 41
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell16(EnemySpell):
    _index = 42
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell17(EnemySpell):
    _index = 43
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell18(EnemySpell):
    _index = 44
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell19(EnemySpell):
    _index = 45
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell20(EnemySpell):
    _index = 46
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell21(EnemySpell):
    _index = 47
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell22(EnemySpell):
    _index = 48
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell23(EnemySpell):
    _index = 49
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell24(EnemySpell):
    _index = 50
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell25(EnemySpell):
    _index = 51
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell26(EnemySpell):
    _index = 52
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell27(EnemySpell):
    _index = 53
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell28(EnemySpell):
    _index = 54
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell29(EnemySpell):
    _index = 55
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell30(EnemySpell):
    _index = 56
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell31(EnemySpell):
    _index = 57
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell32(EnemySpell):
    _index = 58
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell33(EnemySpell):
    _index = 59
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell34(EnemySpell):
    _index = 60
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell35(EnemySpell):
    _index = 61
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell36(EnemySpell):
    _index = 62
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell37(EnemySpell):
    _index = 63
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DrainSpell(EnemySpell):
    _index = 64
    _title = " Drain"
    _fp = 1
    _power = 4
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Hot Shot"


class LightningOrbSpell(EnemySpell):
    _index = 65
    _title = " Lightning Orb"
    _fp = 2
    _power = 8
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameSpell(EnemySpell):
    _index = 66
    _title = " Flame"
    _fp = 3
    _power = 12
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BoltSpell(EnemySpell):
    _index = 67
    _title = " Bolt"
    _fp = 4
    _power = 20
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class CrystalSpell(EnemySpell):
    _index = 68
    _title = " Crystal"
    _fp = 5
    _power = 25
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameStoneSpell(EnemySpell):
    _index = 69
    _title = " Flame Stone"
    _fp = 6
    _power = 32
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MegaDrainSpell(EnemySpell):
    _index = 70
    _title = " Mega Drain"
    _fp = 7
    _power = 40
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Fire Saber"


class WillyWispSpell(EnemySpell):
    _index = 71
    _title = " Willy Wisp"
    _fp = 8
    _power = 48
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Will-O-Wisp"


class DiamondSawSpell(EnemySpell):
    _index = 72
    _title = " Diamond Saw"
    _fp = 9
    _power = 60
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ElectroshockSpell(EnemySpell):
    _index = 73
    _title = " Electroshock"
    _fp = 10
    _power = 72
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BlastSpell(EnemySpell):
    _index = 74
    _title = " Blast"
    _fp = 11
    _power = 89
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class StormSpell(EnemySpell):
    _index = 75
    _title = " Storm"
    _fp = 12
    _power = 108
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class IceRockSpell(EnemySpell):
    _index = 76
    _title = " Ice Rock"
    _fp = 13
    _power = 130
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class EscapeSpell(EnemySpell):
    _index = 77
    _title = " Escape"
    _fp = 0
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.NO_DMG
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DarkStarSpell(EnemySpell):
    _index = 78
    _title = " Dark Star"
    _fp = 20
    _power = 160
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class RecoverSpell(EnemySpell):
    _index = 79
    _title = " Recover"
    _fp = 3
    _power = 50
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MegaRecoverSpell(EnemySpell):
    _index = 80
    _title = " Mega Recover"
    _fp = 9
    _power = 200
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameWallSpell(EnemySpell):
    _index = 81
    _title = " Flame Wall"
    _fp = 2
    _power = 8
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class StaticESpell(EnemySpell):
    _index = 82
    _title = " Static E!"
    _fp = 4
    _power = 12
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Static Elec."


class SandStormSpell(EnemySpell):
    _index = 83
    _title = " Sand Storm"
    _fp = 6
    _power = 16
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]


class BlizzardSpell(EnemySpell):
    _index = 84
    _title = " Blizzard"
    _fp = 8
    _power = 22
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DrainBeamSpell(EnemySpell):
    _index = 85
    _title = " Drain Beam"
    _fp = 10
    _power = 26
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Painspout"


class MeteorBlastSpell(EnemySpell):
    _index = 86
    _title = " Meteor Blast"
    _fp = 12
    _power = 30
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class LightBeamSpell(EnemySpell):
    _index = 87
    _title = " Light Beam"
    _fp = 13
    _power = 34
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]


class WaterBlastSpell(EnemySpell):
    _index = 88
    _title = " Water Blast"
    _fp = 14
    _power = 39
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SolidifySpell(EnemySpell):
    _index = 89
    _title = " Solidify"
    _fp = 15
    _power = 47
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class PetalBlastSpell(EnemySpell):
    _index = 90
    _title = " Petal Blast"
    _fp = 16
    _power = 40
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUSHROOM]


class AuroraFlashSpell(EnemySpell):
    _index = 91
    _title = " Aurora Flash"
    _fp = 17
    _power = 50
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]


class BoulderSpell(EnemySpell):
    _index = 92
    _title = " Boulder"
    _fp = 18
    _power = 72
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class CoronaSpell(EnemySpell):
    _index = 93
    _title = " Corona"
    _fp = 19
    _power = 88
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False

    _remake_name = " Flare"


class MeteorSwarmSpell(EnemySpell):
    _index = 94
    _title = " Meteor Swarm"
    _fp = 20
    _power = 100
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class Engine023Spell(EnemySpell):
    _index = 95
    _title = " Engine 023"
    _fp = 0
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = True
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class WeirdMushroomSpell(EnemySpell):
    _index = 96
    _title = " Weird Mushroom"
    _fp = 0
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BreakerBeamSpell(EnemySpell):
    _index = 97
    _title = " Breaker Beam"
    _fp = 15
    _power = 80
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ShredderSpell(EnemySpell):
    _index = 98
    _title = " Shredder"
    _fp = 8
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4), TempStatBuff(5), TempStatBuff(6)]


class SledgeSpell(EnemySpell):
    _index = 99
    _title = " Sledge"
    _fp = 6
    _power = 50
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SwordRainSpell(EnemySpell):
    _index = 100
    _title = " Sword Rain"
    _fp = 8
    _power = 80
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SpearRainSpell(EnemySpell):
    _index = 101
    _title = " Spear Rain"
    _fp = 5
    _power = 60
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ArrowRainSpell(EnemySpell):
    _index = 102
    _title = " Arrow Rain"
    _fp = 2
    _power = 40
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BigBangSpell(EnemySpell):
    _index = 103
    _title = " Big Bang"
    _fp = 0
    _power = 100
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell38(EnemySpell):
    _index = 104
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 10
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SCARECROW]


class DummySpell39(EnemySpell):
    _index = 105
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 82
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]


class DummySpell40(EnemySpell):
    _index = 106
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE]


class DummySpell41(EnemySpell):
    _index = 107
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.POISON]


class CakerBeamSpell(EnemySpell):
    _index = 108
    _title = " Caker Beam"
    _fp = 0
    _power = 50
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = True
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell42(EnemySpell):
    _index = 109
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell43(EnemySpell):
    _index = 110
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell44(EnemySpell):
    _index = 111
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell45(EnemySpell):
    _index = 112
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell46(EnemySpell):
    _index = 113
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell47(EnemySpell):
    _index = 114
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell48(EnemySpell):
    _index = 115
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell49(EnemySpell):
    _index = 116
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell50(EnemySpell):
    _index = 117
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell51(EnemySpell):
    _index = 118
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell52(EnemySpell):
    _index = 119
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell53(EnemySpell):
    _index = 120
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell54(EnemySpell):
    _index = 121
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell55(EnemySpell):
    _index = 122
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell56(EnemySpell):
    _index = 123
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell57(EnemySpell):
    _index = 124
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell58(EnemySpell):
    _index = 125
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell59(EnemySpell):
    _index = 126
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell60(EnemySpell):
    _index = 127
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


ALL_SPELLS = SpellCollection(
    [
        JumpSpell(),  # index: 0
        FireOrbSpell(),  # index: 1
        SuperJumpSpell(),  # index: 2
        SuperFlameSpell(),  # index: 3
        UltraJumpSpell(),  # index: 4
        UltraFlameSpell(),  # index: 5
        TherapySpell(),  # index: 6
        GroupHugSpell(),  # index: 7
        SleepyTimeSpell(),  # index: 8
        ComeBackSpell(),  # index: 9
        MuteSpell(),  # index: 10
        PsychBombSpell(),  # index: 11
        TerrorizeSpell(),  # index: 12
        PoisonGasSpell(),  # index: 13
        CrusherSpell(),  # index: 14
        BowserCrushSpell(),  # index: 15
        GenoBeamSpell(),  # index: 16
        GenoBoostSpell(),  # index: 17
        GenoWhirlSpell(),  # index: 18
        GenoBlastSpell(),  # index: 19
        GenoFlashSpell(),  # index: 20
        ThunderboltSpell(),  # index: 21
        HPRainSpell(),  # index: 22
        PsychopathSpell(),  # index: 23
        ShockerSpell(),  # index: 24
        SnowySpell(),  # index: 25
        StarRainSpell(),  # index: 26
        DrainSpell(),  # index: 64
        LightningOrbSpell(),  # index: 65
        FlameSpell(),  # index: 66
        BoltSpell(),  # index: 67
        CrystalSpell(),  # index: 68
        FlameStoneSpell(),  # index: 69
        MegaDrainSpell(),  # index: 70
        WillyWispSpell(),  # index: 71
        DiamondSawSpell(),  # index: 72
        ElectroshockSpell(),  # index: 73
        BlastSpell(),  # index: 74
        StormSpell(),  # index: 75
        IceRockSpell(),  # index: 76
        EscapeSpell(),  # index: 77
        DarkStarSpell(),  # index: 78
        RecoverSpell(),  # index: 79
        MegaRecoverSpell(),  # index: 80
        FlameWallSpell(),  # index: 81
        StaticESpell(),  # index: 82
        SandStormSpell(),  # index: 83
        BlizzardSpell(),  # index: 84
        DrainBeamSpell(),  # index: 85
        MeteorBlastSpell(),  # index: 86
        LightBeamSpell(),  # index: 87
        WaterBlastSpell(),  # index: 88
        SolidifySpell(),  # index: 89
        PetalBlastSpell(),  # index: 90
        AuroraFlashSpell(),  # index: 91
        BoulderSpell(),  # index: 92
        CoronaSpell(),  # index: 93
        MeteorSwarmSpell(),  # index: 94
        Engine023Spell(),  # index: 95
        WeirdMushroomSpell(),  # index: 96
        BreakerBeamSpell(),  # index: 97
        ShredderSpell(),  # index: 98
        SledgeSpell(),  # index: 99
        SwordRainSpell(),  # index: 100
        SpearRainSpell(),  # index: 101
        ArrowRainSpell(),  # index: 102
        BigBangSpell(),  # index: 103
        CakerBeamSpell(),  # index: 108
    ],
    additional_desc_ranges=[(0x3A1EA0, 0x3A20F0)]
)
