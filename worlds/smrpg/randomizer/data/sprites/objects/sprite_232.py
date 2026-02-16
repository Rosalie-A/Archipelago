# SPR0232_LEVEL_UP_BONUS_HP

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL496_LEVEL_UP_BONUS_HP
sprite = CompleteSprite(
    animation=AnimationPack(373, length=107, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbb\x7f\x8c?\x1ff\x7f\x8f\xef\xdb\xf9\xe9\xff}\xeekfxc<\xe7\x7f\xb7p\xfe&\x0f\x161\x90\x91\x90'),
                            bytearray(b'b\xc7\xc2\xc7\xc2\x07\x02\x87\xc2\x87\x82\x87B\x87\x02\x07\xa5xE\xf8\xc5\xf8\x05\xf8ExEx\xc5x\x85\xf8'),
                            bytearray(b'\xbe\xf4\xf7\x7f\xff\xdb\xad\xff\xe9\xa9?\xff\xff\xff\xff\x00M\td\xc8\xced\xf7$)??\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x07\x82\x07\x82\x07\x82\x07\x02\x07\xfe\xfd\xfd\xfa\xc68\x05\xf8\x85\xf8\x85\xf8\x85\xf8\x05\xf8\xf9\x00\x02\x018\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xdf\xc0\xdf\xc0\xdf\xc0\xdf\xc0\xe3\xc0\xe3\xc0\xe7\xc0\xef\xc0?\x01?\x01?\x01>\x01\x03<\x03<\x078\x0f0'),
                            bytearray(b'\x9fC\xcf\x07\xc3\x10\xf8\x01\x85\xca\x99d\xfd\x0f\xff\x1fa!70<\x1f\x07\x81\xf9\xc7\xa7{\xd31\xf1\x11'),
                            bytearray(b'\xef\xc0\xef\xd0\xec\xd0\xf0\xc0\xc0\xe0\xff\xdf\x7f\xbf? \x0f0\x1f0\x1c3\x10/ \x1f\x1f\x00\x80\x00\x00\x00'),
                            bytearray(b'\x0f\x8f\x03\x01\x01\x03\x01\x00\x01\x00\xff\xff\xff\xf7\xff\x00\x8c\xf8\x04\xfc\x00\xfe\x01\xff\x01\xff\xff\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xff\x00\xff\xff\xff\xff\xff\xff\x00\x000\xa0\xfc\xf0\xfe\xfd\x00\x00\x00\x00\x00\x00\xff\xff\x00\xffp\xff\x88?\x02\xff'),
                            bytearray(b'\xf0\x00\xfc\xf4\xf2\xfc\xfa\xfe\x06\x03\x06\x03\x02\x07\x02\x07\x00\x00\x00\x00\x00\x00\xfc\xf8\x01\xfc\x01\xfc\x05\xf8\x05\xf8'),
                            bytearray(b'\xfc\xff{\xff\xbb\xff\xbf\xff?\xff\x7f\xff\xfb\xff\xfb\xff\x03\xfc\x86xF8\xc0<\xc0?\x80\x7f\x07\xf8\x80\xf8'),
                            bytearray(b'\x02\x87\x02\x87B\x87\xc2\x07\xe2\xc7\xe2\xc7b\xc7\xe2\xc7\x05\xf8\x05\xf8\xc5xEx%\xf8%\xf8\xa5x\xa5x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f\x10?\x0fo?\x7f\xdf\xe0\xc0\xc0\xe0\xc0\xe0\xd0\xc8\x00\x00\x00\x00 \x00\x9f?\x00? \x1f \x1f8\x0f'),
                            bytearray(b'\xff\x00\xff\xff\xff\xff\xff\xff\xf0\x00\xf1\x03\xf2\x01\xcf?\x00\x00\x00\x00\x00\x00\xff\xff\xf0\x0f\xf1\x0f\xfd\x0e\xc0<'),
                            bytearray(b"\xdf\xc0\xde\xc0\xde\xe0\xce\xe0\xc7\xe0\xc3\xe0\xc3\xe0\xef\xc0?\x00?\x01?\x01/\x11\'\x18#\x1c#\x1c\x0f0"),
                            bytearray(b'??\xfc\xff\xbb\xff\x7f\xff\xfb\xff\xec\xff\x81\xe7\x14\xc0\xc0\xff\x03<D8\x00x\x07\xf8\xb9\xfe\xfd\xff\xebQ'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00'),
                            None,
                            bytearray(b'@\xc0@\xc0@\xc0@\xc0\x80@\x80\x00\x80\x80\x00\x00@\x00@\x00@\x00@\x00\x00\xc0\x80\x80\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x0c`-b,c,b"p&q&q.q_\x00~\x01~\x01}\x02s\x0cv\tw\x08\x7f\x00'),
                            bytearray(b'\x1f\x9f\x17\x1f\x1f\x97\x17\x7fo\xdf\x7fo\xff\x7f/\xf7w\x80\xe7\x18\x7f\x98\xdf O\xb0\xcf\x907\x80\xf7\x08'),
                            bytearray(b',p,p,` ` 0??????|\x03|\x03|\x03p\x0f0\x0f\x03\x00\x03\x00\x01\x00'),
                            bytearray(b'\xaf\xf7\x17\xb7/wG_eF\xff\xfc\xfb\xff\xff\xff\xdf\x08\xdfh\xf7\xa0\x7f\xa0\x04\xbb\xfb\x03\xf7\x03\xf7\x07'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x80\xc0\xc0\xc0@\xc0@\xc0@\xc0@\xc0\x00\x00\x80\x00\xc0\x00\x80\x00@\x00@\x00@\x00@\x00'),
                            None,
                            bytearray(b'@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\xc0@\x00@\x00@\x00@\x00@\x00@\x00@\x00@\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'????\x1d?\x1f\x7f@bCpCpAa\x1f\x00?\x00\x00\x00\x7f\x1f\x10\x1f\x13\x0c\x13\x0c\x10\x0f'),
                            bytearray(b"\xff\xff\xfe\xff\xff\xff\xff\xff\x07\x07\xa7\'\x07g7\xe7\xff\x00\xfe\x00\x07\x00\xff\xf8\x07\xf8\xe7\xf8\xc7\xb8\xd78"),
                            bytearray(b'OaMcMsMsCrBsDrLs\x1e\x01\x1c\x03\x1e\x01\x1e\x01\x11\x0f\x10\x0f\x15\x0b\x1d\x02'),
                            bytearray(b'\xff\xf7\xff\xff\xff\xef\xff\xff\xbf\xff\xff\xff\x7f\xff\x7f\x7f\x07\xe8\x17\xe0\x8f \xcf G8\x07\xf8\x1f\xe0\xdf`'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'p;p;p;p:p=s=p?p?\x14\x0f\x14\x0f\x14\x0f\x15\x0f\x12\x0f\x13\x0f\x10\x0f\x10\x0f'),
                            bytearray(b'\xef\x02/\x82?\xca?Z\xcf\x8a\x07\x92\xaf\x02\xaf\x8a\xfe\xfd~\xfd>\xfd\xbe\xfd\xfe\xfdl\xfd\xfc\xfd\xfc\xfd'),
                            bytearray(b'r<s<s8s0s0px\x00{\x00\x00\x13\x0f\x13\x0f\x17\x0f\x1f\x0f\x1f\x0f\x07\x0ft\x0f\x7f\x7f'),
                            bytearray(b'\x1e\x03\x1e\x03^\xe3NK\xfe#\x80\x02\x00\xf8\x00\x00\xfc\xfd\xfc\xfd\\\xfd\xfc\xfd\xfc\xfd\xff\xfd\x07\xff\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x008\x0fp?{ s;s8q:q:\x00\x00\x0c\x03\x08\x07\x07\x0f\x17\x0f\x17\x0f\x15\x0f\x15\x0f'),
                            bytearray(b'\x00\x00\x00\xf8\x00\xf8\xfe\x0c\xff\xfe\xff\xc6\xff\xe2\x7f\xe2\x00\x00\x06\xfe\x07\xff\xff\xff\xfe\xff\xfc\xfd\xfe\xfd\x1e\xfd'),
                            bytearray(b's=q=p>p8r>s:s?p=\x12\x0f\x12\x0f\x11\x0f\x17\x0f\x11\x0f\x15\x0f\x13\x0f\x12\x0f'),
                            bytearray(b'\xff\xe2\xff\xe2o\xe2o\xf2\x7f\xf2\x7f\xf2\xefb\xefb\x1e\xfd\x1e\xfd\x1e\xfd\x0e\xfd\x0e\xfd\x0e\xfd\x9e\xfd\x9e\xfd'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=1, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=1, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL496_LEVEL_UP_BONUS_HP,
    palette_offset=0,
    unknown_num=0
)
