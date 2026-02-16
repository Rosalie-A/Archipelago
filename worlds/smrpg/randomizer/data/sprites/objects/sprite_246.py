# SPR0246_BLUE_MUSIC_DRINK

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(166, length=91, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0f\x00\x0f\x00\x0c\x02\x0c\x02\x0f\x00\r\x03\r\x03\x05\x03\x00\x07\x00\x07\x03\x07\x03\x07\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x008\x00\x18\x008\x008\x808@8@8`\x10\xf8\xf0\xb8\xf0\xb8\xf0\xb8\xf08\xf0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
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
    palette_offset=2,
    unknown_num=0
)
