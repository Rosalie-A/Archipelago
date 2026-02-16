from .types import BowserPalette
from randomizer.types.flags import BowserPaletteOptions


# bowser palettes
class BowserDefault(BowserPalette):
    colours = [
        0xF8F0F0,
        0xF8F850,
        0xF0C830,
        0xB83810,
        0x503818,
        0x38A830,
        0x207820,
        0x184810,
        0x202818,
        0xC88020,
        0x884820,
        0x201008,
        0x909080,
        0x606040,
        0x181818,
    ]
    overworld_map_colours = [
        0xF8F8F8,
        0xF8F850,
        0xF0C830,
        0xB83810,
        0x503818,
        0x38A830,
        0x207820,
        0x184810,
        0x202818,
        0xC88020,
        0x884820,
        0x201008,
        0x909080,
        0x606040,
        0x181818,
    ]


class BowserDrybone(BowserPalette):
    colours = [
        0xF8F0F0,
        0xE8E0B0,
        0xF0E8C0,
        0xB81010,
        0x501818,
        0x383030,
        0x202020,
        0x181010,
        0x201818,
        0xC8B8A0,
        0x988870,
        0x200808,
        0x908080,
        0x604040,
        0x181818,
    ]
    poison_colours = [
        0xC098F8,
        0xB890D0,
        0xC090F0,
        0x880000,
        0x280000,
        0x180828,
        0x000008,
        0x000000,
        0x000000,
        0x9870C0,
        0x685080,
        0x000000,
        0x604090,
        0x381838,
        0x000000,
    ]
    underwater_colours = [
        0x8985B0,
        0x817D90,
        0x858198,
        0x691540,
        0x351944,
        0x292550,
        0x1D1D48,
        0x191540,
        0x1D1944,
        0x716988,
        0x595170,
        0x1D113C,
        0x554D78,
        0x3D2D58,
        0x191944,
    ]
    id = BowserPaletteOptions.DRYBONE
    name = "Dry Bone"
    author = "DEVILING"


class BowserCulex(BowserPalette):
    colours = [
        0xB0D8F8,
        0xC09848,
        0xB86028,
        0x982818,
        0x502010,
        0x705090,
        0x502870,
        0x381048,
        0x180808,
        0x984818,
        0x703010,
        0x201008,
        0x48A0D0,
        0x205888,
        0x102028,
    ]
    poison_colours = [
        0xD0C8F8,
        0xB87080,
        0xB04870,
        0x8D2058,
        0x481830,
        0x785090,
        0x582870,
        0x381048,
        0x180810,
        0x903058,
        0x682040,
        0x200B10,
        0x8070D0,
        0x484088,
        0x181828,
    ]
    underwater_colours = [
        0x5868B0,
        0x604858,
        0x583038,
        0x481040,
        0x281038,
        0x382878,
        0x281068,
        0x180858,
        0x080038,
        0x482040,
        0x381838,
        0x100838,
        0x205098,
        0x102878,
        0x081048,
    ]
    id = BowserPaletteOptions.CULEX
    name = "Culex"
    rename_character = False
    author = "AARONDOBBE"


class BowserWabowser(BowserPalette):
    colours = [
        0xF8F8C0,
        0xC8C8C8,
        0x909090,
        0x484848,
        0x383838,
        0xA880C8,
        0x8860B0,
        0x583080,
        0x202020,
        0x707070,
        0x384858,
        0x001018,
        0xE0B860,
        0xA88840,
        0x382010,
    ]
    poison_colours = [
        0xF8A8F8,
        0xD088F8,
        0x9058F8,
        0x382068,
        0x281050,
        0xA850F8,
        0x8830F8,
        0x5010D8,
        0x100020,
        0x6838B0,
        0x282090,
        0x000010,
        0xE87098,
        0xA85060,
        0x280000,
    ]
    underwater_colours = [
        0x7C7C91,
        0x646495,
        0x484879,
        0x242456,
        0x1C1C4E,
        0x544095,
        0x443089,
        0x2C1871,
        0x101042,
        0x383869,
        0x1C245E,
        0x00083E,
        0x705C62,
        0x544452,
        0x18103A,
    ]
    id = BowserPaletteOptions.WABOWSER
    name = "Wabowser"
    author = "HERRSHAUN"


class BowserRed(BowserPalette):
    colours = [
        0xF8F8F8,
        0xD0D0D0,
        0xF0C8C8,
        0xB83838,
        0x503838,
        0xA83830,
        0x782020,
        0x481810,
        0x202828,
        0xC88080,
        0x884848,
        0x884848,
        0x909090,
        0x606060,
        0x181818,
    ]
    poison_colours = [
        0xB8E0F8,
        0x98B8F8,
        0xB8A8F8,
        0x802038,
        0x282038,
        0x702028,
        0x500018,
        0x200000,
        0x000820,
        0x9068A8,
        0x582850,
        0x582850,
        0x6070C0,
        0x304070,
        0x000000,
    ]
    underwater_colours = [
        0x8989B4,
        0x7575A0,
        0x85719C,
        0x692954,
        0x352954,
        0x612950,
        0x491D48,
        0x311940,
        0x1D214C,
        0x714D78,
        0x51315C,
        0x51315C,
        0x555580,
        0x3D3D68,
        0x191944,
    ]
    id = BowserPaletteOptions.RED
    name = "Red"
    rename_character = False
    author = "DEVILING"


class BowserDark(BowserPalette):
    colours = [
        0xF8F8F8,
        0xF8F850,
        0xF0C830,
        0xB83810,
        0x503818,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0xC88020,
        0x884820,
        0x201008,
        0x909080,
        0x606040,
        0x181818,
    ]
    poison_colours = [
        0xA0F8F8,
        0xA0F860,
        0x98D028,
        0x702800,
        0x202800,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x808018,
        0x503818,
        0x000000,
        0x5090A8,
        0x285848,
        0x000000,
    ]
    underwater_colours = [
        0x82829A,
        0x828246,
        0x7E6A36,
        0x622226,
        0x2E222A,
        0x05051E,
        0x05051E,
        0x05051E,
        0x05051E,
        0x6A462E,
        0x4A2A2E,
        0x160E22,
        0x4E4E5E,
        0x36363E,
        0x12122A,
    ]
    id = BowserPaletteOptions.DARK
    name = "Dark"
    rename_character = False
    author = "EGGTALK"


class BowserKronk(BowserPalette):
    colours = [
        0xF8F080,
        0xD8B8A0,
        0xB89068,
        0x383838,
        0x181010,
        0xD82830,
        0xA81820,
        0x600000,
        0x300000,
        0x886848,
        0x704830,
        0x201008,
        0xD0B060,
        0x806820,
        0x482810,
    ]
    poison_colours = [
        0xF8B0F8,
        0xF888F8,
        0xD068E0,
        0x382070,
        0x180018,
        0xF81860,
        0xC01038,
        0x680000,
        0x300000,
        0x984898,
        0x803060,
        0x200000,
        0xE888D0,
        0x904838,
        0x501818,
    ]
    underwater_colours = [
        0x7C7871,
        0x6C5C81,
        0x5C4865,
        0x1C1C4E,
        0x0C083A,
        0x6C144A,
        0x540C42,
        0x300032,
        0x180032,
        0x443456,
        0x38244A,
        0x100836,
        0x685862,
        0x403442,
        0x24143A,
    ]
    id = BowserPaletteOptions.KRONK
    name = "Korush"
    author = "HERRSHAUN"


class BowserZeccet(BowserPalette):
    colours = [
        0xF8F8F8,
        0xF8D8B0,
        0xE0B088,
        0x703038,
        0x481E24,
        0xC84858,
        0xA04068,
        0x683858,
        0x482840,
        0xB08860,
        0x886048,
        0x201008,
        0x909080,
        0x606040,
        0x181818,
    ]
    poison_colours = [
        0xA8F8F8,
        0xA8E0F8,
        0x98B0B0,
        0x382038,
        0x201018,
        0x883868,
        0x603088,
        0x302868,
        0x201848,
        0x708870,
        0x505850,
        0x000000,
        0x5890A8,
        0x305848,
        0x000000,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C6C89,
        0x705875,
        0x38184E,
        0x241042,
        0x64245E,
        0x502065,
        0x341C5E,
        0x241452,
        0x584462,
        0x443056,
        0x100836,
        0x484871,
        0x303052,
        0x0C0C3E,
    ]
    id = BowserPaletteOptions.ZECCET
    name = "Zeccet"
    author = "PIDGEZERO_ONE"


class BowserBlue(BowserPalette):
    colours = [
        0xF8F8F8,
        0xCACEA5,
        0xBCBB6F,
        0xC76714,
        0x21451C,
        0x4E4EE8,
        0x3D3DB8,
        0x1818A5,
        0x103008,
        0x699C69,
        0x387131,
        0x201008,
        0x909080,
        0x606040,
        0x181818,
    ]
    poison_colours = [
        0xF8E088,
        0xE0B050,
        0xD0A028,
        0xE05000,
        0x102800,
        0x483080,
        0x302860,
        0x080050,
        0x001800,
        0x688828,
        0x285808,
        0x100000,
        0x987040,
        0x584810,
        0x080000,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x646885,
        0x605C69,
        0x64343A,
        0x102442,
        0x2828A5,
        0x20208D,
        0x0C0C85,
        0x081836,
        0x345065,
        0x1C384A,
        0x100836,
        0x484871,
        0x303052,
        0x0C0C3E,
    ]
    id = BowserPaletteOptions.BLUE
    name = "Melee Blue"
    rename_character = False
    author = "PIDGEZERO_ONE"


class BowserSking(BowserPalette):
    colours = [
        0xF8F8F8,
        0xF8E0C8,
        0xE09870,
        0x985010,
        0x181818,
        0x284050,
        0x203040,
        0x182028,
        0x700000,
        0x586848,
        0x786828,
        0x383838,
        0xD0C8C8,
        0x786860,
        0x181818,
    ]
    poison_colours = [
        0xA8F8F8,
        0xA8F8B0,
        0x989868,
        0x604800,
        0x000000,
        0x003048,
        0x002030,
        0x001018,
        0xA80000,
        0x087038,
        0x286818,
        0x102850,
        0x88D0D0,
        0x486058,
        0x000000,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C68A0,
        0x704C69,
        0x4C2839,
        0x0C0C3D,
        0x142059,
        0x101851,
        0x0C1045,
        0xA80031,
        0x000058,
        0x002048,
        0x1C1C99,
        0x686495,
        0x3C3461,
        0x0C0C3D,
    ]
    id = BowserPaletteOptions.SKING
    name = "S.King"
    author = "SMBAI"
    rename_character = False


all_palettes: list[BowserPalette] = [
    BowserDefault(),
    BowserDrybone(),
    BowserCulex(),
    BowserWabowser(),
    BowserRed(),
    BowserDark(),
    BowserKronk(),
    BowserZeccet(),
    BowserBlue(),
    BowserSking(),
]
