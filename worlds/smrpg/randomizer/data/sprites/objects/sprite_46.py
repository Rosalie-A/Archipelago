# SPR0046_STICK_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL534_STICK_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(389, length=189, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x18\x14\x08\x1c\x10\x18\x00\x00\x00\x00\x00\x00\x01\x00\x01\x04\x17\x03\x04,\x08\x18'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=130),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00P\x90\x00\xb0\xc6\x0cd\xb7\x13\xdf\x1c\xb7\x00\x00\x00\x00p\x80\x08\xc0\x1ea\x83\x1c\xc4?\x0f\xff'),
                            bytearray(b'\x00\x00\x1d\x01Q! \xef\x00C\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x03@\x0f_?\xc3\xc3\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe4\xeeD\x9c\xa0\xd8\x00\xb0\x00\xc0\x00\x00\x00\x00\x00\x00\x1e\xfe|\xfc8\xf8\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=122),
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
    palette_id=SPAL534_STICK_PACKET,
    palette_offset=0,
    unknown_num=0
)
