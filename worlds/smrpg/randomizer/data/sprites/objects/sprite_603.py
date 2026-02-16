# SPR0603_FIRE_CRYSTAL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL406_FIRE_CRYSTAL
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\x0f\x00\x07\x00\x07\x00\x03\x00\x03\x00\x01\x00\x01\x00\x00\x0f\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x03\x00\x01\x00\x01'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x00?\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00?\x00\x7f\x00\xff'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xe0\x00\xf0\x00\xf8\xc0\xfc\xf0\xfe\xfc\xff\x00\x80\x00\xc0\x00\xe0\x00\xf0\x00\xf8\x00\xfc\x00\xfe\x00\xff'),
                            bytearray(b'?\xc0\x0f\xf0\x03|\x00\x7f\x00?\x00?\x00\x1f\x10\x0f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00?\x00\x1f\x00\x1f'),
                            bytearray(b'\xfb\xf8\xef\xe0\xbe\x80\xfe\x00\xfc\x00\xfc\x00\xf8\x00\xf0\x00\x07\xff\x1f\xff~\xfe\xfe\xfe\xfc\xfc\xfc\xfc\xf8\xf8\xf8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
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
