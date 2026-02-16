class Direction(int):
    """Base class representing directions in which an object can walk or face."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Direction, cls).__new__(cls, num)
