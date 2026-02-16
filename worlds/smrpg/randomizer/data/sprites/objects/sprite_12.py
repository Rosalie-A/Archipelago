# SPR0012_TOADSTOOL_NONPROTAGONIST_6

from randomizer.data.variables.sprite_palette_names import SPAL659_TOADSTOOL_SLAP_ATTACK
from smrpgpatchbuilder.datatypes.graphics.classes import (
    CompleteSprite,
    AnimationPack,
    AnimationPackProperties,
    AnimationSequence,
    AnimationSequenceFrame,
    Mold,
    Tile,
    Clone,
)

sprite = CompleteSprite(
    animation=AnimationPack(
        253,
        length=985,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(30, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'\xec\xe4\x9c\x84\xd8\x18\xe0 \xe0`\x80\x80\x00\x00\x00\x00\xec\x14\x9cd\xd88\xe0 \xe0`\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'\t\x02\t\x02\x07\x18/0=#\x1e\x1e\x00\x00\x00\x00\n\x06\x0b\x07\x1f\x1f<<##\x1e\x1e\x00\x00\x00\x00'),
                            bytearray(b'\x0f\x0f0?\x80\x0f\x97\x16\xf3\x00\xff\xc3<<\x00\x00\x0f\xf0?\xc0\x8fp\x97h\xf3\x0c\xff\xc3<<\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'@\x00\x80\x80\xc0\x80@\x00\xdeD>"\xfc\xfc\xe8\xe8@\x80\x80@\xc0\x00@\x80\xc4Z2\xee\xfc\x0c\xe8\x18'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=116),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'slbo~o\xa9 \x88\x07J\x05~E?<\x9f`\x8eq\x9ea\xd9&\xff\x07\x7f\x07\x7fG??'),
                            bytearray(b'\xff\xf8Oy\xcd9\xfc\x00\x9c\x03\xfd\x02\xf4\n\xe0\x04cc\x83\x02\xc5\x06\xf4\x07\x97g\xf7\x06\xfe\x0f\xe4\x1f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=116),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                            None,
                            bytearray(b'\xc0@\x00\xc0\x00\xe0@\xe0 \xa0\x80\x80  \xc0@\x80\xc0 \xc0\x00\xe0\x00\xe0@\xa0`\x80\xe0 \xc0@'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=100),
                        Tile(mirror=False, invert=False, format=1, length=11, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0e\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x16`_\xa5\xda\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x16\x16\xbf\x7f:\xfa'),
                            bytearray(b'\x0b\x0b\x07\x07\x1f\x1f\x13\x13\x03\x03\x03\x0311zp\x14\x0b\x08\x07 \x1f,\x13\x1c\x03<\x03N1\x0bt'),
                            bytearray(b'\x1c\xc2\x1e\xc4\x1a\xe1\x80\xff\xc0\xff`\x7f\x0b\x0f\xfb\xf83\xf35\xf1\x10\xf5\x00\xff\x00\xf0\x80y\xf0\x0f\x14\x10'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                    ]
                ),
                Mold(1, gridplane=False, tiles=[]),
                Mold(2, gridplane=False, tiles=[]),
                Mold(3, gridplane=False, tiles=[]),
                Mold(4, gridplane=False, tiles=[]),
                Mold(5, gridplane=False, tiles=[]),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'L\x8c\xe0\x9c\xf0\x18p\x00\xb8@\xa0`\xa0p\xf0 \xf3\x0c\xe2\x1c\xe6\x18\xfc\x00x@``ppp`'),
                            None,
                            bytearray(b'\xf00p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00\xf0\xf0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x07\x00\x06\x01\x0e\x03\x08\x03\x04\x07\x00\x07\x01\x02\x00\x00\x05\x05\x05\x04\x0f\x0c\x0b\x0c\x07\x00\x07\x08'),
                            bytearray(b'\x18\xcf\x00\x173\xb3G\xc1\x1d\xfe\x01\xfe\x01\xfe\x00\xff\xff07\xe8\x93\xcc\xc68\xfe\x00\xff\x01\xff\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0`\xe0\xb8\xb8\x80\x90\x00\x00\x00\x00\x00\x00@\x80 \xc0\x10\xe0D\xb8h\x90'),
                            None,
                            bytearray(b'\x98\x98\x10\x10\x00\x00\x10p\xd0\xf0Pp\xa0 \x80\x80`\x98\xe8\x10\xf8\x00\x880\x0c0\x8e\xf0\xde \xff\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x02\x03\x00\x01\x06\x07\x00\x03\x03\x03\x00\x00\x00\x00\x00\x01\x00\x03\x02\x01\x00\x07\x00\x03\x00\x03'),
                            bytearray(b'4\x02~\x01v\x11X\xaa8\xf1\x18\xff\x00\xff\x04\xff""AA\xcfWw\xde6\xc5\x00\xff\x00\x9f\x00\x9f'),
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x03\x03\x03\x03\x00\x01\x00\x03\x00\x03\x00\x01\x02\x00\x02\x00\x00\x03\x00\x03\x01\x02\x03\x00\x03\x00'),
                            bytearray(b'\x94\xf7O_\x0fcI\xa4\x85\xfc\x9a\xf8N\xc44\xd7\x08\xf7\xa0\xc7\x94\x95\x13\x10\x03\x00\x87\x01\xff\x05\xf7('),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xc0\x9cU\x1c\xc1@\xe2\xc0\xf0\xc0\xf8```` \xe3\x1cc\x9c\xff@\xfe\xc0\xfc\xc0\xf8``\xe0`\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x0c\x13\x0c\x13\x00\x0e\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x1b\x1b\x1b\x1b\x0e\x0e\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'\xba\xc7\x98\xa7\x1c c|\x87\x80z\xfe\x00\xfe\x00\xff\xefl\xf7tt\xd7\x7f\x9c\x87x\xfe\x01\xfe\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80 \xc0\xe0\x00'),
                            None,
                            bytearray(b'00  \x00\x00Pp\xd0p\xd00\xa0 \x8c\x8c\xc00\xd0 \xf0\x00\x88p\x8cp\xce0\xde \xf3\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x01\x00\x01\x00\x00\x02\x0c\x0e\x00\x07\x14\x1f$/\x01\x01\x00\x00\x00\x00\x03\x03\x01\x0f\x08\x07\x00\x1e\x10.'),
                            bytearray(b'P\x08\x08\xf4X\xa4\xe6N\xa9\x1f\x01\xff\x01\xff!\xffXX\xfc\xfc\xec\xecX\x1e\x10_\x00\xff\x00\x7f\x00\x7f'),
                            bytearray(b'\x04\x05\x03\x03\x00\x01\x02\x03\t\n\x03\x04\x06\x01\x06\t\x1a\x05\x0c\x01\x06\x02\x04\x00\x07\x0b\x0f\x07\r\x05\r\r'),
                            bytearray(b'y\xff\xef\xef\x00\x825\xf4`\x91\xf3\x0b\xf1\x0c;\xc7\x00\xff\x10\x8f}r\x0b\x04\xfe\xf0<8\x1f\x1e\xef\xec'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\x9cU\x1c\xc1@\xe2\xc0\xf0\xc0\xf8```` \xe3\x1cc\x9c\xff@\xfe\xc0\xfc\xc0\xf8``\xe0`\xa0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x13\x0c\x13\x00\x0e\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x1b\x1b\x1b\x1b\x0e\x0e\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'\xba\xc7\x98\xa7\x1c c|\x87\x80z\xfe\x00\xfe\x00\xff\xefl\xf7tt\xd7\x7f\x9c\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80 \xc0\xe0\x00'),
                            None,
                            bytearray(b'00  \x00\x00Pp\xd0p\xd00\xa0 \x8c\x8c\xc00\xd0 \xf0\x00\x88p\x8cp\xce0\xde \xf3\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x01\x00\x01\x00\x00\x02\x0c\x0e\x00\x07\x14\x1f$/\x01\x01\x00\x00\x00\x00\x03\x03\x01\x0f\x08\x07\x00\x1e\x10.'),
                            bytearray(b'P\x08\x08\xf4X\xa4\xe6N\xa9\x1f\x01\xff\x01\xff!\xffXX\xfc\xfc\xec\xecX\x1e\x10_\x00\xff\x00\x7f\x00\x7f'),
                            bytearray(b'\x04\x05\x03\x03\x00\x01\x02\x03\t\n\x03\x04\x06\x01\x06\t\x1a\x05\x0c\x01\x06\x02\x04\x00\x07\x0b\x0f\x07\r\x05\r\r'),
                            bytearray(b'y\xff\xef\xef\x00\x825\xf4`\x91\xf3\x0b\xf1\x0c;\xc7\x00\xff\x10\x8f}r\x0b\x04\xfe\xf0<8\x1f\x1e\xef\xec'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=101),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xfa\x00\xf4\x04\xf4\x1c\xe0\x00\xf0H``p p \xfe\x00\xfa\x04\xe2\x1c\xfc\x00\xf8H`\xe0p\xa0p\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x04\x07\x00\x07\x01\x01\x00\x00\x00\x00\x01\x00\x03\x00\x03\x04\x07\x00\x07\x08'),
                            bytearray(b'\xa9\xdf!\x10wp\x8f\x809\xff\x00\xff\x00\xff\x00\xff\xff`q\xeew\x88\x8fp\xff\x00\xff\x00\xff\x00\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x80@\x80@`\xe0\x90\xf0\x10\xf0\x18\xf8\xfc\x04\x80\x80\xc0\xc0\xc0\xc0\x80\xe0\x00\xf0\x00\xf0\x80\xf8\x82\x84'),
                            None,
                            bytearray(b'\xf0\x08\xd0 \xa0@\xe8\x00h\x80x\x80|\x00\xf8\x80\x9c\x98|`x@|\x00\xfc\x80\xfe\x80~\x80\xfe\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x05\x1c"\x06\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\r\'&\x0b\n'),
                            bytearray(b'\x05\x10\x1f\x00\x0e \xce\xe4\nyB\xff\xae\xbf1\xfd\x15\x15\x0e\x0e55\x15\xf1\x81}\x00\xe7@\xbf\x82\xa1'),
                            bytearray(b'\x06\x00\x06\x00\x02\x04\x03\x00\x03\x03\x01\x03\x01\x03\x00\x00\x03\x02\x05\x04\x05\x04\x01\x01\x03\x00\x03\x04\x03\x04\x00\x03'),
                            bytearray(b'\xcd1\x86\xfc\xa2\xff\x95\xdc\tZ\x93\xb0\rg\x80\xb7\xce\x01\x03\x00!\x01\x03!\x06\xa2\xce\x02o\xf0\xd7x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00P\x00p\x00 \x00\x00\x00\x04\x00\x02\x00\x01\x00PP\xa8p\x88 P\x00 \x00\x04\x00\x02\x00\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=96),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'l\x0c\xc0\x9c\xd0\x98\xe0\x80\xfc@\xf8 \xf8\x80l\xc0s\x8c\xe3\x9c\xe6\x98\xfe\x80\xfc@\xf8 \xf8\x00\xec\x10'),
                            None,
                            bytearray(b'\\\xc0\xc4\xc0\x9c\x80x\x00>\x1e\xfe>\xf8\xf8\x80\x80\xdc \xc48\x9c`x\x80>\xde\xfe>\xf8\xf8\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x03\x03\x03\x03\x00\x00\x02\x02\x01\x01\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x00\x03\x02\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80\xff\x89\xffwwss\xfcx\xba8\xc3\xc0??\xff\x00\xff\x00w\x88s\x8c\xfc\x03\xbaE\xc3\xfc??'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x80@\x80@`\xe0\x90\xf0\x10\xf0\x18\xf8\xfc\x04\x80\x80\xc0\xc0\xc0\xc0\x80\xe0\x00\xf0\x00\xf0\x80\xf8\x82\x84'),
                            None,
                            bytearray(b'\xf0\x08\xd0 \xa0@\xe8\x00h\x80x\x80|\x00\xf8\x80\x9c\x98|`x@|\x00\xfc\x80\xfe\x80~\x80\xfe\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x05\x1c"\x06\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\r\'&\x0b\n'),
                            bytearray(b'\x05\x10\x1f\x00\x0e \xce\xe4\nyB\xff\xae\xbf1\xfd\x15\x15\x0e\x0e55\x15\xf1\x81}\x00\xe7@\xbf\x82\xa1'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x00\x06\x00\x02\x04\x03\x00\x03\x03\x01\x03\x01\x03\x00\x00\x03\x02\x05\x04\x05\x04\x01\x01\x03\x00\x03\x04\x03\x04\x00\x03'),
                            bytearray(b'\xcd1\x86\xfc\xa2\xff\x95\xdc\tZ\x93\xb0\rg\x80\xb7\xce\x01\x03\x00!\x01\x03!\x06\xa2\xce\x02o\xf0\xd7x'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00'),
                            bytearray(b'\x0c\xbf\x9c\xf8wq\x03\x01\x87\x80z\xfe\x00\xff\x00\xff\xff@\xfc\x03w\x89\x03\xfd\x87x\xfe\x01\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=108),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00P\x00p\x00 \x00\x00\x00\x04\x00\x02\x00\x01\x00PP\xa8p\x88 P\x00 \x00\x04\x00\x02\x00\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=95),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'l\x0c\xc0\x9c\xd0\x98\xe0\x80\xfc@\xf8 \xf8\x80l\xc0s\x8c\xe3\x9c\xe6\x98\xfe\x80\xfc@\xf8 \xf8\x00\xec\x10'),
                            None,
                            bytearray(b'\\\xc0\xc4\xc0\x9c\x80x\x00>\x1e\xfe>\xf8\xf8\x80\x80\xdc \xc48\x9c`x\x80>\xde\xfe>\xf8\xf8\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00'),
                            bytearray(b'\x0c\xbf\x9c\xf8wq\x03\x01\x87\x80z\xfe\x00\xff\x00\xff\xff@\xfc\x03w\x89\x03\xfd\x87x\xfe\x01\xff\x00\xff\x00'),
                            bytearray(b'\x00\x03\x03\x03\x03\x03\x00\x00\x02\x02\x01\x01\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x00\x03\x02\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80\xff\x89\xffwwss\xfcx\xba8\xc3\xc0??\xff\x00\xff\x00w\x88s\x8c\xfc\x03\xbaE\xc3\xfc??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x80@\x80@`\xe0\x90\xf0\x10\xf0\x18\xf8\xfc\x04\x80\x80\xc0\xc0\xc0\xc0\x80\xe0\x00\xf0\x00\xf0\x80\xf8\x82\x84'),
                            None,
                            bytearray(b'\xf0\x08\xd0 \xa0@\xe8\x00h\x80x\x80|\x00\xf8\x80\x9c\x98|`x@|\x00\xfc\x80\xfe\x80~\x80\xfe\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x05\x1c"\x06\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\r\'&\x0b\n'),
                            bytearray(b'\x05\x10\x1f\x00\x0e \xce\xe4\nyB\xff\xae\xbf1\xfd\x15\x15\x0e\x0e55\x15\xf1\x81}\x00\xe7@\xbf\x82\xa1'),
                            bytearray(b'\x06\x00\x06\x00\x02\x04\x03\x00\x03\x03\x01\x03\x01\x03\x00\x00\x03\x02\x05\x04\x05\x04\x01\x01\x03\x00\x03\x04\x03\x04\x00\x03'),
                            bytearray(b'\xcd1\x86\xfc\xa2\xff\x95\xdc\tZ\x93\xb0\rg\x80\xb7\xce\x01\x03\x00!\x01\x03!\x06\xa2\xce\x02o\xf0\xd7x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=100),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00P\x00p\x00 \x00\x00\x00\x04\x00\x02\x00\x01\x00PP\xa8p\x88 P\x00 \x00\x04\x00\x02\x00\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'l\x0c\xc0\x9c\xd0\x98\xe0\x80\xfc@\xf8 \xf8\x80l\xc0s\x8c\xe3\x9c\xe6\x98\xfe\x80\xfc@\xf8 \xf8\x00\xec\x10'),
                            None,
                            bytearray(b'\\\xc0\xc4\xc0\x9c\x80x\x00>\x1e\xfe>\xf8\xf8\x80\x80\xdc \xc48\x9c`x\x80>\xde\xfe>\xf8\xf8\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00'),
                            bytearray(b'\x0c\xbf\x9c\xf8wq\x03\x01\x87\x80z\xfe\x00\xff\x00\xff\xff@\xfc\x03w\x89\x03\xfd\x87x\xfe\x01\xff\x00\xff\x00'),
                            bytearray(b'\x00\x03\x03\x03\x03\x03\x00\x00\x02\x02\x01\x01\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x00\x03\x02\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80\xff\x89\xffwwss\xfcx\xba8\xc3\xc0??\xff\x00\xff\x00w\x88s\x8c\xfc\x03\xbaE\xc3\xfc??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x80@\x80@`\xe0\x90\xf0\x10\xf0\x18\xf8\xfc\x04\x80\x80\xc0\xc0\xc0\xc0\x80\xe0\x00\xf0\x00\xf0\x80\xf8\x82\x84'),
                            None,
                            bytearray(b'\xf0\x08\xd0 \xa0@\xe8\x00h\x80x\x80|\x00\xf8\x80\x9c\x98|`x@|\x00\xfc\x80\xfe\x80~\x80\xfe\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=383, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x05\x1c"\x06\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\r\'&\x0b\n'),
                            bytearray(b'\x05\x10\x1f\x00\x0e \xce\xe4\nyB\xff\xae\xbf1\xfd\x15\x15\x0e\x0e55\x15\xf1\x81}\x00\xe7@\xbf\x82\xa1'),
                            bytearray(b'\x06\x00\x06\x00\x02\x04\x03\x00\x03\x03\x01\x03\x01\x03\x00\x00\x03\x02\x05\x04\x05\x04\x01\x01\x03\x00\x03\x04\x03\x04\x00\x03'),
                            bytearray(b'\xcd1\x86\xfc\xa2\xff\x95\xdc\tZ\x93\xb0\rg\x80\xb7\xce\x01\x03\x00!\x01\x03!\x06\xa2\xce\x02o\xf0\xd7x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=367, y=100),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ` \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=102),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00  \xa8\x88\x88 \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=102),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ` \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00  \xa8\x88\x88 \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ` \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00  \xa8\x88\x88 \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ` \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=105),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=99),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00  \xa8\x88\x88 \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=105),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=99),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ` \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x10\x0e\x10\x0e\x10\x00\x00\x00\x00\x00\x00\x08\x08\x08\x08\x1c\x1c\x1c\x1c\x1c\x1c'),
                            None,
                            bytearray(b'\x18\x04\x10( P@\xa0\x80@\x00\x80\x00\x00\x00\x00\x0c\x0c88pp\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=102),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00  \xa8\x88\x88 \x10 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000000'),
                            None,
                            bytearray(b'4,~~\xcf\xff\xaf\xdf\x9f\xff\xff\xff~~<<<<~~\xff\xff\xff\xff\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=102),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x10\x00\x18\x00|\x00=\x027\x08\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00$$\x07\x07\x1d\x1d\x04\x04\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x05\x02\x07\x00\x05\x00\x01\x00\r\x0c\x18\x1f\x01\x1f\x01\x01\x06\x06\x06\x06\x06\x06\x0f\x03\x13\r\x00\x1f \x1f'),
                            bytearray(b'\x00\xc0 \xd0p\xa0\xf0 t\x1cj~\x01\xff\x11\xff\xc0\xc0\xd0\xd0\xa0\x800\x10\xa0\xbc\x80\xfe\x00\xf9\x00\xfd'),
                            bytearray(b'9?\x1f\x1f\x19\x1f\x1a\x1a;9\x04<J~y|@? \x1f \x1fe\x1aF9C<\x81~\x83|'),
                            bytearray(b'\x9d\xff\xda\xfe\xc1\xc3H#i\xa7\xc8\xce\x96\x06\x80\x08\x00\xff\x00\xf2<\xc4\xdc,P 0\x00\xf8`\xe8x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'p0p0p0p\x10p\x10\xe0 \xc0\xc0\x00\x00p\xb0p\xb0p\xb0p\x90p\x90\xe0 \xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x06\x07\x07\x07\x03\x03\x13\x13\t\t\x07\x07\x00\x00\x07\x08\x07\x18\x07\x18\x03\x1c\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b'\x00\xff \xff\xb0\xfe\xdc\xdc\xc8\xc8\xc0\xc0!\x00\xff\xff\xff\x00\xff\x00\xfe\x01\xdc#\xc87\xc0?!\xde\xff\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x84\x04\x80\x80B\x00\xc4\x00\xc4\x80\xf8@`@` \xfa\x04\xfe\x00~\x80\xfc\x00\xfc\x80\xf8@`\xc0`\xa0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x04\x07\x08\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x07\x08\x0f\x00'),
                            bytearray(b'A\xa3\x0c\xbf\x007a`\x87\x80z\xfe\x00\xfe\x00\xff\xe3|\xdf`w\xc8a\x9e\x87x\xfe\x01\xfe\x01\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=116),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            bytearray(b'\xc0\x00\x80\x80\x80\x80\x80\x80\x00\x00@\x80\x00\x00\x00\x00\xc0\x00\x80@\x80@\x80@\x00\xc0\xc0\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x101 sC?\x00?\x00?\x00\x1f\x00\x1f\x00?\x101.sL'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xb0\x80\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xbf@'),
                            bytearray(b"sL]~>\\\'=\x0f\x0c\x05\x04\x03\x03\x00\x00\x7f\\\x7f\x7f\x7f|><\x0c\x0f\x06\x05\x03\x03\x00\x00"),
                            bytearray(b'y8o\x8f\xbbC\xaa4\xfd\xde\xfe\x87\xbf\x9f\xf0\xf0y\x86\xef\x90\xfbd\xfe=\x9f\xbe\x87\xff\xdf\xbf\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            None,
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x07<Cp\x8f\x00\xff\x008\x00\x00\x00\x00\x00\x00\x07\x07\x7f\x7f\xff\xff\xff\xff88\x00\x00\x00\x00'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x10(\x148D\xf8\x00\xf8\x00p\x08\x00\x00\x00\x0000\x1c\x1c\\\\xx8888'),
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x0e\t\x04\x1e\x08\x18\x18\x18\x00\x00\x00\x00\x00\x00\x01\x01\x0f7\x1eb\x18d\x18d\x008'),
                            bytearray(b'\xc0 \x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=103),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            bytearray(b'\xc0\x00\x80\x80\x80\x80\x80\x80\x00\x00@\x80\x00\x00\x00\x00\xc0\x00\x80@\x80@\x80@\x00\xc0\xc0\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"sL]~>\\\'=\x0f\x0c\x05\x04\x03\x03\x00\x00\x7f\\\x7f\x7f\x7f|><\x0c\x0f\x06\x05\x03\x03\x00\x00"),
                            bytearray(b'y8o\x8f\xbbC\xaa4\xfd\xde\xfe\x87\xbf\x9f\xf0\xf0y\x86\xef\x90\xfbd\xfe=\x9f\xbe\x87\xff\xdf\xbf\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            None,
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07<Cp\x8f\x00\xff\x008\x00\x00\x00\x00\x00\x00\x07\x07\x7f\x7f\xff\xff\xff\xff88\x00\x00\x00\x00'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x101 sC?\x00?\x00?\x00\x1f\x00\x1f\x00?\x101.sL'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xb0\x80\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x10(\x148D\xf8\x00\xf8\x00p\x08\x00\x00\x00\x0000\x1c\x1c\\\\xx8888'),
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x0e\t\x04\x1e\x08\x18\x18\x18\x00\x00\x00\x00\x00\x00\x01\x01\x0f7\x1eb\x18d\x18d\x008'),
                            bytearray(b'\xc0 \x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=102),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            bytearray(b'\xc0\x00\x80\x80\x80\x80\x80\x80\x00\x00@\x80\x00\x00\x00\x00\xc0\x00\x80@\x80@\x80@\x00\xc0\xc0\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x101 sC?\x00?\x00?\x00\x1f\x00\x1f\x00?\x101.sL'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xb0\x80\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xbf@'),
                            bytearray(b"sL]~>\\\'=\x0f\x0c\x05\x04\x03\x03\x00\x00\x7f\\\x7f\x7f\x7f|><\x0c\x0f\x06\x05\x03\x03\x00\x00"),
                            bytearray(b'y8o\x8f\xbbC\xaa4\xfd\xde\xfe\x87\xbf\x9f\xf0\xf0y\x86\xef\x90\xfbd\xfe=\x9f\xbe\x87\xff\xdf\xbf\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07<Cp\x8f\x00\xff\x008\x00\x00\x00\x00\x00\x00\x07\x07\x7f\x7f\xff\xff\xff\xff88\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=109),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x10(\x148D\xf8\x00\xf8\x00p\x08\x00\x00\x00\x0000\x1c\x1c\\\\xx8888'),
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x0e\t\x04\x1e\x08\x18\x18\x18\x00\x00\x00\x00\x00\x00\x01\x01\x0f7\x1eb\x18d\x18d\x008'),
                            bytearray(b'\xc0 \x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=101),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 `\x00\x00\x00\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'C\x03C\x03c\x033\x03\x19\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03<\x03\x1e\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\xe0\x10\xf0\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xa0\x00p\x08p'),
                            None,
                            bytearray(b'\x08\xf8\x10\xf0\xa0\xe0\x80\x80\xc0\xc0 \xe0\x00\xc0\x00\xc0\x008\x00\xf0\x00\xe0`\x80 \xc0\x00\xe0\x00\xc0\x00@'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x07\x03\x03\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x07\x04\x03\x06\t'),
                            bytearray(b'\n\x00\x0f\x00\x1f\x00\x1f\x03\xef\xf8\xe6\xf0\x8e\xff\x00\xff\n\n\x06\x06\x17\x17\xf8\x1b\x1b\xf3\x13\xfb\x00\xff\x00\xff'),
                            bytearray(b'\x02\x00\x02\x00\x06\x00\x04\x00\x00\x00\x01\x01\x01\x01\x01\x01\x07\x00\x07\x00\x07\x00\x0f\x00\x0f\x00\x1e\x01>\x01>\x01'),
                            bytearray(b'\x80\xff\x80\xff@\x7fs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x80q\x80\x7f\xe0\x1f\xe0\x1f\x00\xfc\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0c\x00\x0c\x13\xeb\xf4\xe7\xe8\xcc\xd2\xdc\xc0\x18$\x008\x00\x00\x1f\x1f\xfc\x1c\xec\x1c\xd66\xd444\xf488'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=113),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 `\x00\x00\x00\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'C\x03C\x03c\x033\x03\x19\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03<\x03\x1e\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\xe0\x10\xf0\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xa0\x00p\x08p'),
                            None,
                            bytearray(b'\x08\xf8\x10\xf0\xa0\xe0\x80\x80\xc0\xc0 \xe0\x00\xc0\x00\xc0\x008\x00\xf0\x00\xe0`\x80 \xc0\x00\xe0\x00\xc0\x00@'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x07\x03\x03\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x07\x04\x03\x06\t'),
                            bytearray(b'\n\x00\x0f\x00\x1f\x00\x1f\x03\xef\xf8\xe6\xf0\x8e\xff\x00\xff\n\n\x06\x06\x17\x17\xf8\x1b\x1b\xf3\x13\xfb\x00\xff\x00\xff'),
                            bytearray(b'\x02\x00\x02\x00\x06\x00\x04\x00\x00\x00\x01\x01\x01\x01\x01\x01\x07\x00\x07\x00\x07\x00\x0f\x00\x0f\x00\x1e\x01>\x01>\x01'),
                            bytearray(b'\x80\xff\x80\xff@\x7fs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x80q\x80\x7f\xe0\x1f\xe0\x1f\x00\xfc\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0c\x00\x0c\x13\xeb\xf4\xe7\xe8\xcc\xd2\xdc\xc0\x18$\x008\x00\x00\x1f\x1f\xfc\x1c\xec\x1c\xd66\xd444\xf488'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80@\xc0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x00\xc0\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 `\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03C\x03C\x03c\x031\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03|\x03>\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x03\x06\x074?\x1c\x1f\x00\x00\x00\x00\x01\x01\x07\x01\x05\x03\t\x07\x00? \x1f'),
                            bytearray(b'\xa0\x00\xf8\x00\xf8\x00\xf83\xfc\x87h\x0f\xe0\xff\x00\xff\xa0\xa0``pp\x80\xb7\xbc;0\xbf\x00\xfb\x00\xf9'),
                            bytearray(b"$\'\n\x03\x0b\x03\x19\x01\x10\x00\x02\x02\x03\x03\x03\x03\x18\'\x1c\x03\x1c\x03\x1e\x01\x1f\x00=\x02<\x03|\x03"),
                            bytearray(b'\x00\xff\x00\xfe\x03\xff\xcf\xff\x7f\x7f8?\xe0\xff\xc0\xff\x00\x81\x01\x82\x00\xc7\x00\xff\x80\x7f\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'8\xc00\xc80\xc8p\x80 \x90\xe0\xd0\xc0\xc0\xc0\xc0\xe8\xe8\xe8\xe8\xc8\xc8\xd0\xd0\x90\xd0\xf00\xc0 \xc0 '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00XX\xa6`\x9eR\xac\x1f\xe0\x1f\xe0\x1e\xe1\x1c\xe2XX\xfe\xfe\xfe\xfe\xee\xee\xe9\xe9\xe1\xe1\xef\xef\xfe\xfe'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=102),
                    ]
                ),
                Mold(29, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80@\xc0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x00\xc0\x00\xc0'),
                            None,
                            bytearray(b'\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 `\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03C\x03C\x03c\x031\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03|\x03>\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x03\x06\x074?\x1c\x1f\x00\x00\x00\x00\x01\x01\x07\x01\x05\x03\t\x07\x00? \x1f'),
                            bytearray(b'\xa0\x00\xf8\x00\xf8\x00\xf83\xfc\x87h\x0f\xe0\xff\x00\xff\xa0\xa0``pp\x80\xb7\xbc;0\xbf\x00\xfb\x00\xf9'),
                            bytearray(b"$\'\n\x03\x0b\x03\x19\x01\x10\x00\x02\x02\x03\x03\x03\x03\x18\'\x1c\x03\x1c\x03\x1e\x01\x1f\x00=\x02<\x03|\x03"),
                            bytearray(b'\x00\xff\x00\xfe\x03\xff\xcf\xff\x7f\x7f8?\xe0\xff\xc0\xff\x00\x81\x01\x82\x00\xc7\x00\xff\x80\x7f\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00XX\xa6`\x9eR\xac\x1f\xe0\x1f\xe0\x1e\xe1\x1c\xe2XX\xfe\xfe\xfe\xfe\xee\xee\xe9\xe9\xe1\xe1\xef\xef\xfe\xfe'),
                            None,
                            bytearray(b'8\xc00\xc80\xc8p\x80 \x90\xe0\xd0\xc0\xc0\xc0\xc0\xe8\xe8\xe8\xe8\xc8\xc8\xd0\xd0\x90\xd0\xf00\xc0 \xc0 '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=101),
                    ]
                ),
                Mold(30, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80@\xc0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x00\xc0\x00\xc0'),
                            None,
                            bytearray(b'\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x80\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 `\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03C\x03C\x03c\x031\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03|\x03>\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x03\x06\x074?\x1c\x1f\x00\x00\x00\x00\x01\x01\x07\x01\x05\x03\t\x07\x00? \x1f'),
                            bytearray(b'\xa0\x00\xf8\x00\xf8\x00\xf83\xfc\x87h\x0f\xe0\xff\x00\xff\xa0\xa0``pp\x80\xb7\xbc;0\xbf\x00\xfb\x00\xf9'),
                            bytearray(b"$\'\n\x03\x0b\x03\x19\x01\x10\x00\x02\x02\x03\x03\x03\x03\x18\'\x1c\x03\x1c\x03\x1e\x01\x1f\x00=\x02<\x03|\x03"),
                            bytearray(b'\x00\xff\x00\xfe\x03\xff\xcf\xff\x7f\x7f8?\xe0\xff\xc0\xff\x00\x81\x01\x82\x00\xc7\x00\xff\x80\x7f\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00XX\xa6`\x9eR\xac\x1f\xe0\x1f\xe0\x1e\xe1\x1c\xe2XX\xfe\xfe\xfe\xfe\xee\xee\xe9\xe9\xe1\xe1\xef\xef\xfe\xfe'),
                            None,
                            bytearray(b'8\xc00\xc80\xc8p\x80 \x90\xe0\xd0\xc0\xc0\xc0\xc0\xe8\xe8\xe8\xe8\xc8\xc8\xd0\xd0\x90\xd0\xf00\xc0 \xc0 '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=99),
                    ]
                ),
                Mold(31, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'l\x0c\xc0\x9c\xd0\x98\xe0\x80\xfc@\xf8 \xf8\x80l\xc0s\x8c\xe3\x9c\xe6\x98\xfe\x80\xfc@\xf8 \xf8\x00\xec\x10'),
                            None,
                            bytearray(b'\\\xc0\xc4\xc0\x9c\x80x\x00>\x1e\xfe>\xf8\xf8\x80\x80\xdc \xc48\x9c`x\x80>\xde\xfe>\xf8\xf8\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00'),
                            bytearray(b'\x0c\xbf\x9c\xf8wq\x03\x01\x87\x80z\xfe\x00\xff\x00\xff\xff@\xfc\x03w\x89\x03\xfd\x87x\xfe\x01\xff\x00\xff\x00'),
                            bytearray(b'\x00\x03\x03\x03\x03\x03\x00\x00\x02\x02\x01\x01\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x00\x03\x02\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80\xff\x89\xffwwss\xfcx\xba8\xc3\xc0??\xff\x00\xff\x00w\x88s\x8c\xfc\x03\xbaE\xc3\xfc??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x80@\x80@`\xe0\x90\xf0\x10\xf0\x18\xf8\xfc\x04\x80\x80\xc0\xc0\xc0\xc0\x80\xe0\x00\xf0\x00\xf0\x80\xf8\x82\x84'),
                            None,
                            bytearray(b'\xf0\x08\xd0 \xa0@\xe8\x00h\x80x\x80|\x00\xf8\x80\x9c\x98|`x@|\x00\xfc\x80\xfe\x80~\x80\xfe\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=383, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009\x05\x1c"\x06\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\r\'&\x0b\n'),
                            bytearray(b'\x05\x10\x1f\x00\x0e \xce\xe4\nyB\xff\xae\xbf1\xfd\x15\x15\x0e\x0e55\x15\xf1\x81}\x00\xe7@\xbf\x82\xa1'),
                            bytearray(b'\x06\x00\x06\x00\x02\x04\x03\x00\x03\x03\x01\x03\x01\x03\x00\x00\x03\x02\x05\x04\x05\x04\x01\x01\x03\x00\x03\x04\x03\x04\x00\x03'),
                            bytearray(b'\xcd1\x86\xfc\xa2\xff\x95\xdc\tZ\x93\xb0\rg\x80\xb7\xce\x01\x03\x00!\x01\x03!\x06\xa2\xce\x02o\xf0\xd7x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=367, y=100),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=12, mold_id=3),
                        AnimationSequenceFrame(duration=12, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=8, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=31),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=23),
                        AnimationSequenceFrame(duration=4, mold_id=24),
                        AnimationSequenceFrame(duration=4, mold_id=25),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=26),
                        AnimationSequenceFrame(duration=8, mold_id=27),
                        AnimationSequenceFrame(duration=6, mold_id=28),
                        AnimationSequenceFrame(duration=6, mold_id=29),
                        AnimationSequenceFrame(duration=6, mold_id=30),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL659_TOADSTOOL_SLAP_ATTACK,
    palette_offset=0,
    unknown_num=0,
)
