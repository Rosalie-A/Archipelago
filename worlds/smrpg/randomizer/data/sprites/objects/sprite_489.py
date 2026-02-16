# SPR0489_EXOR

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL290_EXOR
sprite = CompleteSprite(
    animation=AnimationPack(152, length=270, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=372),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=380),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=374),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            None,
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0@\xd0\xa0h\xb0h\x00\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x10\x00\x10\x00'),
                            None,
                            bytearray(b'\xb0hP\xd8\xf00\xe0\xe0 \x80\x00\x00\x00\x00\x00\x00\x10\x000\x00\xf0\x00\xf0\x00`\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=371),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x03\x05\x04\x0f\x0e\x1d\x0b\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x0b\x1c\x04\x0f\x07\x0b\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=371),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00hH\xb4\xb4\xfcHxH\xb4\xb4hH\x00\x00\x00\x00x\x00\xcc\x00\x84\x00\x84\x00\xcc\x00x\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00hH\xb4\xb4\xfcHxH\xb4\xb4hH\x00\x00\x00\x00x\x00\xcc\x00\x84\x00\x84\x00\xcc\x00x\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=377),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00w\x9f\x1f8\x07\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a\x00\x00\x00\x03\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\xa0\x00\xbeb88\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00`\x00\x9e\x008\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00w\x9f\x1f8\x07\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a\x00\x00\x00\x03\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\xa0\x00\xbeb88\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00`\x00\x9e\x008\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=377),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'0\x000\x00\x080 00\x10\x10\x10\x00\x00\x10\x00\x08\x00\x08\x00\x08\x00\x00\x00 \x00\x00\x00\x10\x00\x10\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x10\x00\x00\x00\x00\x10\x00\x10(08 8\x00\x10\x00\x10\x00\x10\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10\x00\x10\x00\x00\x00\x00\x10\x00\x10(08 8\x00\x10\x00\x10\x00\x10\x00\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                            bytearray(b'0\x000\x00\x080 00\x10\x10\x10\x00\x00\x10\x00\x08\x00\x08\x00\x08\x00\x00\x00 \x00\x00\x00\x10\x00\x10\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=117),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x108(|T8(\x10\x10\x00\x00\x00\x00\x00\x00\x10\x008\x00l\x008\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x108(|T8(\x10\x10\x00\x00\x00\x00\x00\x00\x10\x008\x00l\x008\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=377),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x04\x06\x08\x03\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x0f\x00\x1d\x00\x1c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80@@ \xb0\x10\xa0\x08\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xe8\x00t\x18|'),
                            bytearray(b'\x03\x08\x00\x14\x01\x02\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1f\x00\x0f\x01\x07\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xa0\x08@8\x00\xb8\x00\xf0\x00 \x00\x00\x00\x00\x00\x00\x18|\x18\xfcp\xf8\xe0\xf0\x00\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x04\x06\x08\x03\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x0f\x00\x1d\x00\x1c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80@@ \xb0\x10\xa0\x08\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xe8\x00t\x18|'),
                            bytearray(b'\x03\x08\x00\x14\x01\x02\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1f\x00\x0f\x01\x07\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xa0\x08@8\x00\xb8\x00\xf0\x00 \x00\x00\x00\x00\x00\x00\x18|\x18\xfcp\xf8\xe0\xf0\x00\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL290_EXOR,
    palette_offset=0,
    unknown_num=8
)
