# SPR0337_MAGMUS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL102_MAGMITE
sprite = CompleteSprite(
    animation=AnimationPack(31, length=794, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xc0\x10\x00\x10 \xe0 ` \xe0\xa0\x00\x00\x00\x00\xf8\xf8\xf8\xf8\xf0\xf0\xc0\xe0\x00\xe0@ \x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xef\x1fO\x1bya\x05,\x01_\x02\x1d\x0e\x0e\x00\x00\xbc\xc3\xb8\xc76\xdf2/"_\x01\x1e\x01\x00\x00\x00'),
                            bytearray(b'A\x01\xe8\x0c\xf0#<1\xbf!o\x8aL\xbc\x00\x00\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf5\x7f\x80t\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                            None,
                            bytearray(b'\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x08h\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8\xf0\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x07\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01\x0e\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f\xff\x1f'),
                            bytearray(b'\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\xeb5\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01<\xc3'),
                            bytearray(b'\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xcb\xc3\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f\xc4?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0`\xe0@\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1bya\x95\xfcA\xdf\x02=\x0e\x0e<\xc3\xbc\xc3\xb8\xc76\xdf2/"\x1f!\x1e\x01\x00'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!o\x8bu\x8d\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf4\x7f\xb0{'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08h\x00\xc0\x10\x00\x10 \xf0\x10\xa0\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xd0\xa0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1bya\x05,\x01\x1f\x02\x1d\x0e\x0e<\xc3\xbc\xc3\xb8\xc76\xdf2/"\x1f\x01\x1e\x01\x00'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!o\x8a\x1c\xec\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf5\x7f\x90L'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\xbf\x00\xfe\x00\xfc\x00\xf8\x00\xe0\x00\x00\x00\x00\x00\x00\xff\xff\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x08\x03\x00\x05\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x07\x05\x07\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x07\xd0\x0f\x04\xfbT\x01\x07\x03\x0e\n\x00\x00\x00\x00\xf7\xff\xff\xff\xff\xff\x7f\x7f\x00\x0f\x04\x02\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0\xf0\xf0\x88\xf0\x8c\xf0\x0c\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x10\xc8x\xbc|\x9c\xfc'),
                            None,
                            bytearray(b'P\x0c\xf0Nt\x8a0\xce8\xc7\x92-\xc2=.\xd1\x9c\xfc\xde\xbe\xbe\xfe\xee\xfe\xff\xff\x7f\xff\x7f\xff\xff\xff'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x07\x07nA\x96\x04s,C|\x00\x00\x00\x00\x00\x00\x07\x00\x7f\x00\xf7\x08\xfe\x1f\xfe?'),
                            bytearray(b'\x06\x04\x04\x04\x0f\r\x0f\x0f\x1f\x0f\x1e\x01\x0b\x03\x05\x10\x07\x00\x07\x00\x0f\x00\x0f\x00\x0f\x10\x05\x1a\x17\x08\x08\x07'),
                            bytearray(b'\xd7\xe8\xbd\xc0\xfa\xa5d\xa1~\xa1ze\xff\x04\xbcC\xfc\x1f\xf9\x1f\xe5\x1b\xe7\x1b\x85{\x05\xfbw\xfb\xf3\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'.\xd1@\xbf\x00\xfe\x00\xfc\x00\xf8\x00\xe0\x00\x00\x00\x00\xff\xff\xff\xff\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x05\x10\x0f\x08\x03\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x08\x07\x11\x07\x05\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbcC\xf8\x07\xd0\x0f\x04\xfbT\x01\x1f\x17\x00\x00\x00\x00\xf3\xff\xf7\xff\xff\xff\xff\xff\x7f\x7f\x08\x07\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0\xf0\xf0\x88\xf0\x8c\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x10\xc8x\xbc|'),
                            None,
                            bytearray(b'\xf0\x0cP\x0c\xf0Nt\x8a0\xce8\xc7\x92-\xc2=\x9c\xfc\x9c\xfc\xde\xbe\xbe\xfe\xee\xfe\xff\xff\x7f\xff\x7f\xff'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07nA\x96\x04s,\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x7f\x00\xf7\x08\xfe\x1f'),
                            bytearray(b'\x02\x02\x06\x04\x04\x04\x0f\r\x0f\x0f\x1f\x0f\x1e\x01\x0b\x03\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00\x0f\x10\x05\x1a\x17\x08'),
                            bytearray(b'C|\xd7\xe8\xbd\xc0\xfa\xa5d\xa1~\xa1ze\xff\x04\xfe?\xfc\x1f\xf9\x1f\xe5\x1b\xe7\x1b\x85{\x05\xfbw\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'.\xd1@\xbf\x00\xfe\x00\xfc\x00\xf8\x80\xe0\x00\x00\x00\x00\xff\xff\xff\xff\xfe\xfe\xfc\xfc\xf8\xf8`\xe0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x05\x10\x0f\x08\x07\x0e\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x08\x07\x11\x07\x05\x0b\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbcC\xf8\x07\xd0\x0f\x04\xfbT\x01\x03\x01\x07\x05\x00\x00\xf3\xff\xf7\xff\xff\xff\xff\xff\x7f\x7f\x00\x07\x02\x01\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0\xf0\xf0\x88\xf0\x8c\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x10\xc8x\xbc|'),
                            None,
                            bytearray(b'\xf0\x0cP\x0c\xf0Nt\x8a0\xce8\xc7\x92-\xc2=\x9c\xfc\x9c\xfc\xde\xbe\xbe\xfe\xee\xfe\xff\xff\x7f\xff\x7f\xff'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07nA\x96\x04s,\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x7f\x00\xf7\x08\xfe\x1f'),
                            bytearray(b'\x02\x02\x06\x04\x04\x04\x0f\r\x0f\x0f\x1f\x0f\x1e\x01\x0b\x03\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00\x0f\x10\x05\x1a\x17\x08'),
                            bytearray(b'C|\xd7\xe8\xbd\xc0\xfa\xa5d\xa1~\xa1ze\xff\x04\xfe?\xfc\x1f\xf9\x1f\xe5\x1b\xe7\x1b\x85{\x05\xfbw\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=380),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=372),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'` \xe0\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0 0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\xf0\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x7f\x00\x9f\xa8\x07y\t\xf69:\x00\x00\x00\x00\x00\x00\x7f\x7fG\xbf\x88\x7f\x87y\x06\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80\xe0\x80`\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'  \xa0\xe0`\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@ \x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=126),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=373),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=365),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=357),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'` \xe0\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=380),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0 0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\xf0\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=381),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x7f\x00\x9f\xa8\x07y\t\xf69:\x00\x00\x00\x00\x00\x00\x7f\x7fG\xbf\x88\x7f\x87y\x06\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80\xe0\x80`\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=377),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'  \xa0\xe0`\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@ \x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=378),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=367),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=351),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'` \xe0\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=376),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0 0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\xf0\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=377),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x7f\x00\x9f\xa8\x07y\t\xf69:\x00\x00\x00\x00\x00\x00\x7f\x7fG\xbf\x88\x7f\x87y\x06\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80\xe0\x80`\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=373),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'  \xa0\xe0`\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@ \x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=374),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=155, y=107),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=358),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=400, y=112),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=151, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=362),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=116),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=403, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=158, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=116),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>^\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>^\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=370),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=118),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=389, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=378, y=118),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=383, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=392, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=120),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=379),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=371),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=363),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=122),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=375),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=359),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=120),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=369),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=361),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=353),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=116),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=358, y=371),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=358, y=355),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=118),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=350, y=377),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=358, y=369),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=350, y=361),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=120),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b',4>\x06O\x03\x83\x05\x03\x82\xc7\x02\x02\x04\x1c\x10\x10\x0c`\x1e\xc0\x0f\x84\x07\x85\x07\x04\xc7\x04\x06\x0c\x1c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b',4&\x06C\x03\x8b\t\x19\x90\xc5\x00P\x00\x00\x00\x10\x0c`\x06\xc0\x03\x80\x1b\x81\x19\x0c\xcd8x\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=88, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=346, y=127),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=354, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=346, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=120),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=381, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1b\xf9a\x1d\x04\x05\x03\x01\x00\x00\x00<\xc3\xbc\xc3\xb8\xc7\xb6\xdf:?\x06\x07\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=346, y=135),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!\xef\x08\x00\x00\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefV\xff\xf7\xff\x00\x00'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=354, y=127),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=346, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=120),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xc0\x10\x00\x10 \xe0 ` \xe0\xa0\x00\x00\x00\x00\xf8\xf8\xf8\xf8\xf0\xf0\xc0\xe0\x00\xe0@ \x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xef\x1fO\x1bya\x05,\x01_\x02\x1d\x0e\x0e\x00\x00\xbc\xc3\xb8\xc76\xdf2/"_\x01\x1e\x01\x00\x00\x00'),
                            bytearray(b'A\x01\xe8\x0c\xf0#<1\xbf!o\x8aL\xbc\x00\x00\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf5\x7f\x80t\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                            None,
                            bytearray(b'\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x08h\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8\xf0\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x07\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01\x0e\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f\xff\x1f'),
                            bytearray(b'\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\xeb5\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01<\xc3'),
                            bytearray(b'\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xcb\xc3\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f\xc4?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=355),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=410, y=361),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>L\x1c\x108\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x08\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=398, y=111),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1bya\x95\xfcA\xdf\x02=\x0e\x0e<\xc3\xbc\xc3\xb8\xc76\xdf2/"\x1f!\x1e\x01\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!o\x8bu\x8d\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf4\x7f\xb0{'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0`\xe0@\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=356),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=362),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2\xb6\xd6\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf(\x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=398, y=112),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xeb5\xef\x1fO\x1bya\x05,\x01\x1f\x02\x1d\x0e\x0e<\xc3\xbc\xc3\xb8\xc76\xdf2/"\x1f\x01\x1e\x01\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x80\x00\x00  \x00\x00\x10\x10P\x10\x18\x18\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xe0\xe0\xe0\xf0\xe0\xf0\xe0\xf8'),
                            bytearray(b'\xcb\xc3A\x01\xe8\x0c\xf0#<1\xbf!o\x8a\x1c\xec\xc4?\x06\xff\x07\xff\x0f\xff\x17\xefT\xff\xf5\x7f\x90L'),
                            bytearray(b'\x08h\x00\xc0\x10\x00\x10 \xf0\x10\xa0\x00\x00\x00\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xd0\xa0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x84\xddt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc{\x8f'),
                            bytearray(b'\x07\n\x11\x0e0\x1d\x16(3\x00a \x10@\x13\xa2\x0e\x01\x0f\x10\x1f ?\x00?\x00\x1f@~\x01\xfe\x01'),
                            bytearray(b'\x00l\xa0o \xd9\x0e\xc0.\x0e\x0e:\xce6\xbb\xf7\xff\x1f\xff\x1f\xdf?\xd1?\xe1\x1f\xf1\x0f\xf1\x0f\xf4\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>^\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=356),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>^\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=362),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x00xP(\x10o)\xf9X\xe5\xd2>^\x0e\x088\x04&\x0e\xd6.\x82\x7f\x07\xff\x1f\xbf \x1e\x06\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=368),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=10, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=1),
                        AnimationSequenceFrame(duration=10, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=10, mold_id=3),
                        AnimationSequenceFrame(duration=12, mold_id=4),
                        AnimationSequenceFrame(duration=10, mold_id=3),
                        AnimationSequenceFrame(duration=12, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=6, mold_id=15),
                        AnimationSequenceFrame(duration=8, mold_id=16),
                        AnimationSequenceFrame(duration=10, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=16),
                        AnimationSequenceFrame(duration=10, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=10, mold_id=23),
                        AnimationSequenceFrame(duration=12, mold_id=24),
                        AnimationSequenceFrame(duration=10, mold_id=23),
                        AnimationSequenceFrame(duration=12, mold_id=25),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL102_MAGMITE,
    palette_offset=1,
    unknown_num=0
)
