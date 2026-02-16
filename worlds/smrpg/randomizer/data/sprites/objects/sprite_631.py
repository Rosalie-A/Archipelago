# SPR0631_HINOPIO_S_MODEL_AIRPLANE_BLUE_GREY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL710_HINOPIO_S_MODEL_AIRPLANE_BLUE_GREY
sprite = CompleteSprite(
    animation=AnimationPack(411, length=61, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0c\x0c\t\x0e\x07\t\x1f\x073\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b' \x00@ B \x84B\x88D\xf0\xec\xe0\xdc\xc8\xf8 \x00`\x00b\x00\xc6\x00\xcc\x00\x1c\x00<\x00\x00\x00'),
                            bytearray(b'A?\x80\x7f\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x01\x07\x03\x07\x07'),
                            bytearray(b'\x82\xfe\xcc\xff\xc0\xd8@D\xc0\xc0\xe0\xe0\xf0\xf0\xc0\xc0\x00\x00\xf0\xc0\xd8\xc0D@\xc0\xc0\xe0\xe0\xf0\xf0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=115),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x03\x04\x0e\x01\x11\x00;\x18\x16\x11u2\x00\x00\x03\x00\x03\x04\x0f\x00\x11\x0e8\x07\x11.s\x0c'),
                            bytearray(b'\x80\x80\x00\x80\x02\xc0\xc7\t\xe4\x1b\x99g\xd8/A\xbf\x00\x80\x00\x00B\x00\xce\x01\xfe\x00\xfe\x01V\xa8\xf6\x01'),
                            bytearray(b'i&p\x0f\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x03\x03g\x18\x7f\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x02\x03\x03'),
                            bytearray(b'\xc08\x00\xc0``  ppxx\xfc\xfc\xc0\xc0\xf8\x00\xc0\x00``  pp\xf8x\xfc\xfc\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=115),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x04\x00\x00\x00\x08\x006\x19-\x12\x13,\x00\x00\x00\x00\x07\x07\x0f\x0f\x1f\x1f7/*6\x1f/'),
                            bytearray(b'\x00\x00$\x04\xf0\x08p\x08$\xdc\xe8\x1e<\x02\xdc$\x0c\x0c<8\xf8\xf8\xf8\xfc\xfc\xfc\xfe\xf6\xfe\xfe\xfc\xfa'),
                            bytearray(b'2\r\x1f\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01?\x0f\x1f\x1f\x07\x07\x00\x00\x00\x00\x01\x00\x03\x00\x03\x01'),
                            bytearray(b'@\xb8\x00\xf0`\xe0  0088\xfc\xfc\xd0\xd0\xf8\xfc\xf0\xf0\xe0\xe0  00\xf88\xfc\xfc\xd0\xd0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=115),
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
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL710_HINOPIO_S_MODEL_AIRPLANE_BLUE_GREY,
    palette_offset=0,
    unknown_num=0
)
