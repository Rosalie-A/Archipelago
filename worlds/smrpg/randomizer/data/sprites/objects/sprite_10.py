# SPR0010_TOADSTOOL_NONPROTAGONIST_4

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
        251,
        length=777,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00 \x00,P@\xbc\xc0<\x80x\x00\x80\x00\x00\x00\x00  ||\xfc\xfc\xbc\xbcxx\x80\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'O\xc0p\xcf\x00\xc0\x00\xc0@\xc0\xe0\xe0\xb0\xb00pI\xb1\x7f\x8f\x00\xc0\x00\xc0\x00\xe0 \xd0p\x88\xf0\x08'),
                            None,
                            bytearray(b'@p\x08x\xf8\xf8\xb0\xb0\xb4\xb4\xc8\x88\xf0\xf0\x80\x80\xf0\x0cx\x84\xf8\x04\xb0L\xb4L\xc88\xf0p\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07G\x07G\x07g\x073\x03=\x01\x1e\x00\x07\x00x\x07x\x07x\x07x\x07<\x03>\x01\x1f\x00\x07\x00'),
                            bytearray(b'\x80\xff\x00\xff\x00\xff\x00\xff\xc0\xff\xf9\xff\x7f\x7f\x86\x06\x00\xe1\x00\xc1\x00\xc1\x00\xc1\x00\xe3\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'\xf0\x00\xff\xe0\xf9\xe1\xf3\x03\xcb\x03\x8b\x03\xcb\xc3??\xff\x00\xff\xe0\xf9\xe6\xf3\x0c\xcb4\x8bt\xcb\xf4??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00\xe0'),
                            None,
                            bytearray(b' \xe0@\xc0\x00\x00\xc0\xc0\x80\x80\x00\x80A\xc2W\xd0\x00\xe0\x00\xc0\xc0\x00\x00\xc0@\x80\x00\x80C\xb3V\xae'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1e\x1f\x0c\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3p\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfb\x00\xf9'),
                            bytearray(b'\x14\x17\x02\x03\x03\x03\t\x01\x08\x00\x04\x04\x07\x07\x07\x07\x08\x17\x0c\x03\x0c\x03\x0e\x01\x1f\x00\x1b\x048\x07x\x07'),
                            bytearray(b'\x00\xff\x00\xff\x02\xfe\xcf\xff\x7f\x7fp\x7f\xc0\xff\x80\xff\x00\x81\x00\x83\x01\xc6\x00\xff\x80\x7f\x80\x7f\x00\xf9\x00\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x00 P\x0c\xf0\xc0<\xc0<\x00\xd8\x00\x00\x00\x00\x10\x10pp\xfc\xfc\xbc\xbc||\xd8\xd8\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'O\xc0p\xcf\x00\xc0\x00\xc0@\xc0\xe0\xe0\xb0\xb00pI\xb1\x7f\x8f\x00\xc0\x00\xc0\x00\xe0 \xd0p\x88\xf0\x08'),
                            None,
                            bytearray(b'@p\x08x\xf8\xf8\xb0\xb0\xb4\xb4\xc8\x88\xf0\xf0\x80\x80\xf0\x0cx\x84\xf8\x04\xb0L\xb4L\xc88\xf0p\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07G\x07G\x07g\x073\x03=\x01\x1e\x00\x07\x00x\x07x\x07x\x07x\x07<\x03>\x01\x1f\x00\x07\x00'),
                            bytearray(b'\x80\xff\x00\xff\x00\xff\x00\xff\xc0\xff\xf9\xff\x7f\x7f\x86\x06\x00\xe1\x00\xc1\x00\xc1\x00\xc1\x00\xe3\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'\xf0\x00\xff\xe0\xf9\xe1\xf3\x03\xcb\x03\x8b\x03\xcb\xc3??\xff\x00\xff\xe0\xf9\xe6\xf3\x0c\xcb4\x8bt\xcb\xf4??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00\xe0'),
                            None,
                            bytearray(b' \xe0@\xc0\x00\x00\xc0\xc0\x80\x80\x00\x80A\xc2W\xd0\x00\xe0\x00\xc0\xc0\x00\x00\xc0@\x80\x00\x80C\xb3V\xae'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1e\x1f\x0c\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3p\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfb\x00\xf9'),
                            bytearray(b'\x14\x17\x02\x03\x03\x03\t\x01\x08\x00\x04\x04\x07\x07\x07\x07\x08\x17\x0c\x03\x0c\x03\x0e\x01\x1f\x00\x1b\x048\x07x\x07'),
                            bytearray(b'\x00\xff\x00\xff\x02\xfe\xcf\xff\x7f\x7fp\x7f\xc0\xff\x80\xff\x00\x81\x00\x83\x01\xc6\x00\xff\x80\x7f\x80\x7f\x00\xf9\x00\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'O\xc0p\xcf\x00\xc0\x00\xc0@\xc0\xe0\xe0\xb0\xb00pI\xb1\x7f\x8f\x00\xc0\x00\xc0\x00\xe0 \xd0p\x88\xf0\x08'),
                            None,
                            bytearray(b'@p\x08x\xf8\xf8\xb0\xb0\xb4\xb4\xc8\x88\xf0\xf0\x80\x80\xf0\x0cx\x84\xf8\x04\xb0L\xb4L\xc88\xf0p\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07G\x07G\x07g\x073\x03=\x01\x1e\x00\x07\x00x\x07x\x07x\x07x\x07<\x03>\x01\x1f\x00\x07\x00'),
                            bytearray(b'\x80\xff\x00\xff\x00\xff\x00\xff\xc0\xff\xf9\xff\x7f\x7f\x86\x06\x00\xe1\x00\xc1\x00\xc1\x00\xc1\x00\xe3\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00\x07\x00\x07\x03\x07\x03\x07\x06\x07\x04\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'\xf0\x00\xff\xe0\xf9\xe1\xf3\x03\xcb\x03\x8b\x03\xcb\xc3??\xff\x00\xff\xe0\xf9\xe6\xf3\x0c\xcb4\x8bt\xcb\xf4??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00\xe0'),
                            None,
                            bytearray(b' \xe0@\xc0\x00\x00\xc0\xc0\x80\x80\x00\x81C\xc4W\xd0\x00\xe0\x00\xc0\xc0\x00\x00\xc0@\x80\x01\x81G\xb7V\xae'),
                            bytearray(b'\x00\x00 \x00,R\x00~@\xbe\xc0<\x80@\x00\x80\x00\x00  ~~~~\xfe\xfe\xbc\xbc@@\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1e\x1f\x0c\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3p\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfb\x00\xf9'),
                            bytearray(b'\x14\x17\x02\x03\x03\x03\t\x01\x08\x00\x04\x04\x07\x07\x07\x07\x08\x17\x0c\x03\x0c\x03\x0e\x01\x1f\x00\x1b\x048\x07x\x07'),
                            bytearray(b'\x00\xff\x00\xff\x02\xfe\xcf\xff\x7f\x7fp\x7f\xc0\xff\x80\xff\x00\x81\x00\x83\x01\xc6\x00\xff\x80\x7f\x80\x7f\x00\xf9\x00\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'`\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 ``\x80@\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
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
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x01\xc2!\xe2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0#\xc3\x03\xe3'),
                            None,
                            bytearray(b'"\xe5B\xc5\x06\x01\xc6\xd9\xbe\x81<\xc20\x8c`\xd8\x07\xe7\x05\xc5\xc5\x05\x1f\xdfw\xb7N\xce<\xdcx\x98'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1a\x1f\x0e\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc38\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfd\x00\xfc'),
                            bytearray(b'\x12\x13\x05\x01\x05\x01\x0c\x00\x08\x00\x02\x02\x03\x03\x03\x03\x0c\x13\x0e\x01\x0e\x01\x0f\x00\x1f\x00\x1d\x02<\x03|\x03'),
                            bytearray(b'\x00\xff\x00\xff\x81\xff\xe7\xff??8?\xe0\xff\xc0\xff\x00\xc0\x00\xc1\x00\xe3\x00\xff\xc0?\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0 \x00\xe0\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=106),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x02\x06\x89L\xd3\x08\xd7(\xf6\x00\x00\x00\x00\x00\x00\x02\x02\x0b\x8b\x1f\xdf7\xd7\x1e\xfe'),
                            None,
                            bytearray(b' \xfeH\xd4\x18\x04\xd8\xc4\xb8\x840\xc80\x88`\xd0\x1e\xfe\x1c\xdc\xd4\x14\x14\xd4l\xacX\xd88\xd8p\x90'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'`\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 ``\x80@\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
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
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1a\x1f\x0e\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc38\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfd\x00\xfc'),
                            bytearray(b'\x12\x13\x05\x01\x05\x01\x0c\x00\x08\x00\x02\x02\x03\x03\x03\x03\x0c\x13\x0e\x01\x0e\x01\x0f\x00\x1f\x00\x1d\x02<\x03|\x03'),
                            bytearray(b'\x00\xff\x00\xff\x81\xff\xe7\xff??8?\xe0\xff\xc0\xff\x00\xc0\x00\xc1\x00\xe3\x00\xff\xc0?\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00`P\xa8\xd0(\x80|\x10\xec\x18\xe4\x00\x00\x00\x00``\xf8\xf8\xf8\xf8\xfc\xfc\xec\xec\xec\xec'),
                            None,
                            bytearray(b'X\xa4(V\x04;\x07\x18\x03\x0c\x01\x02\x00\x00\x00\x00\xec\xec~~??\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x03\x03\x03\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80@\xd0 P\xa8\x10\xe8\x18\xe48\xc48\xc6\x14k\xc0\xc0\xe0\xe0\xe8\xe8\xe8\xe8\xfc\xfc\xec\xec\xfe\xfe\x7f\x7f'),
                            None,
                            bytearray(b'\x07\x18\x03\x0c\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=103),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x03\x03\x03\x03\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x80@\xd0 P\xa8\x10\xe8\x18\xe48\xc48\xc6\x14k\xc0\xc0\xe0\xe0\xe8\xe8\xe8\xe8\xfc\xfc\xec\xec\xfe\xfe\x7f\x7f'),
                            None,
                            bytearray(b'\x07\x18\x03\x0c\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=104),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0370Ox@p\x00\x00\x00\x00\x00\x00\x00\x00\x03\x036Ny\x01p\x08\x00p'),
                            bytearray(b'\x00\x00\x10 0N\xfe\x00\xfc\x02\x1c\xe2\x08\x14\x00\x00\x00\x0000nn\xc2\xc222\xf6\xf6\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' V&Y8\xc7w\x88~\x81r\x8d|\x020\x0cvvyy\xf7\xf7\xf8\xf8\xff\xff\xff\xff~~<<'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' V&Y8\xc7w\x88~\x81r\x8d|\x020\x0cvvyy\xf7\xf7\xf8\xf8\xff\xff\xff\xff~~<<'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=107),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00`P\xa8\xd0(\x80|\x10\xec\x18\xe4\x00\x00\x00\x00``\xf8\xf8\xf8\xf8\xfc\xfc\xec\xec\xec\xec'),
                            None,
                            bytearray(b'X\xa4(V\x04;\x07\x18\x03\x0c\x01\x02\x00\x00\x00\x00\xec\xec~~??\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=100),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x10(8!9&?\x04?\x00?@\x00\x00\x10\x1088\t\t\x0f\x0f**..\x7f\x7f'),
                            bytearray(b'\x00\x000@p\x88p\x88\xe0\x1e\xfe1\xfeA\xf8\x04\x00\x00pp\x88\x88\x98\x98>>OO\xa3\xa3\x8c\x8c'),
                            bytearray(b'?@\x7f\x00\x7f\x00\x7f\x00\x7f\x00\x1ea\x00\x1e\x00\x00\x7f\x7f\x7f\x7f~~~~\x7f\x7f\x7f\x7f\x1e\x1e\x00\x00'),
                            bytearray(b'\xe08\xfe\x01\xfe\x01\xf0<\xf8\x048\xc4\x008\x00\x00\x18\x18\x03\x03\x7f\x7f\xcc\xcc<<\xcc\xcc88\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00  Qq\x02s\x06w\x08?@\x00\x00\x00\x00  qqSSTT^^\x7f\x7f'),
                            bytearray(b'\x00\x00\x00``\x90\xe0\x10\xe0\x10\xdc`\xfc\x00\xf8\x04\x00\x00``\xd0\xd0\x10\x100000\xc4\xc4\x1c\x1c'),
                            bytearray(b'?@\x7f\x00\x7f\x00\x7f\x00\x7f\x00\x1c#\x00\x1c\x00\x00\x7f\x7f\x7f\x7f~~~~\x7f\x7f??\x1c\x1c\x00\x00'),
                            bytearray(b'\xc0x\xfc\x02\xf8\x06\xe0|\xf0\x08p\x88\x00p\x00\x0088bb\xfe\xfe\x1c\x1c\x98\x98\xf8\xf8pp\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            None,
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00.$\x1a4K5K}K}K\xfc#\xfc#..>>oonn&&&&\xc7\xc7\x87\x87'),
                            None,
                            bytearray(b"\xfc\'\xfc\'x\x87x\x878O\x00\x1f\x00\x00\x00\x00\x8b\x8b\x8b\x8b\xef\xef\xff\xffww\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00|\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xfc\xfc||\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=96),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            None,
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=380, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00.$\x1a4K5K}K}K\xfc#\xfc#..>>oonn&&&&\xc7\xc7\x87\x87'),
                            None,
                            bytearray(b"\xfc\'\xfc\'x\x87x\x878O\x00\x1f\x00\x00\x00\x00\x8b\x8b\x8b\x8b\xef\xef\xff\xffww\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00|\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xfc\xfc||\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=97),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            None,
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=379, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00.$\x1a4K5K}K}K\xfc#\xfc#..>>oonn&&&&\xc7\xc7\x87\x87'),
                            None,
                            bytearray(b"\xfc\'\xfc\'x\x87x\x878O\x00\x1f\x00\x00\x00\x00\x8b\x8b\x8b\x8b\xef\xef\xff\xffww\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00|\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xfc\xfc||\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=98),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80@\xc0@\xc0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\xc0\x00\xc0\x00\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x18\x00\x18\x00\x1c\x00\x0ep\x06\xf8\xc78\xc3<\x00\x00\x18\x18\x10\x10\x14\x14\nz\x80\xc8\xc5\r\xe2>'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa6?\x7f\x7fy\x7f8:\x15\x10\xe0>\xc1\x7f\xc1\xff\xc0>\x81~\x81~\xc4;\xef\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80@\xc0@\xc0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\xc0\x00\xc0\x00\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x18\x00\x18\x00\x1c\x00\x0ep\x06\xf8\xc78\xc3<\x00\x00\x18\x18\x10\x10\x14\x14\nz\x80\xc8\xc5\r\xe2>'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa6?\x7f\x7fy\x7f8:\x15\x10\xe0>\xc1\x7f\xc1\xff\xc0>\x81~\x81~\xc4;\xef\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=100),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=101),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x00\x00@@\x80\x80\x00\x00\x00\x00\x80\xc0\x80@\x80@\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x7f\x1f\x7f>\x7f>\x7f`|@8 \x1c\x1c\x03\x03\x7f\x1f\x7f>\x7f>\x7f`|C8\'\x1c\x1f\x03\x03"),
                            bytearray(b'\xff`\xfe?\x9f\x1f;;\xbb;\xbc8\xbf?\xf8\xf8\xff`\xff>\x9f`;\xc4\xbbD\xbcC\xbfG\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x00?\x18?\x1e?\x00?\x00?\x00\x1f\x00\x1f\x00?\x00?\x18?\x1e'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xf0\x00\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=100),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x00?\x18?\x1e?\x00?\x00?\x00\x1f\x00\x1f\x00?\x00?\x18?\x1e'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xf0\x00\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x00\x00@@\x80\x80\x00\x00\x00\x00\x80\xc0\x80@\x80@\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x7f\x1f\x7f>\x7f>\x7f`|@8 \x1c\x1c\x03\x03\x7f\x1f\x7f>\x7f>\x7f`|C8\'\x1c\x1f\x03\x03"),
                            bytearray(b'\xff`\xfe?\x9f\x1f;;\xbb;\xbc8\xbf?\xf8\xf8\xff`\xff>\x9f`;\xc4\xbbD\xbcC\xbfG\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0370Ox@p\x00\x00\x00\x00\x00\x00\x00\x00\x03\x036Ny\x01p\x08\x00p'),
                            bytearray(b'\x00\x00\x10 0N\xfe\x00\xfc\x02\x1c\xe2\x08\x14\x00\x00\x00\x0000nn\xc2\xc222\xf6\xf6\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18$0Lp\x88p\x88p\x888\xc48D\x00<<<||\xf8\xf8\xe8\xe8\xc8\xc8\xcc\xccll<<'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18$0Lp\x88p\x88p\x888\xc48D\x00<<<||\xf8\xf8\xe8\xe8\xc8\xc8\xcc\xccll<<'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\t?0OpFy\x00\x06\x00\x00\x00\x00\x00\x00\x0f?9Iq\x11\x7f\x1f\x06>'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=111),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 \xe0 \xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x10'),
                            None,
                            bytearray(b'\x00\xc0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xc00\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'N\x0fN\x0fl\x0fd\x07>\x07\x1b\x03\x0c\x00\x0f\x0cp\x0fp\x0fp\x0fx\x078\x07\x1c\x03\x0f\x00\x0f\x0c'),
                            bytearray(b'9\xff\x10\xd6`\xe01\xa1&\xa7\x80\x9f`\x7f@\x7f\x1f\xe06\xc9 \xffq\xaeg\xb8\x1f\xe0\xff\x00\x7f\x80'),
                            bytearray(b'\x1f\x00\x1e\x0c\x1f\x0c\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1e\r\x1f\x0c\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\x00\x7f@\x7f\x0f\x0f\x0e\x0e.\x0e/\x0e/\x0f\xfe\xfe\x7f\x80\x7f\x80\x0f\xf0\x0e\xf1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80\x00\xc0\x00\xc0@\x80'),
                            None,
                            bytearray(b'\x80\x80\x80\x80\x00\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x04\x07\x01\x07\x01\x07\x04\x07\x00\x00\x00\x00\x01\x00\x01\x02\x00\x07\x08\x07\x08\x07\x08\x07'),
                            bytearray(b'h\x00\xfc\x00\xc6:n\x13\xb8\x83\x00\xff\x80\xff\x80\xff``\x84\x84\x82\x90\xeeml\xef\x00\xf9\x00\xc1\x00\xc3'),
                            bytearray(b'\n\x03\r\x01\x0f\x00\x07\x01\x00\x00\x00\x00\x03\x03F\x07\x0c\x03\x0e\x01\x1f\x00>\x01?\x00\x7f\x00|\x03x\x07'),
                            bytearray(b'\x00\xfc2\xf8\x9a\xf8\x08\xfb\xd0\xf3p`\x06\xe4\x05\xe5\x03\xe0\x07\xfb\x05\xf9\x04\xf8\x0c\xe0\x9ex\x1e\xfa\x17\xea'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 ``\x80@\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03C\x03C\x03c\x031\x01\x1d\x01\x0e\x00\x0f\x00|\x03|\x03|\x03|\x03>\x01\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xc0\xff\x80\xff\x80\xff\x80\xff\xe0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf0\x00\xe0\x00\xe0\x00\xe0\x00\xf1\x00\xff\x80\x7f\xf9\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x01\xc2!\xe2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0#\xc3\x03\xe3'),
                            None,
                            bytearray(b'"\xe5B\xc5\x06\x01\xc6\xd9\xbe\x81<\xc20\x8c`\xd8\x07\xe7\x05\xc5\xc5\x05\x1f\xdfw\xb7N\xce<\xdcx\x98'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1a\x1f\x0e\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc38\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfd\x00\xfc'),
                            bytearray(b'\x12\x13\x05\x01\x05\x01\x0c\x00\x08\x00\x02\x02\x03\x03\x03\x03\x0c\x13\x0e\x01\x0e\x01\x0f\x00\x1f\x00\x1d\x02<\x03|\x03'),
                            bytearray(b'\x00\xff\x00\xff\x81\xff\xe7\xff??8?\xe0\xff\xc0\xff\x00\xc0\x00\xc1\x00\xe3\x00\xff\xc0?\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0 \x00\xe0\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\xe0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xe0\x18\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xe0\x00\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\x00\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x02\x06\x89L\xd3\x08\xd7(\xf6\x00\x00\x00\x00\x00\x00\x02\x02\x0b\x8b\x1f\xdf7\xd7\x1e\xfe'),
                            None,
                            bytearray(b' \xfeH\xd4\x18\x04\xd8\xc4\xb8\x840\xc80\x88`\xd0\x1e\xfe\x1c\xdc\xd4\x14\x14\xd4l\xacX\xd88\xd8p\x90'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'`\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\xa0\xa0 ``\x80@\x80\x00\xc0\x00\xc0\x00\xc0\x00\xe0`\x90\xe0\x18'),
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
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1a\x1f\x0e\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc38\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfd\x00\xfc'),
                            bytearray(b'\x12\x13\x05\x01\x05\x01\x0c\x00\x08\x00\x02\x02\x03\x03\x03\x03\x0c\x13\x0e\x01\x0e\x01\x0f\x00\x1f\x00\x1d\x02<\x03|\x03'),
                            bytearray(b'\x00\xff\x00\xff\x81\xff\xe7\xff??8?\xe0\xff\xc0\xff\x00\xc0\x00\xc1\x00\xe3\x00\xff\xc0?\xc0?\x00\xfc\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(29, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                    ]
                ),
                Mold(30, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0 \xc0\x00`'),
                            None,
                            bytearray(b' \xe0@\xc0\x80\x80\xc0\xc0\x80\x80\x00\x80@\xc0@\xc0\x00`\x00\xc0@\x80\x00\xc0@\x80\x00\x80@\x00@ '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x1d\x1f\x0f\x0f\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x00\x1f\x10\x0f'),
                            bytearray(b'(\x00>\x00~\x00~\x0c\xbf\xe1\x9a\xc3\x1c\xff\x00\xff((\x18\x18\\\\\xe0mo\xceL\xef\x00\xfe\x00\xfe'),
                            bytearray(b'\x11\x11\x02\x00\x06\x00\x0e\x00\x0c\x00\x01\x01\x01\x01\x01\x01\x0e\x11\x0f\x00\x0f\x00\x0f\x00\x1f\x00\x1e\x01>\x01~\x01'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xffs\x7f\x1f\x1f\x1c\x1f\xf0\xff\xe0\xff\x00\xe0\x00\xe0\x00\xf1\x80\x7f\xe0\x1f\xe0\x1f\x00\xfe\x00\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0\x00\xc0\x00\xc0@\xc0\xc0\xc0\x80\x80 `@ @ \x00@\x00@\x00\xc0\x00\xe0@\xb0\xe0\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01A\x01A\x01a\x010\x00\x1d\x01\x0e\x00\x0f\x00~\x01~\x01~\x01~\x01?\x00\x1e\x01\x0f\x00\x0f\x00'),
                            bytearray(b'\xe0\xff\xc0\xff\xc0\xff\xc0\xff\xf0\xff\xf8\xff\x7f\x7f\x86\x06\x00\xf8\x00\xf0\x00\xf0\x00\xf0\x00\xf8\x00\xff\x80\x7f\xf9\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' \xe0 \xe0\xe0\xe0\xc0\xc0\xd0\xd0  \xc0\xc0\x00\x00\xe0\x10\xe0\x10\xe0\x10\xc00\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\x08\x07\x07\x00\x00\x1f\x00\x1f\x0f\x1f\x0f\x1f\x18\x1f\x10\x0e\t\x07\x07\x00\x00'),
                            bytearray(b'\xc1\x01\xfc\x81\xe7\x87\xce\x0e.\x0e/\x0e/\x0f\xfe\xfe\xff\x00\xfd\x82\xe7\x98\xce1.\xd1/\xd0/\xd1\xfe\xfe'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=8, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=6, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=23),
                        AnimationSequenceFrame(duration=4, mold_id=22),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=6, mold_id=26),
                        AnimationSequenceFrame(duration=2, mold_id=27),
                        AnimationSequenceFrame(duration=2, mold_id=28),
                        AnimationSequenceFrame(duration=2, mold_id=29),
                        AnimationSequenceFrame(duration=4, mold_id=30),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL659_TOADSTOOL_SLAP_ATTACK,
    palette_offset=0,
    unknown_num=0,
)
