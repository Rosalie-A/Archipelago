class Coord(int):
    """Base class representing coordinate axes for commands requiring a coordinate
    or coordinate set."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x01, 0x02, 0x05]
        return super(Coord, cls).__new__(cls, num)

