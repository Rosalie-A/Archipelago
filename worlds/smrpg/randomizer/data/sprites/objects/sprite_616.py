# SPR0616_YELLOW_LETTER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL498_YELLOW_LETTER
sprite = CompleteSprite(
    animation=AnimationPack(379, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x17\x0e\x0f\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x10\x0c\x00\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'A\x7f=\xbc\r\xbf\x8d\xc78\x0c <\x1c\x1e\x00\x00\x81\x00c I\n1\nr\x10"\x00\x10\x02\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x04\x04\x1c\x9e\xde\xaf\xfcV|?8<=\x1a>\x10\x04\x00\x0cA\x0c\x04\xff$]\x00\x1c\x02\x19\x01\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00@@ h \xbc\xf8\xb1\xbd\x00\x00\x00\x00\x00\x00\x80\x00@\x80\x18\xc0\x84\xc0\xc2\x80'),
                            bytearray(b'./+/\x179\x0f\x10;\x0c5>\x0f;\x1f>4\x04\x13\x03\x07\x07/\x0f;;\x05\x05\x02\x06A\x00'),
                            bytearray(b'\x19\xf5]\xfc\xff\xea\x9c}\xce\x7fh\x95\x98\xfa\xc1\xfd\x02\x08\x13\x10\x8d\x98\x83\x80\xc1\xc0bi\x17\x10\x83\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=105),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x17\x0e\x0f\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x10\x0c\x00\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'A\x7f=\xbc\r\xbf\x8d\xc78\x0c <\x1c\x1e\x00\x00\x81\x00c I\n1\nr\x10"\x00\x10\x02\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x08\x18\x14\x1c\x11\x1f\x12\x1f,\x1b\x17\x1f\t\x1e<?\x00\x00\x02\x00\x00\x00\x00\x00,\x00"\x00 \x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x00\x80\x00\xa0(\xe0\xfcx\xf1\xfd\x00\x00\x00\x00\x80\x00\x00\x00@\x00\x18\x00\x84\x80\xc2@'),
                            bytearray(b'./+/\x179\x0f\x10;\x0c5>\x0f;\x1f>4\x04\x13\x03\x07\x07/\x0f;;\x05\x05\x02\x06A\x00'),
                            bytearray(b'\x19\xf5]\xfc\xff\xea\x9c}\xce\x7fh\x95\x98\xfa\xc1\xfd\x02\x08\x13\x10\x8d\x98\x83\x80\xc1\xc0bi\x17\x10\x83\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=105),
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
            ]
        )
    ),
    palette_id=SPAL498_YELLOW_LETTER,
    palette_offset=0,
    unknown_num=0
)
