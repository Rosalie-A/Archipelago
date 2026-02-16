import math

def dbyte_str(offset=0):
    def inner_dbyte(args):
        if len(args) < 1:
            raise ValueError(f"dbyte_str: Expected at least 1 byte, got {len(args)} bytes")
        return "0x%04x" % (2 * args[0] + offset), args[1:]

    return inner_dbyte

def hbyte_str(offset=0):
    def inner_hbyte(args):
        if len(args) < 1:
            raise ValueError(f"hbyte_str: Expected at least 1 byte, got {len(args)} bytes")
        return "0x%04x" % (0x20 * args[0] + offset), args[1:]

    return inner_hbyte

def dbyte(offset=0):
    def inner_dbyte(args):
        if len(args) < 1:
            raise ValueError(f"dbyte: Expected at least 1 byte, got {len(args)} bytes")
        return (2 * args[0] + offset), args[1:]

    return inner_dbyte

def hbyte(offset=0):
    def inner_hbyte(args):
        if len(args) < 1:
            raise ValueError(f"hbyte: Expected at least 1 byte, got {len(args)} bytes")
        return (0x20 * args[0] + offset), args[1:]

    return inner_hbyte

def shortify(arr: bytearray, dex: int) -> int:
    if len(arr) < dex + 2:
        raise ValueError(f"shortify: Expected at least {dex + 2} bytes, got {len(arr)} bytes")
    return arr[dex] + (arr[dex + 1] << 8)

def shortify_signed(arr, dex):
    if len(arr) < dex + 2:
        raise ValueError(f"shortify_signed: Expected at least {dex + 2} bytes, got {len(arr)} bytes")
    num = arr[dex] + (arr[dex + 1] << 8)
    if num > 32767:
        offset = num - 32767 - 1
        num = -32768 + offset
    assert -32768 <= num <= 32767
    return num

def byte_signed(num):
    if num > 127:
        offset = num - 127 - 1
        num = -128 + offset
    assert -128 <= num <= 127
    return num

def bit(arr, dex, bit_num):
    return (arr[dex] & (1 << bit_num)) >> bit_num

def bit_bool_from_num(num, bit_num):
    return ((num & 1 << bit_num) >> bit_num) == 1

def byte_str(offset=0, prefix="", table=None):
    def inner_byte(args):
        if len(args) < 1:
            raise ValueError(f"byte_str: Expected at least 1 byte, got {len(args)} bytes")
        if table and args[0] in table:
            return "%s%s" % (prefix and (prefix + "."), table[args[0]]), args[1:]
        return "0x%02x" % (args[0] + offset), args[1:]

    return inner_byte

def byte(offset=0, prefix="", table=None):
    def inner_byte(args):
        if len(args) < 1:
            raise ValueError(f"byte: Expected at least 1 byte, got {len(args)} bytes")
        return (args[0] + offset), args[1:]

    return inner_byte

def byte_int_str(offset=0):
    def inner_byte(args):
        if len(args) < 1:
            raise ValueError(f"byte_int_str: Expected at least 1 byte, got {len(args)} bytes")
        return "%i" % (args[0] + offset), args[1:]

    return inner_byte

def byte_int(offset=0):
    def inner_byte(args):
        if len(args) < 1:
            raise ValueError(f"byte_int: Expected at least 1 byte, got {len(args)} bytes")
        return (args[0] + offset), args[1:]

    return inner_byte

def short_int_Str(offset=0):
    def inner_short(args):
        if len(args) < 2:
            raise ValueError(f"short_int_Str: Expected at least 2 bytes, got {len(args)} bytes")
        return "%i" % (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short

def short_int(offset=0):
    def inner_short(args):
        if len(args) < 2:
            raise ValueError(f"short_int: Expected at least 2 bytes, got {len(args)} bytes")
        return (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short

def short_str(offset=0):
    def inner_short(args):
        if len(args) < 2:
            raise ValueError(f"short_str: Expected at least 2 bytes, got {len(args)} bytes")
        return "0x%04x" % (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short

def short(offset=0):
    def inner_short(args):
        if len(args) < 2:
            raise ValueError(f"short: Expected at least 2 bytes, got {len(args)} bytes")
        return (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short

def con_str(constant):
    def inner_con(args):
        return "0x%02x" % (constant), args

    return inner_con

def con(constant):
    def inner_con(args):
        return constant, args

    return inner_con

def con_int_str(constant):
    def inner_con(args):
        return "%i" % (constant), args

    return inner_con

def con_int(constant):
    def inner_con(args):
        return constant, args

    return inner_con

def con_bitarray_str(arr):
    def inner_con(args):
        return "%r" % (arr), args

    return inner_con

def con_bitarray(arr):
    def inner_con(args):
        return arr, args

    return inner_con

def named(name, *arg_parsers):
    def inner_named(args):
        acc = []
        for parse in arg_parsers:
            parsed_arg, args = parse(args)
            acc.append(parsed_arg)
        return name, acc

    return inner_named

def build_table(list):
    return {i.index: i.name for i in list}

def use_table_name(prefix, table, val):
    return "%s%s" % (prefix and (prefix + "."), table[val])

def flags_short(prefix="", table=None, bits=None):
    return flags(prefix, table, bits, size=2)

def flags_short_str(prefix="", table=None, bits=None):
    return flags_str(prefix, table, bits, size=2)

def flags_str(prefix="", table=None, bits=None, size=None):
    def inner_flags(args):
        if size:
            length = size
        elif bits:
            length = math.ceil(max(bits) / 8)
        else:
            length = 1
        b = get_flag_string(args[:length], prefix, table, bits)
        return b, args[length:]

    return inner_flags

def flags(prefix="", table=None, bits=None, size=None):
    def inner_flags(args):
        if size:
            length = size
        elif bits:
            length = math.ceil(max(bits) / 8)
        else:
            length = 1
        b = parse_flags(args[:length], prefix, table, bits)
        return b, args[length:]

    return inner_flags

def get_flag_string(value, prefix="", table=None, bits=None):
    b = parse_flags_as_str(value, prefix, table, bits)
    if len(b) > 0:
        return "[%s]" % (", ".join(b))
    else:
        return "[]"

def parse_flags_as_str(value, prefix="", table=None, bits=None):
    val = 0x00
    if isinstance(value, bytearray):
        for i in range(len(value)):
            val |= value[i] << (8 * i)
    else:
        val = value
    if not bits:
        bits_to_check = [i for i in range(val.bit_length())]
    else:
        bits_to_check = [i for i in bits]
    b = []
    for i in bits_to_check:
        if val & (1 << i) > 0:
            if table and prefix:
                b.append("%s" % (use_table_name(prefix, table, i)))
            else:
                b.append("%i" % i)
    return b

def parse_flags(value, prefix="", table=None, bits=None):
    val = 0x00
    if isinstance(value, bytearray):
        for i in range(len(value)):
            val |= value[i] << (8 * i)
    else:
        val = value
    if not bits:
        bits_to_check = [i for i in range(val.bit_length())]
    else:
        bits_to_check = [i for i in bits]
    b = []
    for i in bits_to_check:
        if val & (1 << i) > 0:
            b.append(i)
    return b

def writeline(f, ln):
    print(ln.replace("\x00", ""), file=f)

def writeline_dialog(f, ln):
    print(ln, file=f)
