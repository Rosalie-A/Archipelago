# SPR0670_MACK_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL784_MACK_STATUE

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
                                None,
                                bytearray(
                                    b"\x00\x00\x00\x00\x01\x00\x02\x00\x02\x01\x0f\x08\x0c<\tA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00;\x00G0"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00 \x00@\x00P\x00\xe4\xc0\xd2\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x004\x00\xde\x00"
                                ),
                                None,
                                bytearray(
                                    b",\x0b\x06'\x00\x13\x03)\x04#\"\x10z\x10q\x00\x080.\x10\x10\x00(\x13#\x1c0/p\x7f~\x7f"
                                ),
                                bytearray(
                                    b"\xf2\x92\x1c\xdc\x08\x90\x08\x10\xb8\xd0|`\x1c\x1084\xfe\x00\x1c`\x10\xe8\x90\xe8\xc08x\x84\x18\xe44\xc8"
                                ),
                                None,
                                bytearray(
                                    b">\x00\x1f\x00\x0f\x0c\x07\x00\x07\x00\x07\x00\x03\x04\x01\x06??\x1f\x1f\r\r\x04\x00\x03\x00\x00\x04\x04\x03\x06\x01"
                                ),
                                bytearray(
                                    b"\x00d\xdc\xfa\xf8&\xf0\x0c\xe0x\xc0\x00\xc0\x00\x80@\xe4\x98\xec\xde\xf8\xfe\xf0\xfc`x\xc0\x00\x00@@\x80"
                                ),
                                None,
                                bytearray(
                                    b"\x00\x06\x00\x06\x04\x02\x06\x03\x07\x01\x03\x01\x00\x00\x00\x00\x07\x01\x07\x01\x03\x05\x01\x06\x00\x07\x00\x03\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"@@\x00@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x80\xc0\xc0\x80\x80\xc0\x80\xc0\x00\x80\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
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
    palette_id=SPAL784_MACK_STATUE,
    palette_offset=0,
    unknown_num=0)
