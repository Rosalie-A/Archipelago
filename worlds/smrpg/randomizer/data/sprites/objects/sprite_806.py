# SPR0806_ROYAL_FLUSH_CARD

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL310_CARD
sprite = CompleteSprite(
    animation=AnimationPack(177, length=96, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0e\x004\x02\xf8\x04\xf0\x08\xe0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0f\x00\x1f\x00>\x01X\x06\xe0\x18\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x06 \x18\x00`\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0 \x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xde\x00\x7f\x00\x1f\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00!\x80\x00`\x00\x18\x00\x06\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'{\x00\xfe\x01\xf8\x06\xe0\x18\x80`\x00\x80\x00\x00\x00\x00\x00\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa1!\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x00\x7f\x00^\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf8\x00|\x00'),
                            bytearray(b'A\x01 \x00\x10\x00\x08\x00\x04\x00\x01\x00\x00\x00\x00\x00>\x00\x1f\x00\x0f\x00\x07\x00\x03\x00\x03\x00\x00\x00\x00\x00'),
                            bytearray(b'\x84\x84\x00\x01\x00\x06\x00\x18\x00`\x00\x80\x00\x00\x00\x00z\x00\xff\x00\xfe\x00\xf8\x00\xe0\x00\x80\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x08\x07\x02\x07\x00\x07\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x07\x00\x0f\x00\x0f\x00'),
                            bytearray(b'\x00\x00\x10\x08`\x18\x80x\x00\xf8\x00\xf8\x00\xf8\xc0\xf8\x00\x00\x18\x00x\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00'),
                            bytearray(b'\x08\x07\x08\x07\x08\x07\x08\x07\x08\x07\x08\x04\x00\x00\x00\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0c\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0\xf8\x10\xf8\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x06\x06\x01\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0c\x01\x07\x02\x01\x11\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x08\xbc(\xf8\x00\xe0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1c\xc4\xfcx\xf8 \xe0'),
                            bytearray(b'\x1f\x00x\x01x\x04\xc0\x10\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x07\x00\x84\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0p\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL310_CARD,
    palette_offset=0,
    unknown_num=8
)
