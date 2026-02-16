# SPR0793_BIG_PINK_HEART

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL318_BIG_PINK_HEART
sprite = CompleteSprite(
    animation=AnimationPack(185, length=312, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x08:\x1c\x0b,InDw\x00\x00\x00\x00\x00\x00\x0c\x12\x00!0@p\x00x\x00'),
                            None,
                            bytearray(b'ss\x05\x18\x00\x0f\x04\x06\r\r\x01\x01\x00\x00\x00\x00|\x00\x1f`\x0f0\x06\x19\r\x02\x01\x02\x00\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x08:\x1c\x0b,InDw\x00\x00\x00\x00\x00\x00\x0c\x12\x00!0@p\x00x\x00'),
                            None,
                            bytearray(b'ss\x05\x18\x00\x0f\x04\x06\r\r\x01\x01\x00\x00\x00\x00|\x00\x1f`\x0f0\x06\x19\r\x02\x01\x02\x00\x01\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'h*\x19\x19\x08\x08\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00*U\x19\x06\x08\x07\x01\x02\x00\x01\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=132),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00Q\x1e\x96\x18W\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c A \xc1\xe0\x00'),
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xf7\xb8\x11\xde,\xcf\x7fO\x98\xe0\t4@_\xad-\xc0\x00\xe0\x00\xf0\x00p\x80\xff\x00?\xc0_\xa0-\xd2'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'h*\x19\x19\x08\x08\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00*U\x19\x06\x08\x07\x01\x02\x00\x01\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00Q\x1e\x96\x18W\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c A \xc1\xe0\x00'),
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xf7\xb8\x11\xde,\xcf\x7fO\x98\xe0\t4@_\xad-\xc0\x00\xe0\x00\xf0\x00p\x80\xff\x00?\xc0_\xa0-\xd2'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'.*(/ \x13\x01\x0b\x14\x04\t\x01\x05\x01\x00\x02/\x10/\x10\x13,\x0b\x14\x04\x1b\x01\x0e\x01\x06\x02\x01'),
                            bytearray(b'_\x1f\xa0\x00&\x94Ox@\xfe27ai\x8b\x9b\xe0\x00\xbf@\xff\x00\x7f\x80\xff\x007\xc8i\x96\x9bd'),
                            None,
                            bytearray(b'\xe7\xe7a!\x06\x16\x06\x06\x00\x00\x01\x00\x00\x00\x00\x00\xe7\x18!^\x16\t\x06\x01\x00\x03\x00\x01\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xa4\x80\xc0\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xe0\x1c\x00\x00'),
                            bytearray(b'\x1a\x02\x0f\x03\x14\x18=)0<*<!.\x07\x14\x01\x1c\x0c\x10\x1f >\x00?\x00?\x00/\x10\x17('),
                            bytearray(b'\xdc\xe3\xde\xe1\xdf\xe0\xdf\xe0\xc7\xf8a~p\x7f\xbe?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'.*(/ \x13\x01\x0b\x14\x04\t\x01\x05\x01\x00\x02/\x10/\x10\x13,\x0b\x14\x04\x1b\x01\x0e\x01\x06\x02\x01'),
                            bytearray(b'_\x1f\xa0\x00&\x94Ox@\xfe27ai\x8b\x9b\xe0\x00\xbf@\xff\x00\x7f\x80\xff\x007\xc8i\x96\x9bd'),
                            None,
                            bytearray(b'\xe7\xe7a!\x06\x16\x06\x06\x00\x00\x01\x00\x00\x00\x00\x00\xe7\x18!^\x16\t\x06\x01\x00\x03\x00\x01\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xa4\x80\xc0\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xe0\x1c\x00\x00'),
                            bytearray(b'\x1a\x02\x0f\x03\x14\x18=)0<*<!.\x07\x14\x01\x1c\x0c\x10\x1f >\x00?\x00?\x00/\x10\x17('),
                            bytearray(b'\xdc\xe3\xde\xe1\xdf\xe0\xdf\xe0\xc7\xf8a~p\x7f\xbe?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x11l2<q}|\x7f!3\x00\x02\t\r\n\x1a\x7f\x00?@}\x02\x7f\x003\x0c\x02=\r\x12\x1a\x05'),
                            bytearray(b'rR|\x80\xb6\x00\x08]\x80\xfc\xb8\xff]\x7fW\xdf\xad\x00\xff\x00\xff\x00\xff\x00\xfe\x01\xff\x00\x7f\x80\xdf '),
                            bytearray(b'\x05\r\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x02\x07\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\t/UU\x83\x83\x8e.\x10\x10\x01\x07\x03\x00\x00\x00/\xd0U\xaa\x83|.\xd1\x10/\x07\x00\x00\x03\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x01\x06\x07\x0e\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0000|\x83\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x14\x17\x06\x17?\x0f/GSCYa\x12jjp\x18\x00\x18 0\x00x\x00|\x00~\x00}\x00\x7f\x00'),
                            bytearray(b'\x7f\x80?\xc0\r\xf2\x80\xff\xc0\xff\x7f\x7f\xff\xff??\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x11l2<q}|\x7f!3\x00\x02\t\r\n\x1a\x7f\x00?@}\x02\x7f\x003\x0c\x02=\r\x12\x1a\x05'),
                            bytearray(b'rR|\x80\xb6\x00\x08]\x80\xfc\xb8\xff]\x7fW\xdf\xad\x00\xff\x00\xff\x00\xff\x00\xfe\x01\xff\x00\x7f\x80\xdf '),
                            bytearray(b'\x05\r\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x02\x07\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\t/UU\x83\x83\x8e.\x10\x10\x01\x07\x03\x00\x00\x00/\xd0U\xaa\x83|.\xd1\x10/\x07\x00\x00\x03\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x01\x06\x07\x0e\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0000|\x83\x7f\x80\x7f\x80\x00\x00\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x14\x17\x06\x17?\x0f/GSCYa\x12jjp\x18\x00\x18 0\x00x\x00|\x00~\x00}\x00\x7f\x00'),
                            bytearray(b'\x7f\x80?\xc0\r\xf2\x80\xff\xc0\xff\x7f\x7f\xff\xff??\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x8aP\xd7h\x82-\x0eI\x04+\x19\x1f\x107\x12\x03\x7f\x80~\x81?\xc0M2/P\x1f 7\x08\x03\x1c'),
                            bytearray(b'\xd0\x00M\x005@0\xce\xbdB\x8b\xf7\xe0\xef!g\xff\x00\xff\x00\xff\x00\xff\x00\xd7(\xff\x00\xff\x00g\x98'),
                            bytearray(b'\x00\x0c\x05\x05\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\x05\x02\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\xff\x1c_&.\xd1U\x1b;\x06\x01\x01\x00\x00\x00\xff\x00_\xa0.\xd1U\xaa;\x04\x01\x06\x00\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\t\x06\x08\x0f\x18\x1f\x00\x00\x00\x00\x00\x00\x01\x00\x04\x00\x00\x08\x10\x00\x00 '),
                            bytearray(b'\x00\x00\x00\x00L|\xfc\x03\xff\x00\xff\x00 \xdfA\xbe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1e\x1fN\x0f\x8fO\xeb+\xb7W\xda\n\xf0\x00\xd4  @p\x00p\x80T\x80h\x80u\x80_\xa0\x7f\x80'),
                            bytearray(b'\x00\xff\x8a\xff\x7f\xff\xff\xff\xff\xff//\x14\x14\xce\xca\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x00\xeb\x005\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x8aP\xd7h\x82-\x0eI\x04+\x19\x1f\x107\x12\x03\x7f\x80~\x81?\xc0M2/P\x1f 7\x08\x03\x1c'),
                            bytearray(b'\xd0\x00M\x005@0\xce\xbdB\x8b\xf7\xe0\xef!g\xff\x00\xff\x00\xff\x00\xff\x00\xd7(\xff\x00\xff\x00g\x98'),
                            bytearray(b'\x00\x0c\x05\x05\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\x05\x02\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\xff\x1c_&.\xd1U\x1b;\x06\x01\x01\x00\x00\x00\xff\x00_\xa0.\xd1U\xaa;\x04\x01\x06\x00\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\t\x06\x08\x0f\x18\x1f\x00\x00\x00\x00\x00\x00\x01\x00\x04\x00\x00\x08\x10\x00\x00 '),
                            bytearray(b'\x00\x00\x00\x00L|\xfc\x03\xff\x00\xff\x00 \xdfA\xbe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1e\x1fN\x0f\x8fO\xeb+\xb7W\xda\n\xf0\x00\xd4  @p\x00p\x80T\x80h\x80u\x80_\xa0\x7f\x80'),
                            bytearray(b'\x00\xff\x8a\xff\x7f\xff\xff\xff\xff\xff//\x14\x14\xce\xca\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x00\xeb\x005\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x01'),
                            None,
                            bytearray(b'\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=120),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa2\xa26v\x0c\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa2@v\x08\x02\x0c\x00\x02'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00 '),
                            None,
                            bytearray(b'\x00\x00\x00\x18\n\n\x04\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x06\n\x05\x02\x05\x00\x01\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x80\xc0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0c\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00\x00\x10 \x00\x00@\x00\x80'),
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00 '),
                            None,
                            bytearray(b'\x00\x00\x00\x18\n\n\x04\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x06\n\x05\x02\x05\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa2\xa26v\x0c\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa2@v\x08\x02\x0c\x00\x02'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0c\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00\x00\x10 \x00\x00@\x00\x80'),
                            bytearray(b'\x00\x00\x80\xc0\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00 \x10\x10\x08\x04\x03\x01\x00\x00\x00\x00\x00\x80\x00\x00 \x00\x10\x00\x04\x08\x01\x02\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x80\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x01\x00\x00\x00\x18 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 \x10\x10\x08\x04\x03\x01\x00\x00\x00\x00\x00\x80\x00\x00 \x00\x10\x00\x04\x08\x01\x02\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x18 \x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'ss\x05\x18\x00\x0f\x04\x06\r\r\x01\x01\x00\x00\x00\x00|\x00\x1f`\x0f0\x06\x19\r\x02\x01\x02\x00\x01\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x08:\x1c\x0b,InDw\x00\x00\x00\x00\x00\x00\x0c\x12\x00!0@p\x00x\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'ss\x05\x18\x00\x0f\x04\x06\r\r\x01\x01\x00\x00\x00\x00|\x00\x1f`\x0f0\x06\x19\r\x02\x01\x02\x00\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x08:\x1c\x0b,InDw\x00\x00\x00\x00\x00\x00\x0c\x12\x00!0@p\x00x\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=121),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0c\x08\x19\x0c0\x10\t,@`\x08\t\x00\x00\x00\x00\x0c\x01\x00\x10\x00 0@p\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00d \x8aH\x80\x00\x00\x08\x02\x82\x00\x00\x00\x00\x00\x00`\x84\x00\x02\x00\x00(\x02\x02\x00'),
                            bytearray(b'\x0c\x00\x00\x1e\x04\x0e\x00\x00\x0c\x0c\x00\x00\x00\x00\x00\x00\x06\x08\x1e \x0e0\x00\x18\x0c\x02\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'@\x08\x00\xf0@\xd0\x00\x00PP\x00\x00\x00\x00\x00\x00X\x00\xf0\n\xd0\x0c\x00\x18P\x80\x00\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x08\x00\x00@@\x00\x00\x01\x01\x00\x00\x04\x04\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x000\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00B  \x80\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00B\x00 \x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80D\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x90\x10\x84\x84\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x04\x00\x10\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=119),
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
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL318_BIG_PINK_HEART,
    palette_offset=0,
    unknown_num=8
)
