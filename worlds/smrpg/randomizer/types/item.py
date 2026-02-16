from smrpgpatchbuilder.datatypes.items.classes import (
    Item as ItemBase,
    RegularItem as RegularItemBase,
    Weapon as WeaponBase,
    Armor as ArmorBase,
    Accessory as AccessoryBase)
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status, TempStatBuff
from .physical_objects import ItemNPC


def _add_desc_fields(fields: list[tuple[str, object, list | bool]]) -> str:
    """Helper to build description fields based on conditions.

    Args:
        fields: List of (chars, check_value, attribute) tuples where:
            - chars: Characters to add if condition is met
            - check_value: Value to check for in attribute (or True for bool check)
            - attribute: List to check membership, or bool to check directly
    """
    result = ""
    for chars, check_value, attr in fields:
        if isinstance(attr, bool):
            if attr:
                result += chars
            else:
                result += "\x99" * len(chars)
        elif isinstance(attr, (list, tuple)):
            if check_value in attr:
                result += chars
            else:
                result += "\x99" * len(chars)
    return result


class Item(ItemBase):
    _remake_name: str | None = None
    _text_shop_menu: str | None = None
    _remake_text_shop_menu: str | None = None
    
    @property
    def room_service_price(self) -> int:
        return max(2, int(self.price // 2 * 0.75))

    def text_shop_menu(self, use_remake: bool = False) -> str:
        if self._text_shop_menu is None:
            raise ValueError("not a valid shop choice")
        string: str = ""
        if use_remake and self._remake_text_shop_menu is not None:
            string = self._remake_text_shop_menu
        else:
            string = self._text_shop_menu
        if self.price < 100:
            string += "."
        if self.price < 10:
            string += "."

        return f"({string}{self.room_service_price} Coins)"

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._item_name

    def build_equipment_description(self) -> str:
        """Generate shop/menu description text for the item based on stats.

        Returns:
            Description string with special characters for game display.
        """
        if not isinstance(self, (Weapon, Armor, Accessory)):
            return ''

        desc = ''

        # Elemental immunities
        if self.elemental_immunities:
            desc += '\x96\x98'
            desc += _add_desc_fields([
                ('\x80\x98', Element.FIRE, self.elemental_immunities),
                ('\x81', Element.ICE, self.elemental_immunities),
                ('\x82', Element.THUNDER, self.elemental_immunities),
            ])
        else:
            desc += '\x99' * 4
        desc += '\x99'

        # Elemental resistances
        if self.elemental_resistances:
            desc += '\x97\x98'
            desc += _add_desc_fields([
                ('\x80\x98', Element.FIRE, self.elemental_resistances),
                ('\x81', Element.ICE, self.elemental_resistances),
                ('\x82', Element.THUNDER, self.elemental_resistances),
            ])
        else:
            desc += '\x99' * 4
        desc += '\x01'

        # Speed
        desc += ['\x93', '\x94'][self.speed < 0]
        desc += str(abs(self.speed)).ljust(3, '\x99') + '\x99'

        # Status immunities
        desc += _add_desc_fields([
            ('\x83', Status.MUTE, self.status_immunities),
            ('\x84', Status.SLEEP, self.status_immunities),
            ('\x85', Status.POISON, self.status_immunities),
            ('\x86', Status.FEAR, self.status_immunities),
            ('\x98\x87', Status.MUSHROOM, self.status_immunities),
            ('\x88', Status.SCARECROW, self.status_immunities),
            ('\x89', True, self.prevent_ko),
            ('\x8A', Status.BERSERK, self.status_immunities),
        ])
        desc += '\x01'

        # Physical attack/defense
        desc += ['\x8B', '\x8C'][self.attack < 0]
        desc += ['\x20', '\x95'][TempStatBuff.ATTACK in self.temp_buffs]
        desc += str(abs(self.attack)).ljust(3, '\x99')
        desc += '\x99'
        desc += ['\x8F', '\x90'][self.defense < 0]
        desc += ['\x20', '\x95'][TempStatBuff.DEFENSE in self.temp_buffs]
        desc += str(abs(self.defense)).ljust(3, '\x99')
        desc += '\x01'

        # Magic attack/defense
        desc += ['\x8D', '\x8E'][self.magic_attack < 0]
        desc += ['\x20', '\x95'][TempStatBuff.MAGIC_ATTACK in self.temp_buffs]
        desc += str(abs(self.magic_attack)).ljust(3, '\x99')
        desc += '\x99'
        desc += ['\x91', '\x92'][self.magic_defense < 0]
        desc += ['\x20', '\x95'][TempStatBuff.MAGIC_DEFENSE in self.temp_buffs]
        desc += str(abs(self.magic_defense)).ljust(3, '\x99')

        return desc


class Equipment(Item):
    """Base class for equipment items (weapons, armor, accessories)."""
    pass


class Weapon(WeaponBase, Equipment):
    pass


class Armor(ArmorBase, Equipment):
    pass


class Accessory(AccessoryBase, Equipment):
    pass


class RegularItem(RegularItemBase, Item):
    pass