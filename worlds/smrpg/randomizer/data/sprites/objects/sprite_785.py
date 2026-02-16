# SPR0785_SPRITZ_BOMB

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL294_SPRITZ_BOMB
sprite = CompleteSprite(
    animation=AnimationPack(165, length=93, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x08\x06 \x7f(/p\x7f\x00>\x00\x08\x00\x00\x00\x10\x00\x080p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x0000(\x18P@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00008\x10P\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=127),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x08\x06 \x7f(/p\x7f\x00>\x00\x08\x00\x00\x00\x10\x00\x080p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=123),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x0000(\x18P@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00008\x10P\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=125),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x0000(\x18P@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00008\x10P\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x08\x06 \x7f(/p\x7f\x00>\x00\x08\x00\x00\x00\x10\x00\x080p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x0000(\x18P@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00008\x10P\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x08\x06 \x7f(/p\x7f\x00>\x00\x08\x00\x00\x00\x10\x00\x080p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=123),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x08\x06 \x7f(/p\x7f\x00>\x00\x08\x00\x00\x00\x10\x00\x080p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL294_SPRITZ_BOMB,
    palette_offset=0,
    unknown_num=8
)
