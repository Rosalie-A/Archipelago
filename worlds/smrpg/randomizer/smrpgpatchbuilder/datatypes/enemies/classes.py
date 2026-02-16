"""Base classes for enemies encountered in battle and their overworld representations."""

from copy import deepcopy

from smrpgpatchbuilder.datatypes.numbers.classes import (
    BitMapSet,
    ByteField,
    UInt16,
    UInt8,
)
from smrpgpatchbuilder.datatypes.spells.classes import Status, Element
from smrpgpatchbuilder.datatypes.items.classes import RegularItem

from .constants import (
    BASE_ENEMY_ADDRESS,
    BASE_REWARD_ADDRESS,
    FLOWER_BONUS_BASE_ADDRESS,
)

# enemy pointer table address
ENEMY_POINTER_TABLE_ADDRESS = 0x390026

# reward pointer table address
REWARD_POINTER_TABLE_ADDRESS = 0x39142A
REWARD_DATA_BANK = 0x390000  # bank for reward data pointers

# psychopath message addresses
PSYCHOPATH_POINTER_ADDRESS = 0x399FD1
PSYCHOPATH_DATA_START = 0x39A1D1
PSYCHOPATH_DATA_END = 0x39B643

# enemy name base address
ENEMY_NAME_BASE_ADDRESS = 0x3992D1

# cursor position base address
CURSOR_BASE_ADDRESS = 0x39B944

from .enums import (
    ApproachSound,
    HitSound,
    FlowerBonusType,
    CoinSprite,
    EntranceStyle,
)

class Enemy:
    """Class representing an enemy in the game."""

    # properties in lazy shell

    _monster_id: int = 0
    _name: str = ""

    # vital status
    _hp: int = 0
    _fp: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0

    # effect nullification
    _status_immunities: list[Status] = []

    # element weaknesses
    _weaknesses: list[Element] = []

    # element resistances
    _resistances: list[Element] = []

    # rewards
    _xp: int = 0
    _coins: int = 0
    _rare_item_drop: type[RegularItem] | None = None
    _common_item_drop: type[RegularItem] | None = None
    _yoshi_cookie_item: type[RegularItem]

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.NONE
    _flower_bonus_chance: int = 0

    # other properties
    _morph_chance: float = 0
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 0

    # special status
    _invincible: bool = False
    _ohko_immune: bool = False
    _disable_auto_death: bool = False
    _share_palette: bool = False

    # psychopath
    _psychopath_message: str = ""

    # cursor
    _cursor_x: int = 0
    _cursor_y: int = 0

    @property
    def monster_id(self) -> UInt8:
        """Enemy's unique index."""
        return UInt8(self._monster_id)

    @property
    def hp(self) -> UInt16:
        """The enemy's HP at the start of the fight."""
        return UInt16(self._hp)

    def set_hp(self, hp: int) -> None:
        """Set how much HP the enemy will have at the start of the fight."""
        UInt16(hp)
        self._hp = hp

    @property
    def fp(self) -> UInt8:
        """The enemy's FP at the start of the fight."""
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        """Set how much FP the enemy will have at the start of the fight."""
        UInt8(fp)
        self._fp = fp

    @property
    def attack(self) -> UInt8:
        """The enemy's base physical attack power."""
        return UInt8(self._attack)

    def set_attack(self, attack: int) -> None:
        """Set the enemy's base physical attack power."""
        UInt8(attack)
        self._attack = attack

    @property
    def defense(self) -> UInt8:
        """The enemy's base physical defense power."""
        return UInt8(self._defense)

    def set_defense(self, defense: int) -> None:
        """Set the enemy's base physical defense power."""
        UInt8(defense)
        self._defense = defense

    @property
    def magic_attack(self) -> UInt8:
        """The enemy's base magic attack power."""
        return UInt8(self._magic_attack)

    def set_magic_attack(self, magic_attack: int) -> None:
        """Set the enemy's base magic attack power."""
        UInt8(magic_attack)
        self._magic_attack = magic_attack

    @property
    def magic_defense(self) -> UInt8:
        """The enemy's base magic defense power."""
        return UInt8(self._magic_defense)

    def set_magic_defense(self, magic_defense: int) -> None:
        """Set the enemy's base magic defense power."""
        UInt8(magic_defense)
        self._magic_defense = magic_defense

    @property
    def speed(self) -> UInt8:
        """The enemy's speed."""
        return UInt8(self._speed)

    def set_speed(self, speed: int) -> None:
        """Set the enemy's speed."""
        UInt8(speed)
        self._speed = speed

    @property
    def evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a physical attack."""
        return UInt8(self._evade)

    def set_evade(self, evade: int) -> None:
        """Set the enemy's percent likelihood of evading a physical attack."""
        assert 0 <= evade <= 100
        self._evade = evade

    @property
    def magic_evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a magic attack."""
        return UInt8(self._magic_evade)

    def set_magic_evade(self, magic_evade: int) -> None:
        """Set the enemy's percent likelihood of evading a magic attack."""
        assert 0 <= magic_evade <= 100
        self._magic_evade = magic_evade

    @property
    def status_immunities(self) -> list[Status]:
        """The list of status effects that the enemy is unaffected by."""
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: list[Status]) -> None:
        """Overwrite the list of status effects that the enemy is unaffected by."""
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: Status) -> None:
        """Add a status effect that the enemy should be unaffected by."""
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: Status) -> None:
        """Remove a status effect from the list that the enemy should be unaffected by."""
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def weaknesses(self) -> list[Element]:
        """The list of elements that cause double damage to the enemy."""
        return deepcopy(self._weaknesses)

    def set_weaknesses(self, weaknesses: list[Element]) -> None:
        """Overwrite the list of elements that cause double damage to the enemy."""
        self._weaknesses = deepcopy(weaknesses)

    def append_weakness(self, element: Element) -> None:
        """Add an element that should cause double damage to the enemy."""
        if element not in self._weaknesses:
            self._weaknesses.append(element)

    def remove_weakness(self, element: Element) -> None:
        """Remove an element from the list that should cause double damage to the enemy."""
        if element in self._weaknesses:
            self._weaknesses.remove(element)

    @property
    def resistances(self) -> list[Element]:
        """The list of elements which will have their damage to the enemy reduced by 50%."""
        return deepcopy(self._resistances)

    def set_resistances(self, resistances: list[Element]) -> None:
        """overwrite the list of elements which will have their damage to the enemy reduced
        by 50%."""
        self._resistances = deepcopy(resistances)

    def append_resistance(self, element: Element) -> None:
        """Add an element which will have their damage to the enemy reduced by 50%."""
        if element not in self._resistances:
            self._resistances.append(element)

    def remove_resistance(self, element: Element) -> None:
        """remove an element from the list that will have their damage to the enemy
        reduced by 50%."""
        if element in self._resistances:
            self._resistances.remove(element)

    @property
    def xp(self) -> UInt16:
        """the amount of exp awarded by the enemy. this number is divided by the number of
        active party members you have at the start of the battle."""
        return UInt16(self._xp)

    def set_xp(self, xp: int) -> None:
        """set the amount of exp awarded by the enemy. this number is divided by the number of
        active party members you have at the start of the battle."""
        assert 0 <= xp <= 9999
        self._xp = xp

    @property
    def coins(self) -> UInt8:
        """The amount of coins rewarded by the enemy."""
        return UInt8(self._coins)

    def set_coins(self, coins: int) -> None:
        """Set the amount of coins rewarded by the enemy."""
        UInt8(coins)
        self._coins = coins

    @property
    def rare_item_drop(self) -> type[RegularItem] | None:
        """A single item that the enemy has a very small chance of dropping."""
        return self._rare_item_drop

    def set_rare_item_drop(self, rare_item_drop: type[RegularItem] | None) -> None:
        """Set the single item that the enemy has a very small chance of dropping."""
        self._rare_item_drop = rare_item_drop

    @property
    def common_item_drop(self) -> type[RegularItem] | None:
        """A single item that the enemy has a high chance of dropping."""
        return self._common_item_drop

    def set_common_item_drop(self, common_item_drop: type[RegularItem] | None) -> None:
        """Set the single item that the enemy has a high chance of dropping."""
        self._common_item_drop = common_item_drop

    @property
    def yoshi_cookie_item(self) -> type[RegularItem]:
        """The item to be granted if a Yoshi Cookie on this enemy is successful."""
        return self._yoshi_cookie_item

    def set_yoshi_cookie_item(self, yoshi_cookie_item: type[RegularItem]) -> None:
        """Set the item to be granted if a Yoshi Cookie on this enemy is successful."""
        self._yoshi_cookie_item = yoshi_cookie_item

    @property
    def flower_bonus_type(self) -> FlowerBonusType:
        """The bonus flower that is granted by defeating this enemy."""
        return self._flower_bonus_type

    def set_flower_bonus_type(self, flower_bonus_type: FlowerBonusType) -> None:
        """Set the bonus flower that is granted by defeating this enemy."""
        self._flower_bonus_type = flower_bonus_type

    @property
    def flower_bonus_chance(self) -> UInt8:
        """The percent likelihood of this enemy granting a bonus flower."""
        return UInt8(self._flower_bonus_chance)

    def set_flower_bonus_chance(self, flower_bonus_chance: int) -> None:
        """Set the percent likelihood of this enemy granting a bonus flower."""
        assert 0 <= flower_bonus_chance <= 100 and flower_bonus_chance % 10 == 0
        self._flower_bonus_chance = flower_bonus_chance

    @property
    def morph_chance(self) -> float:
        """the percent success rate that the enemy is affected by a yoshi cookie, lamb's lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        return self._morph_chance

    def set_morph_chance(self, morph_chance: float) -> None:
        """set the percent success rate that the enemy is affected by a yoshi cookie, lamb's lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        assert morph_chance in [0, 25, 75, 100]
        self._morph_chance = morph_chance

    @property
    def sound_on_hit(self) -> HitSound:
        """The sound the enemy should make when it attacks you."""
        return self._sound_on_hit

    def set_sound_on_hit(self, sound_on_hit: HitSound) -> None:
        """Set the sound the enemy should make when it attacks you."""
        self._sound_on_hit = sound_on_hit

    @property
    def sound_on_approach(self) -> ApproachSound:
        """The sound the enemy should make when it approaches you."""
        return self._sound_on_approach

    def set_sound_on_approach(self, sound_on_approach: ApproachSound) -> None:
        """Set the sound the enemy should make when it approaches you."""
        self._sound_on_approach = sound_on_approach

    @property
    def invincible(self) -> bool:
        """If true, damage taken will not reduce the enemy's HP."""
        return self._invincible

    def set_invincible(self, invincible: bool) -> None:
        """If true, damage taken will not reduce the enemy's HP."""
        self._invincible = invincible

    @property
    def ohko_immune(self) -> bool:
        """If true, the enemy is immune to a timed Geno Whirl."""
        return self._ohko_immune

    def set_ohko_immune(self, ohko_immune: bool) -> None:
        """If true, the enemy is immune to a timed Geno Whirl."""
        self._ohko_immune = ohko_immune

    @property
    def coin_sprite(self) -> CoinSprite:
        """The type of coin sprite displayed when enemy is defeated."""
        return self._coin_sprite

    def set_coin_sprite(self, coin_sprite: CoinSprite) -> None:
        """Set the type of coin sprite displayed when enemy is defeated."""
        self._coin_sprite = coin_sprite

    @property
    def entrance_style(self) -> EntranceStyle:
        """The entrance animation style of the enemy."""
        return self._entrance_style

    def set_entrance_style(self, entrance_style: EntranceStyle) -> None:
        """Set the entrance animation style of the enemy."""
        self._entrance_style = entrance_style

    @property
    def elevate(self) -> int:
        """The elevation level of the enemy (0-3)."""
        return self._elevate

    def set_elevate(self, elevate: int) -> None:
        """Set the elevation level of the enemy (must be 0, 1, 2, or 3)."""
        assert elevate in [0, 1, 2, 3], "elevate must be 0, 1, 2, or 3"
        self._elevate = elevate

    @property
    def disable_auto_death(self) -> bool:
        """If true, disable automatic death."""
        return self._disable_auto_death

    def set_disable_auto_death(self, disable_auto_death: bool) -> None:
        """Set whether to disable automatic death."""
        self._disable_auto_death = disable_auto_death

    @property
    def share_palette(self) -> bool:
        """If true, share palette with another sprite."""
        return self._share_palette

    def set_share_palette(self, share_palette: bool) -> None:
        """Set whether to share palette with another sprite."""
        self._share_palette = share_palette

    @property
    def psychopath_message(self) -> str:
        """The psychopath message for this enemy."""
        return self._psychopath_message

    def set_psychopath_message(self, psychopath_message: str) -> None:
        """Set the psychopath message for this enemy."""
        self._psychopath_message = psychopath_message

    @property
    def cursor_x(self) -> int:
        """The X position of the cursor when targeting this enemy (0-15)."""
        return self._cursor_x

    def set_cursor_x(self, cursor_x: int) -> None:
        """Set the X position of the cursor when targeting this enemy (must be 0-15)."""
        assert 0 <= cursor_x <= 15, "cursor_x must be 0-15"
        self._cursor_x = cursor_x

    @property
    def cursor_y(self) -> int:
        """The Y position of the cursor when targeting this enemy (0-15)."""
        return self._cursor_y

    def set_cursor_y(self, cursor_y: int) -> None:
        """Set the Y position of the cursor when targeting this enemy (must be 0-15)."""
        assert 0 <= cursor_y <= 15, "cursor_y must be 0-15"
        self._cursor_y = cursor_y

    @property
    def address(self):
        """The ROM address at which to begin writing properties to for this enemy."""
        return BASE_ENEMY_ADDRESS + self.monster_id * 16

    @property
    def reward_address(self):
        """The ROM address at which to begin writing reward/drop properties to for this enemy."""
        return BASE_REWARD_ADDRESS + self.monster_id * 6

    def __str__(self) -> str:
        return f"""<{self.name}
         hp: {self.hp} 
         attack: {self.attack}
         defense: {self.defense} 
         m.attack: {self.magic_attack} 
         m.defense: {self.magic_defense}>"""

    def __repr__(self) -> str:
        return str(self)

    @property
    def name(self) -> str:
        """Human readable enemy name"""
        if self._name != "":
            return self._name
        return self.__class__.__name__

    def set_name(self, name: str) -> None:
        """set the enemy's display name (must be latin-1 encodable and max 13 characters).

        args:
            name: the enemy name (max 13 characters)

        raises:
            valueerror: if name contains non-latin-1 characters or is too long
        """
        if len(name) > 13:
            raise ValueError(f"Enemy name must be 13 characters or less, got {len(name)}")
        try:
            name.encode('latin-1')
        except UnicodeEncodeError:
            raise ValueError("name contains characters not encodable in latin-1")
        self._name = name

    def render(self, enemy_address: int | None = None, reward_address: int | None = None) -> dict[int, bytearray]:
        """get data for this enemy in `{0x123456: bytearray([0x00])}` format.

        args:
            enemy_address: optional override for where to write enemy data (defaults to self.address)
            reward_address: optional override for where to write reward data (defaults to self.reward_address)
        """
        patch: dict[int, bytearray] = {}

        # use provided addresses or calculate from monster_id
        addr = enemy_address if enemy_address is not None else self.address
        reward_addr = reward_address if reward_address is not None else self.reward_address

        # main stats.
        data = bytearray()
        hp_field = ByteField(self.hp)
        hp_bytes = hp_field.as_bytes()
        data += hp_bytes
        data += ByteField(self.speed).as_bytes()
        data += ByteField(self.attack).as_bytes()
        data += ByteField(self.defense).as_bytes()
        data += ByteField(self.magic_attack).as_bytes()
        data += ByteField(self.magic_defense).as_bytes()
        data += ByteField(self.fp).as_bytes()
        data += ByteField(self.evade).as_bytes()
        data += ByteField(self.magic_evade).as_bytes()
        data += ByteField(self.disable_auto_death * 1 + self.share_palette * 2).as_bytes()
        patch[addr] = data

        # special defense bits, sound on hit is top half.
        data = bytearray()
        hit_special_defense = 1 if self.invincible else 0
        hit_special_defense |= (1 if self.ohko_immune else 0) << 1
        morph_chance: int = 0
        if self.morph_chance == 25:
            morph_chance = 1
        elif self.morph_chance == 75:
            morph_chance = 2
        elif self.morph_chance == 100:
            morph_chance = 3
        hit_special_defense |= morph_chance << 2
        hit_special_defense |= self.sound_on_hit << 4
        data.append(hit_special_defense)

        # elemental resistances.
        data += BitMapSet(
            1, [resistance.stat_value for resistance in self.resistances]
        ).as_bytes()

        # elemental weaknesses byte (top half), sound on approach is bottom half.
        weaknesses_approach = self.sound_on_approach
        for weakness in self.weaknesses:
            weaknesses_approach |= 1 << weakness.stat_value
        data.append(weaknesses_approach)

        # status immunities.
        data += BitMapSet(
            1, [immunity.stat_value for immunity in self.status_immunities]
        ).as_bytes()

        patch[addr + 11] = data

        # other properties
        data = bytearray()
        data += ByteField((self.entrance_style & 0x0F) + ((self.elevate & 0x03) << 4) + (self.coin_sprite << 6)).as_bytes()
        patch[addr + 15] = data

        # flower bonus.
        bonus_addr = FLOWER_BONUS_BASE_ADDRESS + self.monster_id
        bonus = (self.flower_bonus_chance // 10) << 4
        bonus |= self.flower_bonus_type
        patch[bonus_addr] = ByteField(bonus).as_bytes()

        yoshi_cookie_item_id = self.yoshi_cookie_item().item_id
        common_item = self.common_item_drop().item_id if self.common_item_drop else 0xFF
        rare_item = self.rare_item_drop().item_id if self.rare_item_drop else 0xFF

        # build reward data patch.
        data = bytearray()
        data += ByteField(self.xp).as_bytes()
        data += ByteField(self.coins).as_bytes()
        data += ByteField(yoshi_cookie_item_id).as_bytes()
        data += ByteField(common_item).as_bytes()
        data += ByteField(rare_item).as_bytes()
        patch[reward_addr] = data

        # name (13 bytes: name + padding with 0x20)
        name_addr = ENEMY_NAME_BASE_ADDRESS + (self.monster_id * 13)
        name_bytes = bytearray()

        # encode the name with special character replacements
        if self._name:
            for char in self._name[:13]:
                if char == '-':
                    name_bytes.append(0x7D)  # hyphen -> 0x7d
                elif char == '\u2019':  # closing quote (u+2019: ')
                    name_bytes.append(0x7E)  # closing quote -> 0x7e
                else:
                    try:
                        # encode regular latin-1 characters
                        name_bytes.extend(char.encode('latin-1'))
                    except UnicodeEncodeError:
                        # if character can't be encoded, use '?'
                        name_bytes.append(0x3F)

        # pad with spaces (0x20) to fill all 13 bytes
        while len(name_bytes) < 13:
            name_bytes.append(0x20)
        patch[name_addr] = name_bytes

        # cursor position (1 byte: cursorX in upper 4 bits, cursorY in lower 4 bits)
        cursor_addr = CURSOR_BASE_ADDRESS + self.monster_id
        cursor_byte = (self.cursor_x << 4) | self.cursor_y
        patch[cursor_addr] = bytearray([cursor_byte])

        return patch

class EnemyCollection:
    """Collection of enemies with rendering support for psychopath messages and pointer tables."""

    def __init__(self, enemies: list[Enemy]):
        """initialize the collection with a list of enemies.

        args:
            enemies: list of enemy objects (should be up to 256 enemies, indexed by monster_id)

        raises:
            valueerror: if the collection contains more than 256 enemies
        """
        if len(enemies) > 256:
            raise ValueError(
                f"EnemyCollection can contain at most 256 enemies, but {len(enemies)} were provided."
            )
        self.enemies = enemies

    def get_by_type(self, enemy_type: type[Enemy]) -> Enemy:
        """Return the enemy that matches the specified type.

        Args:
            enemy_type: The Enemy subclass to search for.

        Returns:
            The enemy instance matching the type.

        Raises:
            KeyError: If no enemy of the specified type is found.
        """
        for enemy in self.enemies:
            if type(enemy) is enemy_type:
                return enemy
        raise KeyError(f"No enemy of type {enemy_type.__name__} found in collection")

    def render(self) -> dict[int, bytearray]:
        """render all enemies including their psychopath messages and pointer table.

        returns:
            dictionary mapping rom addresses to bytearrays
        """
        patch: dict[int, bytearray] = {}

        # Render enemy and reward data at their default addresses (calculated from monster_id).
        # We MUST write to the enemy and reward pointer tables to ensure consistency.
        # The pointer table tells the game where to find each enemy's data.
        for enemy in self.enemies:
            # render enemy data at default addresses (based on monster_id)
            enemy_patch = enemy.render()
            patch.update(enemy_patch)

            # Write enemy data pointer table entry
            # Pointer table is at 0x390026, each entry is 2 bytes
            # The pointer value is the offset from 0x390000
            enemy_ptr_addr = ENEMY_POINTER_TABLE_ADDRESS + enemy.monster_id * 2
            enemy_data_offset = enemy.address - 0x390000  # Offset from bank start
            patch[enemy_ptr_addr] = bytearray([
                enemy_data_offset & 0xFF,
                (enemy_data_offset >> 8) & 0xFF
            ])

            # Write reward data pointer table entry
            # Reward pointer table is at 0x39142A, each entry is 2 bytes
            reward_ptr_addr = REWARD_POINTER_TABLE_ADDRESS + enemy.monster_id * 2
            reward_data_offset = enemy.reward_address - REWARD_DATA_BANK
            patch[reward_ptr_addr] = bytearray([
                reward_data_offset & 0xFF,
                (reward_data_offset >> 8) & 0xFF
            ])

        # now handle psychopath messages
        # Battle dialog character encoding (NO word compression like overworld dialogs)
        # These byte values are specific to SMRPG's battle text rendering
        BATTLE_CHAR_MAP: dict[str, int] = {
            # Control characters
            "\n": 0x01,
            # Standard ASCII characters that map directly
            " ": 32, "!": 33,
            "(": 40, ")": 41, ",": 44, "-": 45, ".": 46, "/": 47,
            "0": 48, "1": 49, "2": 50, "3": 51, "4": 52,
            "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,
            "?": 63,
            "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71,
            "H": 72, "I": 73, "J": 74, "K": 75, "L": 76, "M": 77, "N": 78,
            "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84, "U": 85,
            "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
            "a": 97, "b": 98, "c": 99, "d": 100, "e": 101, "f": 102, "g": 103,
            "h": 104, "i": 105, "j": 106, "k": 107, "l": 108, "m": 109, "n": 110,
            "o": 111, "p": 112, "q": 113, "r": 114, "s": 115, "t": 116, "u": 117,
            "v": 118, "w": 119, "x": 120, "y": 121, "z": 122,
            # Quote characters (remapped from ASCII)
            '"': 34,  # Opening double quote (ASCII " is 34)
            """: 34,  # Curly opening double quote
            """: 35,  # Curly closing double quote
            "'": 39,  # ASCII apostrophe -> closing single quote
            "\u2018": 38,  # Curly opening single quote
            "\u2019": 39,  # Curly closing single quote
            # Special symbols
            "♥": 36, "♪": 37,
            "•": 42, "··": 43,  # Note: •• handled specially below
            "~": 58,
            "「": 59, "」": 60, "『": 61, "』": 62,
            "©": 64,
            # Elemental/status symbols for psychopath messages
            "{": 123,   # Weakness symbol
            "|": 124,   # Resistance symbol
            "}": 125,   # Ice symbol (repurposed from ASCII })
            "~ice~": 125,
            "~fire~": 126,
            "~thunder~": 127,
            "~sleep~": 128,
            "~fear~": 129,
            "~mute~": 130,
            "~poison~": 131,
            "~ohko~": 132,
            "~jump~": 133,
            "~empty~": 141,  # Invisible placeholder (same width as element symbols)
            # Punctuation remapped to higher values
            ":": 142, ";": 143, "<": 144, ">": 145,
            "…": 146, "···": 146,  # Ellipsis
            "#": 147, "+": 148, "×": 149, "%": 150,
            "↑": 151, "→": 152, "←": 153, "*": 154, "&": 156,
        }

        def encode_battle_text(text: str) -> bytearray:
            """Encode text for battle dialogs/psychopath messages (no word compression)."""
            result = bytearray()
            i = 0
            while i < len(text):
                # Check for multi-char sequences first (longest match)
                matched = False
                for length in range(min(10, len(text) - i), 0, -1):
                    substr = text[i:i+length]
                    if substr in BATTLE_CHAR_MAP:
                        result.append(BATTLE_CHAR_MAP[substr])
                        i += length
                        matched = True
                        break
                if not matched:
                    # Unknown character - use its ordinal if in valid range, else skip
                    char_ord = ord(text[i])
                    if 32 <= char_ord <= 156:
                        result.append(char_ord)
                    i += 1
            # Trim trailing empty placeholders (141 = 0x8D)
            while result and result[-1] == 141:
                result.pop()
            # End with [await] (0x02) then null terminator (0x00)
            result.append(0x02)  # [await] - pauses for user input
            result.append(0x00)  # null terminator
            return result

        # Sort enemies by monster_id to ensure correct pointer table ordering
        sorted_enemies = sorted(self.enemies, key=lambda e: e.monster_id)

        current_data_addr = PSYCHOPATH_DATA_START
        total_message_bytes = 0

        for enemy in sorted_enemies:
            # get the psychopath message
            message = enemy.psychopath_message if enemy.psychopath_message else ""

            # encode message using battle text encoding (no compression)
            if message:
                message_bytes = encode_battle_text(message)
            else:
                # empty message, just the terminator
                message_bytes = bytearray([0x00])

            total_message_bytes += len(message_bytes)

            # calculate pointer value (16-bit address)
            pointer_value = current_data_addr & 0xFFFF

            # write pointer at the correct position based on monster_id
            pointer_addr = PSYCHOPATH_POINTER_ADDRESS + enemy.monster_id * 2
            patch[pointer_addr] = bytearray([
                pointer_value & 0xFF,
                (pointer_value >> 8) & 0xFF
            ])

            # write message to rom
            patch[current_data_addr] = message_bytes

            # move to next message address
            current_data_addr += len(message_bytes)

        # check if total message data exceeds available space
        max_message_size = PSYCHOPATH_DATA_END + 1 - PSYCHOPATH_DATA_START
        if total_message_bytes > max_message_size:
            raise ValueError(
                f"Psychopath messages total {total_message_bytes} bytes, "
                f"which exceeds the maximum allowed size of {max_message_size} bytes. "
                f"Reduce message lengths by {total_message_bytes - max_message_size} bytes."
            )

        return patch
