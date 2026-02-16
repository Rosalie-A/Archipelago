# SPR0571_FEAR_EXCLAMATION_POINT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL388_FEAR_EXCLAMATION_POINT
sprite = CompleteSprite(
    animation=AnimationPack(223, length=65, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x00\x1f?\x0f?\x00\x00???\x00\x00\x00\x00\x08\x00\x10\x000\x00?\x00?\x00?\x00'),
                            bytearray(b'\x00\x00\x00\x00\xf00\x18\xf8\xf8\xd8\xf8\x18\x18\xf8\xf8\xf8\x00\x00\x00\x00\xc00 \x18 \x18\xe0\x18\xe0\x18\xe0\x18'),
                            bytearray(b' ?\x08\x08\x07\x0f\x0c\x0b\x07\x07\x01\x01\x00\x00\x00\x00\x1f \x07\x08\x08\x00\x04\x08\x00\x07\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'0\xf000\xf0\xf0p\xb0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\xc00\xc00\x000@0\x00\xe0\x00\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x06\x03\xff\xff{\x03\x03\xff\x03\x03\xff\xff\xff\xff\xffH\x06\x84\x03\x84\x03\xfc\x03\xfc\x03\xfc\x03\xfc\x03\xfc\x03'),
                            None,
                            bytearray(b'\x86\xfeL|FN>~N6~~<<\x18\x18x\x86\x00|0N@\x06H\x06\x00N\x00<\x00\x18'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88\x18(xXxX88\x10\x10\x00\x00\x00\x00@\x08P\x08\x00X X\x008\x00\x10\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'x\x08\x04\xfc\x04\xfc\xfct\x04\x04\x04\x04\xfc\x04\x04\xfcP\x08\x88\x04\x88\x04\x88\x04\xf8\x04\xf8\x04\xf8\x04\xf8\x04'),
                            None,
                            bytearray(b'\xfc\xfc\xfc\xfc\xfc\xfc\x08\xf8\x08\xf8\xf8\x98XHHH\xf8\x04\xf8\x04\xf8\x04\xf0\x08\xf0\x08`\x980H0H'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=108),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=18, mold_id=1),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL388_FEAR_EXCLAMATION_POINT,
    palette_offset=0,
    unknown_num=8
)
