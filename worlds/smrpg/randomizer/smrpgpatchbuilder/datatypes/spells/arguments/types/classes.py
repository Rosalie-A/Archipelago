"""Helper classes defining constants used in spell development."""

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16

class TimingProperties(UInt16):
    """Preset behaviour that defines how the timed hit for the spell works."""

    def __new__(cls, *args: int):
        num = args[0]
        return super(UInt16, cls).__new__(cls, num)

class DamageModifiers(UInt16):
    """(unknown)"""

    def __new__(cls, *args: int):
        num = args[0]
        return super(UInt16, cls).__new__(cls, num)
