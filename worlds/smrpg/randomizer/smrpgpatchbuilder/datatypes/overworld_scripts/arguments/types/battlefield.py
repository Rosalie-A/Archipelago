class Battlefield(int):
    """Base class representing IDs for valid battlefields."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 63
        return super(Battlefield, cls).__new__(cls, num)
