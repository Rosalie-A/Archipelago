"""Base classes that inform argument typing in battle script command classes."""

from smrpgpatchbuilder.datatypes.numbers.classes import Int8

class Origin(int):
    """Int subclass representing the origin point that coords should be relative to."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 3
        return super(Origin, cls).__new__(cls, num)

class PauseUntil(int):
    """Int subclass representing the behaviour of a script pause."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 0x10
        return super(PauseUntil, cls).__new__(cls, num)

class ShiftType(int):
    """Int subclass representing the behaviour of an object shift."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 0x08
        assert num % 2 == 0
        return super(ShiftType, cls).__new__(cls, num)

class MessageType(int):
    """Int subclass representing the context of a dialog displayed in battle."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 5
        return super(MessageType, cls).__new__(cls, num)

class LayerPriorityType(int):
    """Int subclass meaningfully representing layer priority in battle animations."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 3
        return super(LayerPriorityType, cls).__new__(cls, num)

class FlashColour(int):
    """Int subclass describing screen flash colours in battle animations."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 8
        return super(FlashColour, cls).__new__(cls, num)

class BonusMessage(int):
    """Int subclass representing the messages that appear from in-battle bonus flowers."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 6
        return super(BonusMessage, cls).__new__(cls, num)

class BattleTarget(int):
    """Int subclass instances representing valid targets in battle animation script commands."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 47
        return super(BattleTarget, cls).__new__(cls, num)

class MaskEffect(int):
    """Int subclass describing screen mask effects in battle animations."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 7
        return super(MaskEffect, cls).__new__(cls, num)

class MaskPoint(tuple[Int8, Int8]):
    """Tuple subclass representing x-y coords in a battle animation screen mask effect."""

    def __new__(cls, *args: int):
        assert len(args) == 2
        tup = (Int8(args[0]), Int8(args[1]))
        return super(MaskPoint, cls).__new__(cls, tup)

    def __reduce__(self):
        return (self.__class__, (self[0], self[1]))

class WaveEffectLayer(int):
    """Int subclass describing screen mask effects in battle animations."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 2
        return super(WaveEffectLayer, cls).__new__(cls, num)

class WaveEffectDirection(int):
    """Int subclass describing screen mask effects in battle animations."""

    def __new__(cls, *args: int):
        num = args[0]
        assert 0 <= num <= 1
        return super(WaveEffectDirection, cls).__new__(cls, num)
