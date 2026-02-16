"""Base classes that inform argument typing in action script command classes."""

class SequenceSpeed(int):
    """The playback speed for a sprite sequence."""

    def __new__(cls, *args) -> "SequenceSpeed":
        num = args[0]
        assert 0 <= num <= 6
        return super(SequenceSpeed, cls).__new__(cls, num)

class VRAMPriority(int):
    """Describes how a drawn sprite for an object behaves when overlapping with the player."""

    def __new__(cls, *args) -> "VRAMPriority":
        num = args[0]
        assert 0 <= num <= 3
        return super(VRAMPriority, cls).__new__(cls, num)
