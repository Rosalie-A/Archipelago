# SPR0673_BOWYER_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL786_BOWYER_STATUE

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
                            format=1,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x03\x00\x02\x00\x07\x00\x070$\x13`vc$\x00\x00\x00\x00\x01\x00\x00\x000\x003\x00v\t!^"
                                ),
                                bytearray(
                                    b"\xc0 P\xcc\xf0\x80\xee8\xe6\x1c\x9cx\xe8H@\x00\x00\x000\x00\x1c\x00F\x00\x03\x00\x05\x00\xb6\x00\xfa\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\r"
                                ),
                                bytearray(
                                    b"gR_^\x7f\x05}\x01?\x00\x1e \x18xW\xb7\x0bt\x07xZezE/2><tp\xae\xa7"
                                ),
                                bytearray(
                                    b"<\x00\xe0\x00\xe0\x00 \x00 \x00 \x00 \x00\xa0\x80\xfc\x00\xd00\xd0\xb0\x900\x100\x100\x100\x10\xb0"
                                ),
                                bytearray(
                                    b"y\x00H\x00\xd8\x00T\x00\x00 \x00\x00\x00\x00\x00\x00\x07~\xb0\xfe\x00\xfc\x0cx\x00 \x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"x\x10X1]g4D2HuE{c\x7fv\x08\x00\t\x01F_Hx\x0exn\\lr;2"
                                ),
                                bytearray(
                                    b"(\x00 \x884\x180\x10\xd8\xe0\xd0\xc0\xa0\x80 \x00T0\x94\xb0\x84 \x08 \x18\x000\x00`\x00\xe0\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x01\x03\x00\x02\x01\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x01\x03\x01\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xdb{\xe7!\x9cA?\x80\x7f\x02\xff\x00\x1f\x00\x03\x00&\xe2\x07\xc1\x1f\xe3|\xc3\xfc\x81\xfc\x03\x1c\x03\x03\x00"
                                ),
                                bytearray(
                                    b"\xc0\x00\x80\x80\x80\x80\xc0@`@ \x80\xa0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x80\xa0\x80`\xc0`\xc0\xc0\x00"
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
    palette_id=SPAL786_BOWYER_STATUE,
    palette_offset=0,
    unknown_num=0)
