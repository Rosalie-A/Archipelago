
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(188, length=166, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x07\x00\x03\x04\x19\x0f\x1f\x0f\x1f\x1f?\x07\x00\x00\x00\x00\x00\x00\x00\x04\t\x06\x0f\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x1f\x0e_f\x9f\xe2\xcf\xf6\xff\xff\xff\xff\xff\x1f\x7f\x98\x0e\x00F \x82`\xc60\xff\x00\xff\x00\x1f\x00\x18\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=95),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"p\x00\x1f#\x0f3\'???\x7f\x7f}\x7fx\x7f\x00\x00\x03 \x030\'\x18?\x00\x7f\x00}\x02x\x07"),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\xe0\x80\xf0\x92\xf8\x9d\xf8\xc7\xf0\xef\x00\x00\x00\x00\x80\x00\x80\x00\x90\x02\x98\x05\xc0\x07\xe0\x0f'),
                            bytearray(b'\xfb~\xfb\x7f\xfb}\xf9?\xf9\x1e\xfc\x8f\xfc\x8f\xf8\x19z\x04{\x04y\x049\x06\x18\x06\x8c\x03\x8c\x03\x18\x01'),
                            bytearray(b'1\xfe\x82\xf8\xfa\xa0\x10\x00\x00\x00\x00\x00@\x80\x00\x800\xce\x80x\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=95),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x1f\'\x0f?\x7f?\xbfx;<y\x1f\xff\x1f\x1fs\x07 \x0f0?\x008@8\x04\x19\x06\x1f\x00\x13`"),
                            bytearray(b'<\xf3\xf8\xe7\xf9\xee\xfc\xec\xfe\xcd\xff\xcf\xff\xcf\xff\xdf0\xc3\xe0\x07\xe8\x06\xec\x00\xcc\x01\xcf\x00\xcf\x00\xdf\x00'),
                            bytearray(b'[\x7f\x7f~\x7fx\xff\x01\xf8\x07`\x1f\x03<\x03|[$~\x00x\x00\x01\x00\x00\x07\x00\x1f\x00<\x00|'),
                            bytearray(b'\xff\x9f\xfe>\xfc|\xf8\xfcf\xf8\x07\xf80\xc0\xb8@\x9f\x00>\x00|\x00\xf8\x04`\x98\x00\xf8\x00\xc0\x00@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xe0@\x0e\x04s\x00\xf3\x02\xf9\x00\xf9\x02\xf8\x08p`\x80\x00\x0e\x00s\x00\xf3\x00\xf9\x00\xf9\x00\xf8\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=111),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x07\x00\x03\x04\x19\x0f\x1f\x0f\x1f\x1f?\x07\x00\x00\x00\x00\x00\x00\x00\x04\t\x06\x0f\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x1f\x0e_f\x9f\xe2\xcf\xf6\xff\xff\xff\xff\xff\x1f\x7f\x98\x0e\x00F \x82`\xc60\xff\x00\xff\x00\x1f\x00\x18\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"p\x00\x1f#\x0f3\'???\x7f\x7f}\x7fx\x7f\x00\x00\x03 \x030\'\x18?\x00\x7f\x00}\x02x\x07"),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\xe0\x80\xf0\x92\xf8\x9d\xf8\xc7\xf0\xef\x00\x00\x00\x00\x80\x00\x80\x00\x90\x02\x98\x05\xc0\x07\xe0\x0f'),
                            bytearray(b'\xfb~\xfb\x7f\xfb}\xf9?\xf9\x1e\xfc\x8f\xfc\x8f\xf8\x19z\x04{\x04y\x049\x06\x18\x06\x8c\x03\x8c\x03\x18\x01'),
                            bytearray(b'1\xfe\x82\xf8\xfa\xa0\x10\x00\x00\x00\x00\x00@\x80\x00\x800\xce\x80x\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x1f\'\x0f?\x7f?\xbfx;<y\x1f\xff\x1f\x1fs\x07 \x0f0?\x008@8\x04\x19\x06\x1f\x00\x13`"),
                            bytearray(b'<\xf3\xf8\xe7\xf9\xee\xfc\xec\xfe\xcd\xff\xcf\xff\xcf\xff\xdf0\xc3\xe0\x07\xe8\x06\xec\x00\xcc\x01\xcf\x00\xcf\x00\xdf\x00'),
                            bytearray(b'[\x7f\x7f\x7f\x7fx\xff\x01\xf8\x07l\x13\x0e\xf1\x00\x03[$\x7f\x00x\x00\x01\x00\x00\x07\x00\x13\x00\xf1\x00\x03'),
                            bytearray(b'\xff\x9f\xfe>\xfc|\xf8\xf8`\xf8\xc0<\xe6\x18\x07\xf8\x9f\x00>\x00|\x00\xf8\x00`\x98\x00<\x00\x18\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xe0@\x0e\x04s\x00\xf3\x02\xf9\x00\xf9\x02\xf8\x08p`\x80\x00\x0e\x00s\x00\xf3\x00\xf9\x00\xf9\x00\xf8\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x07\x00\x03\x04\x19\x0f\x1f\x0f\x1f\x1f?\x07\x00\x00\x00\x00\x00\x00\x00\x04\t\x06\x0f\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x1f\x0e_f\x9f\xe2\xcf\xf6\xff\xff\xff\xff\xff\x1f\x7f\x98\x0e\x00F \x82`\xc60\xff\x00\xff\x00\x1f\x00\x18\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"p\x00\x1f#\x0f3\'???\x7f\x7f}\x7fx\x7f\x00\x00\x03 \x030\'\x18?\x00\x7f\x00}\x02x\x07"),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\xe0\x80\xf0\x92\xf8\x9d\xf8\xc7\xf0\xef\x00\x00\x00\x00\x80\x00\x80\x00\x90\x02\x98\x05\xc0\x07\xe0\x0f'),
                            bytearray(b'\xfb~\xf9\x7f\xfc\x7f\xfc?\xfe\x1f\xff\x8f\xff\x8f\xf8\x18z\x04y\x06|\x03<\x03\x1e\x01\x8f\x00\x8f\x00\x18\x00'),
                            bytearray(b'3\xfc\x82\xf8\xaa\xa0\x00\xfe\x00\xfc\xf0\xf0\x80\x80\x00\x000\xcc\x80x\xa0\x00\x00\xfe\x00\xfc\xf0\x00\x80\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x1f\'\x0f?\x7f?\xbfx;<y\x1f\xff\x1f\x1fs\x07 \x0f0?\x008@8\x04\x19\x06\x1f\x00\x13`"),
                            bytearray(b'<\xf3\xf8\xe7\xf9\xee\xfc\xec\xfe\xcd\xff\xcf\xff\xcf\xff\xdf0\xc3\xe0\x07\xe8\x06\xec\x00\xcc\x01\xcf\x00\xcf\x00\xdf\x00'),
                            bytearray(b'[\x7f\x7f\x7f\x7fx\xff\x01\xf8\x07l\x13\x0e\xf1\x00\x03[$\x7f\x00x\x00\x01\x00\x00\x07\x00\x13\x00\xf1\x00\x03'),
                            bytearray(b'\xff\x9f\xfe>\xfc|\xf8\xf8`\xf8\xc0<\xe6\x18\x07\xf8\x9f\x00>\x00|\x00\xf8\x00`\x98\x00<\x00\x18\x00\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xe0@\x0e\x04s\x00\xf3\x02\xf9\x00\xf9\x02\xf8\x08p`\x80\x00\x0e\x00s\x00\xf3\x00\xf9\x00\xf9\x00\xf8\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x07\x00\x03\x04\x19\x0f\x1f\x0f\x1f\x1f?\x07\x00\x00\x00\x00\x00\x00\x00\x04\t\x06\x0f\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x1f\x0e_f\x9f\xe2\xcf\xf6\xff\xff\xff\xff\xff\x1f\x7f\x98\x0e\x00F \x82`\xc60\xff\x00\xff\x00\x1f\x00\x18\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"p\x00\x1f#\x0f3\'???\x7f\x7f}\x7fx\x7f\x00\x00\x03 \x030\'\x18?\x00\x7f\x00}\x02x\x07"),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\xe0\x80\xf0\x92\xf8\x9d\xf8\xc7\xf0\xef\x00\x00\x00\x00\x80\x00\x80\x00\x90\x02\x98\x05\xc0\x07\xe0\x0f'),
                            bytearray(b'\xfb~\xf9\x7f\xfc\x7f\xfc?\xfe\x1f\xff\x8f\xff\x8f\xf8\x18z\x04y\x06|\x03<\x03\x1e\x01\x8f\x00\x8f\x00\x18\x00'),
                            bytearray(b'3\xfc\x82\xf8\xaa\xa0\x00\xfe\x00\xfc\xf0\xf0\x80\x80\x00\x000\xcc\x80x\xa0\x00\x00\xfe\x00\xfc\xf0\x00\x80\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x1f\'\x0f?\x7f?\xbfx;<y\x1f\xff\x1f\x1fs\x07 \x0f0?\x008@8\x04\x19\x06\x1f\x00\x13`"),
                            bytearray(b'<\xf3\xf8\xe7\xf9\xee\xfc\xec\xfe\xcd\xff\xcf\xff\xcf\xff\xdf0\xc3\xe0\x07\xe8\x06\xec\x00\xcc\x01\xcf\x00\xcf\x00\xdf\x00'),
                            bytearray(b'[\x7f\x7f~\x7fx\xff\x01\xf8\x07`\x1f\x03<\x03|[$~\x00x\x00\x01\x00\x00\x07\x00\x1f\x00<\x00|'),
                            bytearray(b'\xff\x9f\xfe>\xfc|\xf8\xfcf\xf8\x07\xf80\xc0\xb8@\x9f\x00>\x00|\x00\xf8\x04`\x98\x00\xf8\x00\xc0\x00@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xe0@\x0e\x04s\x00\xf3\x02\xf9\x00\xf9\x02\xf8\x08p`\x80\x00\x0e\x00s\x00\xf3\x00\xf9\x00\xf9\x00\xf8\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'R\t\x1f\x1f\x0f\x16\xa0?\x19?\t0\x19\x0f9\x1f\x00\t\x1f\x00\x06\x10 \x1f\x19&\x000\t\x06\x19\x06'),
                            bytearray(b'\xa0\x00\x80\x80 \x80@\xc0\x80\xc0\x00\xc0\x80\x00\xc0\x80\x00\x00\x80\x00\x00\x80@\x80\x80@\x00\xc0\x00\x00\x80\x00'),
                            bytearray(b'6\x1f\x19?\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\t\x19&\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x80\x80\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80@\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=117),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x07\x00\x03\x04\x19\x0f\x1f\x0f\x1f\x1f?\x07\x00\x00\x00\x00\x00\x00\x00\x04\t\x06\x0f\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x1f\x0e_f\x9f\xe2\xcf\xf6\xff\xff\xff\xff\xff\x1f\x7f\x98\x0e\x00F \x82`\xc60\xff\x00\xff\x00\x1f\x00\x18\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"p\x00\x1f#\x0f3\'???\x7f\x7f}\x7fx\x7f\x00\x00\x03 \x030\'\x18?\x00\x7f\x00}\x02x\x07"),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\xe0\x80\xf0\x92\xf8\x9d\xf8\xc7\xf0\xef\x00\x00\x00\x00\x80\x00\x80\x00\x90\x02\x98\x05\xc0\x07\xe0\x0f'),
                            bytearray(b'\xfb~\xf9\x7f\xfc\x7f\xfc?\xfe\x1f\xff\x8f\xff\x8f\xf8\x18z\x04y\x06|\x03<\x03\x1e\x01\x8f\x00\x8f\x00\x18\x00'),
                            bytearray(b'3\xfc\x82\xf8\xaa\xa0\x00\xfe\x00\xfc\xf0\xf0\x80\x80\x00\x000\xcc\x80x\xa0\x00\x00\xfe\x00\xfc\xf0\x00\x80\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x1f\'\x0f?\x7f?\xbfx;<y\x1f\xff\x1f\x1fs\x07 \x0f0?\x008@8\x04\x19\x06\x1f\x00\x13`"),
                            bytearray(b'<\xf3\xf8\xe7\xf9\xee\xfc\xec\xfe\xcd\xff\xcf\xff\xcf\xff\xdf0\xc3\xe0\x07\xe8\x06\xec\x00\xcc\x01\xcf\x00\xcf\x00\xdf\x00'),
                            bytearray(b'[\x7f\x7f~\x7fx\xff\x01\xf8\x07`\x1f\x03<\x03|[$~\x00x\x00\x01\x00\x00\x07\x00\x1f\x00<\x00|'),
                            bytearray(b'\xff\x9f\xfe>\xfc|\xf8\xfcf\xf8\x07\xf80\xc0\xb8@\x9f\x00>\x00|\x00\xf8\x04`\x98\x00\xf8\x00\xc0\x00@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\xe0@\x0e\x04s\x00\xf3\x02\xf9\x00\xf9\x02\xf8\x08p`\x80\x00\x0e\x00s\x00\xf3\x00\xf9\x00\xf9\x00\xf8\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'x`hX\x00\xf8\x14\xec&\x1c">=w\x1d\x7f`\x00H\x10\x00\xf8\x04\xe8\x04\x18"\x1c5B\x1db'),
                            None,
                            bytearray(b'\x1b7\x1f<\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x13$\x1c \x00\x1f\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'x`hX\x00\xf8\x14\xec&\x1c">=w\x1d\x7f`\x00H\x10\x00\xf8\x04\xe8\x04\x18"\x1c5B\x1db'),
                            None,
                            bytearray(b'\x1b7\x1f<\x08?\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x13$\x1c \x087\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
            ]
        )
    ),
    palette_id=664,
    palette_offset=0,
    unknown_num=0
)
