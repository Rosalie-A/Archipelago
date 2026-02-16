class Scene(int):
    """Base class representing IDs for some predefined cutscenes and screen transitions."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 16
        return super(Scene, cls).__new__(cls, num)
