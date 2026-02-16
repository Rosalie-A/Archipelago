# SPR0171_SPARKLES_FROM_STAR_PIECE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(403, length=150, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x81\x00f$~Z<$<$~Zf$\x81\x00\x00\x00$\x00Z\x00$\x00$\x00Z\x00$\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
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
                            bytearray(b'\x00\x00\x00B\x08,\x1c\x048 \x104\x00B\x00\x00\x00\x00\x00\x00\x08\x00\x04\x00 \x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
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
                            bytearray(b'\x00\x00\x00\x00$\x00\x00\x18\x00\x18$\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00$\x00\x00\x18\x00\x18$\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00B\x08,\x1c\x048 \x104\x00B\x00\x00\x00\x00\x00\x00\x08\x00\x04\x00 \x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00$\x00\x00\x18\x00\x18$\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(7, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
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
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=0,
    unknown_num=8
)
