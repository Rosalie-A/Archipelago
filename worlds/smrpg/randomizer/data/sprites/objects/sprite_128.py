# SPR0128_BLOCK_SHADOW

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL462_BLOCK_SHADOW
sprite = CompleteSprite(
    animation=AnimationPack(344, length=88, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f'),
                            bytearray(b'\x00\x00\x01\x01\x07\x07\x1f\x1f\x7f\x7f\xff\xff\xff\xff\xff\xff\x00\x00\x01\x01\x07\x07\x1f\x1f\x7f\x7f\xff\xff\xff\xff\xff\xff'),
                            bytearray(b'\x00\x00\x80\x80\xe0\xe0\xf8\xf8\xfe\xfe\xff\xff\xff\xff\xff\xff\x00\x00\x80\x80\xe0\xe0\xf8\xf8\xfe\xfe\xff\xff\xff\xff\xff\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xf8\xf8'),
                            bytearray(b'\x1f\x1f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\x7f\x7f\x1f\x1f\x07\x07\x01\x01\x00\x00\xff\xff\xff\xff\xff\xff\x7f\x7f\x1f\x1f\x07\x07\x01\x01\x00\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xfe\xfe\xf8\xf8\xe0\xe0\x80\x80\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xf8\xf8\xe0\xe0\x80\x80\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf8\xf8\xfe\xfe\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf8\xf8\xfe\xfe\xff\xff'),
                            None,
                            None,
                            bytearray(b'\xff\xff\x7f\x7f??\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x7f\x7f??\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xff\xfe\xfe\xfc\xfc\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xfe\xfe\xfc\xfc\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=True, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f??\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f??'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf8\xf8\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf8\xf8\xfc\xfc'),
                            None,
                            None,
                            bytearray(b'??\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00??\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL462_BLOCK_SHADOW,
    palette_offset=0,
    unknown_num=0
)
