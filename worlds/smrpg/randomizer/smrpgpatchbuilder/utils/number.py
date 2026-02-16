"""Numerical util functions."""

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt8
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.byte_var import (
    ByteVar,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.short_var import (
    ShortVar,
)

def bools_to_int(*args: bool) -> int:
    """Accepts a series of bools and creates an int value
    by setting bits to true or false according to the order of
    the given bools. e.g. True, False, False, True = 9"""
    base: int = 0
    position: int
    val: bool
    for position, val in enumerate(args):
        base += val << position
    return base

def set_bits_to_true(bits: list[int]) -> list[bool]:
    """Sets bools in a list to true according to the indexes given
    in the bits argument."""
    array_size = 0
    if len(bits) > 0:
        array_size = max(bits) + 1
    bit_array: list[bool] = [False] * array_size
    for bit in bits:
        bit_array[bit] = True
    return bit_array

def bits_to_int(bits: list[int]) -> int:
    """Accepts a slice of ints and creates an int value
    by setting bits to true at the indexes indicated by
    the bits argument. e.g. [0, 3] = 9"""
    if len(bits) == 0:
        return 0
    bit_array: list[bool] = set_bits_to_true(bits)
    return bools_to_int(*bit_array)

def cast_const(value: UInt16 | UInt8 | int) -> UInt16 | UInt8:
    """Convert a number into a uint8 or a uint16 depending on size"""
    if 0 <= value <= 0xFF:
        return UInt8(value)
    return UInt16(value)

def cast_address(address: ShortVar | ByteVar) -> ShortVar | ByteVar:
    """Convert an address into a uint8 or a uint16 depending on size"""
    if 0x70A0 <= address <= 0x719F:
        return ByteVar(address)
    return ShortVar(address)
