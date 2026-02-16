# SPR0826_FLOWER_BONUS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL314_FLOWER_BONUS
sprite = CompleteSprite(
    animation=AnimationPack(181, length=138, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x07\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x08\x08\x0e\x0e\x1d\x1d@@\x02\x02\x00\x00\x00\x00\x00\x0008p~\xc0\xff\x80\xff$7\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00`\x00\xf8\x01\xfd\x00$\x00\x00\x00\x00\x00\x00\x000`\x18\xfe\x06\xfc\x03$\x18\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1f\xee_\x94~Y\x00\x1c\x08\x08\x08\x08\x08\x08\x00\x00\x02\x01,\x03x\x07\x00\x1c\x00\x08\x00\x08\x00\x08\x08\x0c'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xcc\x8c\xcc\xdcVl\xe2^\x94x\x00\x00\x00\x00\x00\x80\x0c\x00\x0c\x10\x868\xca8\x10`'),
                            None,
                            bytearray(b'<\xf4\\\xa0\x18\xe0\x90\xe0\x80` \xc0\x00\xe0\x80`$@$`\x80\x80\xc0@ \xe0\x00\xe0\x00\xe0\x00\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x000\x108(\x1e,\x0f\x0c\'%\x00\x00\x00\x00\x00\x001\x00\x01\x00\x012:\x01;\x00"),
                            bytearray(b'\x00\x00i \x7f,\xf73Fb>\x12\xfe\x0c\xff\x06\x00\x00`\x00g\x00\xaf@\xdf \xcf \x05".\x00'),
                            bytearray(b'\x1f\x10\x01\x1e\x13\x0c\x0f\x08\x07\x04\x03\x00\x01\x02\x00\x03\x18\x00\x02\x02\x10\x00\x00\x00\x04\x00\x00\x00\x00\x00\x02\x02'),
                            bytearray(b'\xff\x12\xfe\x1d\xfa\x05\xc2\x19\xc3\x1b\xc2\x19\x03\xda\x03\xfc\x0c\x00\x00\x00\x00\x0075?<<?65\x02\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01``xxxx\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x1e\x1f\x1c|\x04|\x80\xf8\x00\xe0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x07\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1f\xee_\x94~Y\x00\x1c\x08\x08\x08\x08\x08\x08\x00\x00\x02\x01,\x03x\x07\x00\x1c\x00\x08\x00\x08\x00\x08\x08\x0c'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xcc\x8c\xcc\xdcVl\xe2^\x94x\x00\x00\x00\x00\x00\x80\x0c\x00\x0c\x10\x868\xca8\x10`'),
                            None,
                            bytearray(b'<\xf4\\\xa0\x18\xe0\x90\xe0\x80` \xc0\x00\xe0\x80`$@$`\x80\x80\xc0@ \xe0\x00\xe0\x00\xe0\x00\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x000\x108(\x1e,\x0f\x0c\'%\x00\x00\x00\x00\x00\x001\x00\x01\x00\x012:\x01;\x00"),
                            bytearray(b'\x00\x00i \x7f,\xf73Fb>\x12\xfe\x0c\xff\x06\x00\x00`\x00g\x00\xaf@\xdf \xcf \x05".\x00'),
                            bytearray(b'\x1f\x10\x01\x1e\x13\x0c\x0f\x08\x07\x04\x03\x00\x01\x02\x00\x03\x18\x00\x02\x02\x10\x00\x00\x00\x04\x00\x00\x00\x00\x00\x02\x02'),
                            bytearray(b'\xff\x12\xfe\x1d\xfa\x05\xc2\x19\xc3\x1b\xc2\x19\x03\xda\x03\xfc\x0c\x00\x00\x00\x00\x0075?<<?65\x02\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x02\x02\x01\x19\x00|\x06\xf0\x0c(\x00\x00\x00\x00\x00\x00\x00\x16\x18\'|\x03\xf6\x0e$\x1c\x00\x00\x00\x00\x00\x00"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=131),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18\x18 8C}\x01\x1d\x12\x16\x00\x00\x00\x00\x00\x00\x00\x18\x18&>C\x1c#\x04:\x00\x0c\x00\x08\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1f\xee_\x94~Y\x00\x1c\x08\x08\x08\x08\x08\x08\x00\x00\x02\x01,\x03x\x07\x00\x1c\x00\x08\x00\x08\x00\x08\x08\x0c'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xcc\x8c\xcc\xdcVl\xe2^\x94x\x00\x00\x00\x00\x00\x80\x0c\x00\x0c\x10\x868\xca8\x10`'),
                            None,
                            bytearray(b'<\xf4\\\xa0\x18\xe0\x90\xe0\x80` \xc0\x00\xe0\x80`$@$`\x80\x80\xc0@ \xe0\x00\xe0\x00\xe0\x00\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x000\x108(\x1e,\x0f\x0c\'%\x00\x00\x00\x00\x00\x001\x00\x01\x00\x012:\x01;\x00"),
                            bytearray(b'\x00\x00i \x7f,\xf73Fb>\x12\xfe\x0c\xff\x06\x00\x00`\x00g\x00\xaf@\xdf \xcf \x05".\x00'),
                            bytearray(b'\x1f\x10\x01\x1e\x13\x0c\x0f\x08\x07\x04\x03\x00\x01\x02\x00\x03\x18\x00\x02\x02\x10\x00\x00\x00\x04\x00\x00\x00\x00\x00\x02\x02'),
                            bytearray(b'\xff\x12\xfe\x1d\xfa\x05\xc2\x19\xc3\x1b\xc2\x19\x03\xda\x03\xfc\x0c\x00\x00\x00\x00\x0075?<<?65\x02\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x07\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x1f\x10\x01\x1e\x13\x0c\x0f\x08\x07\x04\x03\x00\x01\x02\x00\x03\x18\x00\x02\x02\x10\x00\x00\x00\x04\x00\x00\x00\x00\x00\x02\x02'),
                            bytearray(b'\xff\x12\xfe\x1d\xfa\x05\xc2\x19\xc3\x1b\xc2\x19\x03\xda\x03\xfc\x0c\x00\x00\x00\x00\x0075?<<?65\x02\x01'),
                            None,
                            bytearray(b'\x1f\xee_\x94~Y\x00\x1c\x08\x08\x08\x08\x08\x08\x00\x00\x02\x01,\x03x\x07\x00\x1c\x00\x08\x00\x08\x00\x08\x08\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x07\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'(8\x1c`\x1c <\x00\x18\x10\x00\x00\x03\x03\x00\x00Ph|\x9c<\\<<\x08\x1e\x00\x07\x00\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xcc\x8c\xcc\xdcVl\xe2^\x94x\x00\x00\x00\x00\x00\x80\x0c\x00\x0c\x10\x868\xca8\x10`'),
                            None,
                            bytearray(b'<\xf4\\\xa0\x18\xe0\x90\xe0\x80` \xc0\x00\xe0\x80`$@$`\x80\x80\xc0@ \xe0\x00\xe0\x00\xe0\x00\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x000\x108(\x1e,\x0f\x0c\'%\x00\x00\x00\x00\x00\x001\x00\x01\x00\x012:\x01;\x00"),
                            bytearray(b'\x00\x00i \x7f,\xf73Fb>\x12\xfe\x0c\xff\x06\x00\x00`\x00g\x00\xaf@\xdf \xcf \x05".\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'22\xca\xc2\x9c\x80\xce\xc0\x01\x00\x00\x00\x00\x00\x00\x00\x00>\x08\xfe\x1c\xff\x0e\xef\x01\x01\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=131),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL314_FLOWER_BONUS,
    palette_offset=0,
    unknown_num=8
)
