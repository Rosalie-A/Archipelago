# SPR0615_WHIRLPOOL_DESERT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL448_WHIRLPOOL_WATER
sprite = CompleteSprite(
    animation=AnimationPack(339, length=241, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x18\x00\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x08\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x1c\x14\x18\x04\x14\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x04\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x18$<\x084(\x084\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x14\x10\x08\x040\x0c\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x008(xLdX4`0\x00\x00\x00\x00\x00\x00\x00\x00\x0040($@\x14\x000\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00,8~@8Nx\nP0(\x18\x00\x00\x00\x00\x04\x0060& x\x02p\x00\x008\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x1c"<C}\x06}\t9eP (\x18\x00\x006\x00S\x10r1@\x05P\r P\x04<\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0`@\xe0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x08\xb0\x10@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\xee\xf1\x02#\x8a \xf8\x05\xba\x00\x00\x00\x00\x00\x001\xc0\xfc\x005\xc0\x00\xff?\xc0\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xee\x13\xe5\x1fy\xfc\x057@@\x00\x00\x00\x00\x00\x00\x8f\x00?\x00\xfe\x00:\xc1\xe0 \x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b':;\x07\x1d\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04;\x02\x1d\x03\x04\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0}\x98\xffFw\xc6j\x00\x17\x00\x00\x00\x00\x00\x00\xc3<A\xbe0\xcf\x0e1\x10/\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x000\xe0`\x98\xf4\x98\xf8\xc4\x00\x00\x00\x00\x00\x00\x00\x80\x80\x10\xc8\x00\xcc\x00\xcc\x00'),
                            None,
                            bytearray(b'\xdf\xe0\x0c\xe3\x97j\x9fh\x8e\xf0\xeaT\xf8v\xa4\xfc\xe6\x01\xf3\x00\xf1\x00\xf0\x00a\x00\xe1\x01\xcc\x02\xd8\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x03\x83\x7f=\xf2\xc4\xda\x07\xf8\x00\x00\x00\xff\x00\xff\x03\xfc\xff\x00\x0f\x00\xe1\x00\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xc0||\xff\xff\xfe\xff\xbf\x7f\xef\x1f\xfb\x07\x00\x00\xc0 |\x80\xff\x00\xff\x00\xff\x00\xff\x00?\x00'),
                            bytearray(b'\x7f\x80\x0b\x8c\x07\xfe\xff<\x83<\xef0?\x18ox\x00\x00\x0c\xf0\xff\x00\xc3\x00\xc0\x00\xc0\x00 \xc0@\x80'),
                            bytearray(b'\xfe\t\xff\x06\x7f\x83\xff\x81\xff\xc3\xbfA\xff\x01\xff\x02\x07\x00\x01\x00\x00\x00\xc2\x00 \x00"\x00"\x00!\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x01\x0f\x0f\x18\x1fH/\x03c\x00\x00\x00\x00\x00\x00\x01\x02\x0f\x00\x1f\x00\x0fp\x00\x7f'),
                            bytearray(b'\x00\x00\x0c\x00@L\x00@\xff\xc0$\xcb0x\xe0\xe7\x00\x00\x00\x0f\x00\x7f\x00\xff\xff\x00\xf0\x00\x00\xff8\xc0'),
                            bytearray(b'\xfc\xfd\xfe\xff\xfa\xfb\xff\xfb\xfc\xf5\xf4\xff\xc4\xd4`\xf7\x00\xfe\x01\xfc\x04\xfb\r\xf2\x1a\xe4\x19\xe4;\xe4\n\xf4'),
                            bytearray(b'\x17\xf8\xb0\xcc\xc9\x9d\xa0s\xc4\xedceBl\xe8\xefP \x04\xc3\xa1\x1e\x03<\r\xf2\x82\xfc\x82\xfd\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=112),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'L\xc4 \x10\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc84(\xc80\x10@\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\r\xb6\x03\x8c\x03\xfc\x04\xd9 o\x00\x00\x00\x00\x00\x008\xc0\x8fp\x00\x00\x1f\xe0p\x80\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~\xc1;E\xe9\t\x8b\x8b\x00\xa0\x00\x00\x00\x00\x00\x000\x00\x83\x00\x19\x06\x8cp\x90p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10\x7f\x00\x16\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12M\x11\x0e\x01\x06\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'C\xd5\xf1\xf8n\x7f\x10_\x00\x1f\x00\x00\x00\x00\x00\x00!\xf8\x02\xfc\x00\xff@\xbf\x00\x1f\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\x00\xf8`\xfc\xe4z\xe6\xf87\x00\x00\x00\x00\x00\x00\x80@\x90\x08\x1c\x00\x1e\x00\x8f\x00'),
                            None,
                            bytearray(b'\xbc\xdb\xbcK\xfcK\xac[\xb8\x17\xf1\x0f\xf4-\xe8Z\x87\x00\xc7\x00G\x00G\x00O\x00\x1f\x00\x1d\x02:\x05'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x83\x83\x01\x01\x00\x00\xf0\x0c\x08\xf3\x0f\xff\xff\x00\x00\x00\x83|\x01\xfe\x00\xff\x03\x00\xfc\x00\xff\x00\x00\x00'),
                            bytearray(b'\x00\x00\xb0\xe0\x91\xee\xf3\xdc2;\xb1S\xf5M\x1bg\x00\x00\xe0\x10\xde\x01\xec\x00<\xc02\x0c\x8d\x02\xf3\x00'),
                            bytearray(b'\x0e\x0ea~?\xcf\xa6\xbb;\xfc?3?/\x1fc\x0e\xf1\x7f\x80\xf0\x00\xbc@\x00\x00<\xc00\xc0p\x80'),
                            bytearray(b'\xb5\x82~\xe1\xffX\x7f\xfc\xa9\xd6\xf9N\xfb\x04\xf3\x0c\xcc\x00\xf2\x00\xb1\x00\x08\x00\x0c\x00\x04\x00\x0c\x00\x08\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x03\x01\r!\x07>\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0b\t\x06\x18 &\x01'),
                            bytearray(b'\x00\x00\x07\x000\x07\x80\xb0\x11\x16 \xd3\xc8N\x05\xee\x00\x00\x00\x07\x00?\x80\x7f\x18\xe0\x0f\x00\xc0?\x08\xf0'),
                            bytearray(b'\x06>\x1a\xff1\xfaB\xf1\x03\xff=\xe9\x11\xa9c\x9b\x00\xff\x03\xfc\x07\xf8\x0b\xf4\x10\xeb>\xc3^\x83\x14\x8b'),
                            bytearray(b'\x86.\x90x`\xfc\x80\xfb\xe2\xff\xe6\xe9\xcc\xf1\xc5\xf9\xd0\x0f\xc0?\x00\xff\x03\xfc\x02\xfc\x04\xf8\n\xf1\x00\xf3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=112),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xd0\x1c \xf0\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\xb8\x04x\x08\xe0\x00\xc0@\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\xdf\x06q\x00\x1fha\xa1\xfe>>\x00\x00\x00\x00\xd0 ~\x80\x1f\xe0\xfe\x00\xff\x00\xc1\xff\x00\x00\x00\x00'),
                            bytearray(b'\xb0na\x17\x04\xdd\x03\xdf\x00P\x00\x00\x00\x00\x00\x00\x1d\x00\xf8\x00\xe3\x00?\x00\xa8\x18\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1e\x1f\x0f\x0f\x03\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x0f\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b' \x9b\x14\xd6\x88\xe8\xe2\xee<>\x1c\x1c\x00\x00\x00\x00M\x86<\xc3\x1e\xe1\x0f\xf0\x00?\x03\x1f\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\xf0\x00\xfc\x00~\x84\xbeF\x00\x00\x00\x00\x00\x00\x00\x80\xe0\x10\xf8\x04x\x028\x00'),
                            None,
                            bytearray(b'~\x87\xbfE~\x85\xff\x04}\x8a\xfd\x02y\xa7\x9ad\x18\x00\x18\x00\x18\x00\x99\x00\x91\x00\x93\x00\x06\x01.\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\xff7\x83j\xfa\x05\x03\x02\x82\xfe\x04\x07\x01\x01\x00\x00?\xc0\xfb\x04\xe3\x00\x03\xfc\xfe\x01\x07\xf8\x01\xfe'),
                            bytearray(b'\x00\x00\xe0\x00\xfc\xc4\x7f\x80_\xa4VK}\xe2\x1f\xf9\x00\x00\x00\xe0\x00\x00\xe2\x01\x19\x00d\x80\xf0\x00\xfc\x00'),
                            bytearray(b'\x03\xfcg\x9e\xff\x01\x0f\x90\xbf\xd8\xc7\x1b\xc7\xd9\xff\x91\xff\x00\x01\x00\x00\x00`\x00\xe7\x00\xe0\x00\xe0\x00\xe0\x00'),
                            bytearray(b'\xfbf\xe7X\xf7)\xfaUv\x8d\xbeM\xff\xcd\xf7\xc8\xfe\x00\xbf\x00\xdf\x00/\x00\x13\x00\x93\x00\x13\x00\x17\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x07\n\x06\x08\x00 4\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x08\x0f\x10\x0b0'),
                            bytearray(b'\x00\x00\x03\x00\x1e\x0b\xd2S\x00\x00\x90#\x00b\x1c~\x00\x00\x00\x03\x0c\x10S\xac\x00\xff\xff\x00\xe0\x1f\x00\xff'),
                            bytearray(b'\xf9\xfb\xe7\xef\xef\xff^\xbf??\xfe\xff~~~~\x00\xe7\x10\xef\x00\xdf\xc0\x1f\x80\x7f\x00\xff\x00\x7f\x00\x7f'),
                            bytearray(b'\xe6\xe6\x80\xc3\x13\xb4?\xe0\xba\xc6\xf4\x87`\x85a\x85\x06\xf9\x02\xfc\x18\xe0 \xc0\x84\x03\x01\x0e\x19\x0e\t\x1e'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=5),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=8, mold_id=8),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL448_WHIRLPOOL_WATER,
    palette_offset=2,
    unknown_num=0
)
