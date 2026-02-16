# SPR0445_HELIO

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL302_HELIO
sprite = CompleteSprite(
    animation=AnimationPack(169, length=85, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x04\x0e\n\x04\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x1f\x00\x0e\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa0\xc0\xb0\xc0\xb8\xc0x\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0e\x1f\x11\x0e\x1f\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x03\x07\x0f\x1c\x1c0000# \x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x00\x0f\x00\x1f\x00'),
                            bytearray(b'\x00\x00\x00\x00@\x800\xc08\xc0\x9c\xe0\xdc\xe0fx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00'),
                            bytearray(b'-"\x0c\x03\x10\x0f\x16\x0f\x0f\x1f\x07\x0f\x03\x03\x00\x00\x1f\x00?\x00?\x00?\x00\x1f\x00\x0f\x00\x03\x00\x00\x00'),
                            bytearray(b'\x16\x18\x9a\x1c\xfa\x1cp\x840\xc0\xd0\xe0\xc0\xc0\x00\x00\xe0\x00\xe0\x00\xe0\x00\xf8\x00\xf8\x00\xf0\x00\xc0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0c\x18\x06\x08\x0e0>\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x10\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00$(BL\x1c\x0e"\x12^r\x1c\x1c\x00\x00\x00\x00\x10\x000\x00p\x00|\x00<\x008\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x10\x148(,(\x10\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00<\x00\x18\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL302_HELIO,
    palette_offset=0,
    unknown_num=8
)
