# SPR0130_WIGGLER_BODY_SEGMENT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL100_WIGGLER_HEAD
sprite = CompleteSprite(
    animation=AnimationPack(103, length=124, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x80\xe2\x9c\xde\xbd\x00\x00\x10\x00&\x06F\x06\x00\x00\x00\x00\x00\x01\x00\x03'),
                            bytearray(b'\x80`\xe8\x08\xfc\x04\xf2\x04\xf4\x08\xf9\x04\xbaD+\xf7\x00`\x00\x10\x00\x00\x00\x0e\x00\x0e\x80\x87\x00\xe7\x00\xf3'),
                            None,
                            None,
                            bytearray(b"\xa6\xe7BC\x01\x03@\x01 \x000 \'0\x03\x03\x18\x03\xbc\x03|\x03~\x01?\x00\x1f \x0f8??"),
                            bytearray(b'\xdb\xf6\xd9\xf4$\xfc\xca\xf8\x96\xf2\xcf\xcf\xc7/\xe1\xe5\xc10\xc30\x02\xf0\x06\xe0\x0e\x027\x0f\xe7\x1f\xe3\xff'),
                            None,
                            None,
                            bytearray(b'\x07\x07\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfa\xfa\xf2\xee\xe6\xc6{G>>\x00\x00\x00\x00\x00\x00\xe9\xf7\xc1\xff\x85\xfb\x19\x7f\x02>\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x05\x06\x0f\x00\x1f\x00?\x00x\x01\xf4\x83\xe3\x9f\xdb\xbf\x00\x00\x10\x00&\x06F\x06\x00\x07\x00\x0f\x03\x0c\x03\x0c'),
                            bytearray(b'\xc0 \xc8\x10\xd4 \xe0\x12\xe8\x12\xb2\xce{\xc6[\xc6\x00\x00\x008\x00<\x00\x1e\x00\x9e\x01\xcc\x01\xc0\x01\xe0'),
                            None,
                            None,
                            bytearray(b'\xa4\xefCG\x00\x00@\x00 \x00\x19\x01\x1f\x08\x1b\x0b\x10\x0f\xb8\x07\x7f\x00\x7f\x00?\x00\x1e\x00\x07\x18\x07\x1f'),
                            bytearray(b'\xb9\xc45\xcc\xa4\xdc\xea\xe8\xbc\x80\xb6\xce\xffo\x8f\xff\x03\xc0\x03\x80\x02\x00\x16\x00,p\x0eV\xaf_\x87\xff'),
                            None,
                            None,
                            bytearray(b'5%8xrs\x07\x07\x03\x03\x00\x00\x00\x00\x00\x00K\x7f\x86\xff\x8e\xff\xff\xff\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x16\x8e\xea\xba6\xf6\xfc\xfc\xf0\xf0\x00\x00\x00\x00\x00\x00\x02\xfe\xe6^\x0e\xfe\xfc\xfc\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x0f\x00\x1f\x00?\x00\x7f\x00\xe5\x98\xdc\xbb\xa5\xe7\x00\x00\x10\x00&\x06F\x06\x00\x00\x00\x03\x00\x07\x19\x06'),
                            bytearray(b'\xc0 \xe8\x18\xf8\x04\xf2\x08\xf0\x08r\x8dY\xe7\xbf\xe7\x00 \x00\x00\x00\x0c\x00\x1e\x00\x0e\x00\xcf\x00\xe7\x80c'),
                            None,
                            None,
                            bytearray(b'\xc5\xc7\x02\x07\x01\x03@\x00 \x00\x11\x01\x0f\x08\x02\x0e9\x06\xf8\x07|\x03\x7f\x00?\x00\x1e\x00\x07\x08\x01\x0f'),
                            bytearray(b'\xb3\xeeU\xec\x84\xfc\xca\xf8\xb6\xf2\xa7\xbf\xaf?o_\x81`\x03\xe0\x02\xc0\x06\x00\x0e\x02o\x17\xaf_\xef\xbf'),
                            None,
                            None,
                            bytearray(b'\x0c\x0c\x07\x07\x03\x03\x00\x01\x01\x00\x01\x01\x00\x00\x00\x00\x0b\x0f\x07\x07\x03\x03\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xa7\xaf\xaf\xef\x06\xfe\xcc\\\xf88\xe0\xe0\x00\x00\x00\x00\xa7\xdf\xa3\xdf\x02\xfe@\xbc\xe0\xd8\x10\xf0\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x1f\x10? ?@\x1f \x1e <A~\x81\x00\x00\x00\x00\x06\x06\x06F\x00`\x00\xe1\x00\xe3\x00\xc3'),
                            bytearray(b'\xa0`\xe8\x18\xfc\x08\xfa\x08\xfc\x04_C5\xe9\xd2\xfe\x00\x00\x00\x08\x00\x0c\x00\x0e\x00\x06\x00\xe3\x02\xf1\xc10'),
                            None,
                            None,
                            bytearray(b"\xfe\x83=C^a\'8\x10\x1f\x07\x07\x08\x08\x1b;\x00\x03\x80\x03\x00\x01@\x00 \x00\x18\x00\x0f\x10\x1b\'"),
                            bytearray(b'\xd5\xfc&\xfd\xca\xf8\x14\xf2\xe8\xe40\x08\xc0<\xfd\xf9\xc30\x03\xf0\x06\xe0\x0e\x00\x1c\x00\xfc\x04\xf2\x0e\xf2\xff'),
                            None,
                            None,
                            bytearray(b'w\x97\xbf\x07\xd7\x0fk\x1b==\x00\x00\x00\x00\x00\x00\x17\xef#\xff\x03\xff\x07\x7f==\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf1\xff\xf2\xfe\xfe\xfe\xfc\xfc\xf8\xf8\x00\x00\x00\x00\x00\x00\xe0\xff\xe1\xff\xe2\xfe\xfc\xfc\xf8\xf8\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x1f\x10? \x1f \x1f ?@|\x81\xf8\x83\x00\x00\x00\x00\x06\x06\x06f\x00`\x00\xc0\x00\xc3\x00\x07'),
                            bytearray(b'\xa0`\xe8\x18\xf0\x0c\xf2\x08\xf8\x08\xf9\x0c\xbd\x87\x7f\xc7\x00\x00\x00\x00\x00\x0c\x00\x1e\x00\x0e\x80\x8f\x00\xc7\x00\xe3'),
                            None,
                            None,
                            bytearray(b'\xfd\x83=GZg\x05;\x00\x1f\x07\x07\x10\x00\x0b\x0b\x01\x06\x81\x06\x00\x07@\x03 \x00\x18\x00\x07\x18\x0b\x07'),
                            bytearray(b'\xb5\xec\xb6\xedJ\xf8\x84\xe2\xea\xe67\x0f\xdf?\xff\xff\x83`\x83`\x06\xe0\x1e\xc0\x1c\x02\xf9\x07\xe3\x1f\xff\xff'),
                            None,
                            None,
                            bytearray(b'\r\x05\x16\n*\x050\x01\r\x03\x03\x03\x00\x00\x00\x00\x05\x0b\x02\x1d\x08?\x00?\x00\x0f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xff\xff\x7f\x7f\xbe\xbe\xbc\xbcxx\xe0\xe0\x00\x00\x00\x00\xff\xff\xff\xff~\xfe|\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x1f\x10\x1f \x0f0\x0f\x10\x1f >\xc0\x7f\x80\x00\x00\x00\x00\x06&\x06v\x00p\x00\xf0\x00\xe1\x00\x01'),
                            bytearray(b'\xa0`\xe8\x18\xf8\x08\xfc\x04\xfe\x02.b\x1b\xf7i\xfd\x00\x00\x00\x08\x00\x0c\x00\x06\x00\x02\x00\xf3\x00\xf9b\x99'),
                            None,
                            None,
                            bytearray(b'\xbf\xc1~A\x7fP7hdgo\x1f\xec\x80\xb5\xc5\x00\x01\xc0!p  P(P\x00x#\xfc\x02\xff'),
                            bytearray(b'm\xfc\x96\xfdb\xf8\x14\xf2\xea\xe67\x0f\xdf?\xff\xffc\x98\x03\xf8\x06\xf0\x0e\x00\x1e\x02\xff\x07\xef\x1f\x0f\xff'),
                            None,
                            None,
                            bytearray(b'{{\x07\x07\x1f\x1f\x0f\x0f\x0f\x0f\x07\x07\x00\x00\x00\x00\x07\x7f\x1f\x1f\x1f\x1f\x0f\x0f\x0f\x0f\x07\x07\x00\x00\x00\x00'),
                            bytearray(b'\xef\xef\x9f\x9f\xff\xff\xfe\xfe\xfc\xfcpp\x00\x00\x00\x00\x1f\xff\xff\xff\xff\xff\xfe\xfe\xfc\xfcpp\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                        AnimationSequenceFrame(duration=16, mold_id=1),
                        AnimationSequenceFrame(duration=16, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=3),
                        AnimationSequenceFrame(duration=16, mold_id=4),
                        AnimationSequenceFrame(duration=16, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL100_WIGGLER_HEAD,
    palette_offset=0,
    unknown_num=0
)
