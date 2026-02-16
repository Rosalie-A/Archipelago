# SPR0234_YELLOW_BOMB

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(164, length=106, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x00\x1f\x00?\x00\x7f\x00\x7f\x00\xff\x00\xfc\x03y\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x03\x0c\x02\r'),
                            bytearray(b'\xe0\x00\xe8\x18\xc88\x9ax4\xf2\x18\x17\x10\x9f\x90\x7f\x00\x00\x00\x00\x04\x00\x06\x00\x0e\x00\x1f\xe0\x9f`\x7f\xa0'),
                            bytearray(b'\x80\xf3pr\x80\x0fp\x0f\x00\x7f\x00?\x00\x1f\x00\x07\x03\x0c\x82\r\xff\x0c\x7f\x0f\x7f\x00?\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x10\xff\x10\x7f\x10\xff\xf0\xfe\x00\xfe\x00\xfc\x00\xf8\x00\xe0\xff`\x7f\xa0\xff \xfe\x00\xfe\x00\xfc\x00\xf8\x00\xe0\x00'),
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
    palette_offset=3,
    unknown_num=0
)
