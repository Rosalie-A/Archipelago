"""Helper classes defining constants used in monster scripts"""

from smrpgpatchbuilder.datatypes.numbers.classes import UInt8, UInt4, ByteField, BitMapSet
from smrpgpatchbuilder.datatypes.spells.enums import TempStatBuff, Status
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix

class Target(int):
    """Base class representing targetable objects in battle by monsters."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(Target, cls).__new__(cls, num)

class CommandType(int):
    """Base class representing command types (spell, attack, item)."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 2
        return super(CommandType, cls).__new__(cls, num)

class DoNothing:
    """Placeholder class representing a do-nothing action (index 0xFB)."""

    index = 0xFB

