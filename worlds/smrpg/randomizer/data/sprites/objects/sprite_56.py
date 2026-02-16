# SPR0056_CHOMP_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL537_CHOMP_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(391, length=731, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00 0\x0c,\x98\xfc\xbc\x8c\xc0`@\xc0\x00\x00\x00\x008 ,\x18\xb0\xcc\xb4L\x00\xe0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x16\x1b[~\x7f|F\x07]D7?\x00\x00\x01\x01\x11\x1e}@|\x1fe\x06#@3\x0f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5\xb0~\xd0hc\x00\xf9\x7f<8\x1c\x1f\x03\x03D\x84\xe1\x00\xd7 \xcf0o\xf0\x10?\x08\x1f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=122),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0)
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL537_CHOMP_PACKET,
    palette_offset=0,
    unknown_num=0
)
