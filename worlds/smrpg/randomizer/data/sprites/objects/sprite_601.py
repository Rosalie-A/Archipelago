# SPR0601_HAMMER_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL531_HAMMER_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(388, length=426, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x08\r\x00\x120\x00<A\xfc\x80\x01\x00\x01\x00\x03\x00\x0f\x00\x1f\x00/\x00\x03\x00\x83\x00'),
                            bytearray(b'@\x00x\x98$\xa0\x18Z\x16}$\xac\n\xb9\x04b\x80@\x98`|\xc0\xac\xc0\xcd\x12\xdc#x\x07\xe1\x1f'),
                            bytearray(b'\xfe\x81~\xc1\x7f\xf1\xbe0\\>\x0f=\x07\x03\x05\x00\x01\x00\x81\x00\x81\x00\xc0\x01A\x01!\x03\x0b\x17\r\r'),
                            bytearray(b'\x90\xa3G/\x8eN\x1c\x9cx\xf0\xf0\xf0\x80\xc0\x80\x80\x8f\x7f\x1f\xff>\xfe|\xfc\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL531_HAMMER_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
