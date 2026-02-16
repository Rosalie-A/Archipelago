# SPR0090_BOWSER_DOLL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL664_BOWSER_WALKING_DOWN_LEFT
sprite = CompleteSprite(
    animation=AnimationPack(280, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'/Xw\x18+<3\\\x7f\x00\x08\x10\x00\x00\x00\x00$S ?\x025cd(g\x10\x18\x00\x00\x00\x00'),
                            bytearray(b'\xc68\xfe\x04\xb4|\xce4\xde$\xfe,~\x048\x04\x80n0\xde\xc0L\n\xb4\x1a\xec\x10\xce(f\x04,'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\t\x04\x0c\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x03\x00\x1f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc0\x10\xc00\x10~\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x10@\x90\x18\xee'),
                            bytearray(b'\x02\x06\t\x14\x07\x1c-\x17\x13l\x19lu\x0e\x7f`\x0f\x00\x1f\t\x05\x11(\x12\x10owm1j\x11\x0e'),
                            bytearray(b'\xa0|\xd6\xe6t\xe5\xb9d{\x8c\xeft\xf5^\xee\x18\xb4<\xb2\xfc\xe4j\x95vG\xae\x0f\xf6\x07\xee\xa4B'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\\g&[\x17\x1b\x03\x1c\x15\x1a/p9\x7f3\x0cw`Ee\x03\t\x04\x1f\x07\x0e\x0f\x13\x01G\x02='),
                            bytearray(b"\'\xfa\xfe\xfe\xce\xc6\x16\r\'\xfc~\xd4\xa4x(\x1e\xf4\x13\xf6\x0e\xc6>\x14\xefCt\nv\xc4\xe0 \x12"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\r\x00\x1a\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x03\x16\x06\x15'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00 \xe0\xa0`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 @\x80\xe0\x00\xc0\x00'),
                            bytearray(b'\x00\x1e\x18\x1e\x01\x1f\x0f\x00\x0e\x13\x0c\x17I6(w\x1b\x0c\x0f\x00\x0f\x18\x08\x08\x17\x14\x06\x12G\x10\x07P'),
                            bytearray(b'\x80@\x08\x00l\x90\xd0\x0eN\xbc\x1c\xe0\x9a\xf9\x1b\xfa\xa0@\xe0\x00x\x98\xf8\x92\xdaR\xd0\xae\xf8\x07\xf9\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[]
                ),
                Mold(3, gridplane=False,
                    tiles=[]
                ),
                Mold(4, gridplane=False,
                    tiles=[]
                ),
                Mold(5, gridplane=False,
                    tiles=[]
                ),
                Mold(6, gridplane=False,
                    tiles=[]
                ),
                Mold(7, gridplane=False,
                    tiles=[]
                ),
                Mold(8, gridplane=False,
                    tiles=[]
                ),
                Mold(9, gridplane=False,
                    tiles=[]
                ),
                Mold(10, gridplane=False,
                    tiles=[]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x18\x10\x1c\x01\x1e\x00\x0f\x00\x07\x04\x03\x00\x00\x00\x00\x00\x08\x00\x00\x00\x10\x00\t\x00\x07\x07\x03'),
                            bytearray(b'\x05\x00&\x00\x00\x00\x9f\x045\x00\x02\x00\xc0\x0c\xec\r\x1d\x00y\x06\x7f\x06\xff\x04\xfe\t\xf7\x19\xef\x17\xfc\x13'),
                            bytearray(b'\x06\x01\x00\x05\x03\x03\x04\t\x06\t\x06\x0c\t\x0f\x08\x1f\x05\x06\x1d\x06\x0f\x00\x0f\x08\x0f\x00\x0e\t\x03\x04\x03\x14'),
                            bytearray(b'T\xdf\x0c\xff\x1d\xfc7\xe0o\xc0Z\x029\x00\xabn\xdc"\xff\x03\xfc\x03\xfe\x01\xff\x00f\x9f\x08\xf7\xee\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'@\x00\x00\x00"\x04\x82\x0c2,\xf8f~\xa7\xfa\x87\xc0\x00\xe0\x00\xc2$\xe2h\xf2\xe8~\xe67\xe9\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x80\xf0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0 \x00P  '),
                            bytearray(b'r\x9f=\x91\xfa\xd4\xda\xf5\xf7h/\x10\xdf\x00<\xe3>\xdd\xd5\xfe\xf6\xff\xf5\xfdy\xfdP\xfc\xe2>s\xff'),
                            bytearray(b' \xc0\xc0\x00\x10\x10\xc8\xc0`f\x82\x04\x8c`\xe4\x18`\xc0\x80pP\xe0\xc80`\x98\x82\xfc\xe4\xf8\xf8\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x16\x1f\x17?"?Y&\x7f\x03?@Gxl\x13\x00\t\x00(\x00\ry6l+\ny\x03\x0ctw'),
                            bytearray(b'*\xfdL\xffc\xff\xc7\xfe\x1e\xfc\xf9\xe0\x01\x00\xde\xdf\xf6\x95\x00\xb3\x00\x9f\x01>\x03\xfd\x1f\xe6\xff\xfe \xff'),
                            bytearray(b'\xafP\xa5Z\xbeA~\x01\x7f\x00?\x00?\x00\x1f\x00\xd3\xd0]^~A~\x01\x7f\x00?\x00?\x00\x1f\x00'),
                            bytearray(b'\xff\x7f\x82/\xe1\x10q\x82m\x82?\xc0\xbf@\xb3@\x80\x7f\xd1\x7f\xee\x1e~\x8e\x7f\x939\xc6\x81~\x81r'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbe\xc0\xdd"\xf9\x0f\xee\x0f\xf6O\xf7\x1f\xf3\xdf{\x9fCy.\xf7\x00\xffp\x99\xb0I\xe0\x18 \xd8@\xb0'),
                            bytearray(b'\x94\xe8B\xfcTH\xd4\xc8\xcc\xd0\xd4\x88v\xc8\xf4\x08\xfc\xf8\xfe\xfe\xfe\xfax\xfc|\xf8|\xac\n\xfc\x0c\xf8'),
                            bytearray(b'\xc8\x17\xbe\xc1o\x90k\x94\xfb\x04\xf0\x0e\xfc\x02\xfc\x02\xe8;W\xd5\xd7\xd0\xd6\xd5\xfe\r\xfd\x0f\xfd\x03\xfd\x03'),
                            bytearray(b'\xf4\x08\xe0\x18\xe8\x10\xe0\x10\xd8 @  \x00@\x00\x0c\xf8\x18\xf8\x18\xf0\x18\xf8(\xf0\xb0\xf0\xe0\xc0\xc0\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x83@\x81@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81B\x81@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xfc\x02\xf8\x04\xf8\x04\xf0\x08\x00\x00\x00\x00\x00\x00\x00\x00\xfd\x03\xfb\x07\xfa\x06\xf0\x08\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=136),
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
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL664_BOWSER_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=0
)
