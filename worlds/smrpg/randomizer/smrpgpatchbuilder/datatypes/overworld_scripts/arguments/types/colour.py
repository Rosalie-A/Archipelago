class Colour(int):
    """Base class representing a colour to be used by certain graphics commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Colour, cls).__new__(cls, num)
