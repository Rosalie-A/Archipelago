class AreaObject(int):
    """Base class representing field objects, such as party members and NPCs,
    that can be targeted by overworld and NPC action script commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(AreaObject, cls).__new__(cls, num)

