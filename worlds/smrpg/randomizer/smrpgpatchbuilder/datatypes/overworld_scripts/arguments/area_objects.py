"""Int subclass instances representing valid field NPC designations 
that can be used in action and event script commands.\n
The first 11 are in the range specifiable as party characters."""

from .types.area_object import (
    AreaObject,
)
from .types.party_character import (
    PartyCharacter,
)

MARIO = PartyCharacter(0x00)
TOADSTOOL = PartyCharacter(0x01)
BOWSER = PartyCharacter(0x02)
GENO = PartyCharacter(0x03)
MALLOW = PartyCharacter(0x04)
DUMMY_0X05 = PartyCharacter(0x05)
DUMMY_0X06 = PartyCharacter(0x06)
DUMMY_0X07 = PartyCharacter(0x07)
CHARACTER_IN_SLOT_1 = PartyCharacter(0x08)
CHARACTER_IN_SLOT_2 = PartyCharacter(0x09)
CHARACTER_IN_SLOT_3 = PartyCharacter(0x0A)
DUMMY_0X0B = PartyCharacter(0x0B)
SCREEN_FOCUS = AreaObject(0x0C)
LAYER_1 = AreaObject(0x0D)
LAYER_2 = AreaObject(0x0E)
LAYER_3 = AreaObject(0x0F)
MEM_70A8 = AreaObject(0x10)
MEM_70A9 = AreaObject(0x11)
MEM_70AA = AreaObject(0x12)
MEM_70AB = AreaObject(0x13)
NPC_0 = AreaObject(0x14)
NPC_1 = AreaObject(0x15)
NPC_2 = AreaObject(0x16)
NPC_3 = AreaObject(0x17)
NPC_4 = AreaObject(0x18)
NPC_5 = AreaObject(0x19)
NPC_6 = AreaObject(0x1A)
NPC_7 = AreaObject(0x1B)
NPC_8 = AreaObject(0x1C)
NPC_9 = AreaObject(0x1D)
NPC_10 = AreaObject(0x1E)
NPC_11 = AreaObject(0x1F)
NPC_12 = AreaObject(0x20)
NPC_13 = AreaObject(0x21)
NPC_14 = AreaObject(0x22)
NPC_15 = AreaObject(0x23)
NPC_16 = AreaObject(0x24)
NPC_17 = AreaObject(0x25)
NPC_18 = AreaObject(0x26)
NPC_19 = AreaObject(0x27)
NPC_20 = AreaObject(0x28)
NPC_21 = AreaObject(0x29)
NPC_22 = AreaObject(0x2A)
NPC_23 = AreaObject(0x2B)
NPC_24 = AreaObject(0x2C)
NPC_25 = AreaObject(0x2D)
NPC_26 = AreaObject(0x2E)
NPC_27 = AreaObject(0x2F)

AREAOBJECT_FROM_NPC_ID: list[AreaObject] = [
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_5,
    NPC_6,
    NPC_7,
    NPC_8,
    NPC_9,
    NPC_10,
    NPC_11,
    NPC_12,
    NPC_13,
    NPC_14,
    NPC_15,
    NPC_16,
    NPC_17,
    NPC_18,
    NPC_19,
    NPC_20,
    NPC_21,
    NPC_22,
    NPC_23,
    NPC_24,
    NPC_25,
    NPC_26,
    NPC_27,
]
