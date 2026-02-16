# SPR0784_BONE_THROW

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL317_BONE_THROW
sprite = CompleteSprite(
    animation=AnimationPack(184, length=74, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x07\x06zTT:\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x04\x00a\x00\x80\x01'),
                            None,
                            bytearray(b'\xdf9\x9a\xebt\x00Bt\xc6Lx\x08\x00\x00\x00\x00\x03\x00\x07\x00\x8c\x02\x8c\x02\xbc\x02x\x84\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x00'),
                            bytearray(b'\x00\x14t.\xb8\xca\x05\xf2\xe2gO1\xdaI\x13\x8e\x1c\x00\x02@\x86\x01\x8e\x01\x99\x00\x80\x00?\x00\x8eq'),
                            bytearray(b'\r\x02\x18\x00/\x15f\xa8\x88\x08\xf0 \xa0@\x80\x80\t\x00\x04\x13G\x88\x0c\x12H0\xb0@\xc0 \x80\x00'),
                            bytearray(b'\x18 \xe0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\xc4\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18<\x18<\xca\xbeB<F[\xd7Noj\x10\x00<\x00<\x00\xbe\x00\xbe\x00\xbd\x00\xb9\x00n\x11\x000'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00x\x14\xfc\x86\xfc\xc6\x8a:$`(hd`\x00\x00\x1c`\x02\x00\x02\x00\xc6\x00\\\x82h\x14`\x1c'),
                            None,
                            bytearray(b'D`$ l(` $ $ ((\x0c,`\x1c \\(T \\ \x1c \x1c(\x14,\x10'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x04 j\x16:g\\\x04\x1b\x19\x14\x0c\x02\x00\x00\x000\x0cA\x00A\x00"A\'\x00\x1c\x02\x00\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x90'),
                            bytearray(b'\x00\x01\x00\x01\x81\x7f\x10\x00\x0f\x0f\xe3\xec\x00\x00\x00\x00\x01\x00\x00\x00\xff\x00\x00\xff\x0f\xf0\xef\x10\x00\x00\x00\x00'),
                            bytearray(b'H\xa0\xc8(\x9c\x1084\xf6\xe8\x10\xf4H\x00\x00\x00\x10\x08\x18\x00\xe8\x04$\xc0\xe4\x02\xec\x00\x00x\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL317_BONE_THROW,
    palette_offset=0,
    unknown_num=8
)
