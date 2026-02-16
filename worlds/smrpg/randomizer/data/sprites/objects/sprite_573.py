# SPR0573_MOKURA

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL389_MOKURA
sprite = CompleteSprite(
    animation=AnimationPack(224, length=189, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=4096,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x7f\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=144),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x99\xfa\x1c\x07}\x054\x07\x1c\x04\x05\x01\x00\x00\x00\x00\x04\xfex|~x?8\x18\x1f\x06\x07\x00\x00\x00\x00'),
                            bytearray(b'\xaeX\xf3p><\xfc@p \x00\x00\x00\x00\x00\x00G?/\x1f\xe2\x1e\xdc<\x10\xf0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=144),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xfcG\x9f/\xdct\xf2)\xfd@\xa7\r\xc2\xdf \xff\xfc\x9f\xf8\xce\xf1\x80\xfd3\xc4\t\xf6\x10\xff\x10\xff'),
                            bytearray(b'\x1c\xf0\xdc4\x1cx\xec(\x9c\xcc\xe8\xd0\xfc\xf8`\x10\x8c\x04\xc8\x04\xc8\x04\xd8\x04\xf8\x04\xf4\x0c\xf4\x0c\x88x'),
                            bytearray(b'\xfac\xda\x01\xa8En\x03\xcfQ\xae`W\xc0\x7f\x00T\xbf>\xff:\xffl\xff.\xff\x1f\xff?\xff\xff\xff'),
                            bytearray(b'8\xf0\xd8\x18H\xb8`\xc0\x18\xa0p\xf0\xe0\xe0\xc0\x00\x08\xf80\xc8\x18\xc0x\x888\xc8`\x90\x00\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x80\xff\x80\xff\xa0\x7f\xfcG\x08C\xe3H\xf8_\xb7\xe7\xfd?\xbf?\xbf\x1f\x833\xc73\xd4 \xc0 \xf8\x00'),
                            bytearray(b'\x12\xfd\x00\xff\x00\xff\x00\xffF\xff\x8d\x0e\xfat\xe4\xfa\xcf\xcd\xff\xff\xff\xff\xff\xf9\xfe\xb9\x00\xff\x87xK\x04'),
                            bytearray(b'\xee\xf0\xf8?\xe8%\xbfI.\xd9\xce\xde\xff\x01\xf9\xfb\xff\x00\x7f\x00\x10\x03\x11\x00\x00\x00!\x00\xff\x00\xf9\x06'),
                            bytearray(b'\xf3e\xf7s7\x13\xe6\x13\xef\xd1\xdf\xd9\x8c\x07?\xc5\x97\x08\x97\x08\xff\x00\xde!\xde!\xde!\x04\xfb\x02\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xe7\x7f]\x1d0\x1c]6?>\xfe?\xbf\xba\xbd\xba\x80\xffb\x7f#?Tk|C\xbc\xc38\xc78\xc7'),
                            bytearray(b'7\x87s\xaf\x7fj\xbb\xb2}~}h{$\x9f\xd13\xcc\x0c\xc3\xaf\xc0\xa5Hy\x80k\x90#\xd8\x97h'),
                            bytearray(b'\xb9:\xc1#|<\x7f\x00\x1f\x10\x0f\x00\x0f\x00\x00\x00\xf8\xc7\xc1\xfeB\x7f\x7f\x7f/?\x1f\x1f\x0f\x0f\x00\x00'),
                            bytearray(b'\xb4v7>\xbf\xc0uN\xbb\x03\xceDZC=\n7\xc8\xf6\xc8\x00\xfc\x0c\xf0@\xfc\xa7\xf8#|1?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xf0`\xc8\xb8\xb4\x0c\xd6l\xd8d\x00\x00\x00\x00\x00\x00\x90\x10\x00\x00@\x00\x02\x02\x02\x00'),
                            None,
                            bytearray(b'\xf8LY\xba<\xad\xb0M\xa1_\xa1^\x00\xdf\x03\xfd\x02\x00\x87\x81\xd4\x83<\x0f?\x1e?\x1e\xba\x9c\xfa\xfc'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x80 \xc0 \xa0px\x00\x00\x00\x00\x00\x00\x00\x00\xc0@ \x00P\x00\x80\x08'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x05\x02>\x18\xb9Y\xe5\xbfg\xba\xfb;\\\x8bl\xdb\x04\x076!\xa7\xc0\xc0\x01\xc9\x01\xcf\x00{\x04{\x04'),
                            bytearray(b'\xc0\x00p\x80\x18\xc0-\xe0\xa2o\xe3\xfe\xef\xfe\xfb\x12\xc0\xc0p\xf08\xf8\x1d\xfd\x92|\x80|\x04\xf8\xa4\xf8'),
                            bytearray(b'q_\x1b\xder\xbf|\x99t\x8b\xf8\x87\xd2\xfd\x80\x1e\xf9\x06:\x05\x18\x07\x1b\x07\x11\x0f\x10\x0f\x18\x0f\xfc\x1f'),
                            bytearray(b'\xaa\x97\xf4Gx\xc3\x16\xf9=\xdam\xc4\xed\x14n\x11E\xf9\x1f\xa3\x97\xe3\xe1\xc1\xc0\xc0\x92\x80\x82\x00\x83\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x04\x07'),
                            bytearray(b'\x00\x00\x0e\x007\x17|/7$\xf9$\xef\xf2\x96[\x00\x00\x0e\x0e,1t@|@\xbe\xc0\xee\x00\xe6\x00'),
                            bytearray(b'J\x07\xd4\x06\xbf\x80\xed\xe0\xee\xa3\xba\x93\x01\r\x84fKL\xdd\xdaq\xfe\x11\xfe\x03\xfc\x13\xec\x81\xfe\x80\xff'),
                            bytearray(b'\x85+Np\xbc\xe2A{<;\xdc\x11\xba\xc4\xfc\xff\xd2\x00\x89\x00\t\x00\x84\x00\xc4\x00\xee\x00\xff\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x1c\x1c6>Zfzf\xe6~\xbe>\xc1\x00\x07\x00\x03\x00\x01\x00\x01\x00\x01\x00\x81\x00\xc1\x00\xff\x00'),
                            bytearray(b' \xe0\x90pT0T2T2U3\xd73\xb6r\xe0\x00\xf0\x08\xf0\x0c\xf0\x0e\xf0\x0e\xf0\x0f\xf0\x0f\xf1\x0f'),
                            bytearray(b'c\x80\x18\xe7\xc1\xff\x1e\x1ew\x00\x00?\x1f\x1f\x00\x00\xff\x00\xff\x00\xff\x00\x1ea\x00\x7f\x00?\x00\x1f\x07\x07'),
                            bytearray(b'j\xe6\xd5\xcc\xa9\x98\xd20f\xe0\xcc\xc08\x00\xe0\x00\xe1\x1f\xc3?\x87\x7f\x0e\xfe\x1e\xfe<\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x06\x06\n\x0e\x1c\x1a:\x1e1\x00\x00\x00\x00\x00\x03\x00\t\x00\x11\x00\x01\x00!\x00?\x00'),
                            bytearray(b'\x00\x00\x00\x00@\xc0\xa0`(h h$l\xe8h\x00\x00\x00\x00\xc0\x00\xe0\x10\xe0\x18\xe0\x18\xe0\x1c\xe4\x1c'),
                            bytearray(b'\x19 1?\x06\x06\x1b\x00\x0f\x0f\x00\x00\x00\x00\x00\x00?\x00?\x00\x06\x19\x00\x1f\x00\x0f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'X\xc8\xd4\xb0\xa8`H\xc0p\x00\xc0\x00\x00\x00\x00\x00\xc4<\x8c|\x18\xf88\xf8\xf0\xf0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x104pT|p\\\x12B~<<\x00\x00\x00\x00\x0c\x00\x0c\x02\x08\x060N\x00~\x00<\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x18\x0c<08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x04\x14,\x18\x18\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x18\x10\x18\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x08\x08\x18\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xfac\xda\x01\xa8En\x03\xcfQ\xae`W\xc0\x7f\x00T\xbf>\xff:\xffl\xff.\xff\x1f\xff?\xff\xff\xff'),
                            bytearray(b'8\xf0\xd8\x18H\xb8`\xc0\x18\xa0p\xf0\xe0\xe0\xc0\x00\x08\xf80\xc8\x18\xc0x\x888\xc8`\x90\x00\xe0\xc0\xc0'),
                            bytearray(b'\x7f\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=135),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xee\xf0\xf8?\xe8%\xbfI.\xd9\xce\xde\xff\x01\xf9\xfb\xff\x00\x7f\x00\x10\x03\x11\x00\x00\x00!\x00\xff\x00\xf9\x06'),
                            bytearray(b'\xf3e\xf7s7\x13\xe6\x13\xef\xd1\xdf\xd9\x8c\x07?\xc5\x97\x08\x97\x08\xff\x00\xde!\xde!\xde!\x04\xfb\x02\x7f'),
                            bytearray(b'\x99\xfa\x1c\x07}\x054\x07\x1c\x04\x05\x01\x00\x00\x00\x00\x04\xfex|~x?8\x18\x1f\x06\x07\x00\x00\x00\x00'),
                            bytearray(b'\xaeX\xf3p><\xfc@p \x00\x00\x00\x00\x00\x00G?/\x1f\xe2\x1e\xdc<\x10\xf0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=135),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xb9:\xc1#|<\x7f\x00\x1f\x10\x0f\x00\x0f\x00\x00\x00\xf8\xc7\xc1\xfeB\x7f\x7f\x7f/?\x1f\x1f\x0f\x0f\x00\x00'),
                            bytearray(b'\xb4v7>\xbf\xc0uN\xbb\x03\xceDZC=\n7\xc8\xf6\xc8\x00\xfc\x0c\xf0@\xfc\xa7\xf8#|1?'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=105, y=135),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x80 \xc0 \xa0px\x00\x00\x00\x00\x00\x00\x00\x00\xc0@ \x00P\x00\x80\x08'),
                            None,
                            bytearray(b'\x1c\xf0\xdc4\x1cx\xec(\x9c\xcc\xe8\xd0\xfc\xf8`\x10\x8c\x04\xc8\x04\xc8\x04\xd8\x04\xf8\x04\xf4\x0c\xf4\x0c\x88x'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xf8LY\xba<\xad\xb0M\xa1_\xa1^\x00\xdf\x03\xfd\x02\x00\x87\x81\xd4\x83<\x0f?\x1e?\x1e\xba\x9c\xfa\xfc'),
                            None,
                            bytearray(b'\x00\xfcG\x9f/\xdct\xf2)\xfd@\xa7\r\xc2\xdf \xff\xfc\x9f\xf8\xce\xf1\x80\xfd3\xc4\t\xf6\x10\xff\x10\xff'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'q_\x1b\xder\xbf|\x99t\x8b\xf8\x87\xd2\xfd\x80\x1e\xf9\x06:\x05\x18\x07\x1b\x07\x11\x0f\x10\x0f\x18\x0f\xfc\x1f'),
                            bytearray(b'\xaa\x97\xf4Gx\xc3\x16\xf9=\xdam\xc4\xed\x14n\x11E\xf9\x1f\xa3\x97\xe3\xe1\xc1\xc0\xc0\x92\x80\x82\x00\x83\x01'),
                            bytearray(b'\x80\xff\x80\xff\xa0\x7f\xfcG\x08C\xe3H\xf8_\xb7\xe7\xfd?\xbf?\xbf\x1f\x833\xc73\xd4 \xc0 \xf8\x00'),
                            bytearray(b'\x12\xfd\x00\xff\x00\xff\x00\xffF\xff\x8d\x0e\xfat\xe4\xfa\xcf\xcd\xff\xff\xff\xff\xff\xf9\xfe\xb9\x00\xff\x87xK\x04'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'J\x07\xd4\x06\xbf\x80\xed\xe0\xee\xa3\xba\x93\x01\r\x84fKL\xdd\xdaq\xfe\x11\xfe\x03\xfc\x13\xec\x81\xfe\x80\xff'),
                            bytearray(b'\x85+Np\xbc\xe2A{<;\xdc\x11\xba\xc4\xfc\xff\xd2\x00\x89\x00\t\x00\x84\x00\xc4\x00\xee\x00\xff\x00\xff\x00'),
                            bytearray(b'\xe7\x7f]\x1d0\x1c]6?>\xfe?\xbf\xba\xbd\xba\x80\xffb\x7f#?Tk|C\xbc\xc38\xc78\xc7'),
                            bytearray(b'7\x87s\xaf\x7fj\xbb\xb2}~}h{$\x9f\xd13\xcc\x0c\xc3\xaf\xc0\xa5Hy\x80k\x90#\xd8\x97h'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=105, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xf0`\xc8\xb8\xb4\x0c\xd6l\xd8d\x00\x00\x00\x00\x00\x00\x90\x10\x00\x00@\x00\x02\x02\x02\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x05\x02>\x18\xb9Y\xe5\xbfg\xba\xfb;\\\x8bl\xdb\x04\x076!\xa7\xc0\xc0\x01\xc9\x01\xcf\x00{\x04{\x04'),
                            bytearray(b'\xc0\x00p\x80\x18\xc0-\xe0\xa2o\xe3\xfe\xef\xfe\xfb\x12\xc0\xc0p\xf08\xf8\x1d\xfd\x92|\x80|\x04\xf8\xa4\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x04\x07'),
                            bytearray(b'\x00\x00\x0e\x007\x17|/7$\xf9$\xef\xf2\x96[\x00\x00\x0e\x0e,1t@|@\xbe\xc0\xee\x00\xe6\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=105, y=113),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL389_MOKURA,
    palette_offset=0,
    unknown_num=8
)
