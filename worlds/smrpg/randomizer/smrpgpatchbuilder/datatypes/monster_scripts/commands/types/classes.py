"""Base classes supporting monster script assembly."""

from smrpgpatchbuilder.datatypes.numbers.classes import UInt4, UInt8
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptCommand,
    ScriptCommandNoArgs,
)

from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import Target
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.targets import SELF

class MonsterScriptCommand(ScriptCommand):
    """Base class for any command in a monster's battle script."""

class MonsterScriptCommandNoArgs(MonsterScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in a monster's battle script that takes no arguments."""

class MonsterScriptCommandOneVar(MonsterScriptCommand):
    """Base class for any command in a monster's battle script that takes one 0x7EE00X variable."""

    _variable: int

    @property
    def variable(self) -> int:
        """The 0x7EE00X variable used by this command."""
        return self._variable

    def set_variable(self, variable: int) -> None:
        """Designate the 0x7EE00X variable that is to be used by this command."""
        assert 0x7EE000 <= variable <= 0x7EE00F
        self._variable = int(variable)

    def render_var(self):
        """Get the representation of this variable as a patch byte."""
        return UInt4(self.variable & 0x0F)

    def __init__(self, variable: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_variable(variable)

class MonsterScriptCommandOneTarget(MonsterScriptCommand):
    """Base class for any command in a monster's battle script that has one target."""

    _target: Target

    @property
    def target(self) -> Target:
        """The target to be.... targeted.... by this command"""
        return self._target

    def set_target(self, target: Target) -> None:
        """Designate this command's target"""
        self._target = target

    def __init__(self, target: Target, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

class MonsterScriptCommandOneTargetLimited(MonsterScriptCommand):
    """base class for any command that takes one target, where the target value can only
    fall within the range of targets beginning with monster_1_set and ending with self.
    """

    _target: Target

    @property
    def target(self) -> Target:
        """The target to be.... targeted.... by this command"""
        return self._target

    def set_target(self, target: Target) -> None:
        """Designate this command's target"""
        assert 0x13 <= target <= 0x1B
        self._target = target

    def __init__(self, target: Target, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        byte1: int
        if self.target == SELF:
            byte1 = 0
        else:
            byte1 = UInt8(self.target - 0x12)
        return super().render(byte1)

class UsableMonsterScriptCommand(MonsterScriptCommand):
    """subclass for commands that can actually be used in a script
    (no prototypes)."""
