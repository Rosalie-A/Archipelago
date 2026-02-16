# SPR0462_EGGBERT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL252_EGG
sprite = CompleteSprite(
    animation=AnimationPack(132, length=146, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x07\x00\x0f\x00\x1f\x00\x1f ?\x00?@\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x80\x80@\xc0 \xd0 \xc00\xc00\xc80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x7f\x00\x7f\x00\x7f\x00?@?\x00\x1c\x03\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xc80\xc88\x88p\x98h8\xd8x\xb8\xf0p\xe0\xe0\x08\x00\x00\x08\x08\x00\x10\x08 \x18H8\x90p`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=126),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x07\x00\x0f\x00\x1f\x00\x1f ?\x00?@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\xe0\x00\xc0 \xc0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00'),
                            bytearray(b'\x7f\x00\x7f\x00\x7f\x00?@?\x00\x1c\x03\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xd0 \xd0 \x90`\xb0P0\xf0p\xb0\xe0`\x80\x80\x10\x00\x10\x00\x10\x00 \x10\x000P0\xa0`\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=126),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x07\x0f\x00\x1f\x00?\x00?@\x7f\x00\x7f\x80\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80@\xc0 \xe0\x10\xe8\x10\xe0\x18\xe0\x18\xe4\x18\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x7f\x80\x7f\x00?\x00\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xe4\x18\xc4<\xc48\x8ct\x9clx\x98\xf0p\xe0\xe0\x04\x00\x00\x04\x04\x00\x08\x04\x10\x0c`\x18\x90p`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=126),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x07\x00\x0f\x00\x1f\x00\x1f ?\x00?@\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x80\x80@\xc0 \xd0 \xc00\xc00\xc80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x7f\x00\x7f\x00\x7f\x00?@?\x00\x1c\x03\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xc80\xc88\x88p\x98h8\xd8x\xb8\xf0p\xe0\xe0\x08\x00\x00\x08\x08\x00\x10\x08 \x18H8\x90p`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=370),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=126),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x07\x00\x0f\x00\x1f\x00\x1f ?\x00?@\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x80\x80@\xc0 \xd0 \xc00\xc00\xc80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x7f\x00\x7f\x00\x7f\x00?@?\x00\x1c\x03\x11\x0e\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x0c\x03'),
                            bytearray(b'\xc80\xc88\x88p\x98h8\xd8x\xb8\xf0p\xe0\xe0\x08\x00\x00\x08\x08\x00\x10\x08 \x18H8\x90p`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00\x00\x00\x00\x00~~\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=126),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL252_EGG,
    palette_offset=0,
    unknown_num=8
)
