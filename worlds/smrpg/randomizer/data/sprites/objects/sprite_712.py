# SPR0712_STELLA_BEAM

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL756_STELLA_BEAM
sprite = CompleteSprite(
    animation=AnimationPack(48, length=434, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=4096,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x008\x008\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x008\x008\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x0c\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x00\x08\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x000\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00 \x00\x10\x00\x10\x00'),
                            bytearray(b'\x00\x18\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x18\x00\x18\x000\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00 \x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x08\x07\x00\x00\x00\x00\x00\x01\x00\x01\x01\x00\x02\x00\x04\x00\x080'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            bytearray(b'\x08\x07\x04\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x080\x04\x00\x02\x00\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x10\xe0 \xc0@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x0c \x00@\x00\x80\x00\x00\x80\x00\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=103),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\x08\x07\x00\x00\x00\x00\x00\x01\x00\x01\x01\x00\x02\x00\x04\x00\x080'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80 \xc0\x10\xe0\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00@\x00 \x00\x10\x0c'),
                            bytearray(b'\x08\x07\x04\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x080\x04\x00\x02\x00\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x10\xe0 \xc0@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x0c \x00@\x00\x80\x00\x00\x80\x00\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=355),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x18\x000\x000\x000\x00\x00\x00\x00\x00\x00\x07\x00\x08\x00\x10\x00\x10\x00\x10\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\xe0\x00\x10\x00\x08\x00\x08\x00\x08\x00'),
                            bytearray(b'\x000\x000\x00\x00\x00\x00\x00\x0f\x00\x07\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\xf0\x00\xe0\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x10\x00\xe0\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x0f\x00\x1f\x000\x00`\x00`\x00`\x00`\x00\x00\x00\x00\x0f\x00\x10\x00 \x00 \x00 \x00 \x00'),
                            bytearray(b'\x00\x00\x00\xf0\x00\xf8\x00\x0c\x00\x06\x00\x06\x00\x06\x00\x06\x00\x00\x00\x00\xf0\x00\x08\x00\x04\x00\x04\x00\x04\x00\x04\x00'),
                            bytearray(b'\x00`\x00`\x00`\x00\x00\x00\x00\x00\x1f\x00\x0f\x00\x00 \x00 \x00 \x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0c\x00\xf8\x00\xf0\x00\x00\x04\x00\x04\x00\x04\x00\x04\x00\x08\x00\xf0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x01\x02\x01\x0c\x030\x0f\x00\x01\x00\x01\x01\x00\x01\x02\x02\x00\x02\x04\x0c\x100\xc0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            bytearray(b'0\x0f\x0c\x03\x02\x01\x02\x01\x01\x00\x01\x00\x00\x00\x00\x000\xc0\x0c\x10\x02\x04\x02\x00\x01\x02\x01\x00\x00\x01\x00\x01'),
                            bytearray(b'\x0c\xf00\xc0@\x80@\x80\x80\x00\x80\x00\x00\x00\x00\x00\x0c\x030\x08@ @\x00\x80@\x80\x00\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=93),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=103),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x01\x02\x01\x0c\x030\x0f\x00\x01\x00\x01\x01\x00\x01\x02\x02\x00\x02\x04\x0c\x100\xc0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            bytearray(b'0\x0f\x0c\x03\x02\x01\x02\x01\x01\x00\x01\x00\x00\x00\x00\x000\xc0\x0c\x10\x02\x04\x02\x00\x01\x02\x01\x00\x00\x01\x00\x01'),
                            bytearray(b'\x0c\xf00\xc0@\x80@\x80\x80\x00\x80\x00\x00\x00\x00\x00\x0c\x030\x08@ @\x00\x80@\x80\x00\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=164, y=344),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x00?\x00`\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x1f\x00 \x00@\x00@\x00@\x00@\x00@\x00'),
                            bytearray(b'\x00\xf8\x00\xfc\x00\x06\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00\xf8\x00\x04\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00'),
                            bytearray(b'\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00 \x00?\x00\x1f@\x00@\x00@\x00\x00\x00\x00\x00 \x00\x1f\x00\x00\x00'),
                            bytearray(b'\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x06\x00\xfc\x00\xf8\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\xf8\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x0c\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x00\x08\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x000\x00\x18\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00 \x00\x10\x00\x10\x00'),
                            bytearray(b'\x00\x18\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x18\x00\x18\x000\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00 \x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=98),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x18\x000\x000\x000\x00\x00\x00\x00\x00\x00\x07\x00\x08\x00\x10\x00\x10\x00\x10\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\xe0\x00\x10\x00\x08\x00\x08\x00\x08\x00'),
                            bytearray(b'\x000\x000\x00\x00\x00\x00\x00\x0f\x00\x07\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\xf0\x00\xe0\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x10\x00\xe0\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x02\x01\x02\x01\x0c\x030\x0f\x00\x01\x00\x01\x01\x00\x01\x02\x02\x00\x02\x04\x0c\x100\xc0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x80@\x800\xc0\x0c\xf0\x00\x80\x00\x80\x80\x00\x80@@\x00@ 0\x08\x0c\x03'),
                            bytearray(b'0\x0f\x0c\x03\x02\x01\x02\x01\x01\x00\x01\x00\x00\x00\x00\x000\xc0\x0c\x10\x02\x04\x02\x00\x01\x02\x01\x00\x00\x01\x00\x01'),
                            bytearray(b'\x0c\xf00\xc0@\x80@\x80\x80\x00\x80\x00\x00\x00\x00\x00\x0c\x030\x08@ @\x00\x80@\x80\x00\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=338),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=348),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=100),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=356),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x00?\x00`\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x1f\x00 \x00@\x00@\x00@\x00@\x00@\x00'),
                            bytearray(b'\x00\xf8\x00\xfc\x00\x06\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00\xf8\x00\x04\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00'),
                            bytearray(b'\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00 \x00?\x00\x1f@\x00@\x00@\x00\x00\x00\x00\x00 \x00\x1f\x00\x00\x00'),
                            bytearray(b'\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x06\x00\xfc\x00\xf8\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\xf8\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=367),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=364),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x07\x00\x00\x00\x00\x00\x08\x00\x04\x00#\x03\x14\x04\x08\x04\x08'),
                            None,
                            bytearray(b'\x00\x07\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x08\x04\x08\x03\x14\x00#\x00\x04\x00\x08\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x07\x00\x00\x00\x00\x00\x08\x00\x04\x00#\x03\x14\x04\x08\x04\x08'),
                            None,
                            bytearray(b'\x00\x07\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x08\x04\x08\x03\x14\x00#\x00\x04\x00\x08\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=348),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x18\x000\x000\x000\x00\x00\x00\x00\x00\x00\x07\x00\x08\x00\x10\x00\x10\x00\x10\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\xe0\x00\x10\x00\x08\x00\x08\x00\x08\x00'),
                            bytearray(b'\x000\x000\x00\x00\x00\x00\x00\x0f\x00\x07\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x0c\x00\x0c\x00\x0c\x00\x18\x00\xf0\x00\xe0\x00\x00\x00\x00\x08\x00\x08\x00\x08\x00\x10\x00\xe0\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=111),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=356),
                        Tile(mirror=False, invert=True, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x0f\x00\x0f\x00\x04\x00\x00\x00B\x00#\x03\x14\x04\x08\x08\xb0\x08\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x00 \x00\x00\x00B\x00\xc4\xc0( \x10\x10\r\x10\x08'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x0f\x00\x0f\x00\x04\x00\x00\x00B\x00#\x03\x14\x04\x08\x08\xb0\x08\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x00 \x00\x00\x00B\x00\xc4\xc0( \x10\x10\r\x10\x08'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=348),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x0f\x00\x1f\x000\x00`\x00`\x00`\x00`\x00\x00\x00\x00\x0f\x00\x10\x00 \x00 \x00 \x00 \x00'),
                            bytearray(b'\x00\x00\x00\xf0\x00\xf8\x00\x0c\x00\x06\x00\x06\x00\x06\x00\x06\x00\x00\x00\x00\xf0\x00\x08\x00\x04\x00\x04\x00\x04\x00\x04\x00'),
                            bytearray(b'\x00`\x00`\x00`\x00\x00\x00\x00\x00\x1f\x00\x0f\x00\x00 \x00 \x00 \x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0c\x00\xf8\x00\xf0\x00\x00\x04\x00\x04\x00\x04\x00\x04\x00\x08\x00\xf0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=108),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc'),
                            bytearray(b'\x00\x00\x03\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c\x0c30\xcc\xc00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=166, y=348),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x00?\x00`\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x1f\x00 \x00@\x00@\x00@\x00@\x00@\x00'),
                            bytearray(b'\x00\xf8\x00\xfc\x00\x06\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00\xf8\x00\x04\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00'),
                            bytearray(b'\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00 \x00?\x00\x1f@\x00@\x00@\x00\x00\x00\x00\x00 \x00\x1f\x00\x00\x00'),
                            bytearray(b'\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x06\x00\xfc\x00\xf8\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\xf8\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x02\x0c\x04\x18\x00\x04\x00\x02\x00\x11\x01\n\x03D\x07\xa8\x0eP\x1c '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x02\x0c\x04\x18\x00\x04\x00\x02\x00\x11\x01\n\x03D\x07\xa8\x0eP\x1c '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x02\x0c\x04\x18\x00\x04\x00\x02\x00\x11\x01\n\x03D\x07\xa8\x0eP\x1c '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x02\x0c\x04\x18\x00\x04\x00\x02\x00\x11\x01\n\x03D\x07\xa8\x0eP\x1c '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=82),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=149, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=157, y=100),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=157, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=177, y=82),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=177, y=82),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=177, y=81),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=177, y=81),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=165, y=352),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x88\x88\x12\x12@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=173, y=349),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=80),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=179, y=80),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=176, y=83),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=179, y=83),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=174, y=93),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x82\x82\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=165, y=97),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=174, y=78),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=181, y=78),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=174, y=85),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00 \x00\x18\x00\x00\x00p\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=181, y=85),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL756_STELLA_BEAM,
    palette_offset=0,
    unknown_num=0
)