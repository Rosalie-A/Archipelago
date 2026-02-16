# SPR0646_EARTH_CRYSTAL_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL406_FIRE_CRYSTAL
sprite = CompleteSprite(
    animation=AnimationPack(397, length=33, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'),
                            bytearray(b'\x10\x080\x0cp\x0e\xf0\x0f\xf0\x0f\xfc\x0f\xff\x0f\xff\x0f\x00\x08\x00\x0c\x00\x0e\x00\x0f\x00\x0f\x00?\x00\xff\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\xc0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00\xf0'),
                            bytearray(b'\x03\x0c\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x03\x00\x01\x01\x00\x00\x0f\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x03\x00\x01\x00\x01'),
                            bytearray(b'\xff\x0f\xfe\x0e;\xc8\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x00\xff\x01\xff\x07\xff\x0f\xff\x0f\xff\x0f\xff\x0f\xff\x0f\xff'),
                            bytearray(b'\xb0\x80\xf0\x00\xe0\x00\xe0\x00\xc0\x00\xc0\x00\x80\x00\x00\x00p\xf0\xf0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            bytearray(b'\xcc0\xf0\x00p\x00p\x000\x000\x00\x10\x00\x10\x00\x0f\xff\x0f\xff\x0e~\x0e~\x0c<\x0c<\x08\x18\x08\x18'),
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
