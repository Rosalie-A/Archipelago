# SPR0567_RED_SYRUP

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(164, length=106, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x06\x03\x0c\x00\x0c\x03\x02\x00\x00\x00\x18\x00\x1e\x01\x00\x03\x00\x07\x03\x0f\x03\x0e\x00\x07\x00\x0c\x00\x1c\x00>'),
                            bytearray(b'\x00\x80\x80\x80\x00 `\xf0`\xe0\x00\x10\x00\x08\xc0$@\xc0@\xe0\xe0\xf0\xf0\x10\xe0\x80\x10\x00\x08\x00\x04\x00'),
                            bytearray(b">\x01?\x009\x06;\x1cd\' \x00\x11\x00\x05\x00\x00>\x00|\x00x\x00`X\x00?\x00\x1f\x00\x07\x00"),
                            bytearray(b'\xf8\x04\xf8\x06\xf8\x06\xfc\n\\\xc2x\x04\xf0\x08\xc0 \x04\x00\x02\x00\x02\x00\x06\x00>\x00\xfc\x00\xf8\x00\xe0\x00'),
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
