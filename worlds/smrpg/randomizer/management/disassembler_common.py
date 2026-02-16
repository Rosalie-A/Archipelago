import math


def dbyte(offset=0):
    def inner_dbyte(args):
        return "0x%04x" % (2 * args[0] + offset), args[1:]

    return inner_dbyte


def hbyte(offset=0):
    def inner_hbyte(args):
        return "0x%04x" % (0x20 * args[0] + offset), args[1:]

    return inner_hbyte


def shortify(arr, dex):
    return arr[dex] + (arr[dex + 1] << 8)


def shortify_signed(arr, dex):
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
    return (arr[dex] & 1 << bit_num) >> bit_num


def bit_bool_from_num(num, bit_num):
    return ((num & 1 << bit_num) >> bit_num) == 1


def byte(offset=0, prefix="", table=None):
    def inner_byte(args):
        if table and args[0] in table:
            return "%s%s" % (prefix and (prefix + "."), table[args[0]]), args[1:]
        return "0x%02x" % (args[0] + offset), args[1:]

    return inner_byte


def byte_int(offset=0):
    def inner_byte(args):
        return "%i" % (args[0] + offset), args[1:]

    return inner_byte


def short_int(offset=0):
    def inner_short(args):
        return "%i" % (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short


def short(offset=0):
    def inner_short(args):
        return "0x%04x" % (args[0] + (args[1] << 8) + offset), args[2:]

    return inner_short


def con(constant):
    def inner_con(args):
        return "0x%02x" % (constant), args

    return inner_con


def con_int(constant):
    def inner_con(args):
        return "%i" % (constant), args

    return inner_con


def con_bitarray(arr):
    def inner_con(args):
        return "%r" % (arr), args

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


def flags(prefix="", table=None, bits=None, size=None):
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


def get_flag_string(value, prefix="", table=None, bits=None):
    b = parse_flags(value, prefix, table, bits)
    if len(b) > 0:
        return "[%s]" % (", ".join(b))
    else:
        return "[]"


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
            if table and prefix:
                b.append("%s" % (use_table_name(prefix, table, i)))
            else:
                b.append("%i" % i)
    return b


def writeline(f, ln):
    print(ln.replace("\x00", ""), file=f)


def writeline_dialog(f, ln):
    print(ln, file=f)
