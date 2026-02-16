"""Base class for battle music."""

class Music:
    """Base class for music"""

    _name: str = ""
    _value: int = 0

    @property
    def name(self) -> str:
        """Name of the music as it appears in the UI"""
        return self._name

    @property
    def value(self) -> int:
        """ID of the music"""
        return self._value
