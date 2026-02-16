# SPR0930_CONDUCTING_TOADOFSKY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL713_CONDUCTING_TOADOFSKY
sprite = CompleteSprite(
    animation=AnimationPack(415, length=98, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x07\x04\x02\x04\x05\x01\x00\x00\x00\x00\x00\x00\x01\x01\x04\x04\x06\x02\x07\x07\x06\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\x10\xb0\xe0\x90\xd0\xc0\x00\x00\x00\x00\x00\x00\xe0\xe0\x10\x10\xd0@\xf0p0\x10'),
                            bytearray(b'\x02\x07\x04\x05\x06\x00\x02\x05\x01\x07\x04\x02\x04\r\x04\r\x06\x05\x0e\x01\x0f\x00\x01\x01\x01\x01\x05\x03\r\x0b\r\t'),
                            bytearray(b'\xa0\xf0\x10\xd00\x00\x80p\xc0\xf0\xb0\x00\x18X\x10X\xb0P8@\xf8\x00\xc0\xc0\xc0\xc0p\xe0X`XH'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x00\x06\x04\x82\x04\x03\x05&\x03\x00\x00\x00\x00\x00\x00\x03\x03\x05\x01\x87\x87FF\x06\x05'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00 \x00p\x90\xe0\x90\xe0\xd0\xb0\xe0\x00\x00\x00\x00\x00\x00\xe0\xe0\xd0@\xd0P00\xb0P'),
                            bytearray(b'\x04\x1d\x06\x1c\x07\x02\x03\x02\x03\x07\x00\x06\x04\r\x04\r\x06\x01\x07\x00\x07\x03\x01\x02\x05\x07\x07\x07\r\x0b\r\t'),
                            bytearray(b'\x10\xdc\xf0\xfcp \xe0 \xf0\xe0\xa0\x00\x18X\x10X0@0\x00\xf0\xe0\xc0\xa0\xd0\xe0`\xf0X`XH'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x00\x00\x03\x00\x07\x04\x02\x07\x00\x07\x04\x03\x00\x00\x01\x01\x01\x01\x02\x02\x06\x02\x06\x04\x04\x04\x04\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00 \x00P\x90\xa0\xf0\x00p\x90\xe0\x00\x00\x00\x00\x00\x00\xe0\xe0\xf0`\xb0\x10\x90\x10\x90\x10'),
                            bytearray(b'\x07\x00\x07\x01\x07\x06\x02\x03\x03\x07\x04\x02\x04\r\x04\r\x07\x00\x0f\x00\x0f\x03\x01\x03\x05\x07\x07\x03\r\x0b\r\t'),
                            bytearray(b'p\x00P`\xf00\xa0`\xe0\xf0\xa0\x10\x18X\x10X\xf0\x00\xf8 x`\xc0\xe0\xd0\xf0p\xf0X`XH'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00\x06\x04\x02\x04\x03\x05\x06\x03\x04\x05\x07\x05\x06\x03\x03\x03\x05\x01\x07\x07\x06\x06\x06\x05\x0e\x01\x0f\x00\x06\x00'),
                            bytearray(b' \x00p\x90\xe0\x90\xe0\xd0\xb0\xe0\x10\xd0\xf0\xf0\xf0\xe0\xe0\xe0\xd0@\xd0P00\xb0P8@8\x00\xf0 '),
                            bytearray(b'\x02\x07\x03\x07\x00\x06\x04\r\x04\r\x00\x00\x00\x00\x00\x00\x06\x04\x05\x07\x07\x07\r\x0b\r\t\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xf0\xf0\xe0\xa0\x00\x18X\x10X\x00\x00\x00\x00\x00\x00\x90\x10\xd0\xe0`\xf0X`XH\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x00\t\x00\x08\x01\r\x19\x07\x1b\x1f\x07\x0b\x0b\x0e\t\x07\x07\x0e\x0e\x0f\x0e\x1f\x16\x1c\x1c\x1d\x1a\x1d\x02\x1e\x00'),
                            bytearray(b'@@\x80 \x80 \xa0\x80\xc0\xc0\xe0\xe0\x80\xa0\xe0\xe0\xc0\x80\xe0\xe0\xe0\xe0` `\x800\x80p \xc0 '),
                            bytearray(b'\x02\x07\x03\x07\x00\x06\x04\r\x04\r\x00\x00\x00\x00\x00\x00\x06\x04\x05\x07\x07\x07\r\x0b\r\t\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xf0\xf0\xe0\xa0\x00\x18X\x10X\x00\x00\x00\x00\x00\x00\x90\x10\xd0\xe0`\xf0X`XH\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x03\x00\x02\x02\x00\x01\x01\x03\x03\x01\x03\x00\x03\x01\x00\x03\x02\x03\x03\x03\x02\x03\x00\x06\x00\x07\x02\x02\x02'),
                            bytearray(b'\x10\x00H\x00(@\xe8\xc4\xf8\xe4\xfc\xf0\xa8\xe8\xe8\xf8\xf0\xf0\xb8\xb8\xf8\xb8|<\x1c\x9c\\\xac\x9c \xfc\x10'),
                            bytearray(b'\x02\x07\x03\x07\x00\x06\x04\r\x04\r\x00\x00\x00\x00\x00\x00\x06\x04\x05\x07\x07\x07\r\x0b\r\t\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xf0\xf0\xe0\xa0\x00\x18X\x10X\x00\x00\x00\x00\x00\x00\x90\x10\xd0\xe0`\xf0X`XH\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=1),
                        AnimationSequenceFrame(duration=12, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=32, mold_id=3),
                        AnimationSequenceFrame(duration=32, mold_id=4),
                        AnimationSequenceFrame(duration=32, mold_id=3),
                        AnimationSequenceFrame(duration=32, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL713_CONDUCTING_TOADOFSKY,
    palette_offset=0,
    unknown_num=8
)
