# SPR0781_YELLOW_STAR

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL410_YELLOW_STAR
sprite = CompleteSprite(
    animation=AnimationPack(236, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00a _\x04?\x02=\x00\x1f\x00\x1f\x00\x00\x00\x00``\x1c\x0c\x00\x00 \x00\x10\x00\x10\x10'),
                            bytearray(b'\x00\x00\x00\x80\x00\xc0\x00\xc0\x80\xc0\x00\xf0`\x9c\x02\xff\x00\x00\x80\x80\xc0@\xc0@@@p0\x0c\x04\x01\x01'),
                            bytearray(b'\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x19\x00\x00\x00\x00\x00\x00\x10\x10\x10\x00\x00\x00\x07\x00\x19\x19\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf0\x00x\x008\x00\x0c\x03\x07\x1c\x0c\x18\x08\x18\x08\x80\x08H@0 \x0c\x0c'),
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
    palette_id=SPAL410_YELLOW_STAR,
    palette_offset=0,
    unknown_num=8
)
