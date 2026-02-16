class IntroTitleText(int):
    """Base class representing predefined texts that are displayed in the game's intro."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 5
        return super(IntroTitleText, cls).__new__(cls, num)
