"""Item description encoding/decoding utilities"""

# item description character mapping (byte -> string)
ITEM_DESC_BYTE_TO_STR = {
    0x01: '\n',
    0x7E: "'",
    0x7D: '-',
    0x9C: '&',
    0x22: '"',
    0x23: '"',
}

# item description character mapping (string -> byte)
ITEM_DESC_STR_TO_BYTE = {
    '\n': 0x01,
    "'": 0x7E,
    '-': 0x7D,
    '&': 0x9C,
    '"': 0x22,
    '"': 0x23,
}

def encode_item_description(desc: str) -> bytearray:
    """encode a description string to bytes using item description character mapping.

    args:
        desc: description string with special characters

    returns:
        bytearray with encoded description
    """
    result = bytearray()
    for char in desc:
        if char in ITEM_DESC_STR_TO_BYTE:
            result.append(ITEM_DESC_STR_TO_BYTE[char])
        else:
            # use latin-1 encoding for regular characters
            result.extend(char.encode('latin-1'))
    return result

def decode_item_description(data: bytes) -> str:
    """decode description bytes to string using item description character mapping.

    args:
        data: bytearray or bytes with encoded description

    returns:
        decoded description string
    """
    result = []
    for byte in data:
        if byte in ITEM_DESC_BYTE_TO_STR:
            result.append(ITEM_DESC_BYTE_TO_STR[byte])
        else:
            # use latin-1 decoding for regular characters
            try:
                result.append(bytes([byte]).decode('latin-1'))
            except:
                result.append('?')
    return ''.join(result)
