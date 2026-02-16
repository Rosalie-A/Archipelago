# SPR0562_YELLOW_REUSABLE_ITEM_SPRITE_WITH_LETTER_I

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL364_YELLOW_REUSABLE_ITEM_SPRITE_WITH_LETTER_I
sprite = CompleteSprite(
    animation=AnimationPack(208, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x04\x0f\x00\x1c\x038\x00xF\\b\xae2\x92\x1d\x04\x00\x00\x00\x07\x00\x08\x07\x06\x01\x02\x01\xc2\x01\xe0\x03'),
                            bytearray(b'\x80@\xd00\x10\xf0\x14\x10trTre#M\x83\x00\x00\x00\x00\xe8\x00\x1c\xe0n\x80N\x80\x1f\xc0?\xc0'),
                            bytearray(b'N\x89o\x07\x1f`\x078\x10\x1f\x0f\x0f\x03\x00\x00\x00\xf0\x07p\x0fx\x07?\x00\x1f\x00\x0f\x00\x00\x03\x00\x00'),
                            bytearray(b'{\x87\xf2\xee\xe6\x1e\x8c|8\xf8\xf0\xc0\xc0\x00\x00\x00\x1f\xe0\x0e\xf0\x1e\xe0\xfc\x00\xf8\x00\xc00\x00\xc0\x00\x00'),
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
    palette_id=SPAL364_YELLOW_REUSABLE_ITEM_SPRITE_WITH_LETTER_I,
    palette_offset=0,
    unknown_num=8
)
