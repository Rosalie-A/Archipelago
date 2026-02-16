"""Functions that help with dialog development."""

import re
from collections.abc import Sequence

COMPRESSION_TABLE: list[tuple[str, bytes]] = [
    ("[0x7000]", b"\x1C\x00"),
    ("[0x7024]", b"\x1C\x01"),
    ("[0x7000timer]", b"\x1C\x02"),
    ("[0x70A7]", b"\x1A"),
    ("[filename]", b"\x1C\x03"),
    ("[await][pause]", b"\x05"),
    ("\x20\x20\x20\x20", b"\x0A"),
    ("\x20\x20\x20", b"\x09"),
    ("\x20\x20", b"\x08"),
    ("[await][page]\n", b"\x03"),
    ("[page]\n", b"\x04"),
    ("[await]\n", b"\x02"),
    ("[await]", b"\x00"),
    ("\n", b"\x01"),
    ("[end]", b"\x06"),
    ("[select]", b"\x07"),
    ("[delay]", b"\x0C"),
    ("“", b"\x22"),
    ("”", b"\x23"),
    ("♥", b"\x24"),
    ("♪", b"\x25"),
    ("\u2018", b"\x26"),  # ' left single quote
    ("\u2019", b"\x27"),  # ' right single quote
    ("'", b"\x27"),  # ASCII straight apostrophe maps same as right curly
    ("••", b"\x2B"),
    ("•", b"\x2A"),
    ("~", b"\x3A"),
    ("「", b"\x3B"),
    ("」", b"\x3C"),
    ("『", b"\x3D"),
    ("』", b"\x3E"),
    ("©", b"\x40"),
    (":", b"\x8E"),
    (";", b"\x8F"),
    ("<", b"\x90"),
    (">", b"\x91"),
    ("···", b"\x92"),
    ("#", b"\x93"),
    ("+", b"\x94"),
    ("×", b"\x95"),
    ("%", b"\x96"),
    ("↑", b"\x97"),
    ("→", b"\x98"),
    ("←", b"\x99"),
    ("*", b"\x9A"),
    ("&", b"\x9C"),
]

def compress(string: str, compression_table: Sequence[tuple[str, bytes | bytearray]]) -> bytearray:
    """Turns a dialog string into bytes."""
    output = bytearray()
    tbl = dict(compression_table)
    cursor = 0
    while cursor < len(string):
        regex_result = re.search(r"^(\x20\x20\x20\x20\x20+)", string[cursor:])
        if regex_result:
            token = regex_result.group()
            output += bytearray([0x0B, len(token)])
            cursor += len(token)
            continue
        regex_result = re.search(r"^(\[delay_\d+\])", string[cursor:])
        if regex_result:
            token = regex_result.group()
            di = re.search(r"\d+", token)
            assert di is not None, "Delay tag malformed."
            delay_int = di.group()
            delay = int(delay_int)
            output += bytearray([0x0D, delay])
            cursor += len(token)
            continue
        # Find the LONGEST matching key, not just the first one
        cursor_key = None
        max_length = 0
        for key in tbl:
            if string[cursor:].startswith(key) and len(key) > max_length:
                cursor_key = key
                max_length = len(key)
        if cursor_key:
            tmp = tbl[cursor_key]
            output += tmp
            cursor += len(cursor_key)
            continue
        output.append(ord(string[cursor]))
        cursor += 1
    last_byte = output[len(output) - 1]
    if last_byte not in [0x00, 0x06]:
        output.append(0x00)  # Null terminate strings.
    
    return output

def decompress(b, compression_table: list[tuple[str, bytearray]]) -> str: 
    output = ''
    tbl = dict(compression_table) 
    cursor = 0
    while cursor < len(b):
        if b[cursor] == 0x0B:
            cursor += 1
            spaces = b[cursor]
            output += ' ' * spaces
            cursor += 1
            continue
        if b[cursor] == 0x0D:
            cursor += 1
            delay = b[cursor]
            output += '[delay_%i]' % delay
            cursor += 1
            continue
        tbl_match = None
        for key in tbl:
            # check if bytes at cursor position equals any of the compression table bytearrays
            check = zip(tbl[key], b[cursor:])
            matches = [(b1, b2) for (b1, b2) in check if b1 == b2]
            if len(matches) == len(tbl[key]):
                tbl_match = key
                break
        if tbl_match:
            output += tbl_match
            cursor += len(tbl[tbl_match])
            continue
        output += chr(b[cursor])
        cursor += 1
    return output