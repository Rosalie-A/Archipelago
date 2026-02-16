"""Base classes for numbers and numerical operations."""

class UInt4(int):
    """Unsigned 4-bit int"""

    def __new__(cls, *args) -> "UInt4":
        num = args[0]
        assert 0 <= num <= 0x0F
        return super(UInt4, cls).__new__(cls, num)

    def to_byte(self) -> int:
        """Single byte representation as an int"""
        return self

class UInt8(int):
    """Unsigned 8-bit int"""

    def __new__(cls, *args: int) -> "UInt8":
        num = args[0]
        assert 0 <= num <= 0xFF
        return super(UInt8, cls).__new__(cls, num)

    def to_byte(self) -> int:
        """Single byte representation as an int"""
        return int(self)

class Int8(int):
    """Signed 8-bit int"""

    def __new__(cls, *args: int) -> "Int8":
        num = args[0]
        if num > 127:
            offset = num - 127 - 1
            num = -128 + offset
        assert -128 <= num <= 127
        return super(Int8, cls).__new__(cls, num)

    def to_byte(self) -> int:
        """Single byte representation as an int"""
        if self < 0:
            val = 0x100 + self
        else:
            val = int(self)
        return val

class UInt16(int):
    """Unsigned 16-bit int"""

    def __new__(cls, *args: int) -> "UInt16":
        num = args[0]
        assert 0 <= num <= 0xFFFF
        return super(UInt16, cls).__new__(cls, num)

    def to_bytes(self) -> int:
        """Multi-byte representation as an int"""
        return self

    def little_endian(self) -> bytearray:
        """This number as a little-endian bytearray"""
        return bytearray([(self & 0xFF), ((self >> 8))])

class Int16(int):
    """Signed 16-bit int"""

    def __new__(cls, *args) -> "Int16":
        num = args[0]
        if num > 32767:
            offset = num - 32767 - 1
            num = -32768 + offset
        assert -32768 <= num <= 32767
        return super(Int16, cls).__new__(cls, num)

    def to_bytes(self) -> int:
        """Multi-byte representation as an int"""
        if self < 0:
            val = 0x10000 + self
        else:
            val = self
        return val

    def little_endian(self) -> bytearray:
        """This number as a little-endian bytearray"""
        val = self.to_bytes()
        return bytearray([(val & 0xFF), ((val >> 8))])

class BitMapSet(set):
    """a class representing a bitmap of a certain length using the set built-in type to track
    which bits are set."""

    # pylint: disable=w1113
    def __init__(self, num_bytes=1, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._num_bytes = num_bytes

    def as_bytes(self) -> bytearray:
        """return bitmap in little endian byte format for rom patching.

        :rtype: bytearray
        """
        result = 0
        for value in self:
            result |= 1 << value
        return bytearray(result.to_bytes(self._num_bytes, "little"))

    def __str__(self):
        return f"BitMapSet({super().__str__()})"

class ByteField:
    """Base class for an integer value field spanning one or more bytes."""

    def __init__(self, value: UInt8 | UInt16 | int, num_bytes: int = 1) -> None:
        """
        :type value: int
        :type num_bytes: int
        """
        if isinstance(value, UInt16):
            num_bytes = 2
        self._value = int(value)
        self._num_bytes = num_bytes

    @property
    def value(self):
        """Int value of bytefield"""
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)

    def as_bytes(self) -> bytearray:
        """return current value of this stat as a little-endian byte array for the patch.
        If the value is less than zero, convert this to a signed int in byte format."""
        if self._value < 0:
            val = self._value + (2 ** (self._num_bytes * 8))
        else:
            val = self._value
        return bytearray(val.to_bytes(self._num_bytes, "little"))

    def __str__(self):
        return (
            f"ByteField(current value: {self.value}, number of bytes: {self._num_bytes}"
        )
