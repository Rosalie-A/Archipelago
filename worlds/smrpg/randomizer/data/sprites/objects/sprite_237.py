# SPR0237_EGG

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL252_EGG
sprite = CompleteSprite(
    animation=AnimationPack(189, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x07\x00\x0f\x00\x1f\x00\x1f ?\x00?@\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x80\x80@\xc0 \xd0 \xc00\xc00\xc80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x7f\x00\x7f\x00\x7f\x00?@?\x00\x1c\x03\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xc80\xc88\x88p\x98h8\xd8x\xb8\xf0p\xe0\xe0\x08\x00\x00\x08\x08\x00\x10\x08 \x18H8\x90p`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL252_EGG,
    palette_offset=0,
    unknown_num=8
)
