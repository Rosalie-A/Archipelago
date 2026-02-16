# SPR0940_BOWSER_IN_HELICOPTER_CHASING

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL731_BOWSER_IN_HELICOPTER_CHASING
sprite = CompleteSprite(
    animation=AnimationPack(425, length=285, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x19\x00=\x01\x1e\x03\x00\x02\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\xc0\x00\xf0\x00\xf0\x00`\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP~<\xd4\xf00\xf0\x00\x00O0\x06`)u1}\x7f?\x0f\xbf\x0f\xff\xff\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'|Cp \xf0`\xc0@\x90\xf0\xe0\xe0\x0c\xf0\x00\x00\xfc\xc3\xd0\xa0\x90`\xb0p\x08\xf8\x18\xf8\x08\xf8\xfc\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\xa8\x90'),
                            bytearray(b'\x07\x04\x04\x07\x03\x02\x0e?\x16\x0f\r\x0bM\xc6I\x0f\x02\x02\x00\x07\x03\x03\x0c?\x16\x03\x061\x0b0O1'),
                            bytearray(b'\xc0P\xec\xd0\xc6\xd0a\xfb_\x9fu\xb5\xf8|\xf9\xe7\xae\xccc\xc2\xa9\xe98\xf6X\xa3s\xa9\xfa|\xf9\xe7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=105),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x01\x0e\x03\x04\x02\x05\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\xc0\x00\xc0\x00\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x02\x07\x04\x0f<\x14\x0f\x0f\nO\xc5I\x0e\x01\x00\x01\x01\x00\x00\n:\x10\x07\x073\n1O0'),
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP~<\xd4\xf00\xf0\x00\x00O0\x06`)u1}\x7f?\x0f\xbf\x0f\xff\xff\xff'),
                            bytearray(b'\xf9\xc7t#\xf0`\xc0@\x90\xf0\xe0\xe0\x0c\xf0\x00\x00\xf9\xc7\xd4\xa3\x90`\xb0p\x08\xf8\x18\xf8\x08\xf8\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=113),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa8P'),
                            None,
                            bytearray(b'\x00\x10\xec\x10\xc7\x11\xe1{\xef\xff\xd4\xd4|\xb8\xf8d\xef\x0ccC\xa8\xa8\xb8\xf7y\xc3\x92\xe8|\xb8\xfad'),
                            bytearray(b'\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=105),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x02\x03\x04\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x00\x00\x0f<\x17\x0f\x0f\nO\xc6J\x0f\x01\x00\x01\x00\x03\x00\x0f<\x16\x02\x040\t1L3'),
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP~<\xd4\xf00\xf0\x00\x00O1\x06`)u1}\x7f?\x0f\xbf\x0f\xff\xff\xff'),
                            bytearray(b'\xfccp \xf0`\xc0@\x90\xf0\xe0\xe0\x0c\xf0\x00\x00\xdc\xe3\xd0\xa0\x90`\xb0p\x08\xf8\x18\xf8\x08\xf8\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=113),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa8P'),
                            None,
                            bytearray(b'\x00\x10,\x10F\x90!;\xef\x1f\xf5\x15\xf8<y\xe7\xee\x0c\xe3\x82i\xa9\xf86\xb8\xa3SIZ|9\xe7'),
                            bytearray(b'\x00\x00\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=105),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x01\x0e\x03\x04\x02\x05\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\xc0\x00\xc0\x00\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x02\x07\x04\x0f<\x14\x0f\x0f\nO\xc5I\x0e\x01\x00\x01\x01\x00\x00\n:\x10\x07\x073\n1O0'),
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP~<\xd4\xf00\xf0\x00\x00O0\x06`)u1}\x7f?\x0f\xbf\x0f\xff\xff\xff'),
                            bytearray(b'\xf9\xc7t#\xf0`\xc0@\x90\xf0\xe0\xe0\x0c\xf0\x00\x00\xf9\xc7\xd4\xa3\x90`\xb0p\x08\xf8\x18\xf8\x08\xf8\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=113),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa8P'),
                            None,
                            bytearray(b'\x00\x10\xec\x10\xc7\x11\xe1{\xef\xff\xd4\xd4|\xb8\xf8d\xef\x0ccC\xa8\xa8\xb8\xf7y\xc3\x92\xe8|\xb8\xfad'),
                            bytearray(b'\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=105),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP\xde\xfc4\xf0\x1e\x00\x00\x00O0\x06`)u1}\x1f\xbf\x0e\xfe\x1e\x1e\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=129),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00>\x00\x1e\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x0e\x00A<!\x12'),
                            bytearray(b'yGt#\xf8`\xf8\x18`8;<\x008\x00\x00\xf9\xc7\xd4\xa3\x98`\xe4\x1c\xc6\xbeB~G\x7f\xf8\xf8'),
                            bytearray(b'\x00\x0c\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x0c\x08\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=121),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\xa8\x90'),
                            bytearray(b'\x07\x04\x04\x07\x03\x02\x0e?\x16\x0f\r\x0bM\xc6I\x0f\x02\x02\x00\x07\x03\x03\x0c?\x16\x03\x061\x0b0O1'),
                            bytearray(b'\xc0P\xec\xd0\xc6\xd0a\xfb_\x9fu\xb5\xfc|\xf8\xe4\xae\xccc\xc2\xa9\xe98\xf6X\xa3s\xa9\xf8x\xfa\xe4'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=113),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1eP\xde\xfc4\xf0\x00\x00\x00\x00O0\x06`)u1}\x0f\xbf\x0f\xff\x07\x07\x1f\x1f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x03\x00\x03\xc0\x00\x00`\x00 \x00\xe0\x00\x00\x06\x00@\x034\x03'),
                            bytearray(b'\xfc\xc3p \xf0`\xc0@\x90\xf0\xe0\xe0\x0c\xf0\x00\x00\xfc\xc3\xd0\xa0\x90`\xb0p\x08\xf8\x18\xf8\x08\xf8\xfc\xfc'),
                            bytearray(b'\x00\x1e\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1a\x1a\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa8P'),
                            bytearray(b'\x00\x00\x03\x02\x07\x04\x0f<\x14\x0f\x0f\nO\xc5I\x0e\x01\x00\x01\x01\x00\x00\n:\x10\x07\x073\n1O0'),
                            bytearray(b'\x00\x10\xec\x10\xc7\x11\xe1{\xef\xff\xd4\xd4x\xbc\xf9g\xef\x0ccC\xa8\xa8\xb8\xf7y\xc3\x92\xe8z\xbc\xf9g'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'm\x0fo\x1e\xfa\xa0\x1fQ\xdc\xff2\xfe\x00\x03\x00\x00O1\x06`)u2}\x00\xbf\x01\xff\x1c\x1f\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=129),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\xc0\x00\xa0\xe0\xe0\xe0 \xe0\x80\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00`\x00 \x00\xe0\x08\x00a\x00\x02\x00'),
                            bytearray(b'\xfccp \xf0 \xb8\xb8\xbc\x90~\x08\xe8\x00\x00\x00\xdc\xe3\xd0\xa0\xd0 @\xf8l\xd0\xf4\x8c\xbe\x9e\xfc\xfc'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=121),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa8P'),
                            bytearray(b'\x00\x00\x01\x00\x00\x00\x0f<\x17\x0f\x0f\nO\xc6J\x0f\x01\x00\x01\x00\x03\x00\x0f<\x16\x02\x040\t1L3'),
                            bytearray(b'\x00\x10,\x10F\x90!;\xef\x1f\xf5\x15\xf8<y\xe7\xee\x0c\xe3\x82i\xa9\xf86\xb8\xa3SIZ|9\xe7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=113),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x19\x00=\x01\x1e\x03\x00\x02\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\xc0\x00\xf0\x00\xf0\x00`\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x01\x0e\x03\x04\x02\x05\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\xc0\x00\xc0\x00\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x02\x03\x04\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\xc1>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\xff>\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=136),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x18x\x9e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00x\x80\x9e\xe0'),
                            None,
                            bytearray(b'\xc6&\xc00\xb0,\xd0Lp\x8c`\x18 \x180\x00fx0<|<\xfc\xdc\xfc\xfc\xf8x\xf88\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x07\x03\x0c\x07\x18\x07\x18/\x10\x00\x00\x00\x00\x01\x01\x07\x07\x0f\x0f\x1e\x1e\x1c\x1c<\x1c'),
                            bytearray(b'\xc0\xc0\xe0\xf0 <\xd0\x1f\xf8\x1f\xfe\x07\xff\x01\xff\x00\xc0\x00\xf0\x00<\xc0\xdf\xe0\xbf\xa0\x0f\x08\x03\x02\x00\x00'),
                            bytearray(b'/\x10/\x107\x08\x17\x08\x1f\x00\x0f\x00\x01\x06\x00\x038\x188\x18<\x0c\x1c\x0c\x1e\x06\x0f\x07\x07\x07\x03\x03'),
                            bytearray(b'\xff\x00\xff\x00\xff\x0c\xf3\x1e\xe1\x1f\xe0\x1b\xf2\x0cy\x80\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1e$;\xf3\xfc\xff\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL731_BOWSER_IN_HELICOPTER_CHASING,
    palette_offset=0,
    unknown_num=8
)
