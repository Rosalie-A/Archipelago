# SPR0809_BLUE_MUSIC_NOTE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL312_BLUE_MUSIC_NOTE
sprite = CompleteSprite(
    animation=AnimationPack(179, length=64, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x00\x03\x03\x00\x00\x00\x03\x03\x00\x03\x03\x00\x00\x03\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x80\xc0\x00\x00\x00\xf0\xf0\x00\xf8x\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x00\x00\x03\x1f\x1f\x00\x00\x7f\x00\x00\x7f~~\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x7f\x00\x7f\x00~\x00\x00<'),
                            bytearray(b'<\x00\x00\x1c\x18\x18\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x000\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x00\x03\x03\x00\x00\x00\x03\x03\x00\x03\x03\x00\x00\x03\x03\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x03\x00\x00\x03\x1f\x1f\x00\x00\x7f\x00\x00\x7f~~\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x7f\x00\x7f\x00~\x00\x00<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x0f\x0f\x00\x0c\x08\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00<<\x00\xfc\xf4\x00\x00\x00\x0c\x0c\x004\xc4\x00\x00\x0c<\x00\xfc\x00\xf4\x00\xc4\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0b\x00\x00\x0c\x08\x08\x00\x008\x00\x00xxx\x00\x00\x00\x00\x00\x00\x00\x00\x08\x008\x00x\x00x\x00\x000'),
                            bytearray(b'\x04\x00\x00\x04\x04\x04\x00\x00<\x00\x00<\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00<\x00<\x00\x18\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
                        AnimationSequenceFrame(duration=16, mold_id=2),
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
    palette_id=SPAL312_BLUE_MUSIC_NOTE,
    palette_offset=0,
    unknown_num=8
)
