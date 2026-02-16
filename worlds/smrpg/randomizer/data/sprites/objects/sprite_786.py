# SPR0786_WIND_CRYSTAL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL406_FIRE_CRYSTAL
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x0f\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\xc0\xf0\x00\xe0\x00\xe0\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xf0\x00\xf0\x00\xe0\x00\xe0\x00\xc0\x00\xc0\x00\x80\x00\x80\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00<\x03p\x0f\xc0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0\xf8\xf8<<\x0e\x0e\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00'),
                            bytearray(b'\xc0\xff\xf0\xff|\x7f\x7f\x7f????\x1f\x1f\x0f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x04\x03\x10\x0f@>\x00\xfe\x00\xfc\x00\xfc\x00\xf8\x08\xf0\xff\x00\xff\x00\xfe\x00\xfe\x00\xfc\x00\xfc\x00\xf8\x00\xf8\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL406_FIRE_CRYSTAL,
    palette_offset=0,
    unknown_num=8
)
