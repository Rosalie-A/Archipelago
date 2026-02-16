# SPR0719_BOOSTER_TOWER_DOOR


from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL493_BOOSTER_TOWER_DOOR
sprite = CompleteSprite(
    animation=AnimationPack(369, length=66, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xff\xd9\x7fq\x1f\x1c\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\xf6\xff~\x7f\x1f\x1f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xf1\x9fi\xdf\xd5?\x9d?}\x9b};\xfd\xff\xfd7`\xffP?x\x1fx\x1f\\?\xbc\x7f\xf9\xfe9\xfe'),
                            bytearray(b'\xbc\xbe\xbe\x9e\xfe\xde\xffW\xff\xc7\x7fq\x1f\x1c\x03\x03@\xff`\xff`\xff\xe8\xff\xf8\xff~\x7f\x1f\x1f\x03\x03'),
                            bytearray(b'\xfb\x9f\xb2\xdf\xb2_u\x9e\xe5\x7f\xb6>\xff{\xff{\x90\xfe\xd0\xbeR\xbc\x90\xfc\xf0\xfc\xc5\xf8\xc0\xf8\xc0\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xbc\x80\xaf\xf0\xc8\xfb\xf2\xde\xe4\xff\xe0\xff\xe8\xdf\xe8\xdfB\x86`\xe1<\xf8/\xfe\x03\xff\x00\xff \xff \xff'),
                            None,
                            bytearray(b'\xe0\xdf\xe0\xdf\xf0\xdf\xf4\xcf\xf4O\xfco\xec/n/ \xff \xff \xff0\xff\xb0\xff\x90\xff\xd0\xff\xd0\xff'),
                            bytearray(b'\x80\xbf\x81\xbe\xc3\xbc\xc3\xbc\xc3\xbe\xe1\xbea\xbe \xbe@\xff@\xfe@\xfc@\xfc@\xfcA\xfe@\xff@\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x89\xb5\x8e\xb0\xe4\xfau\xea\xbb\xb4\x930\x15\xb9\xdd-C\x83C\xc1`\xc1A\xe0A\xf0\xcd\xf0\xc2x\xb6x'),
                            bytearray(b'\x00\x00\x00\x00 \x80t\xf1\xa0\xe0\x95x\xb7?\xa7?\x00\x00\x80\x80\x10p\x03\x0e\xdf\x80\xff\xf0\xcf\xff\xc0\xff'),
                            bytearray(b'|-\xad\xbc\xee\xf7\xac\xb7/wo\xff\xb6\xee\xd3\xff\xf2<r<:<x>\xf8>\xf1~\xf0\xff \xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'}\xa5:\xf9\xff\xff\xbf\xbf\xd9\x1f\xf0_\xe0\xdf\xf8\xdff\x18\xfe\xff\xe0\xff\xe0\xff\xe0\xff\xa0\xff \xff \xff'),
                            bytearray(b"{\x85\xfd\xfc\xb8\xb9\xfe\xfb~\xff>\xbe\'\xbf\x06\xbf\x03\x00\x83\x00F\xe0H\xf0D\xf8C\xfcA\xfe@\xff"),
                            bytearray(b'\xff\xe1\x9d\xe0\xd3\xe0`@ \x00 \x00 @\x90\xe0\x1e\xff\x01\x83\x04\x10\x80 \xc0 \xc0 \x80 \x08\x98'),
                            bytearray(b'G\xbf\xe2?8O\x8es\x1b<\r\x0c\x03\x00\x00\x00@\xff\xc0\xff\xf0?\x1c\x0f\x07\x03\x02\x01\x03\x00\x00\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=104),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xff\xe1\x9d\xe0\xd3\xe0`@ \x00 \x00 @\x90\xe0\x1e\xff\x01\x83\x04\x10\x80 \xc0 \xc0 \x80 \x08\x98'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL493_BOOSTER_TOWER_DOOR,
    palette_offset=0,
    unknown_num=0
)
