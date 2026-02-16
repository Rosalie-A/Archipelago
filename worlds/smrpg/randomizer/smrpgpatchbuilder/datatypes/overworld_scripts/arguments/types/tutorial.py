class Tutorial(int):
    """Base class representing IDs for some predefined in-game tutorial modes."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 3
        return super(Tutorial, cls).__new__(cls, num)
