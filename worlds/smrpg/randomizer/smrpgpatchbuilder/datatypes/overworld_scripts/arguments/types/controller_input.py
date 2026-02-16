class ControllerInput(int):
    """Base class representing an input from a specific controller button."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(ControllerInput, cls).__new__(cls, num)

