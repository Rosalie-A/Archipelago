# SPR0525_BOWYER_S_ARROW

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL367_BOWYER_S_ARROW
sprite = CompleteSprite(
    animation=AnimationPack(210, length=144, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'8$<\x12<\x0b>\t?\x00>\x10<\x100\x00\x1e\x00\x06\x08\x03\x04\x01\x06\x00\x0f\x00\x0e\x00\x0c\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x01\x02\x06,.\x1b\x1f\x14\x1e\x1c\x1c\x0c\x1e\x08\x08\x00\x01\x02\x04\x0c"\x08\x17\x10\x0e\x14\x08\x02\x1e \x08'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00! \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00:\x00'),
                            bytearray(b'\x00\x00\x00@\x00@\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'8$<\x12<\x0b>\t?\x00>\x10<\x100\x00\x1e\x00\x06\x08\x03\x04\x01\x06\x00\x0f\x00\x0e\x00\x0c\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=True, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x01\x02\x06,.\x1b\x1f\x14\x1e\x1c\x1c\x0c\x1e\x08\x08\x00\x01\x02\x04\x0c"\x08\x17\x10\x0e\x14\x08\x02\x1e \x08'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00! \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00:\x00'),
                            bytearray(b'\x00\x00\x00@\x00@\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'8$<\x12<\x0b>\t?\x00>\x10<\x100\x00\x1e\x00\x06\x08\x03\x04\x01\x06\x00\x0f\x00\x0e\x00\x0c\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=True, invert=True, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x01\x02\x06,.\x1b\x1f\x14\x1e\x1c\x1c\x0c\x1e\x08\x08\x00\x01\x02\x04\x0c"\x08\x17\x10\x0e\x14\x08\x02\x1e \x08'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00! \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00:\x00'),
                            bytearray(b'\x00\x00\x00@\x00@\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'8$<\x12<\x0b>\t?\x00>\x10<\x100\x00\x1e\x00\x06\x08\x03\x04\x01\x06\x00\x0f\x00\x0e\x00\x0c\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x01\x02\x06,.\x1b\x1f\x14\x1e\x1c\x1c\x0c\x1e\x08\x08\x00\x01\x02\x04\x0c"\x08\x17\x10\x0e\x14\x08\x02\x1e \x08'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00! \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00:\x00'),
                            bytearray(b'\x00\x00\x00@\x00@\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x02\xe7\x06\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x1a\x05\x00\x07\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x08\x90\xf0f\xfe\x98\xf8\xc0\xe000\x00\x00\x00\x00\x00\x08\x90``\x9e\x00\xf8\x00\xe0\x000\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03\x07\x03\x1f\x03?\x03\x1f\x1c\x0f\x0c\x07\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x03'),
                            bytearray(b'\x80\x00\xc0\x80\xc0\xa0\xc0\x85\x80@\x80@\x80@\x00\x80\x80\x00@\x00`\x00Z\x00@\x80@\x80@\x80\x80\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x02\xe7\x06\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x1a\x05\x00\x07\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x08\x90\xf0f\xfe\x98\xf8\xc0\xe000\x00\x00\x00\x00\x00\x08\x90``\x9e\x00\xf8\x00\xe0\x000\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03\x07\x03\x1f\x03?\x03\x1f\x1c\x0f\x0c\x07\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x00\x03'),
                            bytearray(b'\x80\x00\xc0\x80\xc0\xa0\xc0\x85\x80@\x80@\x80@\x00\x80\x80\x00@\x00`\x00Z\x00@\x80@\x80@\x80\x80\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL367_BOWYER_S_ARROW,
    palette_offset=0,
    unknown_num=8
)
