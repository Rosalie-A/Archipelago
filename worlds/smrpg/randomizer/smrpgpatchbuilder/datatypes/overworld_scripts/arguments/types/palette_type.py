class PaletteType(int):
    """Base class representing special effects that can be applied to a palette."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x06, 0x0C, 0x0E]
        return super(PaletteType, cls).__new__(cls, num)
