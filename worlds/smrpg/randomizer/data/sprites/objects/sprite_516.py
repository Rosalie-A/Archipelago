# SPR0516_ENEMY_DEFEATED_EXPLOSION_STARS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL315_ENEMY_DEFEATED_EXPLOSION_STARS
sprite = CompleteSprite(
    animation=AnimationPack(182, length=359, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00?\x00\x00\x1f\x00\x1f\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00?\x00\x1f\x00\x1f'),
                            None,
                            bytearray(b'\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x03\x00\x03\x00\x00\x01\x00\x01\x00\x0f\x00\x0f\x07\x07\x07\x07\x03\x03\x03\x03\x01\x01\x01\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00'),
                            None,
                            bytearray(b'\x1f\x1f\x1f\x1f??\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x1f\x00\x1f\x00?\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00?\x00\x00\x1f\x00\x1f\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00?\x00\x1f\x00\x1f'),
                            None,
                            bytearray(b'\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x03\x00\x03\x00\x00\x01\x00\x01\x00\x0f\x00\x0f\x07\x07\x07\x07\x03\x03\x03\x03\x01\x01\x01\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00'),
                            None,
                            bytearray(b'\x1f\x1f\x1f\x1f??\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x1f\x00\x1f\x00?\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=104),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0f\x0f\x07\x07\x07\x07\x03\x03\x03\x00\x01\x00\x00\x01\x00\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x00\x03\x00\x01\x00\x01\x00\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\x00\xff\x00\xff\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00\xff\x00\xff\x00\xff'),
                            None,
                            bytearray(b'\x7f\x7f\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x1f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f\x7f\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x00\x7f\x00'),
                            bytearray(b'\x00\x00\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0f\x0f\x07\x07\x07\x07\x03\x03\x03\x00\x01\x00\x00\x01\x00\x00\x0f\x00\x07\x00\x07\x00\x03\x00\x00\x03\x00\x01\x00\x01\x00\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\x00\xff\x00\xff\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00\xff\x00\xff\x00\xff'),
                            None,
                            bytearray(b'\x7f\x7f\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00\x1f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f\x7f\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x00\x7f\x00'),
                            bytearray(b'\x00\x00\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=104),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x00\x07\x00\x00\x0f\x00\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x00\x07\x00\x07\x00\x0f\x00\x0f'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\x00\xff\x00\xff\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x00\x00\x00\x00\x7f\x00|\x00\x00\xf0\x00\xc0\x00\x1f\x00\x1f????\x7f\x7f||\xf0\xf0\xc0\xc0'),
                            bytearray(b'\xff\xff\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xc0\xc0\xf0\xf0||\x7f\x7f????\x1f\x1f\x1f\x1f\xc0\x00\xf0\x00|\x00\x7f\x00?\x00?\x00\x1f\x00\x1f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x00\x07\x00\x00\x0f\x00\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x00\x07\x00\x07\x00\x0f\x00\x0f'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\x00\xff\x00\xff\xff\x00\xff\x00\xff\x00\xff\x00\x00\xff\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x00\x00\x00\x00\x7f\x00|\x00\x00\xf0\x00\xc0\x00\x1f\x00\x1f????\x7f\x7f||\xf0\xf0\xc0\xc0'),
                            bytearray(b'\xff\xff\xfc\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x01\x00\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0f\x00\x0f\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xc0\xc0\xf0\xf0||\x7f\x7f????\x1f\x1f\x1f\x1f\xc0\x00\xf0\x00|\x00\x7f\x00?\x00?\x00\x1f\x00\x1f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0\xfc\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xfc\x00\xff\x00'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=104),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00'),
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=123),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=107),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=125),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=101),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=135),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x1088\xfe\xfe||||ll\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=105, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x008\x00\xfe\x00|\x00|\x00l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=97),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x10||88((\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=103, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=137),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x10||88((\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=145, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=101),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x00|\x008\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=95),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=147, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=94),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=16, mold_id=16),
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
    palette_id=SPAL315_ENEMY_DEFEATED_EXPLOSION_STARS,
    palette_offset=0,
    unknown_num=12
)
