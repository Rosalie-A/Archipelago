from .area_object import AreaObject

class PartyCharacter(AreaObject):
    """Base AreaObject subclass representing field objects that can be targeted
    by commands targeting a pary member, 0x00 to 0x0B, where 0x00-0x04 represent
    your usable party members."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x0B
        return super(PartyCharacter, cls).__new__(cls, num)

