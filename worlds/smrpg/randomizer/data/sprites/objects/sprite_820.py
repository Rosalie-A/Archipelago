# SPR0820_MAGIKOOPA_S_TRIANGLE_CIRCLE_X_CAST_MAGIC

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL313_MAGIKOOPA_S_TRIANGLE_CIRCLE_X_CAST_MAGIC
sprite = CompleteSprite(
    animation=AnimationPack(180, length=253, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=392, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=372),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=364, y=372),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=368),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=364, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=380, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=368),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=368),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=368),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=364, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=112),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=380, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c88\x00p\x00\xe0\x01\x01\x03\x03\x07\x07\x0e\x0e\x00\x1c\x008\x00p\x00\xe0'),
                            None,
                            bytearray(b'\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01\x00\x00\xe0\x00p\x008\x00\x1c\x00\x0e\x00\x07\x00\x03\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=392, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00pppp\x00\xe0\x00\xe0\x00\x03\x00\x0f\x00\x1f\x00<p\x00p\x00\xe0\x00\xe0\x00'),
                            None,
                            bytearray(b'\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00\xe0\x00\xe0\x00p\x00p\x00<\x00\x1f\x00\x0f\x00\x03\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=368),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x02\x02\x00\x00\x03\x07\x07\x07\x00\x0e\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x0e\x1c\x00\x1c\x008\x008\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL313_MAGIKOOPA_S_TRIANGLE_CIRCLE_X_CAST_MAGIC,
    palette_offset=0,
    unknown_num=12
)
