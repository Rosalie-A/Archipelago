# SPR0791_ICE_ROCK

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL304_ICE_ROCK
sprite = CompleteSprite(
    animation=AnimationPack(171, length=464, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xecC\x8d\x98\xe3\xf8B\xbd\t\xb3X"\x10,\x10h#\x9cf\x81\x06\x81B\x81D\x83@\x87\x08D\x10H'),
                            bytearray(b'\x0e\xd2\xb8\x04\xf4\x8c\x90\xc8\xc0\xb0\x00\x00\x00\x00\x00\x00\xc1?\x00\xfc\x00\xfcP\xa8\x00\xf0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=132),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0c\x17\x0e\x17\x1f\x1f\x0f\x0f\x07\x0f\x01\x01\x01\x01\x00\x00\x10\x0f\x10\x0f\x00\x1f\x00\x0f\x00\x0f\x02\x03\x00\x01\x00\x00'),
                            bytearray(b'B]\x03\x98\xd2\x8d\xc3\xbc\xc0\xf2\xff\xc8\xe7\xc8]b-\xf2)\xf6\x19\xe60\xcf0\xcf\x00\xff\x00\xff\x00\x7f'),
                            None,
                            bytearray(b'>\x11,1(405\x04\x06\x00\x01\x00\x00\x00\x00\x00/\x00\x0f \x0f0\x0f\x00\x07\x00\x03\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x88\xa8\xf4x6z6\xfe8|X\xfcX|\x08\xb8\x80x\xe8\x14\xa0^\x80~\x00\xfc\x00\xfc\x00\xfc@\xfc'),
                            None,
                            bytearray(b'\xa0\xb0 0@@\x00\x10\x00\x10``@@\x00\x00H\xf8\xc8\xf8\xb0\xf0\xe0\xf0\xe0\xf0\x80\xe0\x80\xc0\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xef\x10;\x00\xf7\xf0\xff`\x9f`\xbf`\x7f\x00\xf9\x01\xfe\x00\xf8\x04\x08\x00\x80\x00\x80\x00\x80\x00\x80\x00\x86\x00'),
                            bytearray(b'\xc1=\xe1\x1e\xe6\x19\xdc#\xe0\x1f\xda \x16( \x1e?\x00>\x019\x06#\x1c\x1f  \x1f\xea\x15\xfe\x01'),
                            bytearray(b'P\x94\xb1\x00o\x10?@\xa7H\xaaG\xfd\x03\xe9V\xeb\x00\xbf@\xff\x00\x7f\x80\x0f\xf0\x04\xf8\x02\xfc?\x80'),
                            bytearray(b'\x0c\x13\xce\x11\x8b\x15\xdf\x01\xfe\x00N0\xce\xb0\x0e\xe2\xf2\r\xf0\x0f\xf0\x0f\xf0\x0f\xf1\x0f\xf1\x0fa\x1fA?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x07\x00\x01\x06\x06\x07\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x07\x01\x06'),
                            None,
                            bytearray(b'\x05\x02\x1d\x02=\x00\x078\r"5"\t\x15\x10\x08\x02\x04\x06\x00\x06\x00\x0c0\x048\x00?\x00\x1f\x00\x1f'),
                            bytearray(b'\xbfP\xf3\n\xfd\x03\xfd\x02\xcdr\x9ad\xa9\x96\xc2\xfc\x1f\x00\x05\x00\x00\x00\x01\x00\x0f\x00g\x98\xb7H?\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xc0\xc0\x00\xcc\x00\xfe\x01\xff\x01\xfd\x07\xfbO\xef\x7f\x00\x000\x000\x02\x00\x01\x00\x01\x05\x02\n\x05d\x1b'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x80\xc0\x80\xc0\x00 \x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xc0 \xe0\xc0\xe0'),
                            bytearray(b"\xe5\xff\xc9\xff\xa6~\xdc\\-\xdd\xb4^\xc5,\xe0\x1f\xe4\x1b\xc87\xe5\x1b\x9b\'\xfb\x06\xe0\x0f\xfd\x02\x18!"),
                            bytearray(b'\x00\x00\x00\x00\x1008 (\x98X\xf8\xb8x\xd8\xf8\xe0\xe0\xe0\xe0\xc0\xf0\xe0\xc0\x08\xd0\x88p\x80x\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'),
                            bytearray(b'\x01\x00\x1b\x00;\x02{\x04\xfb\x04\xff\x00\xff\x00\xff\x00\x00\x00\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'?<+ \xe0\x1c\xec\x10\xd0,\xc81\x98\xf4\x7f\x908\x00\x10\x04\x0c\x13\x0c\x13\x1c\x03\t\x06\x1e\x01\x1f\x00'),
                            bytearray(b'\xfd\x00{\x86cu\x1ea\x0fHn!\x98\x07T\xa3\x02\x00\x02\x00\x16\x88\x7f\x80w\x80_\x80\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=114),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xd0\x10\xc0\x08\xd0\x10\xc0@\x80\x00\x00\x80\x00\x00\x00\x00(\xf80\xf8 \xf0 \xe0\x00\x80\x00\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'>9\x1c>\x0c\r\x07\x04\x01\x02\x02\x02\x00\x00\x00\x00\x03<\x02=\x00\x0f\x00\x07\x00\x01\x02\x01\x00\x00\x00\x00'),
                            bytearray(b'\xac\x10o\x80\xfe\x05d\x9bMP\x00~\x10 \x10(\x7f\x80\x0f\xf0\x03\xf8>\xc1(\xc7\x02\xc5\x00\xcc\x00\x08'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\xd00\xa0p\xc0\xc0\x80\xc0P\xd0H\xc8\x00\x00\x00@\x000\x00p0\xf0\xb0p \xf00\xf8'),
                            None,
                            bytearray(b'\x80\xa8(\x98 \xa0<\xd8\x8c|\xd8<\x00\xe8\xa0h\xc0x\xa0X\xe0\x18\xf0\x0c`\x9c\x00\xfc\xd0<P\xb8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x03\x02\x01\x00\x02\x02\x0c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x03\x01\x02'),
                            bytearray(b'\x04\x026\x00w\x08\xff\x00\xff\x03\xb6K\xd5I%?\x00\x00\x01\x08\x00\x00\x00\x00\x03\x00\x02\x01\x1d\xe2\x1b\xc0'),
                            bytearray(b"\x1e\x01\x13\x1e\x1b\x06>\x01\x1f`[D\x04\'4\x1f\x03\x00\x03\x18\x03\x10\x10\x000@\x04{\x03<\x01>"),
                            bytearray(b'\r\x02R\r\xee\x11\xb7\x80~\xa1\xfe!\xf5\x04\x90X?\xc0\xff\x00\xf9\x00q\x08A\x00\xc1\x00\xcb\x00g\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x07\x00\x01\x06\x06\x07\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x07\x01\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xc0\xc0\x00\xcc\x00\xfe\x01\xff\x01\xfd\x07\xfbO\xef\x7f\x00\x000\x000\x02\x00\x01\x00\x01\x05\x02\n\x05d\x1b'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x80\xc0\x80\xc0\x00 \x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xc0 \xe0\xc0\xe0'),
                            bytearray(b"\xe5\xff\xc9\xff\xa6~\xdc\\-\xdd\xb4^\xc5,\xe0\x1f\xe4\x1b\xc87\xe5\x1b\x9b\'\xfb\x06\xe0\x0f\xfd\x02\x18!"),
                            bytearray(b'\x00\x00\x00\x00\x1008 (\x98X\xf8\xb8x\xd8\xf8\xe0\xe0\xe0\xe0\xc0\xf0\xe0\xc0\x08\xd0\x88p\x80x\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'),
                            bytearray(b'\x01\x00\x1b\x00;\x02{\x04\xfb\x04\xff\x00\xff\x00\xff\x00\x00\x00\x00\x04\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'?<+ \xe0\x1c\xec\x10\xd0,\xc81\x98\xf4\x7f\x908\x00\x10\x04\x0c\x13\x0c\x13\x1c\x03\t\x06\x1e\x01\x1f\x00'),
                            bytearray(b'\xfd\x00{\x86cu\x1ea\x0fHn!\x98\x07T\xa3\x02\x00\x02\x00\x16\x88\x7f\x80w\x80_\x80\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=102),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=106),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=116),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=115),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=378),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=372),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=120),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=114),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=102),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=100),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=106, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=111),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=112),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=98),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=98),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=96),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xd0\x10\xc0\x08\xd0\x10\xc0@\x80\x00\x00\x80\x00\x00\x00\x00(\xf80\xf8 \xf0 \xe0\x00\x80\x00\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'>9\x1c>\x0c\r\x07\x04\x01\x02\x02\x02\x00\x00\x00\x00\x03<\x02=\x00\x0f\x00\x07\x00\x01\x02\x01\x00\x00\x00\x00'),
                            bytearray(b'\xac\x10o\x80\xfe\x05d\x9bMP\x00~\x10 \x10(\x7f\x80\x0f\xf0\x03\xf8>\xc1(\xc7\x02\xc5\x00\xcc\x00\x08'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\xd00\xa0p\xc0\xc0\x80\xc0P\xd0H\xc8\x00\x00\x00@\x000\x00p0\xf0\xb0p \xf00\xf8'),
                            None,
                            bytearray(b'\x80\xa8(\x98 \xa0<\xd8\x8c|\xd8<\x00\xe8\xa0h\xc0x\xa0X\xe0\x18\xf0\x0c`\x9c\x00\xfc\xd0<P\xb8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x03\x02\x01\x00\x02\x02\x0c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00\x00\x03\x01\x02'),
                            bytearray(b'\x04\x026\x00w\x08\xff\x00\xff\x03\xb6K\xd5I%?\x00\x00\x01\x08\x00\x00\x00\x00\x03\x00\x02\x01\x1d\xe2\x1b\xc0'),
                            bytearray(b"\x1e\x01\x13\x1e\x1b\x06>\x01\x1f`[D\x04\'4\x1f\x03\x00\x03\x18\x03\x10\x10\x000@\x04{\x03<\x01>"),
                            bytearray(b'\r\x02R\r\xee\x11\xb7\x80~\xa1\xfe!\xf5\x04\x90X?\xc0\xff\x00\xf9\x00q\x08A\x00\xc1\x00\xcb\x00g\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=113),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=134),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=128),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=134),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=111),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=130),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=130),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=136),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=111),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=138),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x00\x1f\x00\x1e\x01\x1f\x01\t\x00\x11\x12?\x00\x00\x00\x02\x00\x00\x00\x00\x01\x03\x003\x0c\x06\x18\x1f\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x800\xb0\xc8h\xb8x\x08\xf8\xb0X\x00\x00\x00\x80\xc0@@\xf0\xc08\xe0\x18\xe0\x18@8'),
                            bytearray(b'/\x14>\x02\x13\x0c\x1f\x18\r\x0c\x04\x06\x00\x00\x00\x00\x02 %\x00\t\x16\x05\x1a\x00\x0f\x00\x05\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xd0\x80P\xa0\xf0\x08\x00` \xc0\x00\x00\x00\x00L<l\x1c\xe8\x18\x00\xf8\x800\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x18\x040\x08>.8<\x18\x0800\x00\x02\x00\x00\x00\x04\x00\x06\x10.#\x0f\x16\x0e\x000\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=138),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=111),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=119),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00A\x00\x08\x00\x10\x08\x18\x18\x08\x00\x80\x01\x00\x00\x00\x00A\x00\x08\x00\x00\x00\x10\x08\x00\x08\x00\x81\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=139),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL304_ICE_ROCK,
    palette_offset=0,
    unknown_num=8
)
