# SPR0645_WATER_CRYSTAL_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL406_FIRE_CRYSTAL
sprite = CompleteSprite(
    animation=AnimationPack(440, length=33, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x18\x08<\x0c~\x0e\xff\x0f\xff\x0f\xc33\x00\xf0\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0f\x00\x0f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0\xe000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00'),
                            bytearray(b'\x0c\x0f\x0f\x0f\x07\x07\x07\x07\x03\x03\x03\x03\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x01\xf0\xc4\xf3\xf0\xff\xf0\xff\xf0\xff\xf0\xff\xf0\xff\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00\x0f\x00'),
                            bytearray(b'@0\x00\xf0\x00\xe0\x00\xe0\x00\xc0\x00\xc0\x00\x80\x80\x00\xf0\x00\xf0\x00\xe0\x00\xe0\x00\xc0\x00\xc0\x00\x80\x00\x80\x00'),
                            None,
                            bytearray(b'3\xfc\x0f\xf0\x0ep\x0ep\x0c0\x0c0\x08\x10\x08\x10\x0f\x00\x0f\x00\x0e\x00\x0e\x00\x0c\x00\x0c\x00\x08\x00\x08\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
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
    palette_id=SPAL406_FIRE_CRYSTAL,
    palette_offset=1,
    unknown_num=0
)
