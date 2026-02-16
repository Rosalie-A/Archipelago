class Layer(int):
    """Base class representing a graphical layer in a level."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Layer, cls).__new__(cls, num)