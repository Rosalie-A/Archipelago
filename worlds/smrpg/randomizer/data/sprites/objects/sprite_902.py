# SPR0902_WAR_FAN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL544_WAR_FAN
sprite = CompleteSprite(
    animation=AnimationPack(394, length=216, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'as/ \r\x02\x11\x1f\x12>\xd4\xfcLL\x08\x08\x03|\x10?r}npLp\x0c\xf08p00'),
                            bytearray(b'\xf0p\xdc\xdc\x88\x88\x08\x08\x08\x08\x08\x08\x08\x08\x00\x00\xf8\x08\x98\x04\x1c\x14\x1c\x14\x18\x10\x10\x18\x10\x10\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03'),
                            bytearray(b'\x00\x04\x00\x0e\x00>(T\x06r*\xd6\x1e\xe2\x1c\xa0\x02\x06\x00\x0e\x01?*~\x08|$\xf8\x00\xfc`\xdc'),
                            bytearray(b'\x00\x00\x00\x03\x00\x00\x01\x07\t\x08\x08\t\x0e\n\x0f\x01\x03\x03\x0c\x0f\x0f\x0f\x19\x1e\x14\x1f\x15\x1e693<'),
                            bytearray(b'|\x84|\x04|\x04\xbcd\xbc\xe4\xfc\x84\xfcT|\xb4\x04\xf8\x04\xf8\x00\xfc`\x9c\xe0\x18\x80xP\xa8\xb0H'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=84),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'as/ \r\x02\x11\x1f\x12>\xd4\xfcLL\x08\x08\x03|\x10?r}npLp\x0c\xf08p00'),
                            bytearray(b'\xf0p\xdc\xdc\x88\x88\x08\x08\x08\x08\x08\x08\x08\x08\x00\x00\xf8\x08\x98\x04\x1c\x14\x1c\x14\x18\x10\x10\x18\x10\x10\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03'),
                            bytearray(b'\x00\x04\x00\x0e\x00>(T\x06r*\xd6\x1e\xe2\x1c\xa0\x02\x06\x00\x0e\x01?*~\x08|$\xf8\x00\xfc`\xdc'),
                            bytearray(b'\x00\x00\x00\x03\x00\x00\x01\x07\t\x08\x08\t\x0e\n\x0f\x01\x03\x03\x0c\x0f\x0f\x0f\x19\x1e\x14\x1f\x15\x1e693<'),
                            bytearray(b'|\x84|\x04|\x04\xbcd\xbc\xe4\xfc\x84\xfcT|\xb4\x04\xf8\x04\xf8\x00\xfc`\x9c\xe0\x18\x80xP\xa8\xb0H'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=84),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\xe0pP \x00    @@@@\x00\x00`\x10@0@`@``@` \x00@\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\xa0@\xa0\x00@\x80\x00``\xc0@\x80\x80@\xc0@\xe0P\xf0\xb0\xf0`\xe0@\xa0\x00\x80\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=85),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x03\x04\x07\x04\x07\x08\x0f\x18\x1f'),
                            bytearray(b'\x00/\tv\x00\xfdO \x14C\xd5\x8a\xd5\x8a\xde\xa0\x10?\x89\xff\x02\xff\xd0\xff\x83\xfc\n\xf5\x8au\xa0_'),
                            bytearray(b'\x02\n\x02\n\x03\n\x03\x14\x03\x05A\x7fMJ??\x16\x1d\x12\x1d\x12\x1d$;5:\x0fp:u@`'),
                            bytearray(b'\xfb\xc4\xfd\xc3\xfe\xc0\xfaF\xfeB\xfc\xc4\xfc\xc4\xf8\xe8\xc4;\xc2=\xc0>D\xba@\xbc\xc0<\xc08\xe0\x18'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=85),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1e\x11\x1d\x18\x1d\x11\x0e\x0e\x18\x18\x18\x18\x18\x080\x00\x01\x0e\x08\x17\x12\x0e\x18\x10\x00\x00\x10\x08 0\x000'),
                            bytearray(b'|\x9c\xf0\xf0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x82v\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x05\x00\x0f\x01\x1e\x00=\x06x\x06q\x05 \x00\x00\x02\x07\x00\x0f!?B\x7f\x00\x7f\x01~@\x7f'),
                            bytearray(b'\x00\x00\x00\x90 \xd0`\x90 T\xc8\x90\xa0\x08\xb0L\x80\x80@\xd0 \xf0h\xf8\xa8\xfc\xac|\x14\xfc@\xbc'),
                            bytearray(b'e`/ / .!>!? ?0\x1f\x10 \x1f\x00?\x00?\x01\x1e\x01\x1e\x00\x1f\x10\x0f\x00\x1f'),
                            bytearray(b'D2H\xb4\x00\xfc\x88T\x1e\xe0\t\xf3\x18\xe29\xc7<\xce\xb2N\xfa\x06R\xae\xe3\x1f\xf0\x0f\xe0\x1e\xc0?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=90),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x0b\x0f\x07\x1c\x14\x18\x18\x18\x18\x18\x08\x10\x10\x00\x00\x02\x0c\x06\x08\x04\x18\x18\x00\x10\x08 0\x00\x00\x00\x00'),
                            bytearray(b'\x06x\xfe\x80\xde\xe4\xf9\xc7|h0<>2\x18\x10\xfb\x87\x03\x7fg\x1b\x00?.\x16\x12\x0e\x0c\x1e\x0c\x0c'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=114),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00@\x00\xf8\x00x`H\x84\xca\x14\x08\x80\x96\xa0\x060p@\xf8\x84\xfcT<T\xbe\x86\xfe\x90n\x01\xff'),
                            bytearray(b'\x01\x01\x01\x01\x01\x00\x03\x02\x03\x02\x00\x01\x03\x02\x07\x01\x00\x01\x01\x00\x00\x01\x00\x03\x00\x03\x03\x02\x04\x05\x02\x04'),
                            bytearray(b'\x08\x87B\x10\x02d\x02L\x00\x9f\x00\xff\x02|\x02\xfc\x82\x7f\x13\xefg\x9bO\xb3\x9cc\xfc\x03\x7f\x83\xff\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=98),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0@\xb0\x00\xe0P\xb0\x10\x90\x10\x90\x00\x00\x00\x00\xc0\xe0\xc0\xf0\xf0\xf0\xc0\xf0`\xf0`\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x17(\x00\xfe?\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x05\x07\xd8\xf8\x01\x01\xc0\xff\x03\xff\x00\x00'),
                            bytearray(b'\x00\x01\x03\x1c\x7f\x80\x80\x7f\x1f\x00\xff\x00\x00\x00\x00\x00\x06\x07l|\x80\x80@@\xe0\xff\x00\xff\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=113),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0@\xb0\x00\xe0P\xb0\x10\x90\x10\x90\x00\x00\x00\x00\xc0\xe0\xc0\xf0\xf0\xf0\xc0\xf0`\xf0`\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=405, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x17(\x00\xfe?\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x05\x07\xd8\xf8\x01\x01\xc0\xff\x03\xff\x00\x00'),
                            bytearray(b'\x00\x01\x03\x1c\x7f\x80\x80\x7f\x1f\x00\xff\x00\x00\x00\x00\x00\x06\x07l|\x80\x80@@\xe0\xff\x00\xff\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=389, y=115),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0@\xb0\x00\xe0P\xb0\x10\x90\x10\x90\x00\x00\x00\x00\xc0\xe0\xc0\xf0\xf0\xf0\xc0\xf0`\xf0`\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=151, y=365),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x17(\x00\xfe?\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x05\x07\xd8\xf8\x01\x01\xc0\xff\x03\xff\x00\x00'),
                            bytearray(b'\x00\x01\x03\x1c\x7f\x80\x80\x7f\x1f\x00\xff\x00\x00\x00\x00\x00\x06\x07l|\x80\x80@@\xe0\xff\x00\xff\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=365),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xe0\xfc\x02\x02\xfc\xbcC\xc1\x19\x00\x00\x00\x00\x00\x00\x80\xe0\x02\x02\x7f\x7f/\xaf\x16\xff'),
                            None,
                            bytearray(b'\x01\x13\x046\x0c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcc\xff\t?\x02>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x13!\x1e8\x07\x0f\x00\x01\x00\x00\x00\x00\x00\x00\x00\x12\x13\x06&\x0080?\x0e\x0f\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80pp\x8f\x0e\xf1\xe1\x1e<\x03\x07\x00\x00\x00\x00\x00`p\x8c\x8f\x11\x11\x02\xe2\xc0\xfc8?\x07\x07'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xe0\xfc\x02\x02\xfc\xbcC\xc1\x19\x00\x00\x00\x00\x00\x00\x80\xe0\x02\x02\x7f\x7f/\xaf\x16\xff'),
                            None,
                            bytearray(b'\x01\x13\x046\x0c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcc\xff\t?\x02>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=403, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x13!\x1e8\x07\x0f\x00\x01\x00\x00\x00\x00\x00\x00\x00\x12\x13\x06&\x0080?\x0e\x0f\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80pp\x8f\x0e\xf1\xe1\x1e<\x03\x07\x00\x00\x00\x00\x00`p\x8c\x8f\x11\x11\x02\xe2\xc0\xfc8?\x07\x07'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=113),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\xe0\xe0\x1c<\x03\xf3\x00\xfe\xe0\x1f\x1e\x00\x00\x00\x00\x80\x80\x10\x10B\x82\x04\xf8\xe0\x1f\x1e\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80`p0\xf00\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00@@\xb0\x000\xc0\xe0\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=103),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'0\x08\x8cp \xdf\x8fp9\x80?\x00\x1f>\x01\x014<\xf6\xf6\xdc\xdc\xf0\xf0b\xfc\xe0\xff^a\x01\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=101),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b' \x1c\x04zH6\\\x02<C,#\x1e\x01\x16\x11`|\xfc\xfe\xf4\xf4\xe0\xc0\x02b2\x02\x00\x10\x19\x01'),
                            None,
                            bytearray(b'\x0b\x00\x07\x00\x05\x04\x02\x00\x03\x02\x01\x01\x00\x00\x00\x00\x04\x08\x00\x04\x06\x00\x01\x02\x02\x01\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\xc0\x80@\x00`\x00`\xe0 \xe0\xe0\x00\x00\x00\x00\x80\x80\x00\x00\xc0@@\xc0 \xc0\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=94),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\xe0\xe0\x1c<\x03\xf3\x00\xfe\xe0\x1f\x1e\x00\x00\x00\x00\x80\x80\x10\x10B\x82\x04\xf8\xe0\x1f\x1e\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80`p0\xf00\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00@@\xb0\x000\xc0\xe0\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'0\x08\x8cp \xdf\x8fp9\x80?\x00\x1f>\x01\x014<\xf6\xf6\xdc\xdc\xf0\xf0b\xfc\xe0\xff^a\x01\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=100),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x1c\x02\xfa\x1e\x02\xfc\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00z|\x82|\x18\xe4\xc00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10o\x10\xee\x14(\x03\x14\x03\x14\x01\x05\x00\x00\x00\x00(h\x1f\xfe\xdc\xff\xe8\xff\xe8\xff:?'),
                            bytearray(b'\x00\x00\x00\x0f\x0f\xf0\x07\x00\xff\x00\xff\x0f\xf0\xf0\x80\x80\x00\x00\x00\x00pp\x80\x7f\x00\xff\x0c\xf3\xc00\x00\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=106, y=106),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
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
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL544_WAR_FAN,
    palette_offset=0,
    unknown_num=0
)
