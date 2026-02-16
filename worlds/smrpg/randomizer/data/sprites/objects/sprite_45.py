# SPR0045_HAMMER_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL349_HAMMER_PACKET

sprite = CompleteSprite(
    animation=AnimationPack(
        201,
        length=140,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=False,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=4,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x88\x00\xa8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00P\x00"
                                ),
                                None,
                                None,
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=133,
                            y=118),
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=7,
                            subtile_bytes=[
                                bytearray(
                                    b"\x07\x00\x0f\x08\x03\x0e\x17\n= 7(;\x147\x10\x07\x07\x0f\x07\x1f\x01\r\x02\x05\x02(\x00\x04\x00H\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\xe0\x00p\x08\xe0\x80\xc0\x80\xc0\x00\xc0@\xc0Y\x00\xc0\xe0\xf0x\xf0\x18\x008\x008\x00?\x00&\x00"
                                ),
                                bytearray(
                                    b"'\x01'0/'>68\x18\x1c\x1c\x00\x05\x00\x00x\x00X\x10\x10\x00A\x00\x07\x00\x03\x00\x02\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x80\x92@x\x000\x00p\x00\xe0\x00\xe0\x00\xc0\x00\x00j\x02\x80\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=117,
                            y=118),
                    ])
            ],
            sequences=[
                AnimationSequence(
                    frames=[AnimationSequenceFrame(duration=2, mold_id=0)]
                ),
            ])),
    palette_id=SPAL349_HAMMER_PACKET,
    palette_offset=0,
    unknown_num=8)
