"""Base classes supporting event script assembly."""

from copy import deepcopy
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
from typing import TypeVar, Union, overload

T = TypeVar('T', bound=UsableActionScriptCommand)
E = TypeVar('E', bound='UsableEventScriptCommand')
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    ActionQueuePrototype,
    EventScriptCommandActionScriptContainer,
    UsableEventScriptCommand,
    NonEmbeddedActionQueuePrototype,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    StopSound,
)

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids.misc import (
    TOTAL_SCRIPTS,
)
from smrpgpatchbuilder.datatypes.numbers.classes import UInt16

class EventScript(Script[UsableEventScriptCommand]):
    """Base class for a single event script, a list of script command subclasses."""

    _contents: list[UsableEventScriptCommand]

    @property
    def contents(self) -> list[UsableEventScriptCommand]:
        return self._contents

    def append(self, command: UsableEventScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: list[UsableEventScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: list[UsableEventScriptCommand] | None = None
    ) -> None:
        super().set_contents(script)

    def __init__(self, script: list[UsableEventScriptCommand] | None = None) -> None:
        if script is None:
            ss = []
        else:
            ss = deepcopy(script)
        super().__init__(ss)

    def insert_before_nth_command(
        self, index: int, command: UsableEventScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableEventScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableEventScriptCommand],
        command: UsableEventScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableEventScriptCommand],
        command: UsableEventScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableEventScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableEventScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: UsableEventScriptCommand) -> None:
        super().replace_at_index(index, content)

class EventScriptBank(ScriptBank[EventScript]):
    """base class for a collection of npc action scripts
    that should belong to the same $##xxxx bank (1e, 1f, or 20)."""

    _scripts: list[EventScript]
    _pointer_table_start: int
    _start: int
    _end: int
    _used_script_length: int

    @property
    def pointer_table_start(self) -> int:
        """The beginning address for this bank's pointer table."""
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        """Set the beginning address for this bank's pointer table."""
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        """the beginning address for this bank's scripts content, indexed by the
        pointer table."""
        return self._start

    def set_start(self, start: int) -> None:
        """set the beginning address for this bank's scripts content, indexed by the
        pointer table."""
        self._start = start

    @property
    def end(self) -> int:
        """The address at which this bank's scripts should have finished by."""
        return self._end

    def set_end(self, end: int) -> None:
        """Set the address at which this bank's scripts should have finished by."""
        self._end = end

    @property
    def script_count(self) -> UInt16:
        """The total number of scripts included in this bank."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> list[EventScript]:
        return self._scripts

    def set_contents(self, scripts: list[EventScript] | None = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: EventScript) -> None:
        assert 0 <= index < self.script_count
        super().replace_script(index, script)

    def __init__(
        self,
        pointer_table_start: int,
        start: int,
        end: int,
        scripts: list[EventScript] | None,
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        self._used_script_length = 0
        super().__init__(scripts)

    def _associate_address(
        self,
        command: UsableEventScriptCommand | UsableActionScriptCommand,
        position: int,
    ) -> int:
        key: str = command.identifier.label
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        if isinstance(command, EventScriptCommandActionScriptContainer):
            position += command.header_size
            action_command: UsableActionScriptCommand
            for action_command in command.subscript.contents:
                position = self._associate_address(action_command, position)
        else:
            position += command.size

        if position > self.end:
            raise ScriptBankTooLongException(
                f"command exceeded max bank size of {self.end:06X}: {key} @ 0x{position:06X}"
            )
        return position

    def render(self) -> bytearray:
        """Return this script set as ROM patch data."""
        position: int = self._start

        script: EventScript
        command: UsableEventScriptCommand

        # build command name and pointer table : address table
        for script_id, script in enumerate(self.scripts):
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            initial_position = position
            c = deepcopy(script.contents)
            for index, command in enumerate(script.contents):
                # if this is a non-embedded action queue, insert dummy commands to fill space before the offset it should be at
                if isinstance(command, NonEmbeddedActionQueuePrototype):
                    relative_offset: int = position - initial_position
                    if relative_offset <= command.required_offset:
                        for _ in range(command.required_offset - relative_offset):
                            c.insert(index, StopSound())
                            position += 1
                    else:
                        raise ScriptBankTooLongException(
                            f"too many commands in script {script_id} before non-embedded action queue"
                        )

                position = self._associate_address(command, position)
            script.set_contents(c)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)
            commands_with_subscripts = [
                cmd
                for cmd in script.contents
                if isinstance(cmd, EventScriptCommandActionScriptContainer)
            ]
            for command in commands_with_subscripts:
                self._populate_jumps(command.subscript)

        # finalize bytes
        for i, script in enumerate(self.scripts):
            self.script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        self._used_script_length = final_length  # Track before padding
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"event script output too long: got {final_length} expected {expected_length}"
            )
        buffer: list[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        return self.pointer_bytes + self.script_bytes

    def get_unused_range(self) -> tuple[int, int] | None:
        """Return (start, end) of unused space after render(). Returns None if fully used."""
        unused_start = self.start + self._used_script_length
        if unused_start < self.end:
            return (unused_start, self.end)
        return None


class EventScriptController:
    """Contains all event script banks. Allows lookup by identifier in any bank."""

    _banks: list[EventScriptBank]

    @property
    def banks(self) -> list[EventScriptBank]:
        """List of event script banks."""
        return self._banks

    def set_banks(self, banks: list[EventScriptBank]) -> None:
        """Overwrite the list of event script banks."""
        self._banks = banks

    def __init__(self, banks: list[EventScriptBank]):
        assert len(banks) == 3
        assert (
            len(banks[0].scripts) + len(banks[1].scripts) + len(banks[2].scripts)
            == TOTAL_SCRIPTS
        )
        self.set_banks(banks)

    @overload
    def get_command_by_identifier(self, identifier: str) -> UsableEventScriptCommand: ...
    @overload
    def get_command_by_identifier(self, identifier: str, cmd_type: type[E]) -> E: ...

    def get_command_by_identifier(
        self, identifier: str, cmd_type: type[E] | None = None
    ) -> UsableEventScriptCommand | E:
        """Get one command from any bank by identifier string.

        Args:
            identifier: The unique identifier of the command to find.
            cmd_type: Optional expected type of the command. If provided, raises
                ValueError if the command is not of this type.

        Returns:
            The command, typed as cmd_type if provided.

        Raises:
            IdentifierException: If no command with the identifier is found.
            ValueError: If cmd_type is provided and the command is not of that type.
        """
        for bank in self.banks:
            for script in bank.scripts:
                for command in script.contents:
                    if command.identifier.label == identifier:
                        if cmd_type is not None and not isinstance(command, cmd_type):
                            raise ValueError(
                                f"Command with ID {identifier} is {type(command).__name__}, "
                                f"expected {cmd_type.__name__}."
                            )
                        return command
        raise IdentifierException(f"could not find command identifier {identifier}")

    def get_subscript_command_by_identifier(
        self,
        event_cmd_id: str,
        subscript_cmd_id: str,
        cmd_type: type[T],
    ) -> T:
        """Get a command from a subscript by identifier.

        Args:
            event_cmd_id: The identifier of the event script command containing the subscript.
            subscript_cmd_id: The identifier of the command within the subscript.
            cmd_type: The expected type of the subscript command.

        Returns:
            The subscript command, typed as cmd_type.

        Raises:
            IdentifierException: If the event command is not found.
            ValueError: If the event command doesn't contain a subscript or
                       the subscript command is not of the expected type.
        """
        ev = self.get_command_by_identifier(event_cmd_id)
        if not isinstance(ev, EventScriptCommandActionScriptContainer):
            raise ValueError(
                f"Event script command with ID {event_cmd_id} does not contain a subscript."
            )
        _, subcmd = ev.subscript.get_command_by_name(subscript_cmd_id, cmd_type)
        return subcmd

    def delete_subscript_command_by_identifier(
        self,
        event_cmd_id: str,
        subscript_cmd_id: str,
    ) -> None:
        """Delete a command from a subscript by identifier.

        Args:
            event_cmd_id: The identifier of the event script command containing the subscript.
            subscript_cmd_id: The identifier of the command within the subscript to delete.

        Raises:
            IdentifierException: If the event command or subscript command is not found.
            ValueError: If the event command doesn't contain a subscript.
        """
        ev = self.get_command_by_identifier(event_cmd_id)
        if not isinstance(ev, EventScriptCommandActionScriptContainer):
            raise ValueError(
                f"Event script command with ID {event_cmd_id} does not contain a subscript."
            )
        for index, subcmd in enumerate(ev.subscript.contents):
            if subcmd.identifier.label == subscript_cmd_id:
                ev.subscript.delete_at_index(index)
                return
        raise IdentifierException(
            f"Could not find subscript command identifier {subscript_cmd_id}"
        )

    def replace_subscript_command_by_identifier(
        self,
        event_cmd_id: str,
        subscript_cmd_id: str,
        replacement: Union[UsableActionScriptCommand, list[UsableActionScriptCommand]],
    ) -> None:
        """Replace a command in a subscript with one or more new commands.

        Args:
            event_cmd_id: The identifier of the event script command containing the subscript.
            subscript_cmd_id: The identifier of the command within the subscript to replace.
            replacement: A single command or list of commands to insert in place of the old one.

        Raises:
            IdentifierException: If the event command or subscript command is not found.
            ValueError: If the event command doesn't contain a subscript.
        """
        ev = self.get_command_by_identifier(event_cmd_id)
        if not isinstance(ev, EventScriptCommandActionScriptContainer):
            raise ValueError(
                f"Event script command with ID {event_cmd_id} does not contain a subscript."
            )
        for index, subcmd in enumerate(ev.subscript.contents):
            if subcmd.identifier.label == subscript_cmd_id:
                # Delete the old command
                ev.subscript.delete_at_index(index)
                # Insert replacement(s)
                if isinstance(replacement, list):
                    for i, new_cmd in enumerate(replacement):
                        ev.subscript.insert_before_nth_command(index + i, new_cmd)
                else:
                    ev.subscript.insert_before_nth_command(index, replacement)
                return
        raise IdentifierException(
            f"Could not find subscript command identifier {subscript_cmd_id}"
        )

    def replace_command_by_identifier(
        self,
        identifier: str,
        replacement: Union[UsableEventScriptCommand, list[UsableEventScriptCommand]],
    ) -> None:
        """Replace an event script command with one or more new commands.

        Args:
            identifier: The unique identifier of the command to replace.
            replacement: A single command or list of commands to insert in place of the old one.

        Raises:
            IdentifierException: If no command with the identifier is found.
        """
        for bank in self.banks:
            for script in bank.scripts:
                for index, command in enumerate(script.contents):
                    if command.identifier.label == identifier:
                        # Delete the old command
                        del script.contents[index]
                        # Insert replacement(s)
                        if isinstance(replacement, list):
                            for i, new_cmd in enumerate(replacement):
                                script.insert_before_nth_command(index + i, new_cmd)
                        else:
                            script.insert_before_nth_command(index, replacement)
                        return
        raise IdentifierException(f"Could not find command identifier {identifier}")

    def delete_command_by_identifier(self, identifier: str) -> None:
        """Delete the command matching the identifier from its script.

        Also checks inside ActionQueuePrototype subscripts for matching identifiers.

        Args:
            identifier: The unique identifier of the command to delete.

        Raises:
            IdentifierException: If no command with the identifier is found.
        """
        for bank in self.banks:
            for script in bank.scripts:
                for index, command in enumerate(script.contents):
                    if command.identifier.label == identifier:
                        del script.contents[index]
                        return
                    # Also check inside ActionQueuePrototype subscripts
                    if isinstance(command, ActionQueuePrototype):
                        for sub_index, sub_command in enumerate(command.subscript.contents):
                            if sub_command.identifier.label == identifier:
                                command.subscript.delete_at_index(sub_index)
                                return
        raise IdentifierException(f"could not find command identifier {identifier}")

    def get_script_by_id(self, script_id: int) -> EventScript:
        """get one script from any bank by absolute id.\n
        It is recommended to use event name constants for this."""
        assert 0 <= script_id < TOTAL_SCRIPTS
        bank_0x1e: EventScriptBank = self.banks[0]
        bank_0x1f: EventScriptBank = self.banks[1]
        bank_0x20: EventScriptBank = self.banks[2]
        range_0x1e = range(0, bank_0x1e.script_count)
        range_0x1f = range(
            bank_0x1e.script_count, bank_0x1e.script_count + bank_0x1f.script_count
        )
        range_0x20 = range(
            bank_0x1e.script_count + bank_0x1f.script_count,
            bank_0x1e.script_count + bank_0x1f.script_count + bank_0x20.script_count,
        )
        if script_id in range_0x1e:
            return bank_0x1e.scripts[script_id]
        if script_id in range_0x1f:
            relative_id: int = script_id - range_0x1f[0]
            return bank_0x1f.scripts[relative_id]
        if script_id in range_0x20:
            relative_id: int = script_id - range_0x20[0]
            return bank_0x20.scripts[relative_id]
        raise IdentifierException(f"could not find script id {id} for some reason")
