class ShortVar(int):
    """An in-game variable that can store 16-bit short int values.\n
    Addresses between 0x7000 and 0x71FE can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7000 <= address <= 0x71FE and address % 2 == 0
        return super(ShortVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = (self - 0x7000) // 2
        assert 0 <= byte <= 0xFF
        return byte
    
class TimerVar(ShortVar):
    """An in-game variable that can store 16-bit short int values.\n
    Addresses between 0x701C and 0x7022 can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x701C <= address <= 0x7022 and address % 2 == 0
        return super(TimerVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = (self - 0x701C) // 2
        assert 0 <= byte <= 0x03
        return byte
