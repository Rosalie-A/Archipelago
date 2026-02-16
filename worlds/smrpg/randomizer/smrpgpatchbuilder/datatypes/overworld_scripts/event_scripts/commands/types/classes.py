"""Base classes supporting event script assembly."""

from typing import TYPE_CHECKING, cast
from copy import deepcopy

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
        ActionScript,
    )

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
from smrpgpatchbuilder.datatypes.items.classes import Item

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptCommand,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandWithJmps,
    ScriptCommandAnySizeMem,
    ScriptCommandShortMem,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import AreaObject
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.short_var import ShortVar
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.byte_var import ByteVar

from smrpgpatchbuilder.datatypes.numbers.classes import UInt8

class EventScriptCommand(ScriptCommand):
    """Base class for any command in an event script."""

class EventScriptCommandWithJmps(EventScriptCommand, ScriptCommandWithJmps):
    """Base class for any command in an event script that contains at least one goto."""

class EventScriptCommandNoArgs(EventScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in an event script that takes no arguments."""

class EventScriptCommandAnySizeMem(EventScriptCommand, ScriptCommandAnySizeMem):
    """base class for any command in an event script that can accept either an
    8 bit or 16 bit var."""

    def __init__(
        self, address: ByteVar | ShortVar, identifier: str | None = None
    ) -> None:
        super().__init__(address, identifier)

        if self.address == ShortVar(0x7000):
            self._size = 1
        else:
            self._size = 2

class EventScriptCommandShortMem(EventScriptCommand, ScriptCommandShortMem):
    """base class for any command in an event script that accepts only
    an 8 bit var."""

class EventScriptCommandShortAddrAndValueOnly(
    EventScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    """base class for any command in an event script that accepts
    an 8 bit var and a literal value (either a number or an item class)."""

    def __init__(
        self,
        address: ShortVar,
        value: int | type[Item],
        identifier: str | None = None,
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == ShortVar(0x7000):
            self._size = 3
        else:
            self._size = 4

class EventScriptCommandBasicShortOperation(
    EventScriptCommand, ScriptCommandBasicShortOperation
):
    """base class for any command in an event script that performs math
    on an 8 bit var."""

class EventScriptCommandActionScriptContainer(EventScriptCommand):
    """base class for commands in an event script that includes
    and runs a NPC action script."""

    _header_size: int
    _subscript: "ActionScript"

    @property
    def header_size(self) -> int:
        """the expected size of the bytes indicating information about
        the subscript before the subscript contents begin."""
        return self._header_size

    @property
    def subscript(self) -> "ActionScript":
        """The contents of the NPC action script that this command runs."""
        return self._subscript

    @property
    def size(self) -> int:
        """The length of this command as a whole."""
        return self.header_size + self.subscript.length

# Import here to avoid circular dependency at module level
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScript,
)

class Subscript(ActionScript):
    """base class for an action script to be used as typing for
    action command subscripts inside event commands. this is specifically
    intended for commands whose subscript must be 127 bytes in length or
    shorter."""

    def _insert(self, index: int, command: UsableActionScriptCommand) -> None:
        assert self.length + command.size <= 0x7F
        super()._insert(index, command)

    def set_contents(
        self, script: list[UsableActionScriptCommand] | None = None
    ) -> None:
        """Overwrite the contents of the action script command list."""
        if script is None:
            script = []
        contents_length = sum(cast(list[int], [c.size for c in script]))
        assert contents_length <= 0x7F
        super().set_contents(script)

class ActionSubcriptCommandPrototype(EventScriptCommandActionScriptContainer):
    """Base class for action queues, must be 127 bytes or less."""

    _target: AreaObject
    _sync: bool
    _subscript: Subscript = Subscript([])
    _header_size: int = 2

    @property
    def target(self) -> AreaObject:
        """The field NPC that this queue should run on."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the field NPC that this queue should run on."""
        self._target = target

    @property
    def sync(self) -> bool:
        """if false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """if false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def subscript(self) -> Subscript:
        """The collection of NPC action script commands to be run."""
        return self._subscript

    def set_subscript(self, subscript: list[UsableActionScriptCommand]) -> None:
        """Overwrite the collection of NPC action script commands to be run."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        target: AreaObject,
        sync: bool = False,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        if subscript is None:
            ss = []
        else:
            ss = deepcopy(subscript)
        self._subscript = Subscript(ss)

class ActionQueuePrototype(ActionSubcriptCommandPrototype):
    """base class for action queues, must be 127 bytes or less.
    Cannot be forcibly stopped, overall command length is shorter."""

    def render(self, *args) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(self.target, header_byte, self.subscript.render())

class StartEmbeddedActionScriptPrototype(ActionSubcriptCommandPrototype):
    """base class for action queues, must be 127 bytes or less.
    Can be forcibly stopped, overall command length is longer."""

    _prefix: UInt8
    _header_size: int = 3

    @property
    def prefix(self) -> UInt8:
        """(unknown, but must be 0xF0 or 0xF1)"""
        return self._prefix

    def set_prefix(self, prefix: int) -> None:
        """(unknown, but must be 0xF0 or 0xF1)"""
        assert prefix in [0xF0, 0xF1]
        self._prefix = UInt8(prefix)

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        sync: bool = False,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, sync, subscript, identifier)
        self.set_prefix(prefix)

    def render(self, *args) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(
            self.target, self.prefix, header_byte, self.subscript.render()
        )

class NonEmbeddedActionQueuePrototype(EventScriptCommandActionScriptContainer):
    """non-embedded action queues are commands representing code that the game
    runs as an action script instead of an event script.\n
    when assembled, these queues contain no header to indicate where they begin.
    the game understands  where these scripts are intended to begin via asm that
    exists outside of the scope of the script bank.\n"""

    _subscript: "ActionScript"
    _header_size: int = 0
    _required_offset: int = 0

    @property
    def required_offset(self) -> int:
        """The required offset of the start of the non-embedded queue relative to the start of the event."""
        return self._required_offset

    @property
    def subscript(self) -> "ActionScript":
        """The contents to be run by this queue."""
        return self._subscript

    def set_subscript(self, subscript: list[UsableActionScriptCommand]) -> None:
        """Overwrite the contents to be run by this queue."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        required_offset: int,
        subscript: list[UsableActionScriptCommand] | None,
        identifier: str | None = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(identifier)
        self._required_offset = required_offset
        self._subscript = ActionScript()
        self.set_subscript(subscript)

    def render(self, *args) -> bytearray:
        return super().render(self.subscript.render())

class UsableEventScriptCommand(EventScriptCommand):
    """subclass for commands that can actually be used in a script
    (no prototypes)."""
