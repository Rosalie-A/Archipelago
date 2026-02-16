"""Base classes supporting battle animation script assembly."""

from .commands.types.classes import (
    UsableAnimationScriptCommand,
)

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)

from typing import TypeVar, overload

T = TypeVar('T', bound=UsableAnimationScriptCommand)

from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.types import (
    UsableAnimationScriptCommand,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import (
    ReturnSubroutine,
)

class AnimationScript(Script[UsableAnimationScriptCommand]):
    """Base class for a single animation script, a list of script command subclasses."""

    _contents: list[UsableAnimationScriptCommand] = []

    @property
    def contents(self) -> list[UsableAnimationScriptCommand]:
        return self._contents

    def append(self, command: UsableAnimationScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: list[UsableAnimationScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: list[UsableAnimationScriptCommand] | None = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: list[UsableAnimationScriptCommand] | None = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(
        self, index: int, content: UsableAnimationScriptCommand
    ) -> None:
        super().replace_at_index(index, content)

    def render(self, _: int | None = None) -> bytearray:
        output = bytearray()
        command: UsableAnimationScriptCommand
        for command in self._contents:
            output += command.render()
        return output

class AnimationScriptBlock(AnimationScript):
    """Covers a range of known animation data in the ROM."""
    _expected_size: int = 0
    _expected_beginning: int = 0

    @property
    def expected_size(self) -> int:
        """The length of bytes that this script should ultimately equal when compiled.  
        The base property should not be mutable."""
        return self._expected_size

    @property
    def expected_beginning(self) -> int:
        """The expected beginning address of this script in the ROM.  
        The base property should not be mutable."""
        return self._expected_beginning
    
    @property
    def expected_end(self) -> int:
        """The expected end address of this script in the ROM."""
        return self._expected_beginning + self._expected_size

    def __repr__(self) -> str:
        """Representation showing expected_size (base 10) and expected_beginning (base 16)."""
        return (
            f"<AnimationScriptBlock expected_size={self.expected_size} "
            f"expected_beginning=0x{self.expected_beginning:06X}>"
        )

    def __str__(self) -> str:
        """Same as repr() but used by print()."""
        return self.__repr__()

    def __init__(
        self,
        expected_size: int,
        expected_beginning: int,
        script: list[UsableAnimationScriptCommand] | None = None,
    ) -> None:
        super().__init__(script)
        self._expected_size = expected_size
        self._expected_beginning = expected_beginning

    def get_rendered_size(self) -> int:
        """Calculate the size of this script when rendered, without padding."""
        return sum(command.size for command in self._contents)

    def render(self, _: int | None = None) -> bytearray:
        output = super().render(_)
        # fill empty bytes
        if len(output) == self.expected_size:
            return output
        if len(output) > self.expected_size:
            raise ScriptBankTooLongException(
                f"animation script output too long: got {len(output)} expected {self.expected_size} "
                f"(over by {len(output) - self.expected_size} bytes)"
            )
        buffer: list[UsableAnimationScriptCommand] = [ReturnSubroutine()] * (self.expected_size - len(output))
        self.set_contents(self.contents + buffer)
        output = super().render(_)
        return output

class AnimationScriptBank(ScriptBank[AnimationScript]):
    """Base class for a collection of scripts that belong to the same bank (ie 0x##0000)
    and are separated by IDs."""

    _scripts: list[AnimationScript | AnimationScriptBlock]
    _name: str
    _bank_end: int | None = None

    @property
    def scripts(self) -> list[AnimationScript | AnimationScriptBlock]:
        return self._scripts

    @property
    def name(self) -> str:
        """An arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        return self._name

    @property
    def bank_end(self) -> int | None:
        """The expected end address of this bank in the ROM. Used to calculate unused space."""
        return self._bank_end

    def set_name(self, name: str) -> None:
        """Set an arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        self._name = name

    def set_bank_end(self, bank_end: int) -> None:
        """Set the expected end address of this bank in the ROM."""
        self._bank_end = bank_end

    def set_contents(self, scripts: list[AnimationScript] | None = None) -> None:
        """Overwrite the entire list of scripts belonging to this bank."""
        if scripts is None:
            scripts = []
        super().set_contents(scripts)

    @overload
    def get_command_by_name(self, identifier: str) -> UsableAnimationScriptCommand: ...
    @overload
    def get_command_by_name(self, identifier: str, cmd_type: type[T]) -> T: ...

    def get_command_by_name(
        self, identifier: str, cmd_type: type[T] | None = None
    ) -> UsableAnimationScriptCommand | T:
        """Return a single command whose unique identifier matches the name provided.

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
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.label == identifier:
                    if cmd_type is not None:
                        if not isinstance(command, cmd_type):
                            raise ValueError(
                                f"Command with ID {identifier} is {type(command).__name__}, "
                                f"expected {cmd_type.__name__}."
                            )
                        return command
                    return command
        raise IdentifierException(f"{identifier} not found")

    def replace_command_by_name(
        self, identifier: str, contents: UsableAnimationScriptCommand
    ) -> None:
        """Overwrite a single command whose unique identifier matches the name provided."""
        for script_id, script in enumerate(self._scripts):
            for index, command in enumerate(script.contents):
                if command.identifier.label == identifier:
                    self._scripts[script_id].contents[index] = contents
                    return
        raise IdentifierException(f"{identifier} not found")

    def delete_command_by_name(self, identifier: str) -> None:
        """Delete a single command whose unique identifier matches the name provided."""
        for script in self._scripts:
            for index, command in enumerate(script.contents):
                if command.identifier.label == identifier:
                    del script.contents[index]
                    return
        raise IdentifierException(f"{identifier} not found")

    def set_addresses(self, addrs: dict[str, int]) -> None:
        """This should ONLY be used when the parent ScriptBankCollection is rendering
        all of its constituent banks. Replaces the identifier-address dict."""
        self._addresses = addrs

    def __init__(
        self,
        name: str,
        scripts: list[AnimationScript] | None = None,
    ) -> None:
        self.set_name(name)
        super().__init__(scripts)

    def _associate_address(
        self, command: UsableAnimationScriptCommand, position: int
    ) -> int:
        """Associates an identifier and an address as a key-value pair in the addresses dict."""
        key: str = command.identifier.label
        if key in self.addresses and self.addresses[key] != position:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position
        position += command.size
        return position

    def build_command_address_mapping(self) -> dict[str, int]:
        """Build and return the command identifier to address mapping.

        This method populates the internal addresses dict and pointer_bytes
        by iterating through all AnimationScriptBlock instances in this bank.

        Returns:
            dict[str, int]: Mapping of command identifiers to their ROM addresses.
        """
        self.addresses.clear()
        self._pointer_bytes = bytearray()

        scripts: list[AnimationScriptBlock] = [
            s for s in self.scripts if isinstance(s, AnimationScriptBlock)
        ]

        # build command name : address table
        for script in scripts:
            position: int = script.expected_beginning
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script.contents:
                position = self._associate_address(command, position)

        return self.addresses

    def _build_size_report(self, scripts: list[AnimationScriptBlock]) -> str:
        """Build a detailed report of all script sizes in this bank."""
        lines: list[str] = [f"\nScript size report for bank '{self.name}':"]
        lines.append("-" * 60)

        total_over = 0
        total_available = 0

        for i, script in enumerate(scripts):
            actual_size = script.get_rendered_size()
            expected_size = script.expected_size
            diff = actual_size - expected_size

            addr_str = f"0x{script.expected_beginning:06X}"

            if diff > 0:
                lines.append(
                    f"  Script {i} @ {addr_str}: {actual_size}/{expected_size} bytes "
                    f"(OVER by {diff} bytes)"
                )
                total_over += diff
            elif diff < 0:
                available = -diff
                lines.append(
                    f"  Script {i} @ {addr_str}: {actual_size}/{expected_size} bytes "
                    f"({available} bytes available)"
                )
                total_available += available
            else:
                lines.append(
                    f"  Script {i} @ {addr_str}: {actual_size}/{expected_size} bytes (exact fit)"
                )

        lines.append("-" * 60)
        lines.append(f"  Total over: {total_over} bytes")
        lines.append(f"  Total available: {total_available} bytes")
        if total_over > total_available:
            lines.append(f"  NET SHORTAGE: {total_over - total_available} bytes")
        else:
            lines.append(f"  Net surplus: {total_available - total_over} bytes")

        return "\n".join(lines)

    def render(self) -> list[tuple[int, bytearray]]:
        """Generate the bytes representing the current state of this bank to be written
        to the ROM."""

        scripts: list[AnimationScriptBlock] = [
            s for s in self.scripts if isinstance(s, AnimationScriptBlock)
        ]

        # build command name : address table
        self.build_command_address_mapping()

        # replace jump placeholders with addresses
        for script in scripts:
            self._populate_jumps(script)

        # Check for oversized scripts before rendering
        oversized: list[tuple[int, AnimationScriptBlock, int]] = []
        for i, script in enumerate(scripts):
            actual_size = script.get_rendered_size()
            if actual_size > script.expected_size:
                oversized.append((i, script, actual_size - script.expected_size))

        if oversized:
            # Build detailed error message
            error_lines = [
                f"Animation script bank '{self.name}' has {len(oversized)} oversized script(s):"
            ]
            for idx, script, over_by in oversized:
                error_lines.append(
                    f"  Script {idx} @ 0x{script.expected_beginning:06X}: "
                    f"over by {over_by} bytes"
                )
            error_lines.append(self._build_size_report(scripts))
            raise ScriptBankTooLongException("\n".join(error_lines))

        return [
            (script.expected_beginning, script.render())
            for script in scripts
        ]

    def get_unused_range(self) -> tuple[int, int] | None:
        """Return (start, end) of unused space after the last script.

        Requires bank_end to be set via set_bank_end(). Returns None if
        bank_end is not set or if there is no unused space.

        Deprecated: Use get_unused_ranges() instead to get all unused ranges.
        """
        ranges = self.get_unused_ranges()
        if not ranges:
            return None
        # Return the last range (tail space) for backwards compatibility
        return ranges[-1]

    def get_unused_ranges(self) -> list[tuple[int, int]]:
        """Return all unused ranges (gaps between scripts and tail space).

        Requires bank_end to be set via set_bank_end(). Returns empty list if
        bank_end is not set or if there are no unused ranges.

        Returns:
            List of (start, end) tuples representing unused address ranges.
        """
        if self._bank_end is None:
            return []

        scripts: list[AnimationScriptBlock] = [
            s for s in self.scripts if isinstance(s, AnimationScriptBlock)
        ]
        if not scripts:
            return []

        # Sort scripts by their expected beginning address
        sorted_scripts = sorted(scripts, key=lambda s: s.expected_beginning)

        unused_ranges: list[tuple[int, int]] = []

        # Find gaps between consecutive scripts
        for i in range(len(sorted_scripts) - 1):
            current_end = sorted_scripts[i].expected_end
            next_start = sorted_scripts[i + 1].expected_beginning
            if current_end < next_start:
                unused_ranges.append((current_end, next_start))

        # Find tail space after the last script
        last_script = sorted_scripts[-1]
        last_end = last_script.expected_end
        if last_end < self._bank_end:
            unused_ranges.append((last_end, self._bank_end))

        return unused_ranges
