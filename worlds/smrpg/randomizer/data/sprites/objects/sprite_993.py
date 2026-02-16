# SPR0993_MARIO_NONPROTAGONIST_4

from randomizer.data.variables.sprite_palette_names import SPAL644_MARIO_ATTACK_UP_RIGHT
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(243, length=977, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'n\x10\xff\x00\xfe\x01\xf9\x06\xfb\x04\xf3\x0c\x9f`m\x12rr\x93\x92\x17\x17\x1f\x1f>>\xfe\xfe\xff\x7f\x7f\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xb0\x00\xc7A\x98x\xe6~\x00\x00\xff\x0e\x00\x00\x00\x00\x80p\xc1?\xf8\x07\xfe\x01\x00\xff\x0e\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x03\x02\x03\x1c\x1d\x1f\x10\x1e\x10\x0f\x08\x07\x07\x00\x00\x04\x07\x0c\x0f\x1e\x1f\x10\x1f\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b' \xe00\xf0\x00\xc0\xf0\x10\xf0\x10\xe0 \xc0\xc0\x00\x00\x10\xf0\x10\xf0 \xe0\xf0\x10\xd00 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x06\x00\x06\x00\x05\x01\x05\x01\x00\x01\x00\x01\x01\x01\x02\x02\x00\x07\x00\x07\x01\x06\x01\x06\x0f\x0e\x0e\x0f\x0e\x0f\x05\x07'),
                            bytearray(b'\x1c(\x80\xb0\x80\xdc\x00\xfc\x04\x9c\x0c\xfc\xb0\xf0\xc0\xc0\\\xe0\xc6<\xea\x1c\xf2\x16\xe2\x1e\x02\xfe\x0c\xfc8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02'),
                            None,
                            bytearray(b'\x1f\x01\x1f\xe1\x03\xf1\xf7\xf1\xff\xf1~r\x0e\x02< \x1d\x03\x1f\xe1\x0f\xf1\r\xf3\r\xf3\x8a\xf6\xf2\xfe <'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=110),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'n\x10\xff\x00\xfe\x01\xf9\x06\xfb\x04\xf3\x0c\x9f`m\x12rr\x93\x92\x17\x17\x1f\x1f>>\xfe\xfe\xff\x7f\x7f\x1e'),
                            bytearray(b'\x00\x00\x00\x00\xb0\x00\xc7A\x98x\xe6~\x00\x00\xff\x0e\x00\x00\x00\x00\x80p\xc1?\xf8\x07\xfe\x01\x00\xff\x0e\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x00\x06\x00\x05\x01\x05\x01\x00\x01\x00\x01\x01\x01\x02\x02\x00\x07\x00\x07\x01\x06\x01\x06\x0f\x0e\x0e\x0f\x0e\x0f\x05\x07'),
                            bytearray(b'\x1c(\x80\xb0\x80\xdc\x00\xfc\x04\x9c\x0c\xfc\xb0\xf0\xc0\xc0\\\xe0\xc6<\xea\x1c\xf2\x16\xe2\x1e\x02\xfe\x0c\xfc8\xf8'),
                            bytearray(b'\x02\x03\x02\x03\x1c\x1d\x1f\x10\x1e\x10\x0f\x08\x07\x07\x00\x00\x04\x07\x0c\x0f\x1e\x1f\x10\x1f\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b' \xe00\xf0\x00\xc0\xf0\x10\xf0\x10\xe0 \xc0\xc0\x00\x00\x10\xf0\x10\xf0 \xe0\xf0\x10\xd00 \xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02'),
                            None,
                            bytearray(b'\x1f\x01\x1f\xe1\x03\xf1\xf7\xf1\xff\xf1~r\x0e\x02< \x1d\x03\x1f\xe1\x0f\xf1\r\xf3\r\xf3\x8a\xf6\xf2\xfe <'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<\x00\x1e`\xfe\x00\xfc\x02\xf0\x0e\xf4\np\x8c\x88p<8vt\x96\x94\x96\x96\x9e\x9e\x9e\x9e\xdc\xdc\xf8p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<\x00\x1e`\xfe\x00\xfc\x02\xf0\x0e\xf4\np\x8c\x88p<8vt\x96\x94\x96\x96\x9e\x9e\x9e\x9e\xdc\xdc\xf8p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'p\x80\xf8\x00\xfc\x00\xf8\x04\xf8\x04\xe0\x1c\xc08@\xb0\x90\x90\x88\x88\x84\x84\x0c\x0c\x9c\x9c\xfc\xfcxx\xf0p'),
                            None,
                            bytearray(b'\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x03\x00\x03\x00\x01\x02\x03\x04\x05\x01\x02\x03\x01\x01\x01\x01\x02\x02\x00\x00\x03\x03\x06\x06\x05\x06\x03\x04'),
                            None,
                            bytearray(b'\x04\x07\x01\x07\x0b\x0e\x1a\x18\xd4\x90\xd0\x80\xa0\x00\xc0\x00\x07\x08\x07\x18\x0e\x11\x18&\x90\xec\x80\xf0\x00\xe0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=100),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x03\x00\x03\x00\x01\x02\x03\x04\x05\x01\x02\x03\x01\x01\x01\x01\x02\x02\x00\x00\x03\x03\x06\x06\x05\x06\x03\x04'),
                            bytearray(b'p\x80\xf8\x00\xfc\x00\xf8\x04\xf8\x04\xe0\x1c\xc08@\xb0\x90\x90\x88\x88\x84\x84\x0c\x0c\x9c\x9c\xfc\xfcxx\xf0p'),
                            bytearray(b'\x04\x07\x01\x07\x0b\x0e\x1a\x18\xd4\x90\xd0\x80\xa0\x00\xc0\x00\x07\x08\x07\x18\x0e\x11\x18&\x90\xec\x80\xf0\x00\xe0\x00\xc0'),
                            bytearray(b'\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x03\x00\x03\x00\x01\x02\x03\x04\x05\x01\x02\x03\x01\x01\x01\x01\x02\x02\x00\x00\x03\x03\x06\x06\x05\x06\x03\x04'),
                            bytearray(b'p\x80\xf8\x00\xfc\x00\xf8\x04\xf8\x04\xe0\x1c\xc08@\xb0\x90\x90\x88\x88\x84\x84\x0c\x0c\x9c\x9c\xfc\xfcxx\xf0p'),
                            bytearray(b'\x04\x07\x01\x07\x0b\x0e\x1a\x18\xd4\x90\xd0\x80\xa0\x00\xc0\x00\x07\x08\x07\x18\x0e\x11\x18&\x90\xec\x80\xf0\x00\xe0\x00\xc0'),
                            bytearray(b'\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\x08\x0f\x10\x1f\x00\xff\x80\x8f\x90\x00\x00\x00\x00\x00\x00\x0e\x0e\x19\x19\x10\x10\x90\xf0\x99\xf9'),
                            None,
                            bytearray(b'\xb6i\x902X\x18$\x00\x18\x00\x00\x00\x00\x00\x00\x00o\x9f2\xce\x18f\x00<\x00\x18\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=103),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=117),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=114),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x06\x08\x0f\x10\x1f\x00\xff\x80\x8f\x90\x00\x00\x00\x00\x00\x00\x0e\x0e\x19\x19\x10\x10\x90\xf0\x99\xf9'),
                            None,
                            bytearray(b'\xb6i\x902X\x18$\x00\x18\x00\x00\x00\x00\x00\x00\x00o\x9f2\xce\x18f\x00<\x00\x18\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=111),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x0e\x00?\x00?@,S\x078(\x16\x0e\x10 ,\x0c\x0c\x18\x18HH{{?8>~\x1e|,\xdc'),
                            bytearray(b'\x02\x00\x06\x00\x1f\x00?\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x1f\x00?\x00\x1e\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'  ``\xe0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00 \xd8`\x90@\xa0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=104),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c\x02\x1e!~\x01u\n1N\x17(\x00\x0e\x18\x18\x02\x0211MM_Z\x7f~?>\x0e>\x18&'),
                            None,
                            bytearray(b'\x18\x18\x0c\x08L\x08\xf8\x00\xf0\x00\xe0\x00\xc0\x00\x00\x00\x18&\x084\x08t\x00\xf8\x00\xf0\x00\xe0\x00\xc0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=102),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c <\x02:\x04}\x02q\x0e&Y\x086\x04\x14  \x02\x02><\x0f\n\x1f\x1e\x7f\x7f>>\x14\x1b'),
                            None,
                            bytearray(b'\x06\x06\x03\x02\x03\x02\x13\x00\x1e\x00>\x00<\x008\x00\x06\t\x02\r\x02\r\x00\x1f\x00\x1e\x00>\x00<\x008'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=98),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c <\x02:\x04}\x02q\x0e&Y\x086\x04\x14  \x02\x02><\x0f\n\x1f\x1e\x7f\x7f>>\x14\x1b'),
                            None,
                            bytearray(b'\x06\x06\x03\x02\x03\x02\x13\x00\x1e\x00>\x00<\x008\x00\x06\t\x02\r\x02\r\x00\x1f\x00\x1e\x00>\x00<\x008'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=97),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x02\x02\x06\x060\x00\'\x01?0\x1f\x1f\x00\x00\x00\x00\x1d\x1f9??\x0f=\x0369\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00@@@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\xf0\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            bytearray(b"\x02\x02\x06\x060\x00\'\x01?0\x1f\x1f\x00\x00\x00\x00\x1d\x1f9??\x0f=\x0369\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00@@@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\xf0\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0e\x02\x1f\x01\xd3\xc1\xcb\xf1\xef\xf1\x7fq~r\x9e\x82\x0e\x02\x1d\x03\x1f\xc1\x0f\xf1\r\xf3\x8d\xf3\x8e\xf2\xea\xf6'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=119),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x02\x02\x06\x060\x00\'\x01?0\x1f\x1f\x00\x00\x00\x00\x1d\x1f9??\x0f=\x0369\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00@@@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\xf0\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0e\x02\x1f\x01\xd3\xc1\xcb\xf1\xef\xf1\x7fq~r\x9e\x82\x0e\x02\x1d\x03\x1f\xc1\x0f\xf1\r\xf3\x8d\xf3\x8e\xf2\xea\xf6'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=117),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x02\x02\x06\x060\x00\'\x01?0\x1f\x1f\x00\x00\x00\x00\x1d\x1f9??\x0f=\x0369\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'\x00\x00@@@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\xf0\xf0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02'),
                            None,
                            bytearray(b'\x1f\x01\x1f\xe1\x03\xf1\xf7\xf1\xff\xf1~r\x0e\x02< \x1d\x03\x1f\xe1\x0f\xf1\r\xf3\r\xf3\x8a\xf6\xf2\xfe <'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=107),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xc0\xc0>\xfe\x06\xfe\xfe\xfe\x00\x00\xff\x0f\x00\x00\x00\xc0\xc08\xfe\x01\xfe\x01\xfe\x01\x00\xff\x0f\xff\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x12\x1f ?\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x1e#"! AA'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xf0\x08\xf0\x0f\xfa\x05\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\x18\x18\x1f\x1f??'),
                            bytearray(b'>A?@\x1f`\x1f \x1f \x1e!\r\x12\x07\x18AAaaaa##33??\x1f\x1e\x1f\x1f'),
                            bytearray(b'\xdb$?\xc0?\xc0?\xc0;\xc4y\x86\xec\x13\xbb@77\xe4\xe4\xe4\xe4\xe4\xe4\xff\xff\xff\xff\xff\xf3\xfb\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x00\x06\x00\x05\x01\x05\x01\x00\x01\x00\x01\x01\x01\x02\x02\x00\x07\x00\x07\x01\x06\x01\x06\x0f\x0e\x0e\x0f\x0e\x0f\x05\x07'),
                            bytearray(b'\x1c(\x80\xb0\x80\xdc\x00\xfc\x04\x9c\x0c\xfc\xb0\xf0\xc0\xc0\\\xe0\xc6<\xea\x1c\xf2\x16\xe2\x1e\x02\xfe\x0c\xfc8\xf8'),
                            bytearray(b'\x02\x03\x02\x03\x1c\x1d\x1f\x10\x1e\x10\x0f\x08\x07\x07\x00\x00\x04\x07\x0c\x0f\x1e\x1f\x10\x1f\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b' \xe00\xf0\x00\xc0\xf0\x10\xf0\x10\xe0 \xc0\xc0\x00\x00\x10\xf0\x10\xf0 \xe0\xf0\x10\xd00 \xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02'),
                            None,
                            bytearray(b'\x1f\x01\x1f\xe1\x03\xf1\xf7\xf1\xff\xf1~r\x0e\x02< \x1d\x03\x1f\xe1\x0f\xf1\r\xf3\r\xf3\x8a\xf6\xf2\xfe <'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'8E\x7f\x80\xff\x00\xfd\x02\xff\x00\xfe\x01\xfe\x01\xff\x00}}\x87\x85\x82\x80\x82\x82\x82\x82\x83\x83\xc1\xc1\xc1\xc1'),
                            bytearray(b'\x00\xf0\xe0\x1f\xf8\x07\xfa\x05\xff\x00\xdf ?\xc0\x7f\x80\xf0\xf0\x1f\x1f\x1f\x1f????\xff\xff\xfd\xfd\xcd\xcd'),
                            bytearray(b'\x7f\x80\x7f\x80\x7f\x80~\x81:\xc5\x0fp\x00\x1f\x00\x00\xc1\xc1\xc1\xc1\xe3\xe3\xff\xff\xff\xfd\x7f\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\xff\x00\xf7\x08w\x88s\x8c\xf9\x06\x9e`\xe0\x00\x00\x00\xcd\xcd\xcd\xcd\xcf\xcf\xff\xff\xff\xf6\xfe\xe0\xe0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xc0\xc0>\xfe\x06\xfe\xfe\xfe\x00\x00\xff\x0f\x00\x00\x00\xc0\xc08\xfe\x01\xfe\x01\xfe\x01\x00\xff\x0f\xff\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x00\x06\x00\x05\x01\x05\x01\x00\x01\x00\x01\x01\x01\x02\x02\x00\x07\x00\x07\x01\x06\x01\x06\x0f\x0e\x0e\x0f\x0e\x0f\x05\x07'),
                            bytearray(b'\x1c(\x80\xb0\x80\xdc\x00\xfc\x04\x9c\x0c\xfc\xb0\xf0\xc0\xc0\\\xe0\xc6<\xea\x1c\xf2\x16\xe2\x1e\x02\xfe\x0c\xfc8\xf8'),
                            bytearray(b'\x02\x03\x02\x03\x1c\x1d\x1f\x10\x1e\x10\x0f\x08\x07\x07\x00\x00\x04\x07\x0c\x0f\x1e\x1f\x10\x1f\x13\x1c\t\x0e\x07\x07\x00\x00'),
                            bytearray(b' \xe00\xf0\x00\xc0\xf0\x10\xf0\x10\xe0 \xc0\xc0\x00\x00\x10\xf0\x10\xf0 \xe0\xf0\x10\xd00 \xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x02'),
                            None,
                            bytearray(b'\x1f\x01\x1f\xe1\x03\xf1\xf7\xf1\xff\xf1~r\x0e\x02< \x1d\x03\x1f\xe1\x0f\xf1\r\xf3\r\xf3\x8a\xf6\xf2\xfe <'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x0f\x00\x03\x00??@\x0f\xf0\x1f \x0f0\x03\x1c\x0f\x0f\x03\x03??CC\xfc\xfc0088\x1e\x1e'),
                            bytearray(b'\x0e\xf0\x1d\xe2\x1d\xe2\xff\x00\xef\x10\xff\x00\xfd\x02\xef\x10\xfe\xf0\xff\xfe\xf3\xf2\xc1\xc010\x13\x12\x17\x16?<'),
                            bytearray(b'\x0f\x10\x07x\x7f\x80\x03<\x0f\x10?\xc0\x00?\x00\x03\x10\x10xx\x80\x80??\x10\x10\xff\xff??\x03\x03'),
                            bytearray(b'\xf3\x0c\xf1\x0e\xf1\x0e\xf9\x06\xf2\x0c\xc48\x00\xf8\x00\xc0\xff\xfc\x1f\x1e\x0f\x0e\x07\x06\x1e\x1c\xfc\xf8\xf8\xf8\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x0f\x00\x03\x00??@\x0f\xf0\x1f \x0f0\x03\x1c\x0f\x0f\x03\x03??CC\xfc\xfc0088\x1e\x1e'),
                            bytearray(b'\x0e\xf0\x1d\xe2\x1d\xe2\xff\x00\xef\x10\xff\x00\xfd\x02\xef\x10\xfe\xf0\xff\xfe\xf3\xf2\xc1\xc010\x13\x12\x17\x16?<'),
                            bytearray(b'\x0f\x10\x07x\x7f\x80\x03<\x0f\x10?\xc0\x00?\x00\x03\x10\x10xx\x80\x80??\x10\x10\xff\xff??\x03\x03'),
                            bytearray(b'\xf3\x0c\xf1\x0e\xf1\x0e\xf9\x06\xf2\x0c\xc48\x00\xf8\x00\xc0\xff\xfc\x1f\x1e\x0f\x0e\x07\x06\x1e\x1c\xfc\xf8\xf8\xf8\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x1b\x03p\x00\x7f\x00~\x00x\x00\x00\x00\x00\x01\x01\x06\x03\x1c\x00\x7f\x00\x7f\x00~\x00x\x00\x00'),
                            bytearray(b'yx\xf6\xf0\xd8\xc0\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00x\x87\xf0\x0e\xc08\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x01\x06\t\x06\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x00\x00\x01\x01\x07\x07\x0e\x0e\x06\x06\x06\x06\x06\x06\x1f\x1f'),
                            bytearray(b'\x00\x00\xe0\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xfe\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03'),
                            bytearray(b'\x07\x18\x078_ \x7f\x00_\x00\x17\x10%<D|\x1f\x1f??a!x\x18^&\x17i=B|\x83'),
                            bytearray(b'\xfe\x01\xfc\x03\xf8\x07\xf0\x0e\x80|\xc00\xc00\x00\xe0\xc7\xc7\xcf\xcf\xff\xff\xfe\xfe||\xf0\xf0\xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x1b\x03p\x00\x7f\x00~\x00x\x00\x00\x00\x00\x01\x01\x06\x03\x1c\x00\x7f\x00\x7f\x00~\x00x\x00\x00'),
                            bytearray(b'yx\xf6\xf0\xd8\xc0\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00x\x87\xf0\x0e\xc08\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=366),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x01\x06\t\x06\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x00\x00\x01\x01\x07\x07\x0e\x0e\x06\x06\x06\x06\x06\x06\x1f\x1f'),
                            bytearray(b'\x00\x00\xe0\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xfe\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03'),
                            bytearray(b'\x07\x18\x078_ \x7f\x00_\x00\x17\x10%<D|\x1f\x1f??a!x\x18^&\x17i=B|\x83'),
                            bytearray(b'\xfe\x01\xfc\x03\xf8\x07\xf0\x0e\x80|\xc00\xc00\x00\xe0\xc7\xc7\xcf\xcf\xff\xff\xfe\xfe||\xf0\xf0\xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=350),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x1b\x03p\x00\x7f\x00~\x00x\x00\x00\x00\x00\x01\x01\x06\x03\x1c\x00\x7f\x00\x7f\x00~\x00x\x00\x00'),
                            bytearray(b'yx\xf6\xf0\xd8\xc0\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00x\x87\xf0\x0e\xc08\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=365),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x01\x06\t\x06\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x00\x00\x01\x01\x07\x07\x0e\x0e\x06\x06\x06\x06\x06\x06\x1f\x1f'),
                            bytearray(b'\x00\x00\xe0\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xfe\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03'),
                            bytearray(b'\x07\x18\x078_ \x7f\x00_\x00\x17\x10%<D|\x1f\x1f??a!x\x18^&\x17i=B|\x83'),
                            bytearray(b'\xfe\x01\xfc\x03\xf8\x07\xf0\x0e\x80|\xc00\xc00\x00\xe0\xc7\xc7\xcf\xcf\xff\xff\xfe\xfe||\xf0\xf0\xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=349),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x1c\x18\x1f\x18\x1f0?0?\x0f\x0f\x07\x07\x10\x1f#? ?`\x7f@\x7f@\x7fp\x7f8?\x10\x1f'),
                            bytearray(b' \x00\xe0\xc0\xe0\xc0\x80\x80\x80\x80\x80\x80\x00\x00\x80\x80\xc0\xf0\x00\xf0\x00\xe0`\xe0`\xe0@\xc0\xc0\xc0@\xc0'),
                            bytearray(b'!?!?\x7f\x01{\x00\x7f\x00\x7fx\x1f\x1f\x00\x00\x00?\x00?|\x03\x7f\x00\x07xx\x7f\x1f\x1f\x00\x00'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0\x00\xc0@\xc0@\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80@\xc0@@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x00\x16\x106p.b\xce\x0e8\x08\x00\x00\x00\x00\x00\x1e\x10np\x8eb\x9e\x0e\xfe\x088\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\r\x01\x13\x03\'\x07O\x0f\x1f\x1f\x9e\x1f\xbe?\x00\x03\x01\x0e\x03\x1c\x078\x0fp\x1f`\x1f\xe0?\xc0"),
                            bytearray(b'@\x00\xd0\xc0\xe8\xe0\xf0\xf0\x18\xf8\x0c\xfc\x04\xfc\x00\xf8\x00\xc0\xc00\xe0\x18\xf0\x08\xf8\x04\xfc\x00\xfc\x00\xf8\x04'),
                            bytearray(b'\xbe?\x9e\x1f\xb8?X\x1fOOp@?1\x19\x19?\xc0\x1f\xe0\xbf@\x1f`Op@\x7f1?\x17\x1f'),
                            bytearray(b'\x08\xf8\x04\xf4\x04\xe0\x04\xc8\xa4\xa8\xf8`\xf8\xe0\xd0\xc0\xf8\x04\xf4\x0c\xe4\x18\xd4 \xb4`x\xe0\xe0\xf8\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f \x17 \x17 \x17\x00\x15\x00\x05\x00\x01\x00\x01\x00::2222\x16\x16\x14\x14\x04\x04\x00\x00\x00\x00'),
                            bytearray(b'\xe0\x10\xc0 \xc0 \x80 \x80 \x80 \x80 \x00 \xf0\xf0\xe0\xe0\xe0\xe0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0  '),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1e\x01?\x00\x7f\x00\x7f\x00\x7f\x00?@?@?@\x1f\x1f  @@@@@@hhhhxx'),
                            bytearray(b'\x00\x80\xf0\x00\xf0\x00\xf0\x08\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x80\x80\xf0\xf0\xf0\xf0\xf8\xf8\xb8\xb8\xb8\xb888\xb8\xb8'),
                            bytearray(b'?@?@?\x00?\x00?\x00\x1f \x1f \x1f hhhh((((((****::'),
                            bytearray(b'\xf0\x08\xf0\x08\xf0\x08\xf0\x08\xe0\x18\xe0\x18\xe0\x10\xe0\x10\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb8\xb0\xb0\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=94),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'000000pppppp\x00\x00\x00\x000\xce0\xce0\xccp\x8cp\x8cp\x88\x00\xf8\x00\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1e\x01\x7f\x00\x7f\x00\x7f\x00?@?@\x0f0\x00\x00\x1f\x1f@@@@@@@@``??'),
                            bytearray(b'\x00\x00\x00\xf0\xc08\xf0\x0c\xf8\x04\xe8\x14\xe8\x14\xe8\x14\x00\x00\xf0\xf0\xf8\xf8<<\x1c\x1c\x1c\x1c\x1c\x1c<<'),
                            bytearray(b'>A>A=B\x1f \x07\x18\x01\x1e\x1f\x00\x0f\x10aaAAOO??\x1f\x1f\x1f\x1f\x1c\x1c\x1c\x1c'),
                            bytearray(b'p\x8c\xf0\x0c\xe0\x1c\xc08\xc08\x80x\xe0\x10\x80p\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8\xf8\xf8\xf8\xf800pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=88),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x11\x1f \x1f \x1e!\x00\x00\x00\x00\x00\x00\x0e\x0e\x1f\x1f11!!33'),
                            None,
                            bytearray(b'?\x003\x1c3\x1e.\x0c"\x00\x1c\x00\x00\x00\x00\x00!\x00>\x01\x1e!\x0c2\x00>\x00\x1c\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x00\x01\x01\x01\x017\x07/\x0f\x10\x1f\x1f\x1f\x18\x18\x01\x0f\x00\x1f\x01\x1e\x078\x1e1 ? ?\'?"),
                            bytearray(b'\x0c\x04\x98\xd8\x00\xf8\xa4\xfc\x10\xf0.\xa0\x8f\x80\x0f\x00\xc0\xfc4\xe8\x04\xf8\x00\xdc\x08\xd8\\\xb2~\xf1\xfe\xf1'),
                            bytearray(b'\x02\x1e">\x05=\xc7=\xff\x01\xf7\x01\xfe\x82||!?A\x7fC\x7fC\xbd\x7f\x81?\xc1\x8a\xf6||'),
                            bytearray(b'?!~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xff~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'000000pppppp\x00\x00\x00\x000\xce0\xce0\xccp\x8cp\x8cp\x88\x00\xf8\x00\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1e\x01\x7f\x00\x7f\x00\x7f\x00?@?@\x0f0\x00\x00\x1f\x1f@@@@@@@@``??'),
                            bytearray(b'\x00\x00\x00\xf0\xc08\xf0\x0c\xf8\x04\xe8\x14\xe8\x14\xe8\x14\x00\x00\xf0\xf0\xf8\xf8<<\x1c\x1c\x1c\x1c\x1c\x1c<<'),
                            bytearray(b'>A>A=B\x1f \x07\x18\x01\x1e\x1f\x00\x0f\x10aaAAOO??\x1f\x1f\x1f\x1f\x1c\x1c\x1c\x1c'),
                            bytearray(b'p\x8c\xf0\x0c\xe0\x1c\xc08\xc08\x80x\xe0\x10\x80p\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8\xf8\xf8\xf8\xf800pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=343),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x04\x07\x08\x0f>\x01\'\x00?0\x1f\x1e\x07\x07\x00\x00\x08\x0f\x10\x1f<\x03?\x003<\x1e\x1f\x07\x07\x00\x00"),
                            bytearray(b'`\xe0`\xe0\xc0\xc0\x80\x00\xe0 \xe0 \xc0\xc0\x00\x00\x00\xe0\x00\xe0\x00\xc0@\xc0 \xe0 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x07\x07\x07\x07\x03\x03\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x18\x1f\x18\x1f\x0c\x0f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\xf8\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xe8\x18'),
                            bytearray(b'\x00\x00\x02\x03\x02\x03\xf0\xf1\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\x00\x00\x00\x03\x1c\x1f\xfe\xff\xff\xff\xff\xff\xff\xff\xf8\xf8'),
                            bytearray(b'\x98\x08\x1c\xc4\x1c\xe4<\xe4\xfc\xe4\x1c\x04x\x08pp\xf8\x084\xcc\x14\xec\x14\xec\x14\xec\xf4\xec\x88\xf8pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=115),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x07\x07\x07\x07\x03\x03\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x18\x1f\x18\x1f\x0c\x0f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            bytearray(b"\x04\x07\x08\x0f>\x01\'\x00?0\x1f\x1e\x07\x07\x00\x00\x08\x0f\x10\x1f<\x03?\x003<\x1e\x1f\x07\x07\x00\x00"),
                            bytearray(b'`\xe0`\xe0\xc0\xc0\x80\x00\xe0 \xe0 \xc0\xc0\x00\x00\x00\xe0\x00\xe0\x00\xc0@\xc0 \xe0 \xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\xf8\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xe8\x18'),
                            bytearray(b'\x00\x00\x02\x03\x02\x03\xf0\xf1\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\x00\x00\x00\x03\x1c\x1f\xfe\xff\xff\xff\xff\xff\xff\xff\xf8\xf8'),
                            bytearray(b'\x98\x08\x1c\xc4\x1c\xe4<\xe4\xfc\xe4\x1c\x04x\x08pp\xf8\x084\xcc\x14\xec\x14\xec\x14\xec\xf4\xec\x88\xf8pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=114),
                    ]
                ),
                Mold(29, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18t\x1c\xf8\x00\xf8\x00p\x88\x00p\x00\x00\x00\x1c\x18$\x1c\x00\x80\x84\x80\x80\xc8\xc8pp'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x04\x07\x08\x0f>\x01\'\x00?0\x1f\x1e\x07\x07\x00\x00\x08\x0f\x10\x1f<\x03?\x003<\x1e\x1f\x07\x07\x00\x00"),
                            bytearray(b'`\xe0`\xe0\xc0\xc0\x80\x00\xe0 \xe0 \xc0\xc0\x00\x00\x00\xe0\x00\xe0\x00\xc0@\xc0 \xe0 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x07\x07\x07\x07\x03\x03\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x18\x1f\x18\x1f\x0c\x0f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\xf8\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xe8\x18'),
                            bytearray(b'\x00\x00\x02\x03\x02\x03\xf0\xf1\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\x00\x00\x00\x03\x1c\x1f\xfe\xff\xff\xff\xff\xff\xff\xff\xf8\xf8'),
                            bytearray(b'\x98\x08\x1c\xc4\x1c\xe4<\xe4\xfc\xe4\x1c\x04x\x08pp\xf8\x084\xcc\x14\xec\x14\xec\x14\xec\xf4\xec\x88\xf8pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=107),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\xe0R\xb2F\xa0x\x80\x00p\x00\x00\x00\x00\x00\x00\xe0\xfe\xf2\xee\xa0\xbe\xe0\xf8pp\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=6, mold_id=16),
                        AnimationSequenceFrame(duration=6, mold_id=15),
                        AnimationSequenceFrame(duration=6, mold_id=14),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=27),
                        AnimationSequenceFrame(duration=2, mold_id=28),
                        AnimationSequenceFrame(duration=4, mold_id=29),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
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
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=26),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL644_MARIO_ATTACK_UP_RIGHT,
    palette_offset=0,
    unknown_num=0
)
