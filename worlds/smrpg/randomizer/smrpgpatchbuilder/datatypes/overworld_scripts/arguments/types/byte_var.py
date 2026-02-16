class ByteVar(int):
    """An in-game variable that can store 8-bit byte int values.\n
    Addresses between 0x7040 and 0x719F can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7040 <= address <= 0x719F
        return super(ByteVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = self - 0x70A0
        assert 0 <= byte <= 0xFF
        return byte
