# SPR0209_SHINY_STONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL250_SHINY_STONE
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x06\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x06\x81\x06\xc1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\x07\x7f\x07?'),
                            bytearray(b'\x04\x03\x04\x03\x18\x07\x1b\x049\x04w\x14? \x00\x00\x00\x00\x00\x08\x10\x10\x10\x00\x00#CO\x1f\x7f\x00\x00'),
                            bytearray(b'\xfa^\xda7\x14\xfb\x98f\xd0\xcc\xc0h\xc00\x00\x00$\x03m\x00o\x00\xfa\x00\x1c\xe0\xa8\xd0\xf0\xc0\x00\x00'),
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
    palette_id=SPAL250_SHINY_STONE,
    palette_offset=1,
    unknown_num=8
)