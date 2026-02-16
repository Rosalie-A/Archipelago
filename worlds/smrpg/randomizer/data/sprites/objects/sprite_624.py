# SPR0624_SMALL_SEA_FISH

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL448_WHIRLPOOL_WATER
sprite = CompleteSprite(
    animation=AnimationPack(357, length=114, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x07\x07\x0f\x0f\x13\x1b\x1f\x1f\x1f\x1f>9>9\x00\x00\x00\x06\x00\n\x03\x14\x1f\x00\x1f\x008\x00:\x00'),
                            bytearray(b'\x00\x00\x0c\x0c\x1c\x1c\xfe\xfe\xf4\xe4\xd8\xf2\xc8\xf4\x90\x88\x00\x00\x80\x08\x80t\xe0\x0c\xea\x10\xc4\n\xc0\x0c\x80x'),
                            None,
                            bytearray(b'g\x05@\x10Q\x18\x03,\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18 \x0f(\x0f\x18\x0f\x00\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\x08`\x18\xc00\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf0\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x01\x0f\x0f\x13\x1b\x1f\x1f\x1e\x19>9?=88\x00\x00\x00\n\x03\x14\x1f\x00\x18\x00:\x008\x008\x07'),
                            bytearray(b'\x00\x02\x00\x00\xe0\xe1\xd2\xf2\xc6\xe2\x8c\x80=\x07r\x0e\x80\x00\x80p\xe0\x18\xc0\x0c\x90\x0c\xb3L\x04\xfe\x03\xfe'),
                            None,
                            bytearray(b'a\x00CT\x10\x1f!/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f \x0fh\x0f\x11\x0f\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0=\x00\xf8 \xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\x00\xf8 \xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x02\x0f\x0f\r\r\x13\x1b??\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\n\x13\x04?\x00'),
                            bytearray(b'\x00\x00\x00\x00\x10\x10\x1f\x1f\x8e\x8e\x0e\x1f\xe0\xe0\xe4\xe0\x00\x00\x00\x00\x00\x10\x00\x08A\x84\x80u\xe6\x18\xe0\x1c'),
                            None,
                            bytearray(b'??~\x19N9\x16\x14 p\x01\x18\x03\x0c\x00\x03?\x00\x18\x00\n\x00a\x08\x00\x1f\x08\x1f\x00\x0f\x00\x03'),
                            bytearray(b'\x88\x84Dl <0\x08`\x18\xc00\x00\xe0\x00\xc0\x90l\x14\x8c\x00\xdc\x00\xf8\x00\xf8\x00\xf0\x00\xe0\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b"\x00\x00\x06\x06\x1f\x1f\x1f\x1f????\xfbz\x7fw\x00\x00\x01\x04\x10\x0c\x030\'\x10/\x10\xef\x87O/"),
                            bytearray(b'\x00\x00\x80\x80\xd0\xd0\xe0\xc0\xe0\xe0\xe0\xe0\xe0`\xc0\xc0\x00\x00\x80\x00\xc0 \xa0P\xc0\x00\xe0`\xe0\xe0\xc0\xc0'),
                            None,
                            bytearray(b'\x7f?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Oo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b"\x00\x00\x06\x06\x1f\x1f\x1f\x1f??\xbf?yx_\x07\x00\x00\x01\x04\x10\x04\x03,\'\x00\xef\xc0\x8f\xa7\x7f\x7f"),
                            bytearray(b'\x00\x00\x80\x80\xd0\xc0\xe8\xc0\xf0\xe0\x00\x00p0\xe0\xe0\x00\x00\x80\x00\xd00\xa8X\xd0\x10\xc0\xc0pp\xe0\xe0'),
                            None,
                            bytearray(b'\x1f\x1f\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x06\x06?\x1f?\x1f\xff?\xbf?\xfbx]E\x00\x00\x01\x040,#<\xe7\xd0\xef\xd0\xef\x87\xff\xbf'),
                            bytearray(b'\x00\x00\x80\x80\xd0\xd0\xe0\xc0\xf0\xe0\xe8\x80\xe0`\xc0\xc0\x00\x00\x80\x00\xc0 \xa0P\xd0\x10\xe8h\xe0\xe0\xc0\xc0'),
                            None,
                            bytearray(b'\xef/00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL448_WHIRLPOOL_WATER,
    palette_offset=1,
    unknown_num=0
)
