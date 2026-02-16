"""Individual monster battle script command classes.
These are the building blocks of monster battle scripts."""

from copy import deepcopy
from typing import Protocol

from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack
from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status
from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt8
from smrpgpatchbuilder.datatypes.spells.classes import Spell

from smrpgpatchbuilder.utils.number import bits_to_int

from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import (
    CommandType,
    DoNothing,
    Target,
)
from smrpgpatchbuilder.datatypes.monster_scripts.ids.misc import TOTAL_ATTACKS
from .types.classes import (
    MonsterScriptCommand,
    MonsterScriptCommandNoArgs,
    MonsterScriptCommandOneTarget,
    MonsterScriptCommandOneTargetLimited,
    MonsterScriptCommandOneVar,
    UsableMonsterScriptCommand,
)

class Attack(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Issue an attack, or one of three attacks at random. Each of the three attacks do not have to be unique from each other.

    ## Lazy Shell command
        `Do 1 of 3 attacks`
        `Do 1 attack`

    ## Opcode
        `0xE0` if 3 attacks
        If only 1 attack, the opcode is the attack ID (0 to 128)

    ## Size
        4 bytes if 3 attacks
        1 byte otherwise

    Args:
        attack_1 (type[EnemyAttack] | type[DoNothing]): The first (or only) attack that can be issued by this command.
        attack_2 (type[EnemyAttack] | type[DoNothing] | None): The optional second attack that can be issued by this command.
        attack_3 (type[EnemyAttack] | type[DoNothing] | None): The optional third attack that can be issued by this command.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _attack_1: type[EnemyAttack] | type[DoNothing]
    _attack_2: type[EnemyAttack] | type[DoNothing] | None
    _attack_3: type[EnemyAttack] | type[DoNothing] | None

    @property
    def size(self) -> int:
        if self.attack_2 is None and self.attack_3 is None:
            return 1
        assert self.attack_2 is not None and self.attack_3 is not None
        return 4

    @property
    def attack_1(self) -> type[EnemyAttack] | type[DoNothing]:
        """The first (or only) attack that can be issued by this command."""
        return self._attack_1

    def set_attack_1(self, attack_1: type[EnemyAttack] | type[DoNothing]) -> None:
        """Set the first (or only) attack that can be issued by this command."""
        self.set_attacks(attack_1, self.attack_2, self.attack_3)

    @property
    def attack_2(self) -> type[EnemyAttack] | type[DoNothing] | None:
        """The optional second attack that can be issued by this command."""
        return self._attack_2

    def set_attack_2(self, attack_2: type[EnemyAttack] | type[DoNothing] | None) -> None:
        """Set the optional second attack that can be issued by this command.
        Will fail if attack_3 is None."""
        self.set_attacks(self.attack_1, attack_2, self.attack_3)

    @property
    def attack_3(self) -> type[EnemyAttack] | type[DoNothing] | None:
        """The optional third attack that can be issued by this command."""
        return self._attack_3

    def set_attack_3(self, attack_3: type[EnemyAttack] | type[DoNothing] | None) -> None:
        """Set the optional third attack that can be issued by this command.
        Will fail if attack_2 is None."""
        self.set_attacks(self.attack_1, self.attack_2, attack_3)

    def set_attacks(
        self,
        attack_1: type[EnemyAttack] | type[DoNothing],
        attack_2: type[EnemyAttack] | type[DoNothing] | None,
        attack_3: type[EnemyAttack] | type[DoNothing] | None,
    ) -> None:
        """Overwrite the attack (or three attacks) that can be issued by this command."""
        a1index = attack_1().index
        if attack_2 is None or attack_3 is None:
            assert attack_2 is None and attack_3 is None
            assert a1index <= TOTAL_ATTACKS
        else:
            assert 0 <= a1index <= TOTAL_ATTACKS or a1index == 251
        self._attack_1 = attack_1
        if attack_2 is not None:
            a2index = attack_2().index
            assert 0 <= a2index <= TOTAL_ATTACKS or a2index == 251
        self._attack_2 = attack_2
        if attack_3 is not None:
            a3index = attack_3().index
            assert 0 <= a3index <= TOTAL_ATTACKS or a3index == 251
        self._attack_3 = attack_3

    def __init__(
        self,
        attack_1: type[EnemyAttack] | type[DoNothing],
        attack_2: type[EnemyAttack] | type[DoNothing] | None = None,
        attack_3: type[EnemyAttack] | type[DoNothing] | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_attacks(
            attack_1,
            attack_2,
            attack_3,
        )

    def render(self, *args) ->bytearray:
        if self.attack_2 is None and self.attack_3 is None:
            return super().render(self.attack_1().index)
        assert self.attack_2 is not None and self.attack_3 is not None
        return super().render(
            0xE0, self.attack_1().index, self.attack_2().index, self.attack_3().index
        )

class SetTarget(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """Choose the target for the actions following this command.

    ## Lazy Shell command
        `Target set`

    ## Opcode
        `0xE2`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xE2
    _size: int = 2

    def render(self, *args) ->bytearray:
        return super().render(self.target)

class RunBattleDialog(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Run a battle dialog (by ID).

    ## Lazy Shell command
        `Run battle dialogue`

    ## Opcode
        `0xE3`

    ## Size
        2 bytes

    Args:
        dialog_id (int): The ID of the dialog to run.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xE3
    _size: int = 2

    _dialog_id: UInt8

    @property
    def dialog_id(self) -> UInt8:
        """The ID of the dialog to run."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        """Set the ID of the dialog to run."""
        self._dialog_id = UInt8(dialog_id)

    def __init__(self, dialog_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)

    def render(self, *args) ->bytearray:
        return super().render(self.dialog_id)

class RunBattleEvent(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Run a battle event by ID. It is encouraged to use battle ID constants for this.

    ## Lazy Shell command
        `Run battle event`

    ## Opcode
        `0xE5`

    ## Size
        2 bytes

    Args:
        event_id (int): The ID of the battle event to run
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xE5
    _size: int = 2

    _event_id: UInt8

    @property
    def event_id(self) -> UInt8:
        """The ID of the battle event to run"""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """Set the ID of the battle event to run.
        It is encouraged to use battle ID constants for this."""
        assert event_id <= 102
        self._event_id = UInt8(event_id)

    def __init__(self, event_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)

    def render(self, *args) ->bytearray:
        return super().render(self.event_id)

class IncreaseVarBy1(MonsterScriptCommandOneVar, UsableMonsterScriptCommand):
    """Increase the given 0x7EE00# variable by 1.

    ## Lazy Shell command
        `Memory increment`

    ## Opcode
        `0xE6 0x00`

    ## Size
        3 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xE6, 0x00])
    _size: int = 3

    def render(self, *args) ->bytearray:
        return super().render(self.render_var())

class DecreaseVarBy1(IncreaseVarBy1):
    """Decrease the given 0x7EE00X variable by 1.

    ## Lazy Shell command
        `Memory decrement`

    ## Opcode
        `0xE6 0x01`

    ## Size
        *No `_size` found*

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xE6, 0x01])

class SetVarBits(MonsterScriptCommandOneVar, UsableMonsterScriptCommand):
    """For the given 0x7EE00# variable, set bits denoted by an ordinality array.

    ## Lazy Shell command
        `Memory set bits`

    ## Opcode
        `0xE7 0x00`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        bits (list[int]): The ordinality array of bits to be set on the given variable.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xE7, 0x00])
    _size: int = 4

    _bits: set[int] = set()

    @property
    def bits(self) -> set[int]:
        """The ordinality array of bits to be set on the given variable."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Overwrite the ordinality array of bits to be set on the given variable."""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = set(bits)

    def __init__(
        self, variable: int, bits: list[int], identifier: str | None = None
    ) -> None:
        super().__init__(variable, identifier)
        self.set_bits(bits)

    def render(self, *args) ->bytearray:
        return super().render(self.render_var(), bits_to_int(list(self.bits)))

class ClearVarBits(SetVarBits):
    """For the given 0x7EE00# variable, clear bits denoted by an ordinality array.

    ## Lazy Shell command
        `Memory clear bits`

    ## Opcode
        `0xE7 0x01`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        bits (list[int]): The ordinality array of bits to be cleared on the given variable.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xE7, 0x01])
    _size: int = 4

    @property
    def bits(self) -> set[int]:
        """The ordinality array of bits to be cleared on the given variable."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: list[int]) -> None:
        """Overwrite the ordinality array of bits to be cleared on the given variable."""
        super().set_bits(bits)

    def clear_bits(self, bits: list[int]) -> None:
        """Overwrite the ordinality array of bits to be cleared on the given variable."""
        self.set_bits(bits)

class ClearVar(MonsterScriptCommandOneVar, UsableMonsterScriptCommand):
    """Set the given 0x7EE00# variable to 0.

    ## Lazy Shell command
        `Memory clear`

    ## Opcode
        `0xE8`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xE8
    _size: int = 2

    def render(self, *args) ->bytearray:
        return super().render(self.render_var())

class RemoveTarget(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """The given target will no longer be active or targetable.

    ## Lazy Shell command
        `Target remove`

    ## Opcode
        `0xEA 0x00 0x00`

    ## Size
        4 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xEA, 0x00, 0x00])
    _size: int = 4

    def render(self, *args) ->bytearray:
        return super().render(self.target)

class CallTarget(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """The given target will become active and targetable.

    ## Lazy Shell command
        `Target call`

    ## Opcode
        `0xEA 0x01 0x00`

    ## Size
        4 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xEA, 0x01, 0x00])
    _size: int = 4

    def render(self, *args) ->bytearray:
        return super().render(self.target)

class MakeInvulnerable(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """The given target will not take damage from any source.

    ## Lazy Shell command
        `Target set invincibility`

    ## Opcode
        `0xEB 0x00`

    ## Size
        3 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xEB, 0x00])
    _size: int = 3

    def render(self, *args) ->bytearray:
        return super().render(self.target)

class MakeVulnerable(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """The given target will be susceptible to damage. This reverses the effects of any previous `MakeInvulnerable` commands applied to this target.

    ## Lazy Shell command
        `Target null invincibility`

    ## Opcode
        `0xEB 0x01`

    ## Size
        3 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xEB, 0x01])
    _size: int = 3

    def render(self, *args) ->bytearray:
        return super().render(self.target)

class ExitBattle(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Abort the battle and return to the level.

    ## Lazy Shell command
        `Exit battle`

    ## Opcode
        `0xEC`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xEC

class Set7EE005ToRandomNumber(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Set a designated random number storage variable to a random number in a given range.

    ## Lazy Shell command
        `Memory = random # <`

    ## Opcode
        `0xED`

    ## Size
        2 bytes

    Args:
        upper_bound (int): The upper bound allowed on the random number range (lower bound 0).
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xED
    _size: int = 2

    _upper_bound: UInt8

    @property
    def upper_bound(self) -> UInt8:
        """The upper bound allowed on the random number range (lower bound 0).
        The upper bound is not included in the result set."""
        return self._upper_bound

    def set_upper_bound(self, upper_bound: int) -> None:
        """Set the upper bound allowed on the random number range (lower bound 0).
        The upper bound is not included in the result set."""
        self._upper_bound = UInt8(upper_bound)

    def __init__(self, upper_bound: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_upper_bound(upper_bound)

    def render(self, *args) ->bytearray:
        return super().render(self.upper_bound)

class CastSpell(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Cast an spell, or one of three spells at random. Each of the three spells do not have to be unique from each other.

    ## Lazy Shell command
        `Do 1 of 3 spells`
        `Do 1 spell`

    ## Opcode
        `0xF0`
        `0xEF`

    ## Size
        4 bytes if 3 spells
        2 bytes otherwise

    Args:
        spell_1 (type[Spell] | type[DoNothing]): The first (or only) spell that can be cast by this command.
        spell_2 (type[Spell] | type[DoNothing] | None): The optional second spell that can be cast by this command.
        spell_3 (type[Spell] | type[DoNothing] | None): The optional third spell that can be cast by this command.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _spell_1: type[Spell] | type[DoNothing]
    _spell_2: type[Spell] | type[DoNothing] | None
    _spell_3: type[Spell] | type[DoNothing] | None

    @property
    def size(self) -> int:
        if self.spell_2 is None and self.spell_3 is None:
            return 2
        assert self.spell_2 is not None and self.spell_3 is not None
        return 4

    @property
    def spell_1(self) -> type[Spell] | type[DoNothing]:
        """The first (or only) spell that can be cast by this command."""
        return self._spell_1

    def set_spell_1(self, spell_1: type[Spell] | type[DoNothing]) -> None:
        """Set the first (or only) spell that can be cast by this command."""
        self.set_spells(spell_1, self.spell_2, self.spell_3)

    @property
    def spell_2(self) -> type[Spell] | type[DoNothing] | None:
        """The optional second spell that can be cast by this command."""
        return self._spell_2

    def set_spell_2(self, spell_2: type[Spell] | type[DoNothing] | None) -> None:
        """Set the optional second spell that can be cast by this command.
        Will fail if spell_3 is None."""
        self.set_spells(self.spell_1, spell_2, self.spell_3)

    @property
    def spell_3(self) -> type[Spell] | type[DoNothing] | None:
        """The optional third spell that can be cast by this command."""
        return self._spell_3

    def set_spell_3(self, spell_3: type[Spell] | type[DoNothing] | None) -> None:
        """Set the optional third spell that can be cast by this command.
        Will fail if spell_2 is None."""
        self.set_spells(self.spell_1, self.spell_2, spell_3)

    def set_spells(
        self,
        spell_1: type[Spell] | type[DoNothing],
        spell_2: type[Spell] | type[DoNothing] | None,
        spell_3: type[Spell] | type[DoNothing] | None,
    ) -> None:
        """Overwrite the spell (or three spells) that can be cast by this command."""
        s1index = spell_1().index
        if spell_2 is None or spell_3 is None:
            assert spell_2 is None and spell_3 is None
            assert s1index <= TOTAL_ATTACKS
        else:
            assert 0 <= s1index <= TOTAL_ATTACKS or s1index == 251
        self._spell_1 = spell_1
        if spell_2 is not None:
            s2index = spell_2().index
            assert 0 <= s2index <= TOTAL_ATTACKS or s2index == 251
        self._spell_2 = spell_2
        if spell_3 is not None:
            s3index = spell_3().index
            assert 0 <= s3index <= TOTAL_ATTACKS or s3index == 251
        self._spell_3 = spell_3

    def __init__(
        self,
        spell_1: type[Spell] | type[DoNothing],
        spell_2: type[Spell] | type[DoNothing] | None = None,
        spell_3: type[Spell] | type[DoNothing] | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_spells(
            spell_1,
            spell_2,
            spell_3,
        )

    def render(self, *args) ->bytearray:
        if self.spell_2 is None and self.spell_3 is None:
            return super().render(0xEF, self.spell_1().index)
        assert self.spell_2 is not None and self.spell_3 is not None
        return super().render(
            0xF0, self.spell_1().index, self.spell_2().index, self.spell_3().index
        )

class RunObjectSequence(UsableMonsterScriptCommand, MonsterScriptCommand):
    """(unknown).

    ## Lazy Shell command
        `Run object sequence`

    ## Opcode
        `0xF1`

    ## Size
        2 bytes

    Args:
        animation_id (int): The ID of the monster behaviour to be run.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xF1
    _size: int = 2

    _animation_id: UInt8

    @property
    def animation_id(self) -> UInt8:
        """The ID of the monster behaviour to be run."""
        return self._animation_id

    def set_animation_id(self, animation_id: int) -> None:
        """Set the ID of the monster behaviour to be run."""
        assert 0 <= animation_id <= 53
        self._animation_id = UInt8(animation_id)

    def __init__(self, animation_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_animation_id(animation_id)

    def render(self, *args) ->bytearray:
        return super().render(self.animation_id)

class SetUntargetable(MonsterScriptCommandOneTargetLimited, UsableMonsterScriptCommand):
    """The target will not be targetable by any subsequent commands.

    ## Lazy Shell command
        `Target disable`

    ## Opcode
        `0xF2 0x00`

    ## Size
        3 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command (must be a monster ID or `SELF`)
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF2, 0x00])
    _size: int = 3

    def render(self, *args) ->bytearray:
        return super().render()

class SetTargetable(MonsterScriptCommandOneTargetLimited, UsableMonsterScriptCommand):
    """The target will become targetable by subsequent commands. This reverses the effects of any previous SetUntargetable commands applied to this target.

    ## Lazy Shell command
        `Target enable`

    ## Opcode
        `0xF2 0x01`

    ## Size
        3 bytes

    Args:
        target (Target): The target to be.... targeted.... by this command (must be a monster ID or `SELF`)
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF2, 0x01])
    _size: int = 3

    def render(self, *args) ->bytearray:
        return super().render()

class EnableCommand(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Enable the given party command types (Attack, Spell, Item).

    ## Lazy Shell command
        `Command enable`

    ## Opcode
        `0xF3 0x00`

    ## Size
        3 bytes

    Args:
        commands (list[CommandType]): The list of command types to be enabled by this command.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF3, 0x00])
    _size: int = 3

    _commands: list[CommandType]

    @property
    def commands(self) -> list[CommandType]:
        """The list of command types to be enabled by this command."""
        return self._commands

    def set_commands(self, commands: list[CommandType]) -> None:
        """Overwrite the list of command types to be enabled by this command."""
        assert len(commands) == len(set(commands))
        self._commands = deepcopy(commands)

    def __init__(
        self, commands: list[CommandType], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(commands)

    def render(self, *args) ->bytearray:
        byte1 = 0
        for item in self.commands:
            byte1 += 1 << int(item)
        return super().render(byte1)

class DisableCommand(EnableCommand):
    """Disable the given party command types (Attack, Spell, Item).

    ## Lazy Shell command
        `Command disable`

    ## Opcode
        `0xF3 0x01`

    ## Size
        3 bytes

    Args:
        commands (list[CommandType]): The list of command types to be disabled by this command.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF3, 0x01])
    _size: int = 3

    @property
    def commands(self) -> list[CommandType]:
        """The list of command types to be disabled by this command."""
        return super().commands

    # pylint: disable=W0246
    def set_commands(self, commands: list[CommandType]) -> None:
        """Overwrite the list of command types to be disabled by this command."""
        super().set_commands(commands)

class RemoveAllInventory(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Temporarily remove all items from party inventory.

    ## Lazy Shell command
        `Set items` (remove case)

    ## Opcode
        `0xF4 0x00 0x00 0x00`

    ## Size
        4 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF4, 0x00, 0x00, 0x00])

class RestoreInventory(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Restore all temporarily-removed items from party inventory, reversing the effects of RemoveAllInventory.

    ## Lazy Shell command
        `Set items` (restore case)

    ## Opcode
        `0xF4 0x00 0x01 0x00`

    ## Size
        4 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xF4, 0x00, 0x01, 0x00])

class IfTargetedByCommand(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by any command in a list of command types. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attacked by command`

    ## Opcode
        `0xFC 0x01`

    ## Size
        4 bytes

    Args:
        commands (list[CommandType]): The list of commands which trigger the if-block. Can only be 1 or 2 commands.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x01])
    _size: int = 4

    _commands: list[CommandType]

    @property
    def commands(self) -> list[CommandType]:
        """The list of commands which trigger the if-block."""
        return self._commands

    def set_commands(self, commands: list[CommandType]) -> None:
        """Overwrite the list of commands which trigger the if-block.
        Given commands must be unique, and there can only be one or two of them."""
        assert len(commands) == len(set(commands))
        assert len(commands) in [1, 2]
        self._commands = deepcopy(commands)

    def __init__(
        self, commands: list[CommandType], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(commands)

    def render(self, *args) ->bytearray:
        effective_commands = deepcopy(self.commands)
        byte_2 = 0
        if len(effective_commands) > 1:
            byte_2 = effective_commands[1]

        return super().render(effective_commands[0] + 2, byte_2 + 2)

class IfTargetedBySpell(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by any spell in a list of spells. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attacked by spell`

    ## Opcode
        `0xFC 0x02`

    ## Size
        4 bytes

    Args:
        spells (list[type[Spell]]): The list of spells which trigger the if-block. Can only be 1 or 2 spells.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x02])
    _size: int = 4

    _spells: list[type[Spell]]

    @property
    def spells(self) -> list[type[Spell]]:
        """The list of spells which trigger the if-block."""
        return self._spells

    def set_commands(self, spells: list[type[Spell]]) -> None:
        """Overwrite the list of spells which trigger the if-block.
        Given spells must be unique, and there can only be one or two of them."""
        assert len(spells) == len(set(spells))
        assert len(spells) in [1, 2]
        self._spells = deepcopy(spells)

    def __init__(
        self, spells: list[type[Spell]], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(spells)

    def render(self, *args) ->bytearray:
        effective_spells = deepcopy(self.spells)
        byte_2 = 0
        if len(effective_spells) > 1:
            byte_2 = effective_spells[1]().index

        return super().render(effective_spells[0]().index, byte_2)

class IfTargetedByItem(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by an item in a list of items. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attacked by item`

    ## Opcode
        `0xFC 0x03`

    ## Size
        4 bytes

    Args:
        items (list[type[Item]]): The list of items which trigger the if-block. Can only be 1 or 2 items.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x03])
    _size: int = 4

    _items: list[type[Item]]

    @property
    def items(self) -> list[type[Item]]:
        """The list of items which trigger the if-block."""
        return self._items

    def set_commands(self, items: list[type[Item]]) -> None:
        """Overwrite the list of items which trigger the if-block.
        Given items must be unique, and there can only be one or two of them."""
        assert len(items) == len(set(items))
        assert len(items) in [1, 2]
        self._items = deepcopy(items)

    def __init__(
        self, items: list[type[Item]], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(items)

    def render(self, *args) ->bytearray:
        effective_items = deepcopy(self.items)
        byte_2 = 0
        if len(effective_items) > 1:
            byte_2 = effective_items[1]().item_id

        return super().render(effective_items[0]().item_id, byte_2)

class IfTargetedByElement(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by an item in a list of items. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attacked by element`

    ## Opcode
        `0xFC 0x04`

    ## Size
        4 bytes

    Args:
        elements (list[Element]): The list of elements which trigger the if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x04])
    _size: int = 4

    _elements: list[Element]

    @property
    def elements(self) -> list[Element]:
        """The list of elements which trigger the if-block."""
        return self._elements

    def set_elements(self, elements: list[Element]) -> None:
        """Overwrite the list of elements which trigger the if-block.
        Given elements must be unique."""
        assert len(elements) == len(set(elements))
        self._elements = deepcopy(elements)

    def __init__(
        self, elements: list[Element], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_elements(elements)

    def render(self, *args) ->bytearray:
        return super().render(
            sum(element.spell_value for element in self.elements), 0x00
        )

class IfTargetedByRegularAttack(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Begin an if-block triggered by being targeted by an A-attack. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attacked`

    ## Opcode
        `0xFC 0x05 0x00 0x00`

    ## Size
        4 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x05, 0x00, 0x00])

class IfTargetHPBelow(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """Begin an if-block triggered by the target's HP falling below a certain threshold. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If target HP is below`

    ## Opcode
        `0xFC 0x06`

    ## Size
        4 bytes

    Args:
        target (Target): The target whose HP to check
        threshold (int): The HP value to fall below in order to trigger this if-block. Must be a multiple of 16.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x06])
    _size: int = 4

    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        """The HP value to fall below in order to trigger this if-block."""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """Set the HP value to fall below in order to trigger this if-block. Must be a multiple of 16."""
        assert threshold % 16 == 0
        self._threshold = UInt8(threshold)

    def __init__(
        self, target: Target, threshold: int, identifier: str | None = None
    ) -> None:
        super().__init__(target, identifier)
        self.set_threshold(threshold)

    def render(self, *args) ->bytearray:
        return super().render(self.target, self.threshold // 16)

class IfHPBelow(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by the monster's HP falling below a certain threshold. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If HP is below`

    ## Opcode
        `0xFC 0x07`

    ## Size
        4 bytes

    Args:
        threshold (int): The HP value to fall below in order to trigger this if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _size: int = 4
    _opcode = bytearray([0xFC, 0x07])

    _threshold: UInt16

    @property
    def threshold(self) -> UInt16:
        """The HP value to fall below in order to trigger this if-block."""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """Set the HP value to fall below in order to trigger this if-block."""
        self._threshold = UInt16(threshold)

    def __init__(self, threshold: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_threshold(threshold)

    def render(self, *args) ->bytearray:
        return super().render(self.threshold)

class IfTargetAfflictedBy(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """Begin an if-block triggered by the monster being afflicted by a status in a list of statuses. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If target affected by`

    ## Opcode
        `0xFC 0x08`

    ## Size
        4 bytes

    Args:
        target (Target): The target whose afflictions to check
        statuses (list[Status]): The list of statuses which trigger the if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x08])
    _size: int = 4

    _statuses: list[Status]

    @property
    def statuses(self) -> list[Status]:
        """The list of statuses which trigger the if-block."""
        return self._statuses

    def set_statuses(self, statuses: list[Status]) -> None:
        """Overwrite the list of statuses which trigger the if-block.
        Given statuses must be unique."""
        assert len(statuses) == len(set(statuses))
        self._statuses = deepcopy(statuses)

    def __init__(
        self,
        target: Target,
        statuses: list[Status],
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, identifier)
        self.set_statuses(statuses)

    def render(self, *args) ->bytearray:
        return super().render(
            self.target, bits_to_int([status.spell_value for status in self.statuses])
        )

class IfTargetNotAfflictedBy(IfTargetAfflictedBy):
    """Begin an if-block triggered by the monster not being afflicted by a status in a list of statuses. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If target not affected by`

    ## Opcode
        `0xFC 0x09`

    ## Size
        4 bytes

    Args:
        target (Target): The target whose afflictions to check
        statuses (list[Status]): The list of statuses which trigger the if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x09])

    @property
    def statuses(self) -> list[Status]:
        """The list of statuses which, if not afflicting the monster, trigger the if-block."""
        return super().statuses

    # pylint: disable=W0246
    def set_statuses(self, statuses: list[Status]) -> None:
        """Overwrite the list of statuses which, if not afflicting the monster,
        trigger the if-block.
        Given statuses must be unique."""
        super().set_statuses(statuses)

class IfTurnCounterEquals(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block triggered by the turn counter reaching a given amount. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If attack phase =`

    ## Opcode
        `0xFC 0x0A`

    ## Size
        4 bytes

    Args:
        phase (int): The number of turns which, when passed, trigger this if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x0A])
    _size: int = 4

    _phase: UInt8

    @property
    def phase(self) -> UInt8:
        """The number of turns which, when passed, trigger this if-block."""
        return self._phase

    def set_phase(self, phase: int) -> None:
        """Designate the number of turns which, when passed, trigger this if-block."""
        self._phase = UInt8(phase)

    def __init__(self, phase: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_phase(phase)

    def render(self, *args) ->bytearray:
        return super().render(self.phase, 0x00)

class IfVarLessThan(MonsterScriptCommandOneVar, UsableMonsterScriptCommand):
    """Begin an if-block triggered by a certain variable value being below a given amount. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If memory less than`

    ## Opcode
        `0xFC 0x0C`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        threshold (int): The value which, if the given variable is below it, will trigger this if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x0C])
    _size: int = 4

    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        """The value which, if the given variable is below it, will trigger this if-block."""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """Set the value which, if the given variable is below it, will trigger this if-block."""
        self._threshold = UInt8(threshold)

    def __init__(
        self,
        variable: int,
        threshold: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(variable, identifier)
        self.set_threshold(threshold)

    def render(self, *args) ->bytearray:
        return super().render(self.render_var(), self.threshold)

class IfVarEqualOrGreaterThan(IfVarLessThan):
    """Begin an if-block triggered by a certain variable value not being below a given amount. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If memory greater than`

    ## Opcode
        `0xFC 0x0D`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        threshold (int): The value which, if the given variable is above or equal to it, will trigger this if-block.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x0D])

    @property
    def threshold(self) -> UInt8:
        """The value which, if the given variable is below it, will trigger this if-block."""
        return super().threshold

    # pylint: disable=W0246
    def set_threshold(self, threshold: int) -> None:
        """Set the value which, if the given variable is below it, will trigger this if-block."""
        super().set_threshold(threshold)

class IfTargetAlive(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """Begin an if-block triggered by a certain target still being present in the battle. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If target alive`

    ## Opcode
        `0xFC 0x10 0x00`

    ## Size
        4 bytes

    Args:
        target (Target): The target whose afflictions to check
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x10, 0x00])
    _size = 4

    def render(self, *args):
        return super().render(self.target)

class IfTargetKOed(MonsterScriptCommandOneTarget, UsableMonsterScriptCommand):
    """Begin an if-block triggered by a certain target no longer being present in the battle. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If target dead`

    ## Opcode
        `0xFC 0x10 0x01`

    ## Size
        4 bytes

    Args:
        target (Target): The target whose afflictions to check
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x10, 0x01])
    _size = 4

    def render(self, *args):
        return super().render(self.target)

class IfVarBitsSet(SetVarBits):
    """Begin an if-block triggered by the given bits being set on the given variable. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If memory bits set`

    ## Opcode
        `0xFC 0x11`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        bits (list[int]): The ordinality array of bits to check on the given variable.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x11])
    _size: int = 4

    @property
    def bits(self) -> set[int]:
        """The bits which, if set on the given variable, trigger this if-block."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: list[int]) -> None:
        """Set the bits which, if set on the given variable, trigger this if-block."""
        super().set_bits(bits)

class IfVarBitsClear(ClearVarBits):
    """Begin an if-block triggered by the given bits being cleared on the given variable. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If memory bits clear`

    ## Opcode
        `0xFC 0x12`

    ## Size
        4 bytes

    Args:
        variable (int): The battle variable to check, 0x7EE000 to 0x7EE00F
        bits (list[int]): The ordinality array of bits to check on the given variable.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x12])
    _size: int = 4

    @property
    def bits(self) -> set[int]:
        """The bits which, if cleared on the given variable, trigger this if-block."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: list[int]) -> None:
        """Set the bits which, if cleared on the given variable, trigger this if-block."""
        super().set_bits(bits)

    def clear_bits(self, bits: list[int]) -> None:
        """Set the bits which, if cleared on the given variable, trigger this if-block."""
        self.set_bits(bits)

class IfCurrentlyInFormationID(UsableMonsterScriptCommand, MonsterScriptCommand):
    """Begin an if-block which this monster will only run if the player is currently in battle against the formation indicated by this command's ID. It is highly encouraged to use formation constants for this. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If in formation`

    ## Opcode
        `0xFC 0x13`

    ## Size
        4 bytes

    Args:
        formation_id (int): The formation ID which the player needs to be in battle against in order for
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x13])
    _size: int = 4

    _formation_id: UInt16

    @property
    def formation_id(self) -> UInt16:
        """The formation ID which the player needs to be in battle against in order for
        the monster to run this if-block."""
        return self._formation_id

    def set_formation_id(self, formation_id: int) -> None:
        """Set the formation ID which the player needs to be in battle against in order for
        the monster to run this if-block.
        It is highly encouraged to use formation constants for this."""
        self._formation_id = UInt16(formation_id)

    def __init__(self, formation_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_formation_id(formation_id)

    def render(self, *args) -> bytearray:
        return super().render(self.formation_id)

class IfLastMonsterStanding(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Begin an if-block triggered by the monster's turn arriving when no other monsters remain. Any following commands between this one and the next Return command will only be executed if the condition of this command is met.

    ## Lazy Shell command
        `If only one alive"`

    ## Opcode
        `0xFC 0x14 0x00 0x00`

    ## Size
        4 bytes

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray([0xFC, 0x14, 0x00, 0x00])

class Wait1Turn(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """The monster's turn ends here, and will resume on the next line after this one on its next turn.

    ## Lazy Shell command
        `Wait 1 turn"`

    ## Opcode
        `0xFD`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xFD

class Wait1TurnandRestartScript(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """The monster's turn ends here, and will resume at the beginning of its script on its next turn.

    ## Lazy Shell command
        `Wait 1 turn, return all`

    ## Opcode
        `0xFE`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xFE

class StartCounterCommands(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Begins the block of code indicating what the monster does in response to a player action that targeted it.

    ## Lazy Shell command
        (None, every monster has this by default)

    ## Opcode
        `0xFF`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = 0xFF

class UnknownCommand(MonsterScriptCommandNoArgs, UsableMonsterScriptCommand):
    """Catch-all for any unknown commands. Unlike in action/event scripts, there are no safeguards on this command.

    ## Lazy Shell command
        (This would likely register as "Do 1 attack" with an illegal value)

    ## Opcode
        (any)

    ## Size
        Usually 1 byte

    Args:
        contents (bytearray): The entire byte string that this command consists of.
        identifier (str | None): Give this command a label if you want it to be easy to find it in a script and manipulate its args, insert other commands after it, etc.
    """

    _opcode = bytearray()

    @property
    def size(self) -> int:
        assert isinstance(self._opcode, bytearray)
        return len(self._opcode)

    def __init__(self, contents: bytearray, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self._opcode = contents
