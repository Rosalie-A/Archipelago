"""Base classes for enemy attack data."""

from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.numbers.classes import (
    BitMapSet,
    ByteField,
    UInt4,
    UInt8,
)

from smrpgpatchbuilder.datatypes.spells.enums import TempStatBuff, Status

from .constants import ENEMY_ATTACK_BASE_ADDRESS, ENEMY_ATTACK_NAME_ADDRESS, ENEMY_ATTACK_NAME_LENGTH

class EnemyAttack:
    """Class representing an enemy attack."""

    # default instance attributes.
    _index: int = 0
    _name: str = ""
    _prefix: ItemPrefix | None = None
    _attack_level: int = 0
    _ohko: bool = False
    _damageless_flag_1: bool = False
    _hide_numbers: bool = False
    _damageless_flag_2: bool = False
    _hit_rate: int = 0
    _status_effects: list[Status] = []
    _buffs: list[TempStatBuff] = []

    @property
    def index(self) -> UInt8:
        """The enemy attack's unique index."""
        assert 0 <= self._index <= 128 or self._index == 251
        return UInt8(self._index)

    @property
    def attack_name(self) -> str:
        """The name of this attack as it appears in-game."""
        return self._name

    def set_attack_name(self, name: str) -> None:
        """Set the name of this attack."""
        self._name = name

    @property
    def prefix(self) -> ItemPrefix | None:
        """The icon prefix that appears before the attack name."""
        return self._prefix

    def set_prefix(self, prefix: ItemPrefix | None) -> None:
        """Set the icon prefix for this attack."""
        self._prefix = prefix

    @property
    def attack_level(self) -> UInt4:
        """The relative damage output of this attack."""
        return UInt4(self._attack_level)

    def set_attack_level(self, attack_level: int) -> None:
        """Set the relative damage output of this attack."""
        assert 0 <= attack_level <= 7
        self._attack_level = attack_level

    @property
    def ohko(self) -> bool:
        """If true, the attack will OHKO when not blocked."""
        return self._ohko

    def set_ohko(self, ohko: bool) -> None:
        """If true, the attack will OHKO when not blocked."""
        self._ohko = ohko

    @property
    def damageless_flag_1(self) -> bool:
        """(unknown)"""
        return self._damageless_flag_1

    def set_damageless_flag_1(self, damageless_flag_1: bool) -> None:
        """(unknown)"""
        self._damageless_flag_1 = damageless_flag_1

    @property
    def hide_numbers(self) -> bool:
        """If true, the damage output will not be displayed on contact."""
        return self._hide_numbers

    def set_hide_numbers(self, hide_numbers: bool) -> None:
        """If true, the damage output will not be displayed on contact."""
        self._hide_numbers = hide_numbers

    @property
    def damageless_flag_2(self) -> bool:
        """(unknown)"""
        return self._damageless_flag_2

    def set_damageless_flag_2(self, damageless_flag_2: bool) -> None:
        """(unknown)"""
        self._damageless_flag_2 = damageless_flag_2

    @property
    def hit_rate(self) -> UInt8:
        """The success rate of this attack (max is 255)."""
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        """Set the success rate of this attack (max is 255)."""
        UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def status_effects(self) -> list[Status]:
        """the list of status effects that are induced by this attack.
        since a party member can only have one status at a time, effectively only the
        status occupying the highest bit (referenced by stat_value) will be applied."""
        return self._status_effects

    def set_status_effects(self, status_effects: list[Status]) -> None:
        """overwrite the list of status effects that are induced by this attack.
        since a party member can only have one status at a time, effectively only the
        status occupying the highest bit (referenced by stat_value) will be applied."""
        self._status_effects = status_effects

    @property
    def buffs(self) -> list[TempStatBuff]:
        """The list of temporary buffs to be applied by this attack."""
        return self._buffs

    def set_buffs(self, buffs: list[TempStatBuff]) -> None:
        """Overwrite the list of temporary buffs to be applied by this attack."""
        self._buffs = buffs

    def __str__(self) -> str:
        return f"<{self.name}>"

    def __repr__(self) -> str:
        return str(self)

    @property
    def name(self) -> str:
        """Attack's default name"""
        return self.__class__.__name__

    def render(self) -> dict[int, bytearray]:
        """Return attack stats and name as bytearrays with their ROM addresses.

        Returns:
            dict[int, bytearray]: {stats_addr: stats_data, name_addr: name_data}
        """
        # Attack stats data
        base_addr = ENEMY_ATTACK_BASE_ADDRESS + (self.index * 4)
        data = bytearray()

        # first byte is attack level + damage type flags in a bitmap.
        attack_flags = [i for i in range(3) if self.attack_level & (1 << i)]
        if self.ohko:
            attack_flags.append(3)
        if self.damageless_flag_1:
            attack_flags.append(4)
        if self.hide_numbers:
            attack_flags.append(5)
        if self.damageless_flag_2:
            attack_flags.append(6)
        data += BitMapSet(1, attack_flags).as_bytes()

        # other bytes are hit rate, status effects, and buffs.
        data += ByteField(self.hit_rate).as_bytes()

        # Convert status effects to their spell_value integers
        status_bits = [status.spell_value for status in self.status_effects]
        data += BitMapSet(1, status_bits).as_bytes()

        # Convert buffs to their integer values
        buff_bits = [int(buff) for buff in self.buffs]
        data += BitMapSet(1, buff_bits).as_bytes()

        # Attack name data (13 bytes: optional prefix + name + padding with 0x20)
        name_addr = ENEMY_ATTACK_NAME_ADDRESS + (self.index * ENEMY_ATTACK_NAME_LENGTH)
        name_bytes = bytearray()

        # Add prefix byte if present
        if self._prefix is not None and self._prefix != ItemPrefix.NONE:
            name_bytes.append(self._prefix)

        # Encode the name
        if self._name:
            # Replace & with \x9c before encoding
            encoded_name = self._name.replace('&', '\x9c')
            name_bytes.extend(encoded_name.encode('latin-1'))

        # Pad to ENEMY_ATTACK_NAME_LENGTH bytes with spaces
        while len(name_bytes) < ENEMY_ATTACK_NAME_LENGTH:
            name_bytes.append(0x20)

        # Truncate if too long
        if len(name_bytes) > ENEMY_ATTACK_NAME_LENGTH:
            name_bytes = name_bytes[:ENEMY_ATTACK_NAME_LENGTH]

        return {
            base_addr: data,
            name_addr: name_bytes
        }

class EnemyAttackCollection:
    """Collection of enemy attacks with rendering support."""

    def __init__(self, attacks: list[EnemyAttack]):
        """Initialize the collection with a list of enemy attacks.

        Args:
            attacks: list of EnemyAttack objects

        Raises:
            ValueError: if there aren't exactly 129 attacks
        """
        if len(attacks) != 129:
            raise ValueError(
                f"EnemyAttackCollection must contain exactly 129 EnemyAttack instances, "
                f"but {len(attacks)} were found."
            )
        self.attacks = attacks

    def render(self) -> dict[int, bytearray]:
        """Render all enemy attacks.

        Returns:
            dictionary mapping ROM addresses to bytearrays
        """
        patch: dict[int, bytearray] = {}

        # Render each attack individually
        for attack in self.attacks:
            attack_patch = attack.render()
            patch.update(attack_patch)

        return patch
