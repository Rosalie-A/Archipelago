# SPR0214_RED_BALL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL119_ORB_USER
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x07\x00\x0f\t\x16\x18\'\x1a%\x18\'\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x1f\x07?\x05=\x07?"),
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\xe0\x10\xc08\x10\xec\xf0\x0c\xe0\x1c\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\xf8\x00\xfc\x00\xfc\x00\xfc'),
                            bytearray(b'\x0f0\x03<\x00?\x07\x18\x03\x0c\x07\x07\x00\x00\x00\x00\x00?\x00?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00'),
                            bytearray(b'\xc0<\x84|4\xcc\xe8\x18\x90p\xe0\xe0\x00\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xf0\x00\xe0\x00\x00\x00\x00'),
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
    palette_id=SPAL119_ORB_USER,
    palette_offset=0,
    unknown_num=8
)