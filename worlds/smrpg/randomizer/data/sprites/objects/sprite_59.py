# SPR0059_TADPOLE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL416_TADPOLE
sprite = CompleteSprite(
    animation=AnimationPack(300, length=180, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x02\x03\x07\x06\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x00\x03\x00\x07'),
                            bytearray(b'\x08\x18\x1404`\xf0P\xa8\xd8`\x80`\xf0\xa0 \x00\x10\x0c0\x0cp\x18\xe0\x10\xe0\x10\xe0`\x80@\x80'),
                            bytearray(b'\x00\x01\x03\x07\x07\x0fM\x1e\x1b\x1d7<\x1e17\x1c\x00\x01\x02\x07\x04\x0fH_\x11\x1e\x07 \x04(Tj'),
                            bytearray(b'9\xce\xbe\xd5\xfa\x16\xff\x06\xce>\xfe\xbf>~\xbe\x7f\x00\xff\x11\xee\x10\xee\x01\xff\x07\xff\x8e\x7f\x9f\x7f\xbe\x7f'),
                            bytearray(b'@\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0 \xc0\xc0\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00'),
                            bytearray(b"n\'\x04\t\x04\x00\t\x17\x03\x04\x00\x01\x00\x00\x00\x00tJ? \x1f\x1d\x01\x1e\x00\x07\x00\x01\x00\x00\x00\x00"),
                            bytearray(b'\xfc\xfc\xacf\x9c\x1c\xf0\xb8\xe0\xf0\x00\xc0\x00\x00\x00\x00\xbe~\x1c\xfe\xe8|\x80x\x00\xf0\x00\xc0\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x01\x03\x03\x03\x07\x03\r\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x07\x08\x0f'),
                            bytearray(b'\x08\x18x0h\xd8\xa8\xd8x\x90\xd0\xb0\xc00\xc0\xe0\x00\x10\x18`\x10\xe0\x10\xe0\x08\xe0 \xc0\x10\xc0\xa0\x00'),
                            bytearray(b'\x00\x00\x01\x03\x07\x07\x0e\x0f\r\x1e\x1f\x1b\x1680<\x00\x00\x00\x03\x02\x07\x04\x0f\x08\x1f\x13\x1c\x13<\x178'),
                            bytearray(b'\x0b\x1d\xa4\xda\xfa\x96\xfe\x04\xf5\x0e\xde\xbe\xfe\xbe~\xbe\x01\x1e\x02\xfc\x12\xec\x00\xfe\x05\xff\x86~\x9f\x7f\x9e~'),
                            bytearray(b'\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\xa0 \xc0\xc0\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00'),
                            bytearray(b'\x1f<4\x7f\x15&\x1e\x0f\x17\x14\t\x01\x02\x01\x00\x00G`dH\x18>\x05\x1e\x14\x0b\x00\x0f\x00\x03\x00\x00'),
                            bytearray(b'\xbe\xfc|\xee\xfe\xbc\xf8\xfc0\xf8p\xe0\xe0\x00\x00\x00\x9e~<\xfe|\xfex\xfc\x00\xf8\x00\xf0\x00\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x01\x03\x06\x06\x03\x0c\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x07\x00\x0f'),
                            bytearray(b'\x00\x00P0\xb0P\xb0\xf0\xe0\xb0\xc0\x80\xf0`\x80\xc0\x00\x00\x10`\x10\xe00\xc00\xc0 \xc0P\x90\x80\x00'),
                            bytearray(b'\x00\x00\x00\x00\x01\x03\x07\x07\x0c\x0f\x0b\x1d\x1f\x1a>\x1c\x00\x00\x00\x00\x01\x03\x06\x07\x04\x0f\t\x1e\x13\x1c\x178'),
                            bytearray(b'\r\x0f\x18\xde\xb0\xcc|\x90\xf5\x0e\xcc>\xdf>\xde\x7f\x01\x0e\x03\xdc\x04\xf8\x10\xec\x03\xff\x04\xfe\x8d\x7f\xdf?'),
                            bytearray(b'\x80\xa0@\x80\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00  \xc0\xc0\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00'),
                            bytearray(b'\x14<7\x18\x1f \x0e4\x1e\x1f\x0f\x1e\x03\x07\x06\x01\x1783<\x1c/\x07,\x04\x1c\x04\x1f\x00\x0f\x00\x07'),
                            bytearray(b'~\xbe\xae\xf6\xfc^\xfc\xfc\xf8\xfc\xf0\xf8\xc0\xf0\x80\x00\x9c~\x9c~|\xfe\xf8\xfc\xf8\xfcp\xf8\x00\xf0\x00\x80'),
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
                            bytearray(b"\x08\x07\x0b\x1f7\x18opowow\x7fwwz\x00\x0f \x1fp\x1f`?\'xgx\xa7\xf8\xa2\xfd"),
                            bytearray(b'@\x80\xf4\xe0h\x90\xf4\x18\xfa\x14\xfa\x14\xdc&\xfd~\x00\xc0\x04\xf4\x00\xf8\x10\xec\x12\xee\x10\xee\x00\xfe\x00\xff'),
                            None,
                            bytearray(b'9\xbe*L< \x1f\x07\x0e\x01\x03\x00\x00\x00\x00\x00\xf0\xffp\x7f#\x1f\x07\x18\x00\x0f\x00\x03\x00\x00\x00\x00'),
                            bytearray(b'}\xfe\xdd?\xb7\x9c\xdc\x83d\xe1\xc0\x00\x00\x00\x00\x008\xff\x00\xff\xc3`\xb0`\x1f\xfb\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'`\x80\x98\xf8`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x18\xe0\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b"\x00\x00\x0b\x07\x0c\x1fw\x18\x7f2?wg\x7f\xf7{\x00\x00\x00\x0f\x00\x1fP?b=\'x\xa7\xf8\xa3\xfc"),
                            bytearray(b'\x00\x00\xa0\xc0@\xf0\xf0\x08\xf84\xfc\x00\xd8/~\xff\x00\x00\x00\xe0\x00\xf0\x00\xf80\xcc\x00\xfc\x08\xf7\xec\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xa0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0'),
                            bytearray(b'4~x\x04;\x0c\x1f\x0f\x0c\x03\x03\x00\x00\x00\x00\x007x7x\x0f3\x0f\x10\x00\x0f\x00\x03\x00\x00\x00\x00'),
                            bytearray(b'\xe4\xbbl3\x1e\xae\xb2`\xf0\xf0\x80\x00\x00\x00\x00\x00`\x1f\xe0\x00\xc1p\x1a\xfa\x00\xf0\x00\x80\x00\x00\x00\x00'),
                            bytearray(b'h\x90\x08\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xe0\xf8\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x03\x00\x06\x0f\x0b\x1c\x1787;\xb4~4}\x00\x00\x00\x03\x00\x0f\x00\x1f\x10?#<\xa7\xf8\xa6\xf8'),
                            bytearray(b'\x00\x00\xc0\x00\xf0\xe0b\x98\xf4\x10\xe9\xe8^S]\xfe\x00\x00\x00\xc0\x00\xf0\x02\xfa\x10\xec\xf4\x01\xb8\x07<\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x10\xe0'),
                            bytearray(b'~3w+\x1b(\x19\x0f\x1f\x00\x04\x03\x00\x00\x00\x00tx<x\x0f3\x0f\x10\x00\x1f\x00\x07\x00\x00\x00\x00'),
                            bytearray(b'\r\x8cm3\xdcx\xe2\x14`\xf8\xa0\xc0\x00\x00\x00\x00s\x00\xe0\x00\xc0<>\xfe\x00\xf8\x00\xe0\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\xe0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x04\x00\x00\x04\x00\x00\x00\x03\x07\x0b<\x0f\x00\x00\x00\x00\x04\x04\x04\x04\x00\x00\x03\x03\x0f\x0f<?'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00`p\x8c\xf0\x08\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\xe0\xe0\x1c\xfc\x00\xf8'),
                            None,
                            bytearray(b'?:>,48=>\x1e\x1f\x07\x07\x00\x00\x00\x003<78?<<?\x1e\x1f\x07\x07\x00\x00\x00\x00'),
                            bytearray(b'\xda=\xcafn\x9e\x9e~<\xfc\xf0\xf0\x00\x00\x00\x00\x8f\x7f\xde>\xfc\xfe\x1e\xfe<\xfc\xf0\xf0\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(7, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x0b\x07\x0c\x17\x10\x10\x00\x00\x00\x00\x00\x00\x01\x01\x06\x07\x0f\x0f\x1c\x1f'),
                            bytearray(b'\x00\x00\x08\x00\x00\x00\x00\x00`\xc0\xb4\xd8|\x9e\xf6\x0c\x00\x00\x08\x08\x00\x00\x00\x00\xb0\xf0\x9c\xec\x1a\xee\x06\xfe'),
                            None,
                            bytearray(b'\x1b\x1d/\x12\x08\x1d\x1d\x1a\x0e\x0f\x07\x07\x03\x03\x00\x00\x11\x1e;<\x1f\x1f\x1c\x1f\x0e\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xca>\xd6.\xce>\x9e~<\xfc\xf8\xf8\xf0\xf0\x00\x00\x0c\xfe\x9e~\xee\xfe\x1e\xfe<\xfc\xf8\xf8\xf0\xf0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(8, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\t\x07\x07\x0f\x8c\x0f\x0b\x1d\x00\x00\x00\x00\x00\x00\x00\x00\r\x0f\x0e\x0f\x94\x9f\x19\x1e'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xe0\xb9\xc0~\x90\xf4\x0e\xcd>\x00\x00\x00\x00\x00\x00\x00\xe0\t\xf9\x12\xee\x02\xfe\x05\xff'),
                            None,
                            bytearray(b'?\x05\x17\x1c\x06\x19\x0c\x0f\x0e\x0f\x07\x07\x07\x07\x01\x01=>\x1c\x1f\x1f\x1f\x0f\x0f\x0e\x0f\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\xc2<\xd8$\xb4L\x88x\xf8\xf8\xf8\xf8\xf0\xf0\xc0\xc0\x06\xfe\x1c\xfc|\xfc\xd8\xf8\xf8\xf8\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL416_TADPOLE,
    palette_offset=0,
    unknown_num=0
)
