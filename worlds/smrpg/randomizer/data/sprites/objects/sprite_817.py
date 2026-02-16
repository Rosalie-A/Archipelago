# SPR0817_GREEN_CANDY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(163, length=121, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x18\x108\x10\x98@\xd7L\x0f\x08\x0f\x10\x0f\x10\x1c\x03\x00\x00\x00\x000\x000\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00@\x00PP\xc8p\xe8\x10(\x00\x00\x00\x00\x00\x00@\x80p\xc08\x00\x18\x008\xe0'),
                            bytearray(b'\x19\x07\x1b\x07\n\x16\n\x06\x06\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x18\x01\x00\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\x18 \xb8\xa0X\x80p\x93\xeb\x00\x03\x1e\x0c\x18\x08\x18\xe0\xb8\xc0\xf8\x00\xf0\x00\xfc\x00\x1f\x00\x00\x00\x00\x00'),
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
    palette_offset=0,
    unknown_num=0
)
