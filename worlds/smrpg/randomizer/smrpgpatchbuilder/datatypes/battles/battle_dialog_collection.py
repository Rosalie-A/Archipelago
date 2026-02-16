"""Battle dialog collection for managing battle dialogs and messages."""

from smrpgpatchbuilder.datatypes.dialogs.utils import compress, COMPRESSION_TABLE

# Battle dialog addresses
BATTLE_DIALOG_POINTER_ADDRESS = 0x396554
BATTLE_DIALOG_DATA_START = 0x396755
BATTLE_DIALOG_DATA_END = 0x3992D0

# Battle message addresses
BATTLE_MESSAGE_POINTER_ADDRESS = 0x3A26F1
BATTLE_MESSAGE_DATA_START = 0x3A274D
BATTLE_MESSAGE_DATA_END = 0x3A29FF

class BattleDialogCollection:
    """Houses battle dialogs and messages with ability to render to ROM bytes."""

    _battle_dialogs: list[str]
    _battle_messages: list[str]
    _compression_table: list[tuple[str, bytes]]

    @property
    def battle_dialogs(self) -> list[str]:
        """The battle dialog strings (256 entries)."""
        return self._battle_dialogs

    def set_battle_dialogs(self, battle_dialogs: list[str]) -> None:
        """Set the battle dialog strings."""
        if len(battle_dialogs) != 256:
            raise ValueError(f"Expected 256 battle dialogs, got {len(battle_dialogs)}")
        self._battle_dialogs = battle_dialogs

    @property
    def battle_messages(self) -> list[str]:
        """The battle message strings (46 entries)."""
        return self._battle_messages

    def set_battle_messages(self, battle_messages: list[str]) -> None:
        """Set the battle message strings."""
        if len(battle_messages) != 46:
            raise ValueError(f"Expected 46 battle messages, got {len(battle_messages)}")
        self._battle_messages = battle_messages

    @property
    def compression_table(self) -> list[tuple[str, bytes]]:
        """The compression table used for battle dialogs and messages."""
        return self._compression_table

    def set_compression_table(self, compression_table: list[tuple[str, bytes]]) -> None:
        """Set the compression table."""
        self._compression_table = compression_table

    def __init__(
        self,
        battle_dialogs: list[str],
        battle_messages: list[str],
        compression_table: list[tuple[str, bytes]] | None = None,
    ) -> None:
        """Initialize the battle dialog collection.

        Args:
            battle_dialogs: List of 256 battle dialog strings
            battle_messages: List of 46 battle message strings
            compression_table: Optional custom compression table. If None, uses default.
        """
        # Battle dialogs use mostly the same encoding as overworld dialogs,
        # but apostrophe has a different byte value (0x9B instead of 0x27).
        # See LAZYSHELL TextHelperReduced.cs lines 185-189 and 260-264.
        if compression_table is None:
            # Battle dialogs and messages use the same character encoding as overworld,
            # just without the word compression. Characters fall back to ASCII for
            # letters/numbers, with special mappings for punctuation in COMPRESSION_TABLE.
            # For battle dialogs, apostrophe encodes to 0x9B (not 0x27 like overworld).
            # Special tokens for item/menu font characters (used by some battle messages):
            #   [item_apos] -> 0x7E (apostrophe in item font)
            #   [item_excl] -> 0x7B (exclamation in item font)
            #   [item_hyphen] -> 0x7D (hyphen in item font)
            compression_table = [
                ("\n", b"\x01"),
                ("[await]", b"\x02"),
                ("[pause]", b"\x03"),
                ("[delay]", b"\x0C"),
                ("'", b"\x9B"),  # Apostrophe in battle dialogs (LazyShell TextHelperReduced.cs line 186)
                ("[item_apos]", b"\x7E"),  # Apostrophe in item/menu font
                ("[item_excl]", b"\x7B"),  # Exclamation in item/menu font
                ("[item_hyphen]", b"\x7D"),  # Hyphen in item/menu font
            ] + COMPRESSION_TABLE[17:]

        self.set_compression_table(compression_table)
        self.set_battle_dialogs(battle_dialogs)
        self.set_battle_messages(battle_messages)

    def render(self) -> dict[int, bytearray]:
        """Convert battle dialogs and messages to ROM patch format.

        Returns:
            Dictionary mapping ROM addresses to bytearrays to patch.
        """
        # Compress all battle dialogs
        compressed_dialogs = []
        for message in self.battle_dialogs:
            if message:
                compressed_dialogs.append(compress(message, self.compression_table))
            else:
                compressed_dialogs.append(bytearray([0x00]))

        # Build the battle dialog data section
        assembled_dialog_data = bytearray()
        dialog_pointer_table = bytearray()
        current_offset = BATTLE_DIALOG_DATA_START & 0xFFFF  # Relative to bank 0x39

        for message_bytes in compressed_dialogs:
            # Add pointer (little-endian 16-bit)
            dialog_pointer_table.append(current_offset & 0xFF)
            dialog_pointer_table.append((current_offset >> 8) & 0xFF)

            # Add message data
            assembled_dialog_data += message_bytes

            # Update offset
            current_offset += len(message_bytes)

        # Check size constraints for battle dialogs
        max_dialog_size = BATTLE_DIALOG_DATA_END - BATTLE_DIALOG_DATA_START + 1
        if len(assembled_dialog_data) > max_dialog_size:
            raise ValueError(
                f"Battle dialog data too long: {len(assembled_dialog_data)} bytes "
                f"(expected up to {max_dialog_size})"
            )

        # Pad data to fill the space
        if len(assembled_dialog_data) < max_dialog_size:
            assembled_dialog_data += bytearray(max_dialog_size - len(assembled_dialog_data))

        # Compress all battle messages
        compressed_messages = []
        for message in self.battle_messages:
            if message:
                compressed_messages.append(compress(message, self.compression_table))
            else:
                compressed_messages.append(bytearray([0x00]))

        # Build the battle message data section
        assembled_message_data = bytearray()
        message_pointer_table = bytearray()
        current_offset = BATTLE_MESSAGE_DATA_START & 0xFFFF  # Relative to bank 0x3A

        for message_bytes in compressed_messages:
            # Add pointer (little-endian 16-bit)
            message_pointer_table.append(current_offset & 0xFF)
            message_pointer_table.append((current_offset >> 8) & 0xFF)

            # Add message data
            assembled_message_data += message_bytes

            # Update offset
            current_offset += len(message_bytes)

        # Check size constraints for battle messages
        max_message_size = BATTLE_MESSAGE_DATA_END - BATTLE_MESSAGE_DATA_START + 1
        if len(assembled_message_data) > max_message_size:
            raise ValueError(
                f"Battle message data too long: {len(assembled_message_data)} bytes "
                f"(expected up to {max_message_size})"
            )

        # Pad data to fill the space
        if len(assembled_message_data) < max_message_size:
            assembled_message_data += bytearray(max_message_size - len(assembled_message_data))

        # Return patch dictionary
        return {
            BATTLE_DIALOG_POINTER_ADDRESS: dialog_pointer_table,
            BATTLE_DIALOG_DATA_START: assembled_dialog_data,
            BATTLE_MESSAGE_POINTER_ADDRESS: message_pointer_table,
            BATTLE_MESSAGE_DATA_START: assembled_message_data,
        }
