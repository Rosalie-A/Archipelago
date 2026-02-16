"""Base classes related to dialogs and dialog collections"""

from smrpgpatchbuilder.datatypes.dialogs.ids.misc import (
    DIALOG_BANK_22_BEGINS,
    DIALOG_BANK_22_ENDS,
    DIALOG_BANK_23_BEGINS,
    DIALOG_BANK_23_ENDS,
    DIALOG_BANK_24_BEGINS,
    DIALOG_BANK_24_ENDS,
)
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
)

from .ids.dialog_bank_ids import (
    DIALOG_BANK_22,
)
from .utils import compress, COMPRESSION_TABLE

class Dialog:
    """An individual dialog in the overworld"""

    _bank: int
    _index: int
    _position: int

    @property
    def bank(self) -> int:
        """The bank that this dialog belongs to"""
        return self._bank

    @property
    def index(self) -> int:
        """The index of the dialog"""
        return self._index

    @property
    def position(self) -> int:
        """The starting position within the raw text where this dialog begins"""
        return self._position

    def set_position(self, position: int) -> None:
        """Overwrite the starting position within the raw text where this dialog begins"""
        self._position = position

    def __init__(self, bank: int, index: int, pos: int) -> None:
        assert 0x22 <= bank <= 0x24, f"Dialog bank must be 0x22, 0x23, or 0x24, got 0x{bank:02X}"
        self._bank = bank
        self._index = index
        self.set_position(pos)

class DialogCollection:
    """Houses all dialog banks to allow retrieval and manipulation of any dialog."""

    _dialogs: list[Dialog]
    _raw_data: list[list[str]]
    _dialog_bank_22_begins: int = DIALOG_BANK_22_BEGINS
    _dialog_bank_22_ends: int = DIALOG_BANK_22_ENDS
    _dialog_bank_23_begins: int = DIALOG_BANK_23_BEGINS
    _dialog_bank_23_ends: int = DIALOG_BANK_23_ENDS
    _dialog_bank_24_begins: int = DIALOG_BANK_24_BEGINS
    _dialog_bank_24_ends: int = DIALOG_BANK_24_ENDS
    _unused_ranges: list[tuple[int, int] | None]

    @property
    def dialogs(self) -> list[Dialog]:
        """The dialogs belonging to this seed."""
        return self._dialogs

    def _set_dialogs(self, dialogs: list[Dialog]) -> None:
        """Overwrite the dialogs belonging to this seed."""
        assert len(dialogs) == 4096
        self._dialogs = dialogs

    @property
    def raw_data(self) -> list[list[str]]:
        """The raw string data comprising dialogs."""
        return self._raw_data

    def _set_raw_data(self, raw_data: list[list[str]]) -> None:
        """Overwrite the raw string data comprising dialogs."""
        assert len(raw_data) == 3
        self._raw_data = raw_data

    def replace_dialog(self, identifier: int, content: str):
        """Replace a whole dialog by its unique ID."""
        dialog = self.dialogs[identifier]
        raw_index = dialog.bank - DIALOG_BANK_22
        self.raw_data[raw_index][dialog.index] = content

    def search_and_replace_in_dialog(self, identifier: int, search: str, replace: str):
        """Replace all instances of the substring in a specific dialog by its unique ID."""
        dialog = self.dialogs[identifier]
        raw_index = dialog.bank - DIALOG_BANK_22
        current_content = self.raw_data[raw_index][dialog.index]
        self.raw_data[raw_index][dialog.index] = current_content.replace(search, replace)

    def search_and_replace_in_all_dialogs(self, search: str, replace: str):
        """Replace all instances of the substring across all dialogs."""
        for bank_index, bank in enumerate(self.raw_data):
            for index, string in enumerate(bank):
                self.raw_data[bank_index][index] = string.replace(search, replace)

    def _set_compression_table(
        self, compression_table: list[tuple[str, bytes | bytearray]]
    ) -> None:
        """Set the compression table for this dialog collection."""
        self._compression_table = compression_table

    @property
    def compression_table(self) -> list[tuple[str, bytes | bytearray]]:
        """Get the compression table for this dialog collection."""
        return self._compression_table

    def __init__(
        self,
        dialogs: list[Dialog],
        raw_data: list[list[str]],
        compression_table: list[tuple[str, bytes | bytearray]],
        dialog_bank_22_begins=DIALOG_BANK_22_BEGINS,
        dialog_bank_22_ends=DIALOG_BANK_22_ENDS,
        dialog_bank_23_begins=DIALOG_BANK_23_BEGINS,
        dialog_bank_23_ends=DIALOG_BANK_23_ENDS,
        dialog_bank_24_begins=DIALOG_BANK_24_BEGINS,
        dialog_bank_24_ends=DIALOG_BANK_24_ENDS,
    ) -> None:
        self._set_dialogs(dialogs)
        self._set_raw_data(raw_data)
        self._set_compression_table([*COMPRESSION_TABLE, *compression_table])
        self._dialog_bank_22_begins = dialog_bank_22_begins
        self._dialog_bank_22_ends = dialog_bank_22_ends
        self._dialog_bank_23_begins = dialog_bank_23_begins
        self._dialog_bank_23_ends = dialog_bank_23_ends
        self._dialog_bank_24_begins = dialog_bank_24_begins
        self._dialog_bank_24_ends = dialog_bank_24_ends
        self._unused_ranges = []

    def render(self) -> dict[int, bytearray]:
        """Get all dialog data in `{0x123456: bytearray([0x00])}` format."""
        if len(self.dialogs) != 4096:
            raise ValueError("must be exactly 4096 dialogs")
        if len(self.raw_data) != 3:
            raise ValueError("must be exactly 3 dialog banks")

        # Validate all dialog pointers reference valid indexes
        bank_sizes = [len(self.raw_data[0]), len(self.raw_data[1]), len(self.raw_data[2])]
        for ptr_id, dialog in enumerate(self.dialogs):
            bank_idx = dialog.bank - 0x22
            if bank_idx < 0 or bank_idx > 2:
                raise ValueError(
                    f"Dialog {ptr_id}: invalid bank 0x{dialog.bank:02x} (must be 0x22-0x24)"
                )
            if dialog.index >= bank_sizes[bank_idx]:
                raise ValueError(
                    f"Dialog {ptr_id}: index {dialog.index} exceeds bank 0x{dialog.bank:02x} "
                    f"table size ({bank_sizes[bank_idx]} entries)"
                )

        self._unused_ranges = []  # Reset unused ranges tracking
        new_pointer_table: list[int] = [-1] * 4096

        compressed_text = [
            [compress(d, self.compression_table) for d in self._raw_data[0]],
            [compress(d, self.compression_table) for d in self._raw_data[1]],
            [compress(d, self.compression_table) for d in self._raw_data[2]],
        ]

        assembled_dialog_data = []
        assembled_pointers = bytearray()

        for bank_index, text_collection in enumerate(compressed_text):
            bank = 0x22 + bank_index
            pointer_position = 0
            assembled_dialog_for_this_bank = bytearray()
            # convert pointer data to offsets
            for dialog_id, dialog_bytes in enumerate(text_collection):
                for index, _ in enumerate(dialog_bytes):
                    indices = [
                        j
                        for j, x in enumerate(self.dialogs)
                        if x.bank == bank
                        and x.index == dialog_id
                        and x.position == index
                    ]
                    for matched_pointer in indices:
                        new_pointer_table[matched_pointer] = pointer_position
                    pointer_position += 1
                assembled_dialog_for_this_bank += dialog_bytes

            # convert to pointers relative to section pointer
            if bank_index == 0:
                table_at_0x200 = new_pointer_table[0x200]
                table_at_0x400 = new_pointer_table[0x400]
                table_at_0x600 = new_pointer_table[0x600]
                assert table_at_0x200 > -1
                assert table_at_0x400 > -1
                assert table_at_0x600 > -1
                offsets = [
                    0,
                    table_at_0x200,
                    table_at_0x400,
                    table_at_0x600,
                ]
                offsets = [o + 8 for o in offsets]
                for index in range(0x3FF, 0x1FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x200
                for index in range(0x5FF, 0x3FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x400
                for index in range(0x7FF, 0x5FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x600
            elif bank_index == 1:
                table_at_0xa00 = new_pointer_table[0xA00]
                assert table_at_0xa00 > -1
                offsets = [0, table_at_0xa00]
                offsets = [o + 4 for o in offsets]
                for index in range(0xBFF, 0x9FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0xa00
            else:
                table_at_0xe00 = new_pointer_table[0xE00]
                assert table_at_0xe00 > -1
                offsets = [0, table_at_0xe00]
                offsets = [o + 4 for o in offsets]
                for index in range(0xFFF, 0xDFF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0xe00

            # final output for data bank: section pointers plus dialog data
            assembled_bank_dialog_data = bytearray([])
            for val in offsets:
                assembled_bank_dialog_data.append(val & 0xFF)
                assembled_bank_dialog_data.append(val >> 8)
            assembled_bank_dialog_data += assembled_dialog_for_this_bank

            # make sure it's not overflowing, fill up with empty data if space left
            if bank_index == 0:
                bank_begins = self._dialog_bank_22_begins
                bank_ends = self._dialog_bank_22_ends
            elif bank_index == 1:
                bank_begins = self._dialog_bank_23_begins
                bank_ends = self._dialog_bank_23_ends
            else:
                bank_begins = self._dialog_bank_24_begins
                bank_ends = self._dialog_bank_24_ends

            max_length = bank_ends - bank_begins
            used_length = len(assembled_bank_dialog_data)
            empty_space = max_length - used_length

            if empty_space < 0:
                length = len(assembled_bank_dialog_data)
                err_bank = 0x22 + bank_index
                raise ScriptBankTooLongException(
                    (
                        f"Bank 0x{err_bank:02x} dialog data too long: "
                        f"{length} bytes (expected up to {max_length})"
                    )
                )

            # Track unused range before padding
            if empty_space > 0:
                unused_start = bank_begins + used_length
                self._unused_ranges.append((unused_start, bank_ends))
                assembled_bank_dialog_data += bytearray(
                    [0x00 for x in range(empty_space)]
                )
            else:
                self._unused_ranges.append(None)

            assembled_dialog_data.append(assembled_bank_dialog_data)

        # pointer bytes
        for ptr_id, val in enumerate(new_pointer_table):
            if val == -1:
                dialog = self.dialogs[ptr_id]
                raise ValueError(
                    f"Dialog {ptr_id}: position {dialog.position} exceeds compressed "
                    f"dialog length at bank 0x{dialog.bank:02x}, index {dialog.index}"
                )
            if val < 0 or val > 0xFFFF:
                dialog = self.dialogs[ptr_id]
                raise ValueError(
                    f"Dialog {ptr_id}: pointer value {val} out of range (0-65535). "
                    f"Dialog: bank=0x{dialog.bank:02x}, index={dialog.index}, pos={dialog.position}"
                )
            assembled_pointers.append(val & 0xFF)
            assembled_pointers.append(val >> 8)

        # compression table
        # Extract the DEFAULT_COMPRESSION_TABLE portion (bytes 0x0E-0x19)
        default_compression = [
            item for item in self.compression_table
            if item not in COMPRESSION_TABLE
        ]

        # Build compression table strings
        compression_strings = bytearray()
        compression_pointers = bytearray()
        # Track seen strings to avoid duplicates: {word: pointer_offset}
        seen_strings = {}

        for word, _ in default_compression:
            # Check if we've already written this string
            if word in seen_strings:
                # Reuse the existing pointer
                pointer = seen_strings[word]
                compression_pointers.append(pointer & 0xFF)
                compression_pointers.append(pointer >> 8)
            else:
                # Store pointer to this string (relative to 0x249100)
                pointer = len(compression_strings)
                compression_pointers.append(pointer & 0xFF)
                compression_pointers.append(pointer >> 8)

                # Mark this string as seen
                seen_strings[word] = pointer

                # Compress the word using COMPRESSION_TABLE
                for char in word:
                    found = False
                    for tbl_char, tbl_byte in COMPRESSION_TABLE:
                        if char == tbl_char:
                            compression_strings += tbl_byte
                            found = True
                            break
                    if not found:
                        compression_strings.append(ord(char))

                # Null terminate
                compression_strings.append(0x00)

        # Pad compression pointers to 256 bytes
        while len(compression_pointers) < 256:
            compression_pointers.append(0x00)

        # Combine pointers and strings
        assembled_compression_table = compression_pointers + compression_strings

        # Pad to match original size (0x249000 to 0x24EDE0 is available space)
        # Original compression table area is at least 0x14A bytes (to 0x249149)
        # Pad to reasonable boundary to avoid issues
        max_compression_size = 0x14A  # 330 bytes minimum
        if len(assembled_compression_table) < max_compression_size:
            assembled_compression_table += bytearray(max_compression_size - len(assembled_compression_table))

        return {
            0x37E000: assembled_pointers,
            0x220000: assembled_dialog_data[0],
            0x230000: assembled_dialog_data[1],
            0x240000: assembled_dialog_data[2],
            0x249000: assembled_compression_table,
        }

    def get_unused_ranges(self) -> list[tuple[int, int]]:
        """Return list of (start, end) tuples for unused space in each bank.

        Call after render(). Returns only non-None ranges (banks with unused space).
        """
        return [r for r in self._unused_ranges if r is not None]
