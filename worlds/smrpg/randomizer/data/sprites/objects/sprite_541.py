# SPR0541_SNOWY_EYES

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL374_SNOWY_EYES
sprite = CompleteSprite(
    animation=AnimationPack(215, length=91, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf8~~\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00 \xe8\x18>@\x12\x1e\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf8~~\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00 \xe8\x18>@\x12\x1e\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c\x04\x06>&\x1ef$~$~<~<~<\x04\x00\x1e8\x1e\x18<\x18$\x00<\x00<\x00<\x00'),
                            None,
                            bytearray(b'>>>>\x1c\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00>\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1c\x04\x06>&\x1ef$~$~<~<~<\x04\x00\x1e8\x1e\x18<\x18$\x00<\x00<\x00<\x00'),
                            None,
                            bytearray(b'>>>>\x1c\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00>\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00'),
                            None,
                            bytearray(b'\xfc\xfc\xfc\xfc||\xf8\xf8\xb0\xf0\xe0\xe0\x80\x80\x00\x00\xfc\x00\xfc\x00|\x80\xf8\x00\xf0\x00\xe0\x00\x80\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x13\x00#\x00#\x00#@\x07\x00G\x00\xc6\x00\xa6\x0f\x1f?\x1f?\x1f\x1f??\x7f?\x7f\xbf\xff\xdf\xff'),
                            bytearray(b'\x0c\x98\x1c\xa9\x11\xa9\x119\x19q)[#S3c\xe5\xfe\xd6\xec\xdb\xe4\xcb\xf4\x8f\xf8\xb5\xc0\xb7\xc8\x9f\xf0'),
                            bytearray(b'\x00\xac\x00L\x00-\x00\x19\x00\x05\x00\x00\x00\x00\x00\x00\xdf\xff\x7f\x7f>?\x1e\x1f\x06\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'S\xa7c\x87b\xd6\xa6o\xc6\x8e\xdf\x9f?\x1f\x00\x00{\x90{\xa0*\xe1\xd7\x00v\xc1\x7f\xc0? \x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00` 0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\xf0@\xf8 \xfc'),
                            None,
                            bytearray(b'\x10\x08\x08\x00\x00\x00\x02\x06\x8c\x0c|||\xfc\xfc\xfc\x18\xf6\x08\xfe\x02\xfc\x02\xf8\xbc\xc0\xfc\x00|\x00\xfc\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00>\x00\xe0\x00\x80`\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00>?\xe0\xff\x80\x9f\xc0?'),
                            bytearray(b'\x03\x00\x01\x02\x00\x02\x00\x04\x00\x04\x00\t\x00\t\x00\x11\x03\x03\x01\x03\x01\x03\x07\x03\x03\x07\x0f\x07\x07\x0f\x1f\x0f'),
                            bytearray(b'\xc0\xc0\xc0`\xc0\x108\x80\t\xc6\x02\xdc\n\xd4\x08\xdc\xc0?\xc0\x9f\xc0\xef\xf8\xff\xff\xf9\xe6\xfb\xef\xf2\xe5\xfa'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=46, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=2),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL374_SNOWY_EYES,
    palette_offset=0,
    unknown_num=8
)
