from typing import NamedTuple

class _Flag(NamedTuple):
    byte: int
    bit: int

class Flag(_Flag):
    """An in-game variable that is a single true/false bit,
    normally carrying meaning independent of the byte it belongs to.\n
    Bits for 8-bit addresses between 0x7040 and 0x709F can be used for this."""

    def __new__(cls, byte: int, bit: int):
        assert 0x7040 <= byte <= 0x709F
        assert 0 <= bit <= 7
        return super().__new__(cls, byte, bit)
