# SPR0188_CANNON_BALL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL482_J_PUZZLE_BLOCK
sprite = CompleteSprite(
    animation=AnimationPack(412, length=97, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x01\x0b\x02\x1c\x17\x02\x11&7\x00\x00\x00\x00\x00\x01\x01\x06\x03\x0c\x07\x18\x03\x1c\x078'),
                            bytearray(b'\x00\x00d\x00\xcd\xc9h\xb8\x0c\xe5\xa14\x02NTN\x00\x00\x00|\xc87\xfc\x03\xdd\x02\xdc\x03\xfe\x01\xbe\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa0 \xf0  \x00h \x00\x00\x00\x00\x00\x00@\xc0\x00\xe0\x10\xf0\x10\xf0\x18\xf8'),
                            None,
                            bytearray(b'2#Y\x01J\x10\x14\\\x0bH\x1eI5\x16\x05%\x03<a~`\x7fd{p\x7fp\x7f(?:?'),
                            bytearray(b"\x8f\'^\xa6\xab\xfaKH\x1e\x01v\xc2\xfc\xb4l.\xdf\x00\xfe\x01\xfa\x05H\xb7\x00\xff\x01\xff\x03\xff\x91\xff"),
                            bytearray(b'@\x00dd\xd4@\xe8\xa4\xa8\xb4\xc0\xdc\xf0\x98\xb0\x188\xf8\x1c\xfc<\xfc\x1c\xfc\\\xfc<\xfcx\xf8\xf8\xf8'),
                            None,
                            bytearray(b'\n\x10\x15\x18\x0f\r\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x1f\x1f\x1f\x1f\x0f\x0f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'%\x04\xbdB\x93\xef#\xff\xff\xff||\x00\x00\x00\x00\xfb\xff\xff\xff\xff\xff\xff\xff\xff\xff||\x00\x00\x00\x00'),
                            bytearray(b'@\xb0 \xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x04\x0f\x04\x04\x00\x16\x04\x00\x00\x00\x00\x00\x00\x02\x03\x00\x07\x08\x0f\x08\x0f\x18\x1f'),
                            bytearray(b'\x00\x00&\x00\xb3\x93\x16\x1d0\xa7\x85,@r*r\x00\x00\x00>\x13\xec?\xc0\xbb@;\xc0\x7f\x80}\x80'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x80\xd0@8\xe8D\x8cd\xec\x00\x00\x00\x00\x00\x80\x80`\xc00\xe0\x18\xc0<\xe0\x1c'),
                            None,
                            bytearray(b'\x02\x00\x06\x06+\x02\x07%\x1d%\x1b#\x0f1\r\x18\x1c\x1f8?<?8?:?<?>?\x1f\x1f'),
                            bytearray(b'\xf1\xe4ze\xd5_\xd2\x12x\x80nC?-6t\xfb\x00\x7f\x80_\xa0\x12\xed\x00\xff\x80\xff\xc0\xff\x89\xff'),
                            bytearray(b'L\xc4\x9a\x80R\x08(:\xd0\x12x\x92\xach\xa0\xa4\xc0<\x86~\x06\xfe&\xde\x0e\xfe\x0e\xfe\x14\xfc\\\xfc'),
                            None,
                            bytearray(b'\x02\x1d\x04\x0f\x07\x07\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x0f\x0f\x07\x07\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xa4 \xbdB\xc9\xf7\xc4\xff\xff\xff>>\x00\x00\x00\x00\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff>>\x00\x00\x00\x00'),
                            bytearray(b'P\x08\xa8\x18\xf0\xb0\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x01\x03\x01\t\t\x00\x05\x1f\x11\x00\x00\x00\x00\x00\x01\x01\x02\x01\x06\x01\x0e\x05\n\x01\x1e'),
                            bytearray(b'\x00\x00x\x00-<mS\x82\xa4\xa3g\tK$\xc2\x00\x00\x00~<\xc3\x7f\x80\xde\x01\xdf\x00\xf7\x00\xfe\x01'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80 `0p(\x00h\x040\x14\x00\x00\x00\x00\x00\x80\x00\xe0\x00\xf0\x18\xf8\x1c\xfc\x0c\xfc'),
                            None,
                            bytearray(b'\x19\x11\x10\x00\r\t$\x00\x07\x06+!&\x06\x0f\x13\x01\x1e ?1>8?8?<?9?\x1c\x1f'),
                            bytearray(b'\x84\xda\xf2\xce\xee\xfe\xd0\xd1\xdf\x03\xf7\x06\xbf\xb6\x9d\x9c\xee\x01\xfe\x01\xfe\x01\xd0/\x00\xff\x00\xff@\xffc\xff'),
                            bytearray(b'\xd0v\x18\x12\xfc\x1a`\xa2\xda\x96nF,\x04|\x8cN\xbe\x0e\xfe\x06\xfe\x1e\xfe.\xfe\xbe\xfe\xfc\xfc\xfc\xfc'),
                            None,
                            bytearray(b'\r\x10\x03\x0e\x02\x07\x02\x03\x00\x01\x00\x00\x00\x00\x00\x00\x1f\x1f\x0f\x0f\x07\x07\x03\x03\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xcb\x18m\x02\xd8/\xb9\xff\xff\xff~~\x00\x00\x00\x00\xe7\xff\xff\xff\xff\xff\xff\xff\xff\xff~~\x00\x00\x00\x00'),
                            bytearray(b'x\xf8\x18\xf8\xf0\xf0\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\xf8\xf0\xf0\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL482_J_PUZZLE_BLOCK,
    palette_offset=3,
    unknown_num=0
)
