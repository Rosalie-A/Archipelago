# SPR0667_BUNDT_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL781_BUNDT_STATUE

sprite = CompleteSprite(
    animation=AnimationPack(
        99,
        length=80,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=3,
                            length=17,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x01\x03\x07\x06\x03\x06\x11\x16\x03>\x01~\x00\x00\x00\x01\x07\x00\x08\x00\x1c\x008\x00b\x1c\x08>"
                                ),
                                bytearray(
                                    b"\x03\x00\xc2\x81\xc3\xc4~izp\xbd8\xa2 r%\x00\x01\xb8|\x188\xa8\x10\xd5\x080GK7\xb7z"
                                ),
                                bytearray(
                                    b"\x00\x00<\x9c^\x1f\x7f>y~\xeb|\xf6\x81~0\x00\x00\x9c \x8b`r\xc0D\x80\x18\x80\x80x\x01\xb8"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x80\x80`\xe0`\x80H\x80\xe4\x80\x00\x00\x00\x00\x00\x00\x00@\xe0\x00\x80`\xf0xx\xfc"
                                ),
                                bytearray(
                                    b"\x01~\x01\x7fg\xbfe\x1b\xe9\x1c\xf0\x0e\xfa\x07\xde!\x0c>\t\xbe\xa2\x18\x81\x18\n\x04\t\x06\x06\x01\x01\x00"
                                ),
                                bytearray(
                                    b"|<\xfe\xfe\xff\xfc\xff\xf8|\xf2|\x18\x08\xc1\x80\xaf\x98cD\x030\x06\xc4\x06u\x0e\x97\x0f?\xcf\xd0\x7f"
                                ),
                                bytearray(
                                    b"_\x1c\xbf\x1f\x9f\x0f\xbf?\xb7?K9G\xb7\x00\xf8\x88!K _0X0;p\xac\xf3\x8d\xbb\x07\xff"
                                ),
                                bytearray(
                                    b"\xc0\xb0\xc2z\xf2\xfa||\xfe\xbe\xefg\x1f\x0c\x7f?\xdc\xfcD\xbe4\x0e&\x9e\x9c~\xfd\xff\xff\xff\xf7\xff"
                                ),
                                bytearray(
                                    b"W\x88\xbf\x18~!}\x03=A_\x06O\xa0- 8\x10X\xb898\xb9\x199\x9b\x1b\xef\xed\xd5\x13i"
                                ),
                                bytearray(
                                    b"\x80X\xfc\x00\x7f\x00\xba\x85\xbaE\xb0\x0e\xb6\x0c\xcc\x0c?\x07\x03\x00\x80\x00\xc0\x80\x80\x80\xc5\x80\x89\xc6\xd5\xee"
                                ),
                                bytearray(
                                    b"\x0f\x03\x03 \xf1\x04'\xc3fd\xfee~<\x1f\xbf\xff\xff\xe0\x1f\x0c\x03['\xfegg\xfe\x1e\xff\xec\x1f"
                                ),
                                bytearray(
                                    b"\xff\xff\xff\x7f\xff7\xff\x97\x7f?\xfe:\xfc\xfc\xfc<\xc7\xff\x17\xff\xff\xff\x1f\xff\x7f\xff\xea\xfe\\\xfc<\xfc"
                                ),
                                bytearray(
                                    b"\x1dB\x1b(\x0f4\x07\x0b\x01\x05\x01\x02\x00\x00\x00\x00Qx,94?\x0b\x0f\x05\x07\x02\x03\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xfd\xb8\xd9)\x7f\r\xef\xcf\xff\xff\x7f\x7f\x0c\xc2\x10\x0f\xfb\xfd\xcb\r\x08\xcf\x8f\xff\xff\xff\x1f\xff\xc2\xfd\x0f\x1f"
                                ),
                                bytearray(
                                    b"\xdb_\xff\xff\xff\xf1\xf7\x8f\xef\xfd\xff\xe1s\x0c0\xc0\xce\xff\xdf\xffq\xff\xef\xf7\xfd\xef\xe2\xff\x0c\xff\xc0\xf0"
                                ),
                                bytearray(
                                    b"\xfe<\xfe\xfc\xfc\xf8\xf8\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\xfc\xfe\xfc\xfe\xf8\xfc\xf0\xf8\xc0\xf0\x00\xc0\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(frames=[]),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=10, mold_id=5),
                        AnimationSequenceFrame(duration=10, mold_id=1),
                        AnimationSequenceFrame(duration=10, mold_id=6),
                    ]
                ),
                AnimationSequence(frames=[]),
                AnimationSequence(frames=[]),
                AnimationSequence(frames=[]),
                AnimationSequence(frames=[]),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ])),
    palette_id=SPAL781_BUNDT_STATUE,
    palette_offset=0,
    unknown_num=8)
