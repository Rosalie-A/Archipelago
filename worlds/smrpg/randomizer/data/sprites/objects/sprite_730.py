# SPR0730_HAMMER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL531_HAMMER_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(388, length=426, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x08\r\x00\x120\x00<A\xfc\x80\x01\x00\x01\x00\x03\x00\x0f\x00\x1f\x00/\x00\x03\x00\x83\x00'),
                            bytearray(b'@\x00x\x98$\xa0\x18Z\x16}$\xac\n\xb9\x04b\x80@\x98`|\xc0\xac\xc0\xcd\x12\xdc#x\x07\xe1\x1f'),
                            bytearray(b'\xfe\x81~\xc1\x7f\xf1\xbe0\\>\x0f=\x07\x03\x05\x00\x01\x00\x81\x00\x81\x00\xc0\x01A\x01!\x03\x0b\x17\r\r'),
                            bytearray(b'\x90\xa3G/\x8eN\x1c\x9cx\xf0\xf0\xf0\x80\xc0\x80\x80\x8f\x7f\x1f\xff>\xfe|\xfc\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=92),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=362),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x08\r\x00\x120\x00<A\xfc\x80\x01\x00\x01\x00\x03\x00\x0f\x00\x1f\x00/\x00\x03\x00\x83\x00'),
                            bytearray(b'@\x00x\x98$\xa0\x18Z\x16}$\xac\n\xb9\x04b\x80@\x98`|\xc0\xac\xc0\xcd\x12\xdc#x\x07\xe1\x1f'),
                            bytearray(b'\xfe\x81~\xc1\x7f\xf1\xbe0\\>\x0f=\x07\x03\x05\x00\x01\x00\x81\x00\x81\x00\xc0\x01A\x01!\x03\x0b\x17\r\r'),
                            bytearray(b'\x90\xa3G/\x8eN\x1c\x9cx\xf0\xf0\xf0\x80\xc0\x80\x80\x8f\x7f\x1f\xff>\xfe|\xfc\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=346),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x08\r\x00\x120\x00<A\xfc\x80\x01\x00\x01\x00\x03\x00\x0f\x00\x1f\x00/\x00\x03\x00\x83\x00'),
                            bytearray(b'@\x00x\x98$\xa0\x18Z\x16}$\xac\n\xb9\x04b\x80@\x98`|\xc0\xac\xc0\xcd\x12\xdc#x\x07\xe1\x1f'),
                            bytearray(b'\xfe\x81~\xc1\x7f\xf1\xbe0\\>\x0f=\x07\x03\x05\x00\x01\x00\x81\x00\x81\x00\xc0\x01A\x01!\x03\x0b\x17\r\r'),
                            bytearray(b'\x90\xa3G/\x8eN\x1c\x9cx\xf0\xf0\xf0\x80\xc0\x80\x80\x8f\x7f\x1f\xff>\xfe|\xfc\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=347),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\x18\x18\x18\x0c\x0c\x08\x0c\x04\x06\x06\x06\x02\x02\x00\x00\x18\x18\x1c\x1c\x0c\x0c\x0e\x0e\x06\x06\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=106, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x00\x00\x04\x05\r\x00\x10\x00\x02$\x04\x00\x00\x00\x00\x01\x02\x07\x00\r\x03\x1a\x07\x1f\x00\x1b '),
                            bytearray(b'p\x10\x18\x00\x08\x04\x08\x1e\x00$\x02L\x02\xb0\x143P\x00h\x80\xf0\x00\xf8\x00\xfc\x03\xfc\x03\xd9\x07\xf1\x0f'),
                            bytearray(b'7%\x7f\x0f<z\x1c\x18\x12&>C\x0e0\x16\t\x08\x04@\x0cC\x18\x03hDyB}!?\x11\x1f'),
                            bytearray(b'"\xe2\x02\xd6f\xce\x8c\xbe\x98800\xe0\xe0\xe0\xf0n\x1e\xce>\xde>\x9e~x\xf8\xf0\xf0\xf0\xf0\xf8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=106, y=84),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x0b!\x05\x04\x042 \x07\x00\x10\x13\x01\x08\x00\x01\x1f \x05:$; \x1f\x10\x1f\x1c\x0f\x0c\x0f\x03\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=100, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x10\x000\x08\x08\xc0\xe0\x80\x00\x00\x00\x00\x00\x00\x00\x18\x000H\xb8x\xe0`\x80\x80\x00\x00'),
                            bytearray(b'h\x08\xec\x08\x88X\x9c\\\x10\xb80p00 \xc0\x1c\xfc\x1c\xfc<\xfc<\xfcx\xf8\xf8\xf8\xf0\xf0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=98),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0 \xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x10\x00'),
                            bytearray(b'\x0f\x00\x1f\x00\x1f\x00\x0f\x00!#\x00\x00\x00\x1b\x00\x1b\x00\x00\x00\x10\x10\x00\x10\x00<\x00\x1f \x1f \x1f '),
                            bytearray(b'\xf0\x00\xf8\x08\xf8\x10\xd8`>\x81PD\xa2\x82\x028\x00\x00\x08\x00\x00\x08 \x1c\xc1>\xcb<\x9f}\x0e\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=100, y=90),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x16\x08\x10\x04\x00 \x00H0 \x00\xe0@`\x00\x00\n\x06\x04\x0c8\x08h\x18p\x10\x80 \xe0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=90),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x00\x1f\x00? ?\x00?\x00\x00\x00\x07\x00\x08\x00\x10\x00\x00\x00 \x00 \x00 \x00'),
                            bytearray(b'\x00\x00\xc0\x88\xd48\xe8\x1c\xec<\xd22\xc6\x00\xd3l\x00\x00\x98D \x04\x1c\x04\x1c\x022\x0c\x00>\x00?'),
                            bytearray(b'? \x0e\x10\x00\x0c\x00\x05\x00\x08\x06\x01\x07\x02\n\x04 \x00\x10!\r\x13\x1a\x1f\x0f\x0f\x01\x03\x03\x01\x04\x02'),
                            bytearray(b"\xb0\xc1(\xc7\xc6\'\x0e\xde>\xfe\xfe\xfe\xfc\xfc0\xd0\x8f\x7f\x17\xff\x1f\xff>\xfe\xfe\xfe\xfe\xfe\xfc\xfc\xf0\xf0"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=74),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'4\x84\xf6\x84D,L,\x88\\\x18\xb8\x98\x18\x10\xe0\x8e~\x8e~\x1e\xfe\x1c\xfc<\xfc|\xfcx\xf8\xf0\xf0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x01\x00\x04\x12\n"\x01x\x00\x00\x00\x00\x00\x00\x00\x01\x02\x07\x00\x0f\x11?\x07\x18x\x00\x00'),
                            bytearray(b'\x01\x15\x002\n\n\xc1\xe8\x83\x04\x0c\r\x00\x04\x00\x00\x1f\x002M\xbe}\xeco\x8c\x8f\x0e\x07\x06\x07\x01\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=94),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x10\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x08\x00'),
                            bytearray(b'\x07\x00\x0f\x00\x0f\x00\x07\x00\x10\x11\x00\x00\x00\r\x00\r\x00\x00\x00\x08\x08\x00\x08\x00\x1e\x00\x0f\x10\x0f\x10\x0f\x10'),
                            bytearray(b'\xf8\x00\xfc\x04\xfc\x08\xec0\x9e\xc0(#P\xc0\x00\x9c\x00\x00\x04\x00\x00\x04\x10\x0ea\x1f\xe5\x1f\xce>\x86~'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=78),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'(\x08\x10x0\xb80pp\xe0 \xc0\x00\x00\x00\x00\x18\xf88\xf8x\xf8\xf0\xf0\xf0\xf0\xe0\xe0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00G\x03\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00_??\x7f'),
                            None,
                            None,
                            bytearray(b' 72\x12\x18\x10\x17\x18\x10\x12\x03\x00\x00\x00\x00\x007\x18\x12=\x10?\x10?1?\x07\x07\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x07\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x08\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xd0 \xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x10\x00\x08\x00'),
                            bytearray(b'\x17\x00\x17\x03#\x02&\x00$\x00H\xc3`\xf3\xa8\x13\x1c\x00\x18\x03\x1c"\x19 ;\x00\xc78\xff\xf8\xd7\xf8'),
                            bytearray(b'\xfc\x00$p\x80\xa4($ \xe00\x88\xac\x98(\x0c\x04\x00\xdc\x0ch\x1c\xe0\x1cl\x1c\x8c|\x8c|\x1c\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=98),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'(\x08\x10x0\xb80pp\xe0 \xc0\x00\x00\x00\x00\x18\xf88\xf8x\xf8\xf0\xf0\xf0\xf0\xe0\xe0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=402, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00G\x03\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x00_??\x7f'),
                            None,
                            None,
                            bytearray(b' 72\x12\x18\x10\x17\x18\x10\x12\x03\x00\x00\x00\x00\x007\x18\x12=\x10?\x10?1?\x07\x07\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x07\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x08\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xd0 \xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x10\x00\x08\x00'),
                            bytearray(b'\x17\x00\x17\x03#\x02&\x00$\x00H\xc3`\xf3\xa8\x13\x1c\x00\x18\x03\x1c"\x19 ;\x00\xc78\xff\xf8\xd7\xf8'),
                            bytearray(b'\xfc\x00$p\x80\xa4($ \xe00\x88\xac\x98(\x0c\x04\x00\xdc\x0ch\x1c\xe0\x1cl\x1c\x8c|\x8c|\x1c\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=394, y=102),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'4\x84\xf6\x84D,L,\x88\\\x18\xb8\x98\x18\x10\xe0\x8e~\x8e~\x1e\xfe\x1c\xfc<\xfc|\xfcx\xf8\xf0\xf0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x01\x00\x04\x12\n"\x01x\x00\x00\x00\x00\x00\x00\x00\x01\x02\x07\x00\x0f\x11?\x07\x18x\x00\x00'),
                            bytearray(b'\x01\x15\x002\n\n\xc1\xe8\x83\x04\x0c\r\x00\x04\x00\x00\x1f\x002M\xbe}\xeco\x8c\x8f\x0e\x07\x06\x07\x01\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x10\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x08\x00'),
                            bytearray(b'\x07\x00\x0f\x00\x0f\x00\x07\x00\x10\x11\x00\x00\x00\r\x00\r\x00\x00\x00\x08\x08\x00\x08\x00\x1e\x00\x0f\x10\x0f\x10\x0f\x10'),
                            bytearray(b'\xf8\x00\xfc\x04\xfc\x08\xec0\x9e\xc0(#P\xc0\x00\x9c\x00\x00\x04\x00\x00\x04\x10\x0ea\x1f\xe5\x1f\xce>\x86~'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=100),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x16\x08\x10\x04\x00 \x00H0 \x00\xe0@`\x00\x00\n\x06\x04\x0c8\x08h\x18p\x10\x80 \xe0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x00\x1f\x00? ?\x00?\x00\x00\x00\x07\x00\x08\x00\x10\x00\x00\x00 \x00 \x00 \x00'),
                            bytearray(b'\x00\x00\xc0\x88\xd48\xe8\x1c\xec<\xd22\xc6\x00\xd3l\x00\x00\x98D \x04\x1c\x04\x1c\x022\x0c\x00>\x00?'),
                            bytearray(b'? \x0e\x10\x00\x0c\x00\x05\x00\x08\x06\x01\x07\x02\n\x04 \x00\x10!\r\x13\x1a\x1f\x0f\x0f\x01\x03\x03\x01\x04\x02'),
                            bytearray(b"\xb0\xc1(\xc7\xc6\'\x0e\xde>\xfe\xfe\xfe\xfc\xfc0\xd0\x8f\x7f\x17\xff\x1f\xff>\xfe\xfe\xfe\xfe\xfe\xfc\xfc\xf0\xf0"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=97),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x16\x08\x10\x04\x00 \x00H0 \x00\xe0@`\x00\x00\n\x06\x04\x0c8\x08h\x18p\x10\x80 \xe0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x00\x1f\x00? ?\x00?\x00\x00\x00\x07\x00\x08\x00\x10\x00\x00\x00 \x00 \x00 \x00'),
                            bytearray(b'\x00\x00\xc0\x88\xd48\xe8\x1c\xec<\xd22\xc6\x00\xd3l\x00\x00\x98D \x04\x1c\x04\x1c\x022\x0c\x00>\x00?'),
                            bytearray(b'? \x0e\x10\x00\x0c\x00\x05\x00\x08\x06\x01\x07\x02\n\x04 \x00\x10!\r\x13\x1a\x1f\x0f\x0f\x01\x03\x03\x01\x04\x02'),
                            bytearray(b"\xb0\xc1(\xc7\xc6\'\x0e\xde>\xfe\xfe\xfe\xfc\xfc0\xd0\x8f\x7f\x17\xff\x1f\xff>\xfe\xfe\xfe\xfe\xfe\xfc\xfc\xf0\xf0"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=96),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xc0\xe0\xe0 \xe0\x88D`\xdc\xfc*8\xf4\x12\xf8\xf5 \x00\x10\x00\x18\x00\x98\x04\x0c\x00\xda\x06\x10\x0f\x02\x0f'),
                            None,
                            bytearray(b'\x00\xf1\x02\xf0\x10\xf0\x08\xe40\xe8\xb8\x80\xd0 \xc0\x00\xf7\x0f\xf6\x0e\xf4\x0c\xe4\x1c\xe0\x18\x88x\x10\xf0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00'),
                            bytearray(b'\x03\x01\x03\x06\x0b\x00\x1f\r\x1f\x1b.\x0c\xeb\xe8\x17\x11\x02\x00\x04\x00\x0c\x00\x00\x10\x00\x001 \xf4\x00\xf8\x00'),
                            bytearray(b'\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xef#,\x07\x08\x0f\x18\x0f\x10\x0f\x0e\x06\x06\x00\x01\x000\xc03 \x17\x00\x07\x10\x1f\x10\x0e\t\x04\x07\x01\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x88p\xf04\xc02\xe6&\x0f\x1c7\xf0if\x00\x00\xf8\x00\x0c\x00\x0e\x00\x1e\x00\xfd\x03\xf1\x0f\xe1\x1f'),
                            None,
                            bytearray(b'\xa1\x92\x80b\x14\xc2\x10\xa6@6\x00\xf8\x00\xe0\x00\x80\x8f\x7f\x12\xfe*\xf6f\xfe\xfe\xfe\xf8\xf8\xe0\xe0\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x10\xa0@Hr\x14\x18\x00\x06\x02\x02\x00\x00\x00\x00\x00\xf0\x10x\x80\\b\x17\x18\x03\x04\x02\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x8f\x07\r9\xb7\xa7\xfe\x06\xff\x03\x00\x00\x00\x00\x00\x00\x08\x80\xf2\x00\xc8\x00\x81\x80\x81\x00'),
                            bytearray(b'\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfe\xc2\xfc\xf0\xfc\xfd\xfe\xfe\xff~>\x7f]?\x10\x07\x03\x00\x00\x03\x00\x03\x03\x01\x83\x01C\x01gC\x03\x1f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=116),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x05\x05\x10\x11\xc0\x04\xa0\x90\x80@\x00\x00\x00\x00\x01\x00\x07\x00\x1f\x03<\xcc\xd00\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x17\x07\x1707p\xbf>\x9f\x1c\x0e\x8f\xc7\xc5fg\x18\x00\x08\x00H\x00\xc0\x00\xe0\x00\xf0\x00\xf8\x01|\x80'),
                            bytearray(b'\xc0\x00\xf0 \x90\x98\xe0\xfc\xdc\xdcz\xacq\xde\xf0\xcf\xc0\x00\x00\x10h\x00\x00\x04 \x08\x00\x06\x07\x0f\x0f\x1f'),
                            bytearray(b'\xc3C\x88\x08wG\x00\xf8\x08\x86\x01\x02\x00\x00\x00\x00\xff\x80o\x90\xd78p\xff\x89\x8f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'@\xaf`\x1f\xc0\xde\x00\xfe\x80<\x008\x000\x00\x00\xbf\x1f\x9f?>>\xfe><\xfc\xf8\xf800\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=106),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x88p\xf04\xc02\xe6&\x0f\x1c7\xf0if\x00\x00\xf8\x00\x0c\x00\x0e\x00\x1e\x00\xfd\x03\xf1\x0f\xe1\x1f'),
                            None,
                            bytearray(b'\xa1\x92\x80b\x14\xc2\x10\xa6@6\x00\xf8\x00\xe0\x00\x80\x8f\x7f\x12\xfe*\xf6f\xfe\xfe\xfe\xf8\xf8\xe0\xe0\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=400, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x10\xa0@Hr\x14\x18\x00\x06\x02\x02\x00\x00\x00\x00\x00\xf0\x10x\x80\\b\x17\x18\x03\x04\x02\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x8f\x07\r9\xb7\xa7\xfe\x06\xff\x03\x00\x00\x00\x00\x00\x00\x08\x80\xf2\x00\xc8\x00\x81\x80\x81\x00'),
                            bytearray(b'\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfe\xc2\xfc\xf0\xfc\xfd\xfe\xfe\xff~>\x7f]?\x10\x07\x03\x00\x00\x03\x00\x03\x03\x01\x83\x01C\x01gC\x03\x1f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=122),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x02\x02\x02\x02\x02\x1a\x06g \xf74\xff7\xe3\x1f\x03\x00\x03\x00\x03\x00\x1b\x1cX\x00\x88\x80\x80\x00\x80\x00'),
                            bytearray(b'\x00\x80\x80\x00\x00\x00\x00\xe0\xdcP\xee8\xe6\xf8\xfe\xf8\x00\x80\x00\x80\x00\x80\x80`$\x08\x02\x00\x02\x00\x18\x02'),
                            bytearray(b'\xe3\x1f\xec<\xd0\x10\xdf\x1f\xf8x\xc0@\x0fp\x10(\x80\x00\x83\x80\xaf\x80\xbf\x80\xb8\x87\xc0\xbf\x00\x7f??'),
                            bytearray(b'\xcc\xcev\xf4ZD\x8e\x84D\x12x\x02\xc0|\x00p8\x02\xf2\n\xc6:\x86z\n\xfe^\xfe|\xfc\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=125),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x02\x02\x02\x02\x02\x1a\x06g \xf74\xff7\xe3\x1f\x03\x00\x03\x00\x03\x00\x1b\x1cX\x00\x88\x80\x80\x00\x80\x00'),
                            bytearray(b'\x00\x80\x80\x00\x00\x00\x00\xe0\xdcP\xee8\xe6\xf8\xfe\xf8\x00\x80\x00\x80\x00\x80\x80`$\x08\x02\x00\x02\x00\x18\x02'),
                            bytearray(b'\xe3\x1f\xec<\xd0\x10\xdf\x1f\xf8x\xc0@\x0fp\x10(\x80\x00\x83\x80\xaf\x80\xbf\x80\xb8\x87\xc0\xbf\x00\x7f??'),
                            bytearray(b'\xcc\xcev\xf4ZD\x8e\x84D\x12x\x02\xc0|\x00p8\x02\xf2\n\xc6:\x86z\n\xfe^\xfe|\xfc\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=126),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x18\x07g \xf74\xff7\xe3\x1f\xe3\x1f\xec<\xd0\x10\x1c\x10X\x00\x88\x80\x80\x00\x80\x00\x80\x00\x83\x80\xaf\x80'),
                            bytearray(b'\x00\xe0\xdcP\xee8\xe6\xf8\xfe\xf8\xcc\xcev\xf4ZD`\x00$\x08\x02\x00\x02\x00\x18\x028\x02\xf2\n\xc6:'),
                            bytearray(b'\xde\x1e\xff\x7f\xc2B\x0er\x12*\x02\x06\x00\x02\x00\x02\xbf\x80\xbe\x80\xc3\xbc\x03|?<\x07\x04\x03\x00\x03\x00'),
                            bytearray(b'ndD\x12x\x02@|\x00p\x80\x00\x00\x80\x00\x80\xe6\x1a\n\xfe^\xfe|\xfcp\xf0\x00\x80\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=99),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x18\x07g \xf74\xff7\xe3\x1f\xe3\x1f\xec<\xd0\x10\x1c\x10X\x00\x88\x80\x80\x00\x80\x00\x80\x00\x83\x80\xaf\x80'),
                            bytearray(b'\x00\xe0\xdcP\xee8\xe6\xf8\xfe\xf8\xcc\xcev\xf4ZD`\x00$\x08\x02\x00\x02\x00\x18\x028\x02\xf2\n\xc6:'),
                            bytearray(b'\xde\x1e\xff\x7f\xc2B\x0er\x12*\x02\x06\x00\x02\x00\x02\xbf\x80\xbe\x80\xc3\xbc\x03|?<\x07\x04\x03\x00\x03\x00'),
                            bytearray(b'ndD\x12x\x02@|\x00p\x80\x00\x00\x80\x00\x80\xe6\x1a\n\xfe^\xfe|\xfcp\xf0\x00\x80\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=99),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x18\x07g \xf74\xff7\xe3\x1f\xe3\x1f\xec<\xd0\x10\x1c\x10X\x00\x88\x80\x80\x00\x80\x00\x80\x00\x83\x80\xaf\x80'),
                            bytearray(b'\x00\xe0\xdcP\xee8\xe6\xf8\xfe\xf8\xcc\xcev\xf4ZD`\x00$\x08\x02\x00\x02\x00\x18\x028\x02\xf2\n\xc6:'),
                            bytearray(b'\xde\x1e\xff\x7f\xc2B\x0er\x12*\x02\x06\x00\x02\x00\x02\xbf\x80\xbe\x80\xc3\xbc\x03|?<\x07\x04\x03\x00\x03\x00'),
                            bytearray(b'ndD\x12x\x02@|\x00p\x80\x00\x00\x80\x00\x80\xe6\x1a\n\xfe^\xfe|\xfcp\xf0\x00\x80\x00\x80\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=99),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00`\x00\x18\x00\xe6 9\x08\x01\x04\x00\x00\x00\x00\x80\x80\xa0`\xe8\x18\xb8\xc6.1\x01\x07'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x05\x02\x03\n\x0e*~\x18\x7f\x01\x7f\x83\xfe\xf1\x01\x00\x00\x04\x0c\x001\x00A\x00\x00\x00\x80\x00\x01\x00'),
                            bytearray(b'\x14\xf8\xd6P\xeb\x1e\xea\xdf:;\xeb\xe8\xf2\xf1\xe0\xe4\xe4\x00*\x00\x05\x00\x07\x00\xc7\x00\x18\x070\x0f\xe3\x1f'),
                            bytearray(b'\xff\xf1\xff\xf9~\xff~\xfe>\x7f\x1e=\x1c\x03\x00\x00\x01\x00\x01\x00\x80\x01\x01\x81A\x01!\x03\x17\x1f\x00\x00'),
                            bytearray(b'\xf4\xc9\x07\x00!\x80F2\x80q\x00\xe0\x00\x00\x00\x00\xcb7h\xf7n\xf1\xfb\xfc\xf0\xf1\xe0\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=102, y=106),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00`\x00\x18\x00\xe6 9\x08\x01\x04\x00\x00\x00\x00\x80\x80\xa0`\xe8\x18\xb8\xc6.1\x01\x07'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x05\x02\x03\n\x0e*~\x18\x7f\x01\x7f\x83\xfe\xf1\x01\x00\x00\x04\x0c\x001\x00A\x00\x00\x00\x80\x00\x01\x00'),
                            bytearray(b'\x14\xf8\xd6P\xeb\x1e\xea\xdf:;\xeb\xe8\xf2\xf1\xe0\xe4\xe4\x00*\x00\x05\x00\x07\x00\xc7\x00\x18\x070\x0f\xe3\x1f'),
                            bytearray(b'\xff\xf1\xff\xf9~\xff~\xfe>\x7f\x1e=\x1c\x03\x00\x00\x01\x00\x01\x00\x80\x01\x01\x81A\x01!\x03\x17\x1f\x00\x00'),
                            bytearray(b'\xf4\xc9\x07\x00!\x80F2\x80q\x00\xe0\x00\x00\x00\x00\xcb7h\xf7n\xf1\xfb\xfc\xf0\xf1\xe0\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=357, y=107),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00`\x00\x18\x00\xe6 9\x08\x01\x04\x00\x00\x00\x00\x80\x80\xa0`\xe8\x18\xb8\xc6.1\x01\x07'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x05\x02\x03\n\x0e*~\x18\x7f\x01\x7f\x83\xfe\xf1\x01\x00\x00\x04\x0c\x001\x00A\x00\x00\x00\x80\x00\x01\x00'),
                            bytearray(b'\x14\xf8\xd6P\xeb\x1e\xea\xdf:;\xeb\xe8\xf2\xf1\xe0\xe4\xe4\x00*\x00\x05\x00\x07\x00\xc7\x00\x18\x070\x0f\xe3\x1f'),
                            bytearray(b'\xff\xf1\xff\xf9~\xff~\xfe>\x7f\x1e=\x1c\x03\x00\x00\x01\x00\x01\x00\x80\x01\x01\x81A\x01!\x03\x17\x1f\x00\x00'),
                            bytearray(b'\xf4\xc9\x07\x00!\x80F2\x80q\x00\xe0\x00\x00\x00\x00\xcb7h\xf7n\xf1\xfb\xfc\xf0\xf1\xe0\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=356, y=108),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=10, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=8, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=4, mold_id=23),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL531_HAMMER_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
