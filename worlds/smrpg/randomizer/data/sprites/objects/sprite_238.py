# SPR0238_RED_JUICE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(163, length=121, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x00\x04\x07\x02\x00\x04\x00\x0c\x00\x0f\x10\x1f\x01\x00\x0f\x00\x0f\x07\x00\x00\x03\x00\x04\x00\x08\x00\x0f\x00\x16'),
                            bytearray(b'\xf0\x00\xf0\x00 \xe0@\xc0\x00 \x00\x10\xe0\x08\xf8\x10\x00\xf0\x00\xf0\xe0\x00\xc0\x80 \x00\x10\x00\x08\xe0H '),
                            bytearray(b'\x1e\x00\x1f\x00\x1f\x00\x1a\x06\x19\x06\x1a\x06\x1a\x06\n\x06\x03\x14\x00\x07\x00\x07\x01\x00\x01\x03\x01\x00\x01\x00\x01\x00'),
                            bytearray(b'\xf8\x90\xf0\x08\xe0\x18\x80x\xc0\xf8\x80x\x80x\x80pH \x98`\x18\xe0\xf8\x008\xc0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL384_YELLOW_JUICE,
    palette_offset=1,
    unknown_num=0
)
