# SPR0021_MALLOW_NONPROTAGONIST_3

from randomizer.data.variables.sprite_palette_names import (
    SPAL697_MALLOW_WALKING_DOWN_LEFT,
)
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
        262,
        length=535,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=2,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x02\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x01\x01\x0e\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x10\x00"
                                ),
                                bytearray(
                                    b"\x00\x00#\x00\x06\x01\x04\x0b\x14\x1b\x11\x1b\xd5\xd2\x1c\xa3\x01\x00\x04\x00\t\x00\x03\x00\x03\x00/\x08)\x01D\x00"
                                ),
                                bytearray(
                                    b"\xc0\xc08\xc8\x1e\xe1_\xe0\x1f\xe0\xff\x80\xde!\xc1\xbf \x00\xc6\x00\xe0\x00\xe0\x00\xc0\x00\xc0@    "
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\x00\xc0\xe0\xa0` \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00"
                                ),
                                bytearray(
                                    b"\x0f\x10\x061\x00.\n\x1f\x08\x18\x00\x00\x00\x00\x00\x00 \x00\x08\x00\x1b\n\x15\x15\x12\x10\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x84?3|\x1a\xdf\x1f/\x0e?6\x0f=\x11\x96\xebD\x04\xc0@\xe3\xc17070+8.\x1c\xfc\x1c"
                                ),
                                bytearray(
                                    b"\xc9\xf0\xb6\xc6\xf2\x8dc\xecK\xd4E\xd6\x82\xfa\xc0?\xa6\xa0\x89\x80\x08\x08\x90\x80\xb0\x10\xb8\x10}x\x07\x1f"
                                ),
                                bytearray(
                                    b"\xa0` \xe0\x00\xd0\x00\xf0\xe0@\x80\xa0\x00\xe0\xa0@P@\x90\x800\x1000 \x00` \xe0\xe0\xc0\xc0"
                                ),
                                None,
                                bytearray(
                                    b"\x01\xfef\xf9}|\x1d<\x00\x00\x01\x01\x0f\x0f\x01\x01\xff\x07\xff\x81}\x02<#\x00\x1c\x01\x01\x0f\x0f\x01\x01"
                                ),
                                bytearray(
                                    b"\x90_\x10\xd0\x82=\x81|>\xfe\xdd\xdc\xfe\xe0\xfc\xfc\xe0\xff\xef\xfe\x7f\xc5}\x82\xfe\x81\xdc\xe3\xfe\xe0\xfc\xfc"
                                ),
                                bytearray(
                                    b"`\xc0\xe0 \xc0\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00  \x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    1,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=2,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\x00\x03\x03\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x04\x03\x08\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x0c\x0cVi\xbe\xe5?\xc5\xfe\x02\x00\x00\x00\x00\x00\x00\x12\x000p~\xda\x03\x02\x00\x01"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xbc`@|\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x84\xe4\x0e\xf0"
                                ),
                                None,
                                bytearray(
                                    b"\x0f\x08\x07\x08\x1f\x10\x0f\x10GXX_\x9f\xdf?\xdf\x10\x00\x10\x00 \x00`\x00 \x00\xa0\x00 \x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x80\xbd\xc3\xc3\xff\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xa0?$\xdb\x9cS\xe8oUqe\x11h\x18r\n\x8fqg]\x077\x13\x03\x8b\x01\x8b\x01\x86\x00\x86\x02"
                                ),
                                None,
                                bytearray(
                                    b"l\xcc\x0c\xbf\x04S\xd8\xef16\x07\x01\x07\x07\x03\x03\x13\x00S\x10\xffT\xff\xe871\x07\x06\x07\x00\x03\x03"
                                ),
                                bytearray(
                                    b"\xfe\xff}x\xf0\xe3d\x1b\x0fw0p\xc0\xc0\x00\x00\x01\x01\x86\x04\x9e\x12\x7f\xfb\x7f\xf7p\xf0\xc0\xc0\x00\x00"
                                ),
                                bytearray(
                                    b"\xb0L\x14\xael>R\x04\xa6\xd4\xaa\xd4nf\x1c\x1c\x02\x00B\x02\x82\x02\xaa\x00\xaa\x80\xee\xc4~f\x1c\x1c"
                                ),
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    2,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=2,
                            length=15,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x05\x04\x05\r\x01\t\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x08\x00\n\x08\x0e\x08"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x1f\x10o\xc0k\x84\x00\x00\x00\x00\x00\x00\x03\x03\x00\x00\xa0\x00\x10\x00\x10\x00"
                                ),
                                bytearray(
                                    b"\x80`\x00\xf0\x08\xf0\x06\xf8\x07\xf8\x8fp\xf7\x18\xff\x00\xf0\x80\xf0\x00\xfc\x08y\x00x\x008\x08\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"@\x18\x18P@@\x0c\x0cD\\\xa0`\xe0`\xa00\x00\x00 \x00\xb8\x00\xf0\x00\xa0\x00\x18\x00\x18\x00P\x10"
                                ),
                                bytearray(
                                    b"\x00\x04\x00\x04\x00\x02\x00\x02\x00\x03\x00\x01\x00\x01\x00\x00\x07\x04\x07\x04\x03\x02\x03\x02\x03\x03\x01\x01\x01\x01\x00\x00"
                                ),
                                bytearray(
                                    b'c\xec\xd9\xde\xde\xdf/c"m,\xaf\x06\x96,\xd1\x10\x00 \x00 \x00\x90\x00\x90\x00\xd0\x80\xf9\x90\xff\xdd'
                                ),
                                bytearray(
                                    b"\xff\x00\xff\x00<\xc3\xe1\xff\xfc\xfcy\xf8\xc1\xc6\x01\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00?\x06\xfd\x1e"
                                ),
                                bytearray(
                                    b"\x00\x90\x00\xa0\x00\x00\x00\x00@\x80\x00\x00\x00\x80\x80\x80p\x10` \xc0\x00\xc0\x00\xc0\xc0\x80\x80\x80\x80\x00\x80"
                                ),
                                None,
                                bytearray(
                                    b"\x0f@s c\x1f\x8f\x8f\x87\x80\x96\x9a{u\x1e\x1eOpX_`\x7f\x90\xff\x87\xf8\x9e\xe5\x7fk\x1e\x1e"
                                ),
                                bytearray(
                                    b"\x01\xf1\x1e\x1aH\xb6s\xeb\xf7\xe7\xfe\xfe\x80\x80\x00\x00\xf0\xff\x1d\xe5\xc2\xc2\x9b\x9d\xe7\xf9\xfe\xfe\x80\x80\x00\x00"
                                ),
                                None,
                            ],
                            is_16bit=True,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(3, gridplane=True, tiles=[]),
                Mold(4, gridplane=True, tiles=[]),
                Mold(5, gridplane=True, tiles=[]),
                Mold(6, gridplane=True, tiles=[]),
                Mold(7, gridplane=False, tiles=[]),
                Mold(8, gridplane=False, tiles=[]),
                Mold(
                    9,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=2,
                            length=15,
                            subtile_bytes=[
                                bytearray(
                                    b"\x02\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x01\x01\x0e\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x10\x00"
                                ),
                                bytearray(
                                    b"\x00\x00#\x00\x06\x01\x04\x0b\x14\x1b\x11\x1b\xd5\xd2\x1c\xa3\x01\x00\x04\x00\t\x00\x03\x00\x03\x00/\x08)\x01D\x00"
                                ),
                                bytearray(
                                    b"\xc0\xc08\xc8\x1e\xe1_\xe0\x1f\xe0\xff\x80\xde!\xc1\xbf \x00\xc6\x00\xe0\x00\xe0\x00\xc0\x00\xc0@    "
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\x00\xc0\xe0\xa0` \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00"
                                ),
                                bytearray(
                                    b"\x0f\x10\x061\x00.\n\x1f\x08\x18\x00\x00\x00\x00\x00\x00 \x00\x08\x00\x1b\n\x15\x15\x12\x10\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x84?3|\x1a\xdf\x1f/\x0e?6\x0f=\x11\x96\xebD\x04\xc0@\xe3\xc17070+8.\x1c\xfc\x1c"
                                ),
                                bytearray(
                                    b"\xc9\xf0\xb6\xc6\xf2\x8dc\xecK\xd4E\xd6\x82\xfa\xc0?\xa6\xa0\x89\x80\x08\x08\x90\x80\xb0\x10\xb8\x10}x\x07\x1f"
                                ),
                                bytearray(
                                    b"\xa0` \xe0\x00\xd0\x00\xf0\xe0@\x80\xa0\x00\xe0\xa0@P@\x90\x800\x1000 \x00` \xe0\xe0\xc0\xc0"
                                ),
                                None,
                                bytearray(
                                    b"\x01\xfef\xf9}|\x1d<\x00\x00\x00\x00\x00\x00\x00\x00\xff\x07\xff\x81}\x02<#\x00\x1c\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x90_\x10\xd0\x82=\x81|>\xfe\x1d\\\x1e \x00\x00\xe0\xff\xef\xfe\x7f\xc5}\x82\xfe\x81\\c> \x00\x00"
                                ),
                                bytearray(
                                    b"`\xc0\xe0 \xc0\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00  \x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=True,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    10,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=2,
                            length=15,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x02\x0c\x00\x1e\x00\x1e\xc1>\xc1:\xc3\x1c\xdf0\x0c\x00\x1e\x02\x1e\x00~\x00=\x01<\x008\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x10\x00\x00\x00\x00\x00\x04\x00\x00\x80\x80\x00\xe0 \xf3\x02\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\x00\x10\x00\x08\x00"
                                ),
                                None,
                                bytearray(
                                    b"\x03\x00\x05\x06\x07\x06\x02\x03\x00\x08\x00\x08\x01\r\x04\x06\x04\x00\x00\x00\x00\x00\x04\x00\x0f\x08\x0f\x08\x0e\x0c\x03\x06"
                                ),
                                bytearray(
                                    b"\xff\x00\xff\x00\xff\x00x\x87\x0f\xff\xeeg\xc4\xd3ww\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x98\x88<\x14\x88\x00"
                                ),
                                bytearray(
                                    b"\xbbJ\x90kH\xfb\xd4\xf3\xea\x86\x9c\\P\xd3\xc0\xde\x04\x00\x04\x00\x04\x00\x08\x00\x11\x00#\x00/\x03>\x1e"
                                ),
                                bytearray(
                                    b"`\x00\xf00\xc0P\x80\x80\x000\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00 \x00p\x00\xf00\xe0\xe0\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x04\x05\x02\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x07\x01\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x19\x99\xc07\xf7\x08\xfe\x00z\x00\x1c\x00\x00\x00\x00\x00\xe6\x80\xff7?\xc8\x83}c\x1d\x1c\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xd0\xcc X\xf0(``\x08\x00\xf0 \x00\x00\x00\x00,\x1e\xf8^\xd8>\x80\xfc\xc8\xf0\xf0\x00\x00\x00\x00\x00"
                                ),
                                None,
                            ],
                            is_16bit=True,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(11, gridplane=False, tiles=[]),
                Mold(12, gridplane=False, tiles=[]),
                Mold(13, gridplane=False, tiles=[]),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'@@@@\xe0\xe000>>\x16\x1e\x0b\x0f\t\x0f@\x00@\x00\xe0\x000@>@\x1e \x0f\x10\x0f\x00'),
                            None,
                            bytearray(b'\x01\x07\x01\x07\x01\x07\x02\x06\x0c\x0c\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00H\x80{\xfa\x05\xfe\x01\xfe\x01\x1e\x00\x00\x00\x00\x00HH\xfb\xfb\xbf\x97\xaf\x83\x8f\x87\x0e\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=102),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xb1:\x1c\xf3\x18\x06\xe0B\x14\xf1\x08\xe8\xf0\xf0\x00\x00\xc4p\x08\xf8\xf9\xe8\xe7\xba\xf5\t\xe8\x18\xf0\xf0\x00\x00'),
                            bytearray(b'\xf00@\xd0\x000\xa0\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x000\x10\xf00`\x00\xc0\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x03\x02\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xf8c\xbf\x0c\xd2?\xef\xfe\xff\x06\x07\x01\x01\x00\x00\x80\x9f\xc0A\xdf?\xef\x1e\xff\xfe\x07\x06\x01\x01\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\xc0@\xf0\x08\xfc\x04\xfc\x00\xf8\x06\xf7\r\x0f\xfd\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'}\x83\xfb\x07\xf6\x0e\x1b\xfa\xf1\xf6\x81\x9e>\xc3\xf6\x03\x00\x00\x00\x00\x01\x00\x04\x00\x0c\x04|\x1c\xf4\xc8\x04\xf8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@\xa0\xf0\x10\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x02\x00'),
                            bytearray(b'\x06\x06\x19\x060\x0f"_\xa0\xdf\xaf\\\xadr\xef\x10\t\x00&\x00O\x00\x1f\x00\x1e\x00\x1e\x02\x0c\x0c4\x14'),
                            bytearray(b'\x00\x01\t\r\x0c\x04\x10\x1f\x0c\x0b\x08\x07\x03\x01\x05\x03\x06\x00\x02\x00\x13\x00\x01\x03\x11\x01\x19\t\x1e\x03\x06\x03'),
                            bytearray(b'.\xf7\xbd\xc6\xc7\xfc\xb1=\x05\x81\x9d\\|\x13\x81\xf8<<,,\x00\x00\xc2\x80\xfe\x84c\xc1o\xafA\xf6'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=108),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00H\x80{\xfa\x05\xfe\x01\xfe\x01\x1e\x00\x00\x00\x00\x00HH\xfb\xfb\xbf\x97\xaf\x83\x8f\x87\x0e\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=103),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'@@@@\xe0\xe000>>\x16\x1e\x0b\x0f\t\x0f@\x00@\x00\xe0\x000@>@\x1e \x0f\x10\x0f\x00'),
                            None,
                            bytearray(b'\x01\x07\x01\x07\x01\x07\x02\x06\x0c\x0c\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xa0\xa0\xf0\x00\xf0\x08\xfc\x04p\x8c\xea\x1e\x84z\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x03\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\x00\x00\x18\x18yFp\x0fp\x8fa\x9f\x1f\xef\xd6+\x00\x00\'\x00\x06\x00\x8e\x00\x0e\x00\x0e\x00\x0e\x00\x04\x04"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'<\xc2}\x83\xf6\x0e\x03\xf2qv\xc1\xde>\xc3\xf6\x03\x01\x00\x00\x00\x01\x00\x0c\x00\x8c\x04<\x1c\xf4\xc8\x04\xf8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@\xa0\xf0\x10\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb1:\x1c\xf3\x18\x06\xe0B\x14\xf1\x08\xe8\xf0\xf0\x00\x00\xc4p\x08\xf8\xf9\xe8\xe7\xba\xf5\t\xe8\x18\xf0\xf0\x00\x00'),
                            bytearray(b'\xf00@\xd0\x000\xa0\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x000\x10\xf00`\x00\xc0\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x08\r\r\x05\x10\x1f\x0c\x0b\x08\x07\x03\x01\x05\x03\x06\x00\x02\x00\x12\x00\x01\x03\x11\x01\x19\t\x1e\x03\x06\x03'),
                            bytearray(b'\xdf!\xff\tv\x89\xa8\xf7W\xdf\xa0`|\x13\x81\xf8\x1b\x01\x1b\t\x1b\x1b\x00\x00\xa0\x80_\xc0o\xafA\xf6'),
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x03\x02\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xf8c\xbf\x0c\xd2?\xef\xfe\xff\x06\x07\x01\x01\x00\x00\x80\x9f\xc0A\xdf?\xef\x1e\xff\xfe\x07\x06\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00H\x80{\xfa\x05\xfe\x01\xfe\x01\x1e\x00\x00\x00\x00\x00HH\xfb\xfb\xbf\x97\xaf\x83\x8f\x87\x0e\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=103),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'@@@@\xe0\xe000>>\x16\x1e\x0b\x0f\t\x0f@\x00@\x00\xe0\x000@>@\x1e \x0f\x10\x0f\x00'),
                            None,
                            bytearray(b'\x01\x07\x01\x07\x01\x07\x02\x06\x0c\x0c\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\xc0\xe0\x10\xf8\x00\xfc\x04\xfc\x00\xfc\x02\xf6\x0c\xec\x1f \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00'),
                            bytearray(b'\x02}\x01\xfe\x00\xffA\xbe7\x18\x9f`\xef\x10c\x9c\xfe\x02\xfe\x00\xff\x00\xfe\xc0\xa0`\x80\x00\xa0\x00\xa0\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\xfd=\xc3\xfe\x06\xcb:\xf1\xf6\x81\x9e>\xc3\xf6\x03\x00\x00\x00\x00\x01\x00\x04\x00\x0c\x04|\x1c\xf4\xc8\x04\xf8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@\xa0\xf0\x10\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb1:\x1c\xf3\x18\x06\xe0B\x14\xf1\x08\xe8\xf0\xf0\x00\x00\xc4p\x08\xf8\xf9\xe8\xe7\xba\xf5\t\xe8\x18\xf0\xf0\x00\x00'),
                            bytearray(b'\xf00@\xd0\x000\xa0\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x000\x10\xf00`\x00\xc0\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\t\r\r\x05\x10\x1f\x0c\x0b\x08\x07\x03\x01\x05\x03\x06\x00\x02\x00\x12\x00\x01\x03\x11\x01\x19\t\x1e\x03\x06\x03'),
                            bytearray(b'P\x8f<\xc3\x1f`\x1f\x00x\xbf\x9f\x7f|\x13\x81\xf8 \x00\x00\x00\x80\x00\xe0\x00\xc0\xc0`\xe0o\xafA\xf6'),
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x03\x02\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xf8c\xbf\x0c\xd2?\xef\xfe\xff\x06\x07\x01\x01\x00\x00\x80\x9f\xc0A\xdf?\xef\x1e\xff\xfe\x07\x06\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00H\x80{\xfa\x05\xfe\x01\xfe\x01\x1e\x00\x00\x00\x00\x00HH\xfb\xfb\xbf\x97\xaf\x83\x8f\x87\x0e\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=103),
                        Tile(mirror=False, invert=False, format=1, length=7, subtile_bytes=[
                            bytearray(b'@@@@\xe0\xe000>>\x16\x1e\x0b\x0f\t\x0f@\x00@\x00\xe0\x000@>@\x1e \x0f\x10\x0f\x00'),
                            None,
                            bytearray(b'\x01\x07\x01\x07\x01\x07\x02\x06\x0c\x0c\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x07\x00\x06\x00\x0c\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x00\x80 \xe0|\x80|\x82\xfc\x02\xfa\x06\xff\x06\x80\x80\x80\x00\xd8\x00\x80\x00\x00\x00\x00\x00\x01\x00\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\x00\x03\x08\x0f\x19\x06\x10/\x17l\xf2\x0f\xef\x10\xc79\x07\x00\x07\x00\'\x01\x0f\x00\x07\x03\x10\x00+\x00\x00\x00"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfd\x02\xfc\x03\xfa\x06\x0b\xfa\xf1\xf6\xc1\x9e>\xc3\xf6\x03\x00\x00\x00\x00\x01\x00\x04\x00\x0c\x04|\\\xf4\xc8\x04\xf8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@@\xa0\xf0\x10\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb1:\x1c\xf3\x18\x06\xe0B\x14\xf1\x08\xe8\xf0\xf0\x00\x00\xc4p\x08\xf8\xf9\xe8\xe7\xba\xf5\t\xe8\x18\xf0\xf0\x00\x00'),
                            bytearray(b'\xf00@\xd0\x000\xa0\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x000\x10\xf00`\x00\xc0\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x03\t\r\x0c\x04\x10\x1f\x0c\x0b\x08\x07\x03\x01\x05\x03\x04\x00\x02\x00\x13\x00\x01\x03\x11\x01\x19\t\x1e\x03\x06\x03'),
                            bytearray(b'W\xb4\xe1\xe0\xc0\xc0\xefoo\xaf\xbeX|\x13\x81\xf8\x14\x08 \x1e\x00?\xaf\x90\xcc\xd0g\xe6o\xafA\xf6'),
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x03\x02\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xf8c\xbf\x0c\xd2?\xef\xfe\xff\x06\x07\x01\x01\x00\x00\x80\x9f\xc0A\xdf?\xef\x1e\xff\xfe\x07\x06\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=6),
                        AnimationSequenceFrame(duration=12, mold_id=7),
                        AnimationSequenceFrame(duration=12, mold_id=6),
                        AnimationSequenceFrame(duration=12, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=8, mold_id=12),
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=14),
                        AnimationSequenceFrame(duration=32, mold_id=15),
                        AnimationSequenceFrame(duration=32, mold_id=14),
                        AnimationSequenceFrame(duration=32, mold_id=16),
                        AnimationSequenceFrame(duration=32, mold_id=14),
                        AnimationSequenceFrame(duration=32, mold_id=17),
                    ]
                ),
                AnimationSequence(frames=[]),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=10),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL697_MALLOW_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=0,
)
