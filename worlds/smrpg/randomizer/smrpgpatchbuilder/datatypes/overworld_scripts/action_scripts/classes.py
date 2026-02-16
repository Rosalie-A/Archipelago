"""Base classes supporting NPC action script assembly."""

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)
from typing import TypeVar, Union

from .commands.types.classes import (
    UsableActionScriptCommand,
)

T = TypeVar('T', bound=UsableActionScriptCommand)
from .ids.misc import (
    TOTAL_SCRIPTS,
)

class ActionScript(Script[UsableActionScriptCommand]):
    """Base class for a single NPC action script, a list of script command subclasses."""

    _contents: list[UsableActionScriptCommand]

    @property
    def contents(self) -> list[UsableActionScriptCommand]:
        return self._contents

    def append(self, command: UsableActionScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: list[UsableActionScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: list[UsableActionScriptCommand] | None = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: list[UsableActionScriptCommand] | None = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableActionScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableActionScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableActionScriptCommand],
        command: UsableActionScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableActionScriptCommand],
        command: UsableActionScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableActionScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableActionScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: UsableActionScriptCommand) -> None:
        super().replace_at_index(index, content)

class ActionScriptBank(ScriptBank):
    """Base class for the collection of NPC action scripts."""

    _scripts: list[ActionScript]
    _pointer_table_start: int = 0x210000
    _start: int = 0x210800
    _end: int = 0x21C000
    _count: int = 1024
    _used_script_length: int = 0

    _addresses: dict[str, int]
    _pointer_bytes: bytearray
    _script_bytes: bytearray

    @property
    def scripts(self) -> list[ActionScript]:
        return self._scripts

    def set_contents(self, scripts: list[ActionScript] | None = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == self._count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: ActionScript) -> None:
        assert 0 <= index < self._count
        super().replace_script(index, script)

    def __init__(
        self,
        scripts: list[ActionScript] | None = None,
        start: int = 0x210800,
        pointer_table_start: int = 0x210000,
        end: int = 0x21C000,
        count: int = TOTAL_SCRIPTS,
    ) -> None:
        self._count = count
        super().__init__(scripts)
        self._start = start
        self._pointer_table_start = pointer_table_start
        self._end = end

    @property
    def addresses(self) -> dict[str, int]:
        return self._addresses

    @property
    def pointer_bytes(self) -> bytearray:
        return self._pointer_bytes

    @property
    def script_bytes(self) -> bytearray:
        return self._script_bytes

    def _associate_address(
        self, command: UsableActionScriptCommand, position: int
    ) -> int:
        key: str = command.identifier.label
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        position += command.size

        if position > self.end:
            raise ScriptBankTooLongException(
                f"command exceeded max bank size of {self.end:06X}: {key} @ {position:06X}"
            )
        return position

    def delete_command_by_identifier(self, identifier: str) -> tuple[int, int]:
        """Delete a command from any script in the bank by its identifier.

        Args:
            identifier: The unique identifier of the command to delete.

        Returns:
            A tuple of (script_index, command_index) indicating where the command was found.

        Raises:
            IdentifierException: If no command with the given identifier is found.
        """
        for script_index, script in enumerate(self._scripts):
            for cmd_index, command in enumerate(script.contents):
                if command.identifier.label == identifier:
                    script.delete_at_index(cmd_index)
                    return (script_index, cmd_index)
        raise IdentifierException(f"identifier not found in any script: {identifier}")

    def get_command_by_identifier(
        self,
        identifier: str,
        cmd_type: type[T],
    ) -> T:
        """Get a command from any script in the bank by its identifier.

        Args:
            identifier: The unique identifier of the command to find.
            cmd_type: The expected type of the command.

        Returns:
            The command, typed as cmd_type.

        Raises:
            IdentifierException: If no command with the given identifier is found.
            ValueError: If the command is not of the expected type.
        """
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.label == identifier:
                    if not isinstance(command, cmd_type):
                        raise ValueError(
                            f"Command with ID {identifier} is not of type {cmd_type.__name__}."
                        )
                    return command
        raise IdentifierException(f"identifier not found in any script: {identifier}")

    def replace_command_by_identifier(
        self,
        identifier: str,
        replacement: Union[UsableActionScriptCommand, list[UsableActionScriptCommand]],
    ) -> None:
        """Replace a command in any script with one or more new commands.

        Args:
            identifier: The unique identifier of the command to replace.
            replacement: A single command or list of commands to insert in place of the old one.

        Raises:
            IdentifierException: If no command with the given identifier is found.
        """
        for script in self._scripts:
            for index, command in enumerate(script.contents):
                if command.identifier.label == identifier:
                    # Delete the old command
                    script.delete_at_index(index)
                    # Insert replacement(s)
                    if isinstance(replacement, list):
                        for i, new_cmd in enumerate(replacement):
                            script.insert_before_nth_command(index + i, new_cmd)
                    else:
                        script.insert_before_nth_command(index, replacement)
                    return
        raise IdentifierException(f"identifier not found in any script: {identifier}")

    def render(self) -> bytearray:
        """Return this script set as ROM patch data."""
        position: int = self._start

        script: ActionScript
        command: UsableActionScriptCommand

        # build command name : address table
        for script in self.scripts:
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script.contents:
                position = self._associate_address(command, position)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)

        # finalize bytes
        for script in self.scripts:
            self.script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        self._used_script_length = final_length  # Track before padding
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"action script output too long: got {final_length} expected {expected_length}"
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
