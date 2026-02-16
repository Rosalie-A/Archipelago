# SPR0678_BOOMER_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL791_BOOMER_STATUE

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
                                    b"\x00\x00\x00\x00\x00\x00\x01\x05\x0c\x02\x0f\x00\x0f\x01\x07\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x0c\x00\x0e\x00\x0e\x00\x04"
                                ),
                                bytearray(
                                    b"\x08\x06\x1f\x10\x1f ~\x01\xfc\x02\xfa\xe4\xff\xe0<#\x00\x00\x00\x00\x01\x00\x03\x80\x06\x01\x04\x03\x06\x01\x06\xe1"
                                ),
                                None,
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00p"
                                ),
                                bytearray(
                                    b"\x03\x0f\x03\x0f\x03\x1d+\x00) $\x1b\x0c?\x1f\t\x00\x01\x00\x01\x18\x00\x1f+>\r\x07<?\x00&\x01"
                                ),
                                bytearray(
                                    b"\x1c\x03<#\xf8\xc7q\x0e\xc0?\x88w\xa8V\x91\xac\xc7\xe0\x07\xe0\x0f\x00\x9e\x01\xbf\xc0\x86\x89\x85\xe9o\x91"
                                ),
                                bytearray(
                                    b"\xe0\xf0\xe0\xf0@\xf0\x80`\xc0\x00\xd0P`\x10\x808\xe0\x00\xe0\x00@\xa0\x00\x80\x00\xc0p\x80\x80p\xd8\x80"
                                ),
                                bytearray(
                                    b"1\x0e\x03\x0c\x01\x0e\x02\x01\x00\x01\x00\x00\x00\x00\x00\x00\x061\x0c\x03\x0e\x01\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"_\x8f\x18\xf8\x1e\xee\x1f\xe7\x1f\xc0\x05\x02\x00\x1e\x00\x19\xa0g\xe1\x07\xe0\x07\xe0\x00\xc0 \x00\x18\x10\x07\x16\x08"
                                ),
                                bytearray(
                                    b"\x1adyF\xf8\xc7\xf8\x07\xf0\x0f\xe0\x1f\x00\x0f\x00\xff-\x82\x86\xc1\x0f\x80\x1f\x00\x1f\x00\xfe\x01\x07\xf8\xff\x00"
                                ),
                                bytearray(
                                    b" \x18@\xb8\x80x\x00\xe0PP\x10\x90`\xbc \xdc\xd8\xa08@x\x80\xe0\x00p\x00\xb0 \xac@\xdc "
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x13 \x020 \x10`\x00\xc0\xa0\xd4\xe0\x00\x1f\x00\x03/\x17/\x07\x0f7\x1f.\x1f\x0e/\x16\x1f\x00\x03\x00"
                                ),
                                bytearray(
                                    b"\x00\x7f\x10o\x10o _\xa0\xdf\xa0\xdf\x04\xfb\x1c\xfb\x9f@\x8fP\x8fP\x9f \x9f \x9f \xff\x00\xe3\x10"
                                ),
                                bytearray(
                                    b"\x00\xf8@\xb80\xc8\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\x80\xf8\x00\xd8\x00\xc8\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\x80\x00"
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
    palette_id=SPAL791_BOOMER_STATUE,
    palette_offset=0,
    unknown_num=0)
