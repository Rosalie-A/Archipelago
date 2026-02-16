"""Dialog bank definition"""

class DialogBankID(int):
    """A section of the ROM, starting with the same uppermost byte, that contains dialogs"""

    def __new__(cls, *args):
        num = args[0]
        assert 0x22 <= num <= 0x24
        return super(DialogBankID, cls).__new__(cls, num)
