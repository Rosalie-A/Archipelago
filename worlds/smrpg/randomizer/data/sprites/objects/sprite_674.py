# SPR0674_PUNCHINELLO_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL787_PUNCHINELLO_STATUE

sprite = CompleteSprite(
    animation=AnimationPack(
        0,
        length=31,
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
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x04\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b'\x0c\x00\x12\x0c"\x10A"A\x00A\x80 \xe1\x08\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x01\x00\x00\x01\x01\x03\x0b\x0f\x03\x0f\x13K\x03\x00\x00\x01\x00\x03\x00\x03\x00\x0f\x00\x0e\x00\x1e\x00>@"
                                ),
                                bytearray(
                                    b"\x07\x00a \xbe\x95\x85\xcf\x13\x11>:{[m\xbf\xc6\x00\xe3\x04\xf0\x0b`\x1a\x00\x0e \x07`\x04\x92@"
                                ),
                                bytearray(
                                    b"\xb0p\xe0\xe0p\xf0\xb00\xa06wq\xfd\xf2\xbe\xfe\x00\x00\xc0\x00\x00\x80\x00\xc0\x16\xc0/\x80=\x02q\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00"
                                ),
                                bytearray(
                                    b";#\x06Wa\x150I\x08L\x00\x14\x00\x00\x00\x00>@/p\n\x7f\x05~\x04@\x00\x94\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"f\x1dC\x80\x03\x02\xa1\xa0\x04G\x06\x04\x0e\x1a\x06\x07\x10\xeb<\xff\xf8\xff\x1c\xdfR9;?\x14\x05\x01\x00"
                                ),
                                bytearray(
                                    b"\xbf\xff\x1e\xde\x8e^\x0e\xde\x1e\x1e\\|1\xf1\xe0\xe01@\xb0`0\xe00\xe0\xc0\xe0\xa1\xc0\xc1\x00\x00\x01"
                                ),
                                bytearray(
                                    b"````\xe0`\xe0`\xb88\xf8<\xb8:\xc0\x08\xc0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe4\x00\xe2\x04\xe0\x1c"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x01\x036\x0f~\x07\x9bd\xa7\\\x1e}\x00\x01\x00\x00\x02\x04\x01\x00\x00\x00@`@@\x00\x01\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xc0\xc11\xb11q\xdd<\xdc<\xf88`\xe0\x00\x00\x00\x01\x00\xc1\x00\x81\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x14\x9cXX`x0@ \x00\x00\x00\x00\x00\x00\x00h\xf0\x00\xe0X\x80\x00p\x00 \x00\x00\x00\x00\x00\x00"
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
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ])),
    palette_id=SPAL787_PUNCHINELLO_STATUE,
    palette_offset=0,
    unknown_num=0)
