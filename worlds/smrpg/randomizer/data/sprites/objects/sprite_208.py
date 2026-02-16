# SPR0208_GLOVE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL644_MARIO_ATTACK_UP_RIGHT
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1e\x01\x7f\x00\x7f\x00\x7f\x00?@?@\x0f0\x00\x00\x1f\x1f@@@@@@@@``??'),
                            bytearray(b'\x00\x00\x00\xf0\xc08\xf0\x0c\xf8\x04\xe8\x14\xe8\x14\xe8\x14\x00\x00\xf0\xf0\xf8\xf8<<\x1c\x1c\x1c\x1c\x1c\x1c<<'),
                            bytearray(b'>A>A=B\x1f \x07\x18\x01\x1e\x1f\x00\x0f\x10aaAAOO??\x1f\x1f\x1f\x1f\x1c\x1c\x1c\x1c'),
                            bytearray(b'p\x8c\xf0\x0c\xe0\x1c\xc08\xc08\x80x\xe0\x10\x80p\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8\xf8\xf8\xf8\xf800pp'),
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
            ]
        )
    ),
    palette_id=SPAL644_MARIO_ATTACK_UP_RIGHT,
    palette_offset=0,
    unknown_num=0
)