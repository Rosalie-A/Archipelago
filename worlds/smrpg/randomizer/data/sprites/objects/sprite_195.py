# SPR0195_FLOWER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\n\x0e\x14\x18Iq\x8f\xe3v\x90`\x1bb\x1e\x00\x03\x0e\x018\'p\x0f\xe4\x1b\x94\t\x18\x84\x1e\x01"),
                            bytearray(b'\x00\x00\xf004\x1c\xfa\xce\xc7\xd73\x05\xe2\x0c\x8a\xfe\x00\xc08\xc8\x1c\xe0\x0e\xf0\x07\xf8\r\xf8\xdc1\xfe\x00'),
                            bytearray(b'\x1f\x10\x0b\x0e\x1f\x1f\xcf/$VXd\x00\x01\x01\x01\x10\x00\x1a\x1c\x7f\x7f\xff\xff\xff\xff\x7f\x7f\x03\x03\x01\x01'),
                            bytearray(b'\x98x\x08\xc8pp\xfe\xfev\xf9\xeds\xa8X\x90\xd0x\x00\xf88\xf0\xf0\xff\xff\xff\xff\xff\xff\xf8\xf8\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x00\x17\x17\x7f\x1f??\xf9_{]\x7f\x7f\xdf_\x00\x07\x06\x19\x00\x7f _F\x99D\x99d\x9b@\xbf'),
                            bytearray(b'\xc0\xc0\xf0\xf0\x94\x84\x92\x82"\x12\xf3\xcb\xe2\xd2\xb2\x8a \xe0\x0c\xfc\x0e\xfe\x0e\xfe\x0f\xff\xc7?\xcf?\x87\x7f'),
                            bytearray(b'\xf3s\x9f\x9f\x7f\x7f\x06\x1d\x0e\x14!\x00\x18\x07\x1f\x1fO\xbf\x7f\xff\x7f\x7f<%\x14%\x00?\x00\x1f\x1f\x1f'),
                            bytearray(b'\xb6\xb6\xfe\xfe\xfe\xfe\x98\xf8\xc8\xa8\x8cL\x18\x98\xf0\xf0\xff\xff\xff\xff\xfe\xfe\x9c\xfc\x9c\xfc<\xfc|\xfc\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00<"z\x07m\x1f\x9a{\x98\xd8\xbf\xd9\x99\xfa\x00\x1e \x01\x00@\x8c\xcc\x1c\x8c\x1c?\x1a<\x18<'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\xa1\x00\xfe@\x86x\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00@\xff\xa0\x01\x00\x01'),
                            bytearray(b'\xb8\xdc\x98\xf8\x89\xc8\x82aA3\x0c7 \x1e\x00\x0c\x18?\x1f?\x1e?\x0e\x9c\x8c\xcc\x08\x00\x00!\x01\x13'),
                            bytearray(b'\x00\x00\x00\x00\x14\x08\x9c\x08\x94\x18\x14\x18\x00\x00\x00\x00\x01\xff\xe4\xfc\xd0\xc4\xd0D\xd0D\x90\x84\x8c\x8c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x00\x01\x01\x03\x00\x03\x00\x07\x01\xffb\xfb\x07\x00\x01\x00\x01\x00\x02\x00\x00\x00\x04\x00\xf8\x83\x02\x03\x82'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\xf0\xc0\x9f\xe0\xb2\xcc\x00\x00\x00\x00\x00\x80\x00\x00\x00@\x00?\x86\x81\x81\x83'),
                            bytearray(b'C?#\x1f\x17\x1a-\x13\x19$d8\x10 \xc0\x00\x83\xc2Cb" \x00 \x00\x03\x02F\x08X \xe0'),
                            bytearray(b'\xe4\x98\xc0\xb0\x10\xf0\x88\xf00`t\x08\x10\x08\x02\x00\x82\x86\x84\x8c\x08\x08\x00\x08\x00\x88\x80\xc4 4\x0c\x0e'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x04\x0b\x00\x0f``8\x18~N\xbf\x83\x07\x07\x18\x1f0?p\x7f\x7f\x7f\x9f\xcf\xcf\x8b\xc3\xc1'),
                            bytearray(b'\x00\x00\x00\x00\x04\x84\x02\x02\x06\x06\x1d\x19\x7fs\xff\xc3\xe0\xe0\xf8\xf8|\xfc\xfe\xfe\xfe\xfe\xf9\xf3\xf3\xd1\xc3\x83'),
                            bytearray(b'\x9c\x80\xc0\xc0\xf7\xf1|}y\x7f??\x0f\x0f\x07\x07\xe3\xe3\xff\xff\xf9\xfa~{x\x7f<?\x0c\x0f\x06\x07'),
                            bytearray(b'?\x07??\xffO\x1e^\xce\xfe\xfc\xfc\xf8\xf8\xe0\xe0\xc7\xc7\xff\xffO\xaf\xbe\xee\x0e\xfe\x1c\xfc8\xf8`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x1e\x08\x0b\x04\x07\x02\x01\x02\x05\x02\x0b\x00-0\x00\x02\x08\x07\x00\x07\x02\x04\x04\x07\x00\x07\x03\x0c1\x06'),
                            bytearray(b'\x00\x80\xd0\xd8\xe0\xd0\x00\xa0 \xe0\x00\xc0P\x10\x8c@\x80@\xd8 \xd0 \x80` \xe0 \xe00\xf00\xfc'),
                            bytearray(b'?@\xff\x80\xfe\x80\x7fp\x9f\x10n\x8f\x13c\x07\x18@\x00\x83\x03\x81\x00q\x81\x11\xe1\x0f\xf1\x03\x7f\x00\x1f'),
                            bytearray(b'\xfa\xf8\xc09\xf2\t\xda9m\xa3Q\xcd\xe6\xd6\xc8(\xf8\x06\xf8\xc7\x88\x87\xb8\x87\xa1\x9f\xc3\xbf\xce\xfe\x18\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\r\r\x1f\x11<#3,\x1b\x1c\'\x08\x00\x00\x00\x01\r\x02\x11\x00#\x00,\x00\x1c \x080"),
                            bytearray(b'\x00\x00\xc0\xc0 \xe0\xf8\x188\xc8\xa8x\x98x\xc4 \x00\x00\xc0 \xe0\x10\x18\x00\xc8\x00x\x04x\x04 \x1c'),
                            bytearray(b'\x17\x187.\x1c/\x13\x13$\x04\x1c\x07\x06\x02\x00\x00\x18 .\x00/\x00\x13,\x04;\x07\x18\x02\x05\x00\x00'),
                            bytearray(b'\xcc(\xa8xH\xd8\x10\x10(\x00\xf0\x80\xc0\x00\x00\x00(\x14x\x04\xd8$\x10\xec\x00\xf8\x80p\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07??7\x08oP\x7fP\xcfP\xcf\x10_ \x07\x08?\x00\x08@P\x80P\x80P\xa0\x10\xe0 \x80'),
                            bytearray(b'\x1c\x1c\xbe\x86\n\xb6\xba~\xfe.\xfd$\xff\x04\xd7.\x1c\xa0\x86@\xb6A~\x01.\x01$\x03\x04\x03.\x01'),
                            bytearray(b'\xaf\xf0\xa0\xff\xbf\xffOo\x80\x00i\x08\r\x0c\x0f\x00\xf0\x00\xff\x00\xff\x00o\x90\x00\xff\x08w\x0c\x13\x00\x0f'),
                            bytearray(b'\x04\xfe}\xff\xb9\xbb\x02\x06E\x0c\x9a\x18\xfc\x00\x80\x00\xfe\x01\xff\x00\xbbD\x06\xf9\x0c\xf3\x18\xe6\x00\xfc\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'p\x00\xa9 \xfb`\xd5@\xbd\x00d\x00F\x00+\x00\x00p \xd9`\x9b@\xb5\x00\xfd\x00d\x00F\x00/'),
                            bytearray(b'\x1c\x00\xb6\x04\xf7\x06\xe9\x00\x07\x00p\x00X\x00\xb8\x00\x00\x1c\x04\xba\x06\xf9\x00\xef\x00\x07\x00p\x00x\x00\xb8'),
                            bytearray(b'\t\x00\x0c\x04^\x06\xd4\x00\xab \xf5pl 8\x00\x00\x0f\x04\x0b\x06Y\x00\xf7 \xdbp\x8d \\\x008'),
                            bytearray(b'\xb8\x00\xda\x00\x1d\x00\xcb\x02\x97\x06-\x0c"\x00\x1c\x00\x00\xb8\x00\xda\x00\x1f\x02\xcd\x06\x99\x0c3\x00>\x00\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x02\x02\x03\x03\x03\x03\x03\x03\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x02\x02\x02\x02\x02\x02\x02\x02'),
                            bytearray(b'\x00\x00\x80\x80\xe0\xe0\xf0\xf000\x10\x10    \x00\x00\x80\x80\xe0\xe0\xf0\xf000\x10\x10    '),
                            bytearray(b'\x02\x02\x1e\x1eoo\xa7\x87\x8f\x8f\xff\xff~~<<\x02\x02\x1e\x1e\x7f\x7f\xdf\xdf\xff\xff\xff\xff~~<<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=9),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
