# SPR0685_CHOMPWEED

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL215_CHOMPWEED

sprite = CompleteSprite(
    animation=AnimationPack(
        109,
        length=66,
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
                            format=0,
                            length=10,
                            subtile_bytes=[
                                None,
                                None,
                                None,
                                bytearray(
                                    b"\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x00\x7f\x80\xff\x00\xfe\x01\x08\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x80\x00\xc0\xb0\xc0 \x80p\x80|\x00\xfc\x00\xf8\x00\xd0\x80\x00`\x10`\x100\x080\x0c0\x0cd\xdcL\xfc"
                                ),
                                None,
                                bytearray(
                                    b"|\x03!\x1e\x00\x07\x18\x13\x1f\x12\x07\x03\x01\x00\x01\x01\x00\x00!\x00\x00\x1f\x17\x0f\x1d\x0f\x05\x07\x00\x01\x00\x01"
                                ),
                                bytearray(
                                    b"\x80\x14\x80|\x00\x98\x00\xa0\xb8\xc8\xf8\xf0x\xb0\x00\xf0\x8c|\x9c|x\xf8\xe0\xe0@\xf88\xc8\xe8\xd8\xf0\xf0"
                                ),
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    1,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=10,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x07\x04\x0f\x00\x0f\x00\x07\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xf0 \xf8\x00\xf0\x0c\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x10\x00\x18\x00\x1c\x00"
                                ),
                                None,
                                bytearray(
                                    b"\x05\x02\x00\x03\x1c&!Y@0`\x18 \x1f\x18\x07\x00\x00\x00\x00!\x00\x06\x00\x0f\x00\x07\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xf0(\xf0,`\x9e\x00~\x00<\x00\x08\x10\xd2 \xe6\x18\x04\x10\x0e<\x0e\x8c\x1e\xc2\x1e\xa6^\x06.\x06\x1e"
                                ),
                                None,
                                bytearray(
                                    b"\x00\x03\x02\x03\x07\x04\x07\x01\x01\x02\x01\x00\x01\x01\x00\x00\x00\x0f\x03\x01\x07\x03\x07\x07\x02\x03\x00\x01\x00\x01\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\xec\x00\xd0\x80\xc0\xf8\xc8\xfcT|\xb08\xf4\x10\x08\x1c\xfc\xf0\xf0@\xc0\x00\xf8H\xbc\xfc\xcc\xec\xdc\x18\x18"
                                ),
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    2,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=10,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x000\x00(\x144\x060\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\n\x00\x0f\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x06\x00\x0e\x01\x16\t$\x1bd\x1b\xc8\xb6\x00\x00\x00\x00\x02\x00\x03\x00\x03\x00\x06\x01\x04\x03\t\x07"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00"
                                ),
                                bytearray(
                                    b"\x18 \x1c\x00\x0e\t\x06\x07\x00\x04\x00\x01\x07\x06\x0f\x0b'\x00\x03\x00\x00\x00\x00\x00\x00\x07\x00\x01\x01\x07\r\x07"
                                ),
                                bytearray(
                                    b"\x80\xbc\x00\xfc h\x00\xda\x00d\x00\xf8\x80\xe0\x80\xc0G\x0f\x8f\x0f\x86\x1e\x06>\x1c\xfc8\xf8`\xe0@\xc0"
                                ),
                                None,
                                bytearray(
                                    b"\r\n\t\x06\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x0e\x07\x0e\x0f\x00\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00"
                                ),
                                bytearray(
                                    b"\xf8X|\xd4|\xa08t\x10\x08\x00\x00\xc0\xc0\x00\x00\x00\xf8\xc8\xbc\xec\xdcl\\\x18\x18\x00\x00\xc0\xc0\x00\x00"
                                ),
                                None,
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
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=10, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
            ])),
    palette_id=SPAL215_CHOMPWEED,
    palette_offset=0,
    unknown_num=8)
