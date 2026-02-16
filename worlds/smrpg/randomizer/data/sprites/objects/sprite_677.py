# SPR0677_CZAR_DRAGON_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL790_CZAR_DRAGON_STATUE

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
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x01\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00 \x10a0Fe\x18F\xb0|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x009\x00\xfa\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x07\x00\x06\x03\x10\t9\x07^\x01t\x83x\xc7\n\xf4\x04\x00\x02\x01\x1f\x00?\x00w\n_\xa4\x7f\x8c\r\xfe"
                                ),
                                bytearray(
                                    b"x\x86\xb8f\xf9'\xfa\xa5sD\xaf\x84\xd7\xc4\xfe\xe5\x8e\x00\xae@/@\xeeC\xdf\x05\xff\xac\xf7\xdd\xd7\xff"
                                ),
                                bytearray(
                                    b"  \xf0\xc00\xf0\xf8 \xf8\x00\xf8\x88y\x98}\x8c \x10\xc00\x00\xf8\x00\xf8\x00\xf9\x80y\x80\xfb\xcc\xfb"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00@\x00\xc0@\xc0P\x90\x08\x80\x8c\x00\x00\x00\x000p \xe0\x00\xc0\x00\xd0\x10\x88\x04\x88"
                                ),
                                bytearray(
                                    b"\x87xM3\x0f/\t\x1f\x03\x10\x0e\x00\x00\x00\x00\x00\x88\x7fP=\x10\x0f\t\t\x00\x1f\x00\x0e\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xc6\xd5\xe4\xea\xc1\xc1\x81\x07\x83\x06\x0e\n\x1e\x10\x1f\x11\xbb\xd77\xeen\xc1@\xc7\x03\x85\x0f\x04\x1e\x05\x1f\x00"
                                ),
                                bytearray(
                                    b"\xff\x03\xff\x93\xa1]\xb0V(\xabXY\xff\x8f\xcf7|\xa3L\xf3\xde\xef\xdf\xf1\xdf\xac\xbf^\x7f\xff\xfd\x8b"
                                ),
                                bytearray(
                                    b"\xc4\x9c\x88\xf8\x9a\xf2\x9e\xfa\x1e\x90\xff\xf1\xfe\xc9\x94\xbeh\xf4`\x98z\x98\xfe\x94\xfe\xe4\xff\xc0\xeb\xc3\xc3\xbe"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b">\t\x14>\x04:\x08\x14\x00\x08\x00\x00\x00\x00\x00\x00+\x03\x03>\x07>\x0f\x1c\x0e\x08\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xfev?c\xff\xe3}\x12(|\tu\x10(\x00\x10}\xea\xfc\x0b>\xc1V\x07\x07|\x0e}\x1e8\x1c\x10"
                                ),
                                bytearray(
                                    b"DzhT\xe0\xe8\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\x87~\xaf\\\xfe\xe8\xe0\xe0\x00\x80\x00\x00\x00\x00\x00\x00"
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
    palette_id=SPAL790_CZAR_DRAGON_STATUE,
    palette_offset=0,
    unknown_num=0)
