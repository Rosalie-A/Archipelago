# SPR0521_LIGHT_BLUE_STARS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL337_LIGHT_BLUE_STARS
sprite = CompleteSprite(
    animation=AnimationPack(192, length=42, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08>>\x1c\x1c\x1c\x1c""\x00\x00\x00\x00\x00\x00\x08\x08>>\x1c\x1c\x1c\x1c""\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x0f\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x0f\x0f\x07\x07'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xf8\xf8\xf0\xf0\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xf8\xf8\xf0\xf0'),
                            bytearray(b'\x03\x03\x03\x03\x07\x07\x07\x07\x0c\x0c\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x07\x07\x07\x07\x0c\x0c\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xe0\xe0\xe0\xf0\xf0pp\x18\x18\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0\xe0\xf0\xf0pp\x18\x18\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x03\x03\x7f\x7f??\x1f\x1f\x00\x00\x00\x00\x01\x01\x01\x01\x03\x03\x7f\x7f??\x1f\x1f'),
                            bytearray(b'\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xff\xff\xfe\xfe\xfc\xfc\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xff\xff\xfe\xfe\xfc\xfc'),
                            bytearray(b'\x0f\x0f\x0f\x0f\x0f\x0f\x1f\x1f\x1f\x1f<<00\x00\x00\x0f\x0f\x0f\x0f\x0f\x0f\x1f\x1f\x1f\x1f<<00\x00\x00'),
                            bytearray(b'\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc||\x1e\x1e\x06\x06\x00\x00\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc||\x1e\x1e\x06\x06\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
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
    palette_id=SPAL337_LIGHT_BLUE_STARS,
    palette_offset=0,
    unknown_num=8
)
