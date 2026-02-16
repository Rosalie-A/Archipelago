# SPR0743_FIRE_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL325_FIRE_CRYSTAL_3D, SPAL406_FIRE_CRYSTAL
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'),
                            bytearray(b'\x10\x00\x08\x08((<\x1c$\x14\xd4\x0c\xe6 \xe6$\x10\x00\x00\x18\x008\x00\x18\x18\\\x80<\x1e \x1e '),
                            None,
                            bytearray(b'\x01\x00\x01\x00\x07\x04\x03\x00\x07\x00\x01\x04\x03\x02\x00\x02\x00\x00\x00\x02\x00\x04\x00\x04\x04\x00\x00\x02\x00\x02\x00\x01'),
                            bytearray(b'\xeb/\xa5\x01\xfbE\xf0\x0f\tv\x08w\x80\xfc\xff\xff<\n\x1ag\x02\x7fA\x7f\x01\xff\x00\xff\x03\xff\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\xc0@\xc0\xc0\x80\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x00\x80\x80\xc0@\x80'),
                            bytearray(b'\x01\x03\x01\x00\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbf\xcf\x1b\xfc!\xfay\xf2\x97\xe00\x812\xc8\xf2J\x7f\xc0\xbb\xc4\xa5\xdc\xfd\x8c\x1f\xf8\xfe\xfe\xfe\xfc\xbc|'),
                            bytearray(b'@\xc0\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'`\xc4d@\x00`X \x08h000  0<|<xxxx000\x000\x10 \x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL325_FIRE_CRYSTAL_3D,
    palette_offset=0,
    unknown_num=8
)
