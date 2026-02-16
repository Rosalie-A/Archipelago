"""ROM's PackCollection disassembled from the original game."""

from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    Formation,
    FormationMember,
    FormationPack,
    PackCollection,
)
from smrpgpatchbuilder.datatypes.battles.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CorndillyMusic,
    BoosterHillMusic,
    VolcanoMusic,
    CulexMusic,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from ..enemies.enemies import *
from ..variables.pack_names import *
from ..variables.battle_event_names import *


# ============================================================================
# Formation Declarations
# ============================================================================

FORM0000 = Formation(
    id=0,
    members=[
        FormationMember(SNIFITEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0001 = Formation(
    id=1,
    members=[
        FormationMember(SPIKEYEnemy, 135, 127),
        FormationMember(SPIKEYEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0002 = Formation(
    id=2,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0003 = Formation(
    id=3,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0004 = Formation(
    id=4,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
        FormationMember(FROGOGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0005 = Formation(
    id=5,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0006 = Formation(
    id=6,
    members=[
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0007 = Formation(
    id=7,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 103),
        FormationMember(SKYTROOPAEnemy, 231, 135),
        None,
        FormationMember(GOOMBAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0008 = Formation(
    id=8,
    members=[
        FormationMember(SKYTROOPAEnemy, 199, 151),
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(FROGOGEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0009 = Formation(
    id=9,
    members=[
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0010 = Formation(
    id=10,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0011 = Formation(
    id=11,
    members=[
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(FROGOGEnemy, 167, 111),
        FormationMember(SPIKEYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0012 = Formation(
    id=12,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 215, 135),
        FormationMember(SPIKEYEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0013 = Formation(
    id=13,
    members=[
        FormationMember(K9Enemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0014 = Formation(
    id=14,
    members=[
        FormationMember(K9Enemy, 199, 159),
        FormationMember(K9Enemy, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0015 = Formation(
    id=15,
    members=[
        FormationMember(K9Enemy, 135, 119),
        FormationMember(K9Enemy, 199, 151),
        FormationMember(SPIKEYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0016 = Formation(
    id=16,
    members=[
        FormationMember(K9Enemy, 183, 127),
        FormationMember(FROGOGEnemy, 215, 143),
        FormationMember(FROGOGEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0017 = Formation(
    id=17,
    members=[
        FormationMember(SHYSTEREnemy, 167, 119),
        FormationMember(SHYSTEREnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0018 = Formation(
    id=18,
    members=[
        FormationMember(SHYSTEREnemy, 151, 111),
        FormationMember(SHYSTEREnemy, 215, 143),
        FormationMember(SHYSTEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0019 = Formation(
    id=19,
    members=[
        FormationMember(RATFUNKEnemy, 199, 143),
        FormationMember(RATFUNKEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0020 = Formation(
    id=20,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(SHADOWEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0021 = Formation(
    id=21,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(HOBGOBLINEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0022 = Formation(
    id=22,
    members=[
        FormationMember(RATFUNKEnemy, 167, 135),
        None,
        FormationMember(HOBGOBLINEnemy, 167, 103),
        FormationMember(HOBGOBLINEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0023 = Formation(
    id=23,
    members=[
        FormationMember(THEBIGBOOEnemy, 151, 119),
        FormationMember(SHADOWEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0024 = Formation(
    id=24,
    members=[
        FormationMember(THEBIGBOOEnemy, 119, 119),
        FormationMember(SHADOWEnemy, 167, 135),
        FormationMember(HOBGOBLINEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0025 = Formation(
    id=25,
    members=[
        FormationMember(THEBIGBOOEnemy, 231, 135),
        FormationMember(THEBIGBOOEnemy, 151, 143),
        FormationMember(THEBIGBOOEnemy, 167, 103),
        FormationMember(SHADOWEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0026 = Formation(
    id=26,
    members=[
        FormationMember(GOBYEnemy, 135, 119),
        FormationMember(GOBYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0027 = Formation(
    id=27,
    members=[
        FormationMember(GOBYEnemy, 151, 119),
        FormationMember(GOBYEnemy, 215, 119),
        FormationMember(GOBYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0028 = Formation(
    id=28,
    members=[
        FormationMember(CROOKEnemyStatic, 167, 111),
        FormationMember(CROOKEnemyStatic, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0029 = Formation(
    id=29,
    members=[
        FormationMember(CROOKEnemyStatic, 199, 143),
        FormationMember(CROOKEnemyStatic, 151, 119),
        FormationMember(SHYGUYEnemyStatic, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0030 = Formation(
    id=30,
    members=[
        FormationMember(CROOKEnemyStatic, 183, 127),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0031 = Formation(
    id=31,
    members=[
        FormationMember(CROOKEnemyStatic, 199, 159),
        None,
        None,
        FormationMember(STARSLAPEnemy, 215, 127),
        FormationMember(ARACHNEEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0032 = Formation(
    id=32,
    members=[
        FormationMember(SHYGUYEnemyStatic, 151, 111),
        None,
        FormationMember(STARSLAPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0033 = Formation(
    id=33,
    members=[
        FormationMember(SHYGUYEnemyStatic, 135, 103),
        FormationMember(SHYGUYEnemyStatic, 215, 143),
        None,
        FormationMember(SNAPDRAGONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0034 = Formation(
    id=34,
    members=[
        FormationMember(SHYGUYEnemyStatic, 231, 135),
        None,
        FormationMember(CROOKEnemyStatic, 199, 143),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0035 = Formation(
    id=35,
    members=[
        FormationMember(STARSLAPEnemy, 199, 159),
        FormationMember(SHYGUYEnemyStatic, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0036 = Formation(
    id=36,
    members=[
        FormationMember(STARSLAPEnemy, 215, 151),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0037 = Formation(
    id=37,
    members=[
        FormationMember(STARSLAPEnemy, 167, 135),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0038 = Formation(
    id=38,
    members=[
        FormationMember(STARSLAPEnemy, 199, 151),
        FormationMember(STARSLAPEnemy, 167, 103),
        FormationMember(STARSLAPEnemy, 231, 135),
        FormationMember(STARSLAPEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0039 = Formation(
    id=39,
    members=[
        FormationMember(WIGGLEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0040 = Formation(
    id=40,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(AMANITAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0041 = Formation(
    id=41,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(WIGGLEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0042 = Formation(
    id=42,
    members=[
        FormationMember(WIGGLEREnemy, 151, 119),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0043 = Formation(
    id=43,
    members=[
        FormationMember(AMANITAEnemy, 135, 127),
        FormationMember(AMANITAEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0044 = Formation(
    id=44,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(BUZZEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0045 = Formation(
    id=45,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0046 = Formation(
    id=46,
    members=[
        FormationMember(AMANITAEnemy, 151, 127),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
        FormationMember(BUZZEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0047 = Formation(
    id=47,
    members=[
        FormationMember(BUZZEREnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0048 = Formation(
    id=48,
    members=[
        FormationMember(BUZZEREnemy, 167, 103),
        FormationMember(BUZZEREnemy, 231, 135),
        FormationMember(AMANITAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0049 = Formation(
    id=49,
    members=[
        FormationMember(BUZZEREnemy, 199, 151),
        None,
        FormationMember(GUERRILLAEnemy, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0050 = Formation(
    id=50,
    members=[
        FormationMember(BUZZEREnemy, 199, 159),
        None,
        FormationMember(GUERRILLAEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0051 = Formation(
    id=51,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0052 = Formation(
    id=52,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(SHYRANGEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0053 = Formation(
    id=53,
    members=[
        FormationMember(SPARKYEnemy, 167, 135),
        FormationMember(SPARKYEnemy, 151, 111),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0054 = Formation(
    id=54,
    members=[
        FormationMember(APPRENTICEEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0055 = Formation(
    id=55,
    members=[
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0056 = Formation(
    id=56,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0057 = Formation(
    id=57,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 215, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
        FormationMember(SHYRANGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0058 = Formation(
    id=58,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 111),
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
        FormationMember(PIRANHAPLANTEnemyStatic, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0059 = Formation(
    id=59,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
        FormationMember(PIRANHAPLANTEnemyStatic, 199, 119),
        FormationMember(PIRANHAPLANTEnemyStatic, 231, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 199, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0060 = Formation(
    id=60,
    members=[
        FormationMember(BOBOMBEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0061 = Formation(
    id=61,
    members=[
        FormationMember(BOBOMBEnemyStatic, 135, 119),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0062 = Formation(
    id=62,
    members=[
        FormationMember(BOBOMBEnemyStatic, 151, 127),
        FormationMember(BOBOMBEnemyStatic, 167, 103),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(BOBOMBEnemyStatic, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0063 = Formation(
    id=63,
    members=[
        FormationMember(BOBOMBEnemyStatic, 135, 119),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(ENIGMAEnemy, 183, 111),
        FormationMember(CLUSTEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0064 = Formation(
    id=64,
    members=[
        FormationMember(SPARKYEnemy, 199, 151),
        FormationMember(ENIGMAEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0065 = Formation(
    id=65,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(BOBOMBEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0066 = Formation(
    id=66,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
        FormationMember(CLUSTEREnemy, 231, 143),
        FormationMember(CLUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0067 = Formation(
    id=67,
    members=[
        FormationMember(SPARKYEnemy, 183, 143),
        FormationMember(SPARKYEnemy, 151, 127),
        FormationMember(ENIGMAEnemy, 167, 103),
        FormationMember(ENIGMAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0068 = Formation(
    id=68,
    members=[
        FormationMember(MAGMITEEnemy, 167, 111),
        FormationMember(MAGMITEEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0069 = Formation(
    id=69,
    members=[
        FormationMember(MAGMITEEnemy, 151, 111),
        FormationMember(BOBOMBEnemyStatic, 183, 127),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0070 = Formation(
    id=70,
    members=[
        FormationMember(MAGMITEEnemy, 151, 127),
        FormationMember(MAGMITEEnemy, 183, 143),
        FormationMember(CLUSTEREnemy, 167, 103),
        FormationMember(CLUSTEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0071 = Formation(
    id=71,
    members=[
        FormationMember(MAGMITEEnemy, 135, 103),
        FormationMember(MAGMITEEnemy, 231, 151),
        FormationMember(BOBOMBEnemyStatic, 167, 135),
        None,
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0072 = Formation(
    id=72,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0073 = Formation(
    id=73,
    members=[
        FormationMember(LAKITUEnemy, 135, 119),
        FormationMember(SPIKESTEREnemy, 199, 159),
        FormationMember(ARTICHOKEREnemy, 183, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0074 = Formation(
    id=74,
    members=[
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0075 = Formation(
    id=75,
    members=[
        FormationMember(LAKITUEnemy, 231, 151),
        FormationMember(LAKITUEnemy, 135, 103),
        None,
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0076 = Formation(
    id=76,
    members=[
        FormationMember(SPIKESTEREnemy, 215, 143),
        FormationMember(CARROBOSCISEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0077 = Formation(
    id=77,
    members=[
        FormationMember(SPIKESTEREnemy, 199, 151),
        FormationMember(SPIKESTEREnemy, 135, 119),
        FormationMember(ARTICHOKEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0078 = Formation(
    id=78,
    members=[
        FormationMember(SPIKESTEREnemy, 183, 127),
        FormationMember(CARROBOSCISEnemy, 135, 119),
        FormationMember(CARROBOSCISEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0079 = Formation(
    id=79,
    members=[
        FormationMember(SPIKESTEREnemy, 119, 111),
        FormationMember(SPIKESTEREnemy, 215, 159),
        FormationMember(SPIKESTEREnemy, 215, 135),
        FormationMember(SPIKESTEREnemy, 167, 111),
        FormationMember(CARROBOSCISEnemy, 151, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0080 = Formation(
    id=80,
    members=[
        FormationMember(SPOOKUMEnemy, 199, 135),
        FormationMember(ORBUSEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0081 = Formation(
    id=81,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(JESTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0082 = Formation(
    id=82,
    members=[
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 167, 151),
        FormationMember(ORBUSEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0083 = Formation(
    id=83,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(REMOCONEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0084 = Formation(
    id=84,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0085 = Formation(
    id=85,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
        FormationMember(ROBOMBEnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0086 = Formation(
    id=86,
    members=[
        FormationMember(ROBOMBEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0087 = Formation(
    id=87,
    members=[
        FormationMember(ROBOMBEnemy, 135, 127),
        FormationMember(ROBOMBEnemy, 231, 127),
        FormationMember(ROBOMBEnemy, 183, 103),
        FormationMember(ROBOMBEnemy, 183, 151),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0088 = Formation(
    id=88,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(JESTEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0089 = Formation(
    id=89,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 135),
        FormationMember(REMOCONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0090 = Formation(
    id=90,
    members=[
        FormationMember(CHOMPEnemy, 151, 111),
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0091 = Formation(
    id=91,
    members=[
        FormationMember(CHOMPEnemy, 199, 119),
        None,
        FormationMember(JESTEREnemy, 135, 103),
        FormationMember(JESTEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0092 = Formation(
    id=92,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0093 = Formation(
    id=93,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0094 = Formation(
    id=94,
    members=[
        FormationMember(BLASTEREnemy, 199, 151),
        FormationMember(BLASTEREnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0095 = Formation(
    id=95,
    members=[
        FormationMember(BLASTEREnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 135, 103),
        FormationMember(ROBOMBEnemy, 231, 151),
        FormationMember(SPOOKUMEnemy, 151, 127),
        FormationMember(SPOOKUMEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0096 = Formation(
    id=96,
    members=[
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 105, 133, hidden_at_start=True),
        FormationMember(WATERCRYS3DEnemy, 121, 149, hidden_at_start=True),
        FormationMember(EARTHCRYS3DEnemy, 153, 165, hidden_at_start=True),
        FormationMember(WINDCRYS3DEnemy, 185, 173, hidden_at_start=True),
    ],
    music=CulexMusic(),
    unknown_bit=True,
    run_event_at_load=77,
)

FORM0097 = Formation(
    id=97,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0098 = Formation(
    id=98,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 119),
        FormationMember(MUKUMUKUEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0099 = Formation(
    id=99,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 111),
        FormationMember(MUKUMUKUEnemy, 215, 143),
        FormationMember(PULSAREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0100 = Formation(
    id=100,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 111),
        FormationMember(GECKOEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0101 = Formation(
    id=101,
    members=[
        FormationMember(SACKITEnemy, 199, 151),
        FormationMember(SACKITEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0102 = Formation(
    id=102,
    members=[
        FormationMember(SACKITEnemy, 151, 127),
        FormationMember(SACKITEnemy, 183, 143),
        FormationMember(MUKUMUKUEnemy, 167, 103),
        FormationMember(GECKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0103 = Formation(
    id=103,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        None,
        FormationMember(PULSAREnemy, 167, 103),
        FormationMember(PULSAREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0104 = Formation(
    id=104,
    members=[
        FormationMember(SACKITEnemy, 215, 143),
        FormationMember(MASTADOOMEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0105 = Formation(
    id=105,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(SACKITEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0106 = Formation(
    id=106,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(MASTADOOMEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0107 = Formation(
    id=107,
    members=[
        FormationMember(GECKOEnemy, 183, 143),
        FormationMember(GECKOEnemy, 151, 127),
        FormationMember(MUKUMUKUEnemy, 135, 103),
        FormationMember(MUKUMUKUEnemy, 231, 151),
        FormationMember(SACKITEnemy, 183, 111),
        FormationMember(SACKITEnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0108 = Formation(
    id=108,
    members=[
        FormationMember(GECKOEnemy, 135, 103),
        FormationMember(GECKOEnemy, 231, 151),
        FormationMember(MASTADOOMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0109 = Formation(
    id=109,
    members=[
        FormationMember(ZEOSTAREnemy, 135, 119),
        FormationMember(ZEOSTAREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0110 = Formation(
    id=110,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 135),
        FormationMember(ZEOSTAREnemy, 183, 103),
        FormationMember(BLOOBEREnemyStatic, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0111 = Formation(
    id=111,
    members=[
        FormationMember(ZEOSTAREnemy, 199, 119),
        FormationMember(ZEOSTAREnemy, 167, 135),
        FormationMember(LEUKOEnemy, 167, 103),
        FormationMember(LEUKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0112 = Formation(
    id=112,
    members=[
        FormationMember(ZEOSTAREnemy, 183, 127),
        FormationMember(LEUKOEnemy, 215, 143),
        FormationMember(CRUSTYEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0113 = Formation(
    id=113,
    members=[
        FormationMember(BLOOBEREnemyStatic, 151, 111),
        FormationMember(MRKIPPEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0114 = Formation(
    id=114,
    members=[
        FormationMember(BLOOBEREnemyStatic, 183, 127),
        FormationMember(BLOOBEREnemyStatic, 231, 143),
        FormationMember(BLOOBEREnemyStatic, 135, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0115 = Formation(
    id=115,
    members=[
        FormationMember(BLOOBEREnemyStatic, 151, 111),
        FormationMember(BLOOBEREnemyStatic, 231, 151),
        FormationMember(MRKIPPEREnemy, 151, 143),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0116 = Formation(
    id=116,
    members=[
        FormationMember(BLOOBEREnemyStatic, 231, 135),
        FormationMember(BLOOBEREnemyStatic, 167, 103),
        FormationMember(ZEOSTAREnemy, 135, 127),
        FormationMember(ZEOSTAREnemy, 183, 151),
        FormationMember(LEUKOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0117 = Formation(
    id=117,
    members=[
        FormationMember(MRKIPPEREnemy, 151, 103),
        FormationMember(MRKIPPEREnemy, 215, 151),
        FormationMember(MRKIPPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0118 = Formation(
    id=118,
    members=[
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0119 = Formation(
    id=119,
    members=[
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(MRKIPPEREnemy, 231, 135),
        FormationMember(CRUSTYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0120 = Formation(
    id=120,
    members=[
        FormationMember(MRKIPPEREnemy, 215, 127),
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 167, 103),
        FormationMember(MRKIPPEREnemy, 151, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0121 = Formation(
    id=121,
    members=[
        FormationMember(BANDANAREDEnemy, 151, 127),
        FormationMember(BANDANAREDEnemy, 183, 143),
        FormationMember(BANDANAREDEnemy, 167, 103),
        FormationMember(BANDANAREDEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0122 = Formation(
    id=122,
    members=[
        FormationMember(BANDANAREDEnemy, 199, 151),
        FormationMember(BANDANAREDEnemy, 135, 119),
        FormationMember(BANDANAREDEnemy, 215, 127),
        FormationMember(BANDANAREDEnemy, 167, 135),
        FormationMember(BANDANAREDEnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0123 = Formation(
    id=123,
    members=[
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFIT2Enemy, 156, 132),
        FormationMember(SNIFIT2Enemy, 143, 104),
        FormationMember(SNIFIT2Enemy, 212, 138),
        FormationMember(BOOSTERDUMMY, 0, 0),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0124 = Formation(
    id=124,
    members=[
        FormationMember(PUNCHINELLO2Enemy, 188, 116),
        FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
        FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
        FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
        FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0125 = Formation(
    id=125,
    members=[
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(DRYBONESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0126 = Formation(
    id=126,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0127 = Formation(
    id=127,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(GREAPEREnemy, 199, 151),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0128 = Formation(
    id=128,
    members=[
        FormationMember(DRYBONESEnemy, 167, 103),
        FormationMember(DRYBONESEnemy, 231, 135),
        FormationMember(GREAPEREnemy, 151, 127),
        FormationMember(GREAPEREnemy, 183, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0129 = Formation(
    id=129,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0130 = Formation(
    id=130,
    members=[
        FormationMember(ALLEYRATEnemy, 135, 119),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 215, 127),
        FormationMember(GREAPEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0131 = Formation(
    id=131,
    members=[
        FormationMember(ALLEYRATEnemy, 151, 127),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 183, 111),
        FormationMember(GORGONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0132 = Formation(
    id=132,
    members=[
        FormationMember(ALLEYRATEnemy, 231, 135),
        FormationMember(REACHEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0133 = Formation(
    id=133,
    members=[
        FormationMember(GREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0134 = Formation(
    id=134,
    members=[
        FormationMember(GREAPEREnemy, 151, 119),
        FormationMember(GREAPEREnemy, 199, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0135 = Formation(
    id=135,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(STRAWHEADEnemy, 215, 135),
        FormationMember(REACHEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0136 = Formation(
    id=136,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 199, 119),
        FormationMember(STRAWHEADEnemy, 215, 143),
        FormationMember(STRAWHEADEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0137 = Formation(
    id=137,
    members=[
        FormationMember(BUNDT2Enemy, 199, 127),
        FormationMember(RASPBERRY2Enemy, 199, 119),
        FormationMember(TORTE2Enemy, 199, 151),
        FormationMember(TORTE2Enemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=17,
)

FORM0138 = Formation(
    id=138,
    members=[
        FormationMember(CROOKEnemyStatic, 135, 119),
        FormationMember(CROOKEnemyStatic, 199, 119),
        FormationMember(CROOKEnemyStatic, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0139 = Formation(
    id=139,
    members=[
        FormationMember(CROOKEnemyStatic, 167, 103),
        FormationMember(CROOKEnemyStatic, 135, 119),
        FormationMember(CROOKEnemyStatic, 183, 127),
        FormationMember(CROOKEnemyStatic, 199, 151),
        FormationMember(CROOKEnemyStatic, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0140 = Formation(
    id=140,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(FINKFLOWEREnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0141 = Formation(
    id=141,
    members=[
        FormationMember(STINGEREnemy, 135, 111),
        FormationMember(STINGEREnemy, 215, 151),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0142 = Formation(
    id=142,
    members=[
        FormationMember(STINGEREnemy, 199, 119),
        None,
        FormationMember(FINKFLOWEREnemy, 215, 143),
        FormationMember(FINKFLOWEREnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0143 = Formation(
    id=143,
    members=[
        FormationMember(STINGEREnemy, 183, 111),
        FormationMember(STINGEREnemy, 199, 151),
        FormationMember(STINGEREnemy, 215, 127),
        FormationMember(STINGEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0144 = Formation(
    id=144,
    members=[
        FormationMember(CHOWEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0145 = Formation(
    id=145,
    members=[
        FormationMember(CHOWEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0146 = Formation(
    id=146,
    members=[
        FormationMember(CHOWEnemy, 199, 151),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0147 = Formation(
    id=147,
    members=[
        FormationMember(CHOWEnemy, 167, 135),
        FormationMember(FINKFLOWEREnemy, 199, 119),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(SHOGUNEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0148 = Formation(
    id=148,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0149 = Formation(
    id=149,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0150 = Formation(
    id=150,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 199, 119),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0151 = Formation(
    id=151,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 135, 119),
        FormationMember(CHOMPCHOMPEnemy, 183, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 127),
        FormationMember(CHOMPCHOMPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0152 = Formation(
    id=152,
    members=[
        FormationMember(SHYAWAYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0153 = Formation(
    id=153,
    members=[
        FormationMember(SHYAWAYEnemy, 151, 111),
        FormationMember(SHYAWAYEnemy, 215, 143),
        FormationMember(KRIFFIDEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0154 = Formation(
    id=154,
    members=[
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
        FormationMember(RIBBITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0155 = Formation(
    id=155,
    members=[
        FormationMember(SHYAWAYEnemy, 215, 135),
        None,
        FormationMember(GECKITEnemy, 167, 143),
        None,
        FormationMember(RIBBITEEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0156 = Formation(
    id=156,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(CHEWYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0157 = Formation(
    id=157,
    members=[
        FormationMember(CHEWYEnemy, 135, 119),
        FormationMember(CHEWYEnemy, 199, 151),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0158 = Formation(
    id=158,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(SPINTHRAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0159 = Formation(
    id=159,
    members=[
        FormationMember(CHEWYEnemy, 183, 151),
        FormationMember(CHEWYEnemy, 135, 127),
        FormationMember(GECKITEnemy, 231, 143),
        FormationMember(GECKITEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0160 = Formation(
    id=160,
    members=[
        FormationMember(GECKITEnemy, 199, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0161 = Formation(
    id=161,
    members=[
        FormationMember(GECKITEnemy, 183, 135),
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0162 = Formation(
    id=162,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(CHEWYEnemy, 167, 103),
        FormationMember(CHEWYEnemy, 231, 135),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0163 = Formation(
    id=163,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(SPINTHRAEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0164 = Formation(
    id=164,
    members=[
        FormationMember(BIRDYEnemyStatic, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0165 = Formation(
    id=165,
    members=[
        FormationMember(BIRDYEnemyStatic, 215, 119),
        FormationMember(BIRDYEnemyStatic, 151, 119),
        FormationMember(BIRDYEnemyStatic, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0166 = Formation(
    id=166,
    members=[
        FormationMember(BIRDYEnemyStatic, 199, 151),
        FormationMember(BIRDYEnemyStatic, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0167 = Formation(
    id=167,
    members=[
        FormationMember(BIRDYEnemyStatic, 151, 111),
        FormationMember(BIRDYEnemyStatic, 215, 143),
        FormationMember(BIRDYEnemyStatic, 151, 143),
        FormationMember(BIRDYEnemyStatic, 215, 111),
        FormationMember(BIRDYEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0168 = Formation(
    id=168,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 199, 151),
        FormationMember(BLUEBIRDEnemyStatic, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0169 = Formation(
    id=169,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 167, 103),
        FormationMember(BLUEBIRDEnemyStatic, 231, 135),
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0170 = Formation(
    id=170,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 183, 143),
        FormationMember(BLUEBIRDEnemyStatic, 183, 111),
        FormationMember(BLUEBIRDEnemyStatic, 231, 135),
        FormationMember(BLUEBIRDEnemyStatic, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0171 = Formation(
    id=171,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 151, 111),
        FormationMember(BLUEBIRDEnemyStatic, 215, 143),
        None,
        None,
        FormationMember(HEAVYTROOPAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0172 = Formation(
    id=172,
    members=[
        FormationMember(PINWHEELEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0173 = Formation(
    id=173,
    members=[
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(MUCKLEEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0174 = Formation(
    id=174,
    members=[
        FormationMember(PINWHEELEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 183, 143),
        FormationMember(MUCKLEEnemy, 151, 103),
        FormationMember(MUCKLEEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0175 = Formation(
    id=175,
    members=[
        FormationMember(PINWHEELEnemy, 151, 143),
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(PINWHEELEnemy, 199, 151),
        FormationMember(SLINGSHYEnemy, 167, 111),
        FormationMember(SLINGSHYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0176 = Formation(
    id=176,
    members=[
        FormationMember(SHAMANEnemy, 151, 111),
        FormationMember(SHAMANEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0177 = Formation(
    id=177,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 199, 151),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0178 = Formation(
    id=178,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(JAWFULEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0179 = Formation(
    id=179,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(SLINGSHYEnemy, 135, 127),
        FormationMember(SLINGSHYEnemy, 183, 151),
        FormationMember(JAWFULEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0180 = Formation(
    id=180,
    members=[
        FormationMember(SLINGSHYEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0181 = Formation(
    id=181,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 127),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0182 = Formation(
    id=182,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0183 = Formation(
    id=183,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 143),
        FormationMember(SLINGSHYEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 151, 111),
        FormationMember(PINWHEELEnemy, 215, 143),
        FormationMember(MUCKLEEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0184 = Formation(
    id=184,
    members=[
        FormationMember(MAGMUSEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0185 = Formation(
    id=185,
    members=[
        FormationMember(MAGMUSEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 215, 143),
        FormationMember(ARMOREDANTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0186 = Formation(
    id=186,
    members=[
        FormationMember(MAGMUSEnemy, 151, 103),
        FormationMember(MAGMUSEnemy, 231, 143),
        FormationMember(MAGMUSEnemy, 199, 119),
        FormationMember(OERLIKONEnemy, 151, 127),
        FormationMember(OERLIKONEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0187 = Formation(
    id=187,
    members=[
        FormationMember(MAGMUSEnemy, 119, 119),
        FormationMember(MAGMUSEnemy, 167, 143),
        FormationMember(ARMOREDANTEnemy, 167, 111),
        FormationMember(ARMOREDANTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0188 = Formation(
    id=188,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(VOMEREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0189 = Formation(
    id=189,
    members=[
        FormationMember(OERLIKONEnemy, 183, 127),
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0190 = Formation(
    id=190,
    members=[
        FormationMember(OERLIKONEnemy, 215, 151),
        FormationMember(CHAINEDKONGEnemy, 183, 127),
        FormationMember(ARMOREDANTEnemy, 135, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0191 = Formation(
    id=191,
    members=[
        FormationMember(OERLIKONEnemy, 135, 127),
        FormationMember(OERLIKONEnemy, 183, 151),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0192 = Formation(
    id=192,
    members=[
        FormationMember(PYROSPHEREEnemy, 151, 135),
        FormationMember(PYROSPHEREEnemy, 215, 135),
        FormationMember(PYROSPHEREEnemy, 183, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0193 = Formation(
    id=193,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 143),
        FormationMember(PYROSPHEREEnemy, 151, 119),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0194 = Formation(
    id=194,
    members=[
        FormationMember(CORKPEDITEEnemy, 135, 119),
        FormationMember(BODYEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0195 = Formation(
    id=195,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 151),
        FormationMember(PYROSPHEREEnemy, 199, 119),
        FormationMember(STUMPETEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0196 = Formation(
    id=196,
    members=[
        FormationMember(VOMEREnemy, 151, 111),
        FormationMember(CHAINEDKONGEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0197 = Formation(
    id=197,
    members=[
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 183, 127),
        FormationMember(VOMEREnemy, 215, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0198 = Formation(
    id=198,
    members=[
        FormationMember(CORKPEDITEEnemy, 199, 151),
        FormationMember(BODYEnemy, 215, 143),
        FormationMember(VOMEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0199 = Formation(
    id=199,
    members=[
        FormationMember(VOMEREnemy, 151, 135),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(STUMPETEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0200 = Formation(
    id=200,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0201 = Formation(
    id=201,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 151, 119),
        FormationMember(TERRACOTTAEnemy, 215, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0202 = Formation(
    id=202,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
        FormationMember(FORKIESEnemy, 151, 111),
        FormationMember(FORKIESEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0203 = Formation(
    id=203,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(GUGOOMBAEnemy, 231, 135),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(FORKIESEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0204 = Formation(
    id=204,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 127),
        FormationMember(TUBOTROOPAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0205 = Formation(
    id=205,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 199, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0206 = Formation(
    id=206,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 103),
        FormationMember(MALAKOOPAEnemy, 231, 151),
        FormationMember(TERRACOTTAEnemy, 167, 135),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0207 = Formation(
    id=207,
    members=[
        FormationMember(MALAKOOPAEnemy, 183, 127),
        None,
        None,
        FormationMember(TUBOTROOPAEnemy, 135, 103),
        FormationMember(TUBOTROOPAEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0208 = Formation(
    id=208,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 111),
        FormationMember(GUGOOMBAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0209 = Formation(
    id=209,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 151),
        FormationMember(GUGOOMBAEnemy, 135, 103),
        FormationMember(STARCRUSTEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0210 = Formation(
    id=210,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 143),
        FormationMember(FORKIESEnemy, 199, 119),
        FormationMember(STARCRUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0211 = Formation(
    id=211,
    members=[
        FormationMember(GUGOOMBAEnemy, 199, 151),
        FormationMember(GUGOOMBAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 167, 135),
        FormationMember(MALAKOOPAEnemy, 199, 119),
        FormationMember(TERRACOTTAEnemy, 167, 103),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0212 = Formation(
    id=212,
    members=[
        FormationMember(BIGBERTHAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0213 = Formation(
    id=213,
    members=[
        FormationMember(BIGBERTHAEnemy, 151, 111),
        FormationMember(BIGBERTHAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0214 = Formation(
    id=214,
    members=[
        FormationMember(BIGBERTHAEnemy, 215, 143),
        FormationMember(FORKIESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0215 = Formation(
    id=215,
    members=[
        FormationMember(BIGBERTHAEnemy, 135, 111),
        FormationMember(BIGBERTHAEnemy, 215, 151),
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0216 = Formation(
    id=216,
    members=[
        FormationMember(JOHNNYEnemy2, 165, 121),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0217 = Formation(
    id=217,
    members=[
        FormationMember(JINXEnemy4, 181, 122),
        FormationMember(TeamGaugeEnemy, 36, 200),
    ],
    music=MidbossMusic(),
)

FORM0218 = Formation(
    id=218,
    members=[
        FormationMember(NINJAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0219 = Formation(
    id=219,
    members=[
        FormationMember(NINJAEnemy, 151, 119),
        FormationMember(DOPPELEnemy, 199, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0220 = Formation(
    id=220,
    members=[
        FormationMember(NINJAEnemy, 199, 151),
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(HIPPOPOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0221 = Formation(
    id=221,
    members=[
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(NINJAEnemy, 183, 127),
        FormationMember(NINJAEnemy, 167, 103),
        FormationMember(NINJAEnemy, 231, 135),
        FormationMember(NINJAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0222 = Formation(
    id=222,
    members=[
        FormationMember(SPRINGEREnemy, 215, 143),
        FormationMember(GLUMREAPEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0223 = Formation(
    id=223,
    members=[
        FormationMember(SPRINGEREnemy, 231, 135),
        FormationMember(SPRINGEREnemy, 167, 103),
        FormationMember(PUPPOXEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0224 = Formation(
    id=224,
    members=[
        FormationMember(SPRINGEREnemy, 183, 127),
        FormationMember(PUPPOXEnemy, 215, 143),
        FormationMember(PUPPOXEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0225 = Formation(
    id=225,
    members=[
        FormationMember(MADMALLETEnemyStatic, 151, 119),
        FormationMember(MADMALLETEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0226 = Formation(
    id=226,
    members=[
        FormationMember(MADMALLETEnemyStatic, 151, 127),
        FormationMember(MADMALLETEnemyStatic, 199, 151),
        FormationMember(MADMALLETEnemyStatic, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0227 = Formation(
    id=227,
    members=[
        FormationMember(MADMALLETEnemyStatic, 183, 127),
        FormationMember(MADMALLETEnemyStatic, 135, 127),
        FormationMember(MADMALLETEnemyStatic, 231, 135),
        FormationMember(MADMALLETEnemyStatic, 167, 103),
        FormationMember(MADMALLETEnemyStatic, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0228 = Formation(
    id=228,
    members=[
        FormationMember(POUNDEREnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0229 = Formation(
    id=229,
    members=[
        FormationMember(POUNDEREnemyStatic, 183, 127),
        FormationMember(POUNDEREnemyStatic, 231, 135),
        FormationMember(POUNDEREnemyStatic, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0230 = Formation(
    id=230,
    members=[
        FormationMember(POUNDEREnemyStatic, 167, 135),
        FormationMember(POUNDEREnemyStatic, 199, 143),
        FormationMember(POUNDEREnemyStatic, 151, 119),
        FormationMember(POUNDEREnemyStatic, 167, 103),
        FormationMember(POUNDEREnemyStatic, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0231 = Formation(
    id=231,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0232 = Formation(
    id=232,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 183, 127),
        FormationMember(POUNDETTEEnemyStatic, 151, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0233 = Formation(
    id=233,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 167, 135),
        FormationMember(POUNDETTEEnemyStatic, 199, 119),
        FormationMember(POUNDETTEEnemyStatic, 135, 119),
        FormationMember(POUNDETTEEnemyStatic, 167, 103),
        FormationMember(POUNDETTEEnemyStatic, 199, 151),
        FormationMember(POUNDETTEEnemyStatic, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0234 = Formation(
    id=234,
    members=[
        FormationMember(AMEBOIDEnemy, 183, 127),
        FormationMember(AMEBOIDEnemy, 167, 103, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 135, 119, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 231, 135, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 199, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0235 = Formation(
    id=235,
    members=[
        FormationMember(GLUMREAPEREnemy, 183, 127),
        FormationMember(GLUMREAPEREnemy, 135, 119),
        FormationMember(GLUMREAPEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0236 = Formation(
    id=236,
    members=[
        FormationMember(GLUMREAPEREnemy, 215, 159),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0237 = Formation(
    id=237,
    members=[
        FormationMember(GLUMREAPEREnemy, 151, 127),
        FormationMember(GLUMREAPEREnemy, 183, 143),
        FormationMember(DOPPELEnemy, 167, 103),
        FormationMember(DOPPELEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0238 = Formation(
    id=238,
    members=[
        FormationMember(GLUMREAPEREnemy, 135, 111),
        FormationMember(GLUMREAPEREnemy, 215, 151),
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0239 = Formation(
    id=239,
    members=[
        FormationMember(LILBOOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0240 = Formation(
    id=240,
    members=[
        FormationMember(LILBOOEnemy, 183, 151),
        FormationMember(LILBOOEnemy, 215, 135),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0241 = Formation(
    id=241,
    members=[
        FormationMember(LILBOOEnemy, 167, 143),
        FormationMember(LILBOOEnemy, 199, 119),
        FormationMember(PUPPOXEnemy, 151, 103),
        FormationMember(DOPPELEnemy, 215, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0242 = Formation(
    id=242,
    members=[
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 151, 111),
        FormationMember(LILBOOEnemy, 215, 143),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0243 = Formation(
    id=243,
    members=[
        FormationMember(JABITEnemy, 215, 135),
        FormationMember(MADMALLETEnemyStatic, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0244 = Formation(
    id=244,
    members=[
        FormationMember(JABITEnemy, 151, 143),
        FormationMember(POUNDEREnemyStatic, 151, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0245 = Formation(
    id=245,
    members=[
        FormationMember(JABITEnemy, 135, 119),
        FormationMember(JABITEnemy, 167, 135),
        FormationMember(JABITEnemy, 231, 135),
        FormationMember(JABITEnemy, 167, 103),
        FormationMember(JABITEnemy, 199, 119),
        FormationMember(JABITEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0246 = Formation(
    id=246,
    members=[
        FormationMember(JABITEnemy, 151, 127),
        FormationMember(JABITEnemy, 183, 143),
        FormationMember(MADMALLETEnemyStatic, 135, 103),
        FormationMember(MADMALLETEnemyStatic, 183, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 127),
        FormationMember(POUNDETTEEnemyStatic, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0247 = Formation(
    id=247,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(RATFUNKEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0248 = Formation(
    id=248,
    members=[
        FormationMember(RATFUNKEnemy, 135, 127),
        FormationMember(RATFUNKEnemy, 167, 103),
        FormationMember(RATFUNKEnemy, 183, 151),
        FormationMember(RATFUNKEnemy, 231, 135),
        FormationMember(RATFUNKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0249 = Formation(
    id=249,
    members=[
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0250 = Formation(
    id=250,
    members=[
        FormationMember(ARTICHOKEREnemy, 151, 119),
        FormationMember(ARTICHOKEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0251 = Formation(
    id=251,
    members=[
        FormationMember(PUNCHINELLOEnemy, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0252 = Formation(
    id=252,
    members=[
        FormationMember(FIREBALLEnemy, 151, 111),
        FormationMember(FIREBALLEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0253 = Formation(
    id=253,
    members=[
        FormationMember(FIREBALLEnemy, 167, 135),
        FormationMember(FIREBALLEnemy, 167, 111),
        FormationMember(FIREBALLEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0254 = Formation(
    id=254,
    members=[
        FormationMember(STUMPETEnemy, 183, 127),
        FormationMember(MAGMUSEnemy, 119, 127),
        FormationMember(MAGMUSEnemy, 183, 159),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0255 = Formation(
    id=255,
    members=[
        FormationMember(STUMPETEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 183, 159),
        FormationMember(MAGMUSEnemy, 199, 135),
        FormationMember(MAGMUSEnemy, 231, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0256 = Formation(
    id=256,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0257 = Formation(
    id=257,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 183, 159),
        FormationMember(OERLIKONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0258 = Formation(
    id=258,
    members=[
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemyHenchman, 135, 119),
        FormationMember(MADMALLETEnemyHenchman, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0259 = Formation(
    id=259,
    members=[
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemyHenchman, 151, 111),
        FormationMember(POUNDEREnemyHenchman, 167, 135),
        FormationMember(POUNDEREnemyHenchman, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0260 = Formation(
    id=260,
    members=[
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemyHenchman, 135, 119),
        FormationMember(POUNDETTEEnemyHenchman, 167, 103),
        FormationMember(POUNDETTEEnemyHenchman, 199, 151),
        FormationMember(POUNDETTEEnemyHenchman, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0261 = Formation(
    id=261,
    members=[
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0262 = Formation(
    id=262,
    members=[
        FormationMember(MADMALLETEnemyHenchman, 151, 111),
        FormationMember(MADMALLETEnemyHenchman, 167, 135),
        FormationMember(MADMALLETEnemyHenchman, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0263 = Formation(
    id=263,
    members=[
        FormationMember(APPRENTICEEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0264 = Formation(
    id=264,
    members=[
        FormationMember(MACHINEMADEDrillbitEnemy, 183, 127),
        FormationMember(MACHINEMADEDrillbitEnemy, 167, 103),
        FormationMember(MACHINEMADEDrillbitEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0265 = Formation(
    id=265,
    members=[
        FormationMember(SHYGUYEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0266 = Formation(
    id=266,
    members=[
        FormationMember(PANDORITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0267 = Formation(
    id=267,
    members=[
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0268 = Formation(
    id=268,
    members=[
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0269 = Formation(
    id=269,
    members=[
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy2, 135, 119, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0270 = Formation(
    id=270,
    members=[
        FormationMember(AEROEnemy, 167, 119),
        FormationMember(AEROEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0271 = Formation(
    id=271,
    members=[
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemyHenchman, 135, 119),
        FormationMember(SNIFITEnemyHenchman, 151, 143),
        FormationMember(SNIFITEnemyHenchman, 199, 151),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=12,
)

FORM0272 = Formation(
    id=272,
    members=[
        FormationMember(BOOSTEREnemy2, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0273 = Formation(
    id=273,
    members=[
        FormationMember(CROCO1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0274 = Formation(
    id=274,
    members=[
        FormationMember(CROCO2Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0275 = Formation(
    id=275,
    members=[
        FormationMember(MACHINEMADEAxemBlackEnemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0276 = Formation(
    id=276,
    members=[
        FormationMember(JOHNNYEnemy, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0277 = Formation(
    id=277,
    members=[
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=26,
)

FORM0278 = Formation(
    id=278,
    members=[
        FormationMember(BELOME1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0279 = Formation(
    id=279,
    members=[
        FormationMember(BELOME2Enemy, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0280 = Formation(
    id=280,
    members=[
        FormationMember(TERRAPINEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0281 = Formation(
    id=281,
    members=[
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0282 = Formation(
    id=282,
    members=[
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0283 = Formation(
    id=283,
    members=[
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=58,
)

FORM0284 = Formation(
    id=284,
    members=[
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0285 = Formation(
    id=285,
    members=[
        FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0286 = Formation(
    id=286,
    members=[
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0287 = Formation(
    id=287,
    members=[
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0288 = Formation(
    id=288,
    members=[
        FormationMember(JINX1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=71,
)

FORM0289 = Formation(
    id=289,
    members=[
        FormationMember(MACKEnemy, 199, 119),
        FormationMember(BODYGUARDEnemy, 135, 111),
        FormationMember(BODYGUARDEnemy, 151, 127),
        FormationMember(BODYGUARDEnemy, 183, 143),
        FormationMember(BODYGUARDEnemy, 215, 151),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0290 = Formation(
    id=290,
    members=[
        FormationMember(YARIDOVICHEnemy, 183, 127),
        FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0291 = Formation(
    id=291,
    members=[
        FormationMember(BOWYEREnemy, 183, 127),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=14,
)

FORM0292 = Formation(
    id=292,
    members=[
        FormationMember(AXEMRANGERSEnemy, 201, 79),
        FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
        FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
        FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
        FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
        FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=61,
)

FORM0293 = Formation(
    id=293,
    members=[
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0294 = Formation(
    id=294,
    members=[
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=52,
)

FORM0295 = Formation(
    id=295,
    members=[
        FormationMember(SMITHY1Enemy, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
    ],
    music=Smithy1Music(),
    unknown_bit=True,
)

FORM0296 = Formation(
    id=296,
    members=[
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=80,
)

FORM0297 = Formation(
    id=297,
    members=[
        FormationMember(JINX2Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=72,
)

FORM0298 = Formation(
    id=298,
    members=[
        FormationMember(JINX3Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=73,
)

FORM0299 = Formation(
    id=299,
    members=[
        FormationMember(JAGGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0300 = Formation(
    id=300,
    members=[
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
        FormationMember(HEAVYTROOPAEnemy, 151, 103),
        FormationMember(HEAVYTROOPAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0301 = Formation(
    id=301,
    members=[
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0302 = Formation(
    id=302,
    members=[
        FormationMember(HELIOEnemy, 167, 119),
        FormationMember(HELIOEnemy, 135, 135),
        FormationMember(HELIOEnemy, 199, 167),
        FormationMember(HELIOEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0303 = Formation(
    id=303,
    members=[
        FormationMember(BODYGUARDEnemy, 167, 119),
        FormationMember(BODYGUARDEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0304 = Formation(
    id=304,
    members=[
        FormationMember(BODYGUARDEnemy, 151, 111),
        FormationMember(BODYGUARDEnemy, 215, 143),
        FormationMember(BODYGUARDEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0305 = Formation(
    id=305,
    members=[
        FormationMember(GENOCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0306 = Formation(
    id=306,
    members=[
        FormationMember(BOWSERCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0307 = Formation(
    id=307,
    members=[
        FormationMember(TOADSTOOL2Enemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0308 = Formation(
    id=308,
    members=[
        FormationMember(MARIOCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0309 = Formation(
    id=309,
    members=[
        FormationMember(MALLOWCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0310 = Formation(
    id=310,
    members=[
        FormationMember(MACHINEMADEAxemPinkEnemy, 151, 111),
        None,
        FormationMember(MACHINEMADEAxemRedEnemy, 151, 143),
        None,
        FormationMember(MACHINEMADEAxemGreenEnemy, 215, 143),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0311 = Formation(
    id=311,
    members=[
        FormationMember(MACHINEMADEAxemBlackEnemy, 151, 119),
        FormationMember(MACHINEMADEAxemBlackEnemy, 231, 127),
        FormationMember(MACHINEMADEAxemYellowEnemy, 199, 143),
        FormationMember(MACHINEMADEAxemYellowEnemy, 183, 103),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0312 = Formation(
    id=312,
    members=[
        FormationMember(BLOOBEREnemyStatic, 183, 127),
        FormationMember(BLOOBEREnemyStatic, 231, 143),
        FormationMember(BLOOBEREnemyStatic, 135, 111),
    ],
    music=None,
)

FORM0313 = Formation(
    id=313,
    members=[
        FormationMember(SHOGUNEnemy, 167, 135),
        FormationMember(SHOGUNEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0314 = Formation(
    id=314,
    members=[
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0315 = Formation(
    id=315,
    members=[
        FormationMember(DODOEnemySolo, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0316 = Formation(
    id=316,
    members=[
        FormationMember(KAMEKEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=101,
)

FORM0317 = Formation(
    id=317,
    members=[
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0318 = Formation(
    id=318,
    members=[
        FormationMember(MACHINEMADEMackEnemy, 199, 119),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 111),
        FormationMember(MACHINEMADEBodyguardEnemy, 151, 127),
        FormationMember(MACHINEMADEBodyguardEnemy, 183, 143),
        FormationMember(MACHINEMADEBodyguardEnemy, 215, 151),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0319 = Formation(
    id=319,
    members=[
        FormationMember(MACHINEMADEBowyerEnemy, 183, 127),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0320 = Formation(
    id=320,
    members=[
        FormationMember(MACHINEMADEYaridovichEnemy, 183, 127),
        FormationMember(MACHINEMADEDrillbitEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 167, 103, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 199, 151, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 231, 135, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0321 = Formation(
    id=321,
    members=[
        FormationMember(SMITHYBodyEnemy, 183, 135, hidden_at_start=True),
        FormationMember(SMITHY2Enemy, 183, 175),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0322 = Formation(
    id=322,
    members=[
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
    ],
    music=CulexMusic(),
    unknown_bit=True,
)

FORM0323 = Formation(
    id=323,
    members=[
        FormationMember(FIRECRYSTALEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=76,
)

FORM0324 = Formation(
    id=324,
    members=[
        FormationMember(WATERCRYSTALEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=20,
)

FORM0325 = Formation(
    id=325,
    members=[
        FormationMember(EARTHCRYSTALEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=11,
)

FORM0326 = Formation(
    id=326,
    members=[
        FormationMember(WINDCRYSTALEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=1,
)

FORM0327 = Formation(
    id=327,
    members=[
        FormationMember(GOOMBETTEEnemy, 183, 127),
        FormationMember(GOOMBETTEEnemy, 231, 135),
        FormationMember(GOOMBETTEEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0328 = Formation(
    id=328,
    members=[
        FormationMember(EGGBERTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0329 = Formation(
    id=329,
    members=[
        FormationMember(EGGBERTEnemy, 167, 111),
        FormationMember(EGGBERTEnemy, 167, 135),
        FormationMember(EGGBERTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0330 = Formation(
    id=330,
    members=[
        FormationMember(EGGBERTEnemy, 135, 127),
        FormationMember(EGGBERTEnemy, 183, 111),
        FormationMember(EGGBERTEnemy, 183, 151),
        FormationMember(EGGBERTEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0331 = Formation(
    id=331,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 111),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0332 = Formation(
    id=332,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 199, 151),
        FormationMember(STARCRUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0333 = Formation(
    id=333,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 151, 103),
        FormationMember(BIGBERTHAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0334 = Formation(
    id=334,
    members=[
        FormationMember(CHOWEnemy, 135, 111),
        FormationMember(CHOWEnemy, 215, 151),
        FormationMember(FORKIESEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0335 = Formation(
    id=335,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 119),
        FormationMember(ARMOREDANTEnemy, 135, 119),
        FormationMember(ARMOREDANTEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0336 = Formation(
    id=336,
    members=[
        FormationMember(BLOOBEREnemyStatic, 199, 119),
        FormationMember(BLOOBEREnemyStatic, 183, 151),
        FormationMember(BLOOBEREnemyStatic, 231, 151),
        FormationMember(STARCRUSTEREnemy, 135, 103),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0337 = Formation(
    id=337,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(STINGEREnemy, 167, 127),
        FormationMember(STINGEREnemy, 199, 143),
        FormationMember(STINGEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0338 = Formation(
    id=338,
    members=[
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(GECKITEnemy, 135, 111),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0339 = Formation(
    id=339,
    members=[
        FormationMember(ROBOMBEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 167, 111),
        FormationMember(BIGBERTHAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0340 = Formation(
    id=340,
    members=[
        FormationMember(VOMEREnemy, 151, 127),
        FormationMember(VOMEREnemy, 183, 143),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0341 = Formation(
    id=341,
    members=[
        FormationMember(MAGMUSEnemy, 151, 127),
        FormationMember(MAGMUSEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 103),
        FormationMember(PULSAREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0342 = Formation(
    id=342,
    members=[
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0343 = Formation(
    id=343,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 127),
        FormationMember(GUGOOMBAEnemy, 183, 143),
        FormationMember(GUGOOMBAEnemy, 199, 119),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(GUGOOMBAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0344 = Formation(
    id=344,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 111),
        FormationMember(MALAKOOPAEnemy, 215, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0345 = Formation(
    id=345,
    members=[
        FormationMember(THEBIGBOOEnemy, 183, 143),
        FormationMember(THEBIGBOOEnemy, 151, 127),
        FormationMember(ORBISONEnemy, 167, 103),
        FormationMember(ORBISONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0346 = Formation(
    id=346,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(SLINGSHYEnemy, 167, 119),
        FormationMember(SLINGSHYEnemy, 199, 135),
        FormationMember(SLINGSHYEnemy, 167, 103),
        FormationMember(SLINGSHYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0347 = Formation(
    id=347,
    members=[
        FormationMember(CHEWYEnemy, 151, 127),
        FormationMember(CHEWYEnemy, 183, 143),
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0348 = Formation(
    id=348,
    members=[
        FormationMember(MRKIPPEREnemy, 167, 135),
        FormationMember(MUCKLEEnemy, 167, 103),
        FormationMember(MUCKLEEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0349 = Formation(
    id=349,
    members=[
        FormationMember(AMANITAEnemy, 215, 143),
        FormationMember(AMANITAEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0350 = Formation(
    id=350,
    members=[
        FormationMember(GREAPEREnemy, 215, 143),
        FormationMember(GREAPEREnemy, 151, 111),
        FormationMember(GLUMREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0351 = Formation(
    id=351,
    members=[
        FormationMember(PYROSPHEREEnemy, 183, 127),
        FormationMember(PYROSPHEREEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0352 = Formation(
    id=352,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0353 = Formation(
    id=353,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 127),
        FormationMember(ZEOSTAREnemy, 183, 143),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0354 = Formation(
    id=354,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 167, 135),
        FormationMember(SHAMANEnemy, 199, 119),
        FormationMember(SHAMANEnemy, 199, 151),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0355 = Formation(
    id=355,
    members=[
        FormationMember(AXEMBLACKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0356 = Formation(
    id=356,
    members=[
        FormationMember(AXEMPINKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0357 = Formation(
    id=357,
    members=[
        FormationMember(AXEMYELLOWEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0358 = Formation(
    id=358,
    members=[
        FormationMember(AXEMGREENEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0359 = Formation(
    id=359,
    members=[
        FormationMember(DINGALINGEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0360 = Formation(
    id=360,
    members=[
        FormationMember(DRILLBITEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0361 = Formation(
    id=361,
    members=[
        FormationMember(DRILLBITEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)


# ============================================================================
# Pack Definitions
# ============================================================================

# Initialize packs array with None values
packs: list[FormationPack] = [None] * 256  # type: ignore

packs[PACK000_TOWER_HENCHMAN_1] = FormationPack(FORM0000)
packs[PACK001_TOWER_HENCHMAN_2] = FormationPack(FORM0000)
packs[PACK002_SPIKEYS_AND_TROOPAS] = FormationPack(FORM0001, FORM0002, FORM0002)
packs[PACK003_SPIKEYS_AND_FROGS] = FormationPack(FORM0003, FORM0004, FORM0004)
packs[PACK004_JUST_TROOPAS] = FormationPack(FORM0005, FORM0006, FORM0006)
packs[PACK005_TROOPAS_WITH_FROGS_OR_GOOMBAS] = FormationPack(FORM0007, FORM0008, FORM0006)
packs[PACK006_JUST_GOOMBAS] = FormationPack(FORM0009, FORM0010, FORM0009)
packs[PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS] = FormationPack(FORM0011, FORM0012, FORM0010)
packs[PACK008_K9S_WITH_SPIKEYS] = FormationPack(FORM0013, FORM0014, FORM0015)
packs[PACK009_K9S_WITH_SPIKEYS_OR_FROGS] = FormationPack(FORM0016, FORM0015, FORM0014)
packs[PACK010_KINGDOM_HENCHMEN_1] = FormationPack(FORM0017, FORM0018, FORM0017)
packs[PACK011_KINGDOM_HENCHMEN_2] = FormationPack(FORM0017, FORM0018, FORM0018)
packs[PACK012_RATFUNKS_WITH_SHADOW_OR_HOBGOBLIN] = FormationPack(FORM0019, FORM0020, FORM0021)
packs[PACK013_RATFUNKS_ALWAYS_WITH_ONE_OTHER_MONSTER] = FormationPack(FORM0022, FORM0021, FORM0020)
packs[PACK014_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_1] = FormationPack(FORM0023, FORM0023, FORM0024)
packs[PACK015_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_2] = FormationPack(FORM0025, FORM0024, FORM0023)
packs[PACK016_MULTIPLE_GOBYS_BIASED_2] = FormationPack(FORM0026, FORM0026, FORM0027)
packs[PACK017_MULTIPLE_GOBYS_BIASED_3] = FormationPack(FORM0027, FORM0027, FORM0026)
packs[PACK018_CROOKS_WITH_SHYGUY_OR_SNAPDRAGON] = FormationPack(FORM0028, FORM0029, FORM0030)
packs[PACK019_CROOKS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0031, FORM0030, FORM0029)
packs[PACK020_SHYGUYS_WITH_STARSLAP_OR_SNAPDRAGON] = FormationPack(FORM0032, FORM0032, FORM0033)
packs[PACK021_SHYGUY_STARSLAP_SNAPDRAGON_CROOK_ARACHNE] = FormationPack(FORM0034, FORM0033, FORM0032)
packs[PACK022_STARSLAP_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0035, FORM0036, FORM0037)
packs[PACK023_STARSLAPS_SOMETIMES_WITH_OTHER_MONSTERS] = FormationPack(FORM0038, FORM0037, FORM0036)
packs[PACK024_WIGGLERS_WITH_AMANITA] = FormationPack(FORM0039, FORM0040, FORM0041)
packs[PACK025_WIGGLERS_WITH_GUERRILLA_OR_AMANITA] = FormationPack(FORM0042, FORM0041, FORM0040)
packs[PACK026_AMANITAS_WITH_BUZZER_OR_OCTOLOT] = FormationPack(FORM0043, FORM0044, FORM0045)
packs[PACK027_AMANITAS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0046, FORM0045, FORM0044)
packs[PACK028_BUZZERS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0047, FORM0048, FORM0049)
packs[PACK029_BUZZERS_WITH_AMANITA] = FormationPack(FORM0050, FORM0049, FORM0048)
packs[PACK030_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0051, FORM0052, FORM0053)
packs[PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0053, FORM0053, FORM0052)
packs[PACK032_TOWER_PASS_HENCHMAN] = FormationPack(FORM0054)
packs[PACK033_POSTGAME_TEMPLE] = FormationPack(FORM0055)
packs[PACK034_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0056, FORM0057, FORM0058)
packs[PACK035_MULTIPLE_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0059, FORM0058, FORM0057)
packs[PACK036_BOBOMB_WITH_CLUSTER] = FormationPack(FORM0060, FORM0061, FORM0062)
packs[PACK037_BOBOMB_WITH_CLUSTER_SOMETIMES_ENIGMA] = FormationPack(FORM0063, FORM0062, FORM0061)
packs[PACK038_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_1] = FormationPack(FORM0064, FORM0065, FORM0066)
packs[PACK039_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_2] = FormationPack(FORM0067, FORM0066, FORM0065)
packs[PACK040_MAGMITES_WITH_SPARKY_BOBOMB_OR_CLUSTER] = FormationPack(FORM0068, FORM0069, FORM0070)
packs[PACK041_MAGMITES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0071, FORM0070, FORM0069)
packs[PACK042_LAKITU_WITH_SPIKESTER_ARTICHOKER] = FormationPack(FORM0072, FORM0073, FORM0074)
packs[PACK043_LAKITU_USUALLY_WITH_ARTICHOKER] = FormationPack(FORM0075, FORM0074, FORM0073)
packs[PACK044_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0076, FORM0077, FORM0078)
packs[PACK045_MULTIPLE_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0079, FORM0078, FORM0077)
packs[PACK046_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0080, FORM0081, FORM0082)
packs[PACK047_MULTIPLE_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0083, FORM0082, FORM0081)
packs[PACK048_ROBOMB_WITH_REMOCON] = FormationPack(FORM0084, FORM0085, FORM0086)
packs[PACK049_ROBOMB_WITH_REMOCON_OR_ORBUSER] = FormationPack(FORM0087, FORM0086, FORM0085)
packs[PACK050_CHOMP_WITH_OTHER_MONSTERS_1] = FormationPack(FORM0088, FORM0089, FORM0090)
packs[PACK051_CHOMP_WITH_OTHER_MONSTERS_2] = FormationPack(FORM0091, FORM0090, FORM0089)
packs[PACK052_BLASTERS_AND_SPOOKUMS_1] = FormationPack(FORM0092, FORM0093, FORM0094)
packs[PACK053_BLASTERS_AND_SPOOKUMS_2] = FormationPack(FORM0095, FORM0094, FORM0093)
packs[PACK054_TOWER_HENCHMAN_3] = FormationPack(FORM0000)
packs[PACK055_MONSTRO_DOOR_POSTGAME] = FormationPack(FORM0096)
packs[PACK056_MUKU_PULSAR_GECKO] = FormationPack(FORM0097, FORM0098, FORM0099)
packs[PACK057_MUKU_PULSAR_GECKO_MULTI] = FormationPack(FORM0100, FORM0099, FORM0098)
packs[PACK058_SACKIT_WITH_OTHER_MONSTERS] = FormationPack(FORM0101, FORM0102, FORM0103)
packs[PACK059_SACKIT_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0104, FORM0103, FORM0102)
packs[PACK060_GECKO_PACK_1] = FormationPack(FORM0105, FORM0106, FORM0107)
packs[PACK061_GECKO_PACK_2] = FormationPack(FORM0108, FORM0107, FORM0106)
packs[PACK062_ZEOSTAR_WITH_BLOOBER_OR_LEUKO] = FormationPack(FORM0109, FORM0110, FORM0111)
packs[PACK063_ZEOSTAR_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0112, FORM0111, FORM0110)
packs[PACK064_BLOOBER_PACK_1] = FormationPack(FORM0113, FORM0114, FORM0115)
packs[PACK065_BLOOBER_PACK_2] = FormationPack(FORM0116, FORM0115, FORM0114)
packs[PACK066_KIPPER_PACK_1] = FormationPack(FORM0117, FORM0118, FORM0119)
packs[PACK067_KIPPER_PACK_2] = FormationPack(FORM0120, FORM0119, FORM0118)
packs[PACK068_SHIP_HENCHMAN_1] = FormationPack(FORM0121)
packs[PACK069_SHIP_HENCHMAN_2] = FormationPack(FORM0122)
packs[PACK070_TOWER_POSTGAME] = FormationPack(FORM0123)
packs[PACK071_MINES_POSTGAME] = FormationPack(FORM0124)
packs[PACK072_DRYBONES_WITH_GREAPER_REACHER] = FormationPack(FORM0125, FORM0126, FORM0127)
packs[PACK073_DRYBONES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0128, FORM0127, FORM0126)
packs[PACK074_ALLEYRAT_PACK_1] = FormationPack(FORM0129, FORM0130, FORM0131)
packs[PACK075_ALLEYRAT_PACK_2] = FormationPack(FORM0132, FORM0131, FORM0130)
packs[PACK076_GREAPER_WITH_REACHER_STRAWHEAD] = FormationPack(FORM0133, FORM0134, FORM0135)
packs[PACK077_GREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0136, FORM0135, FORM0134)
packs[PACK078_CHAPEL_POSTGAME] = FormationPack(FORM0137)
packs[PACK079_MINES_HENCHMAN_RIGHT] = FormationPack(FORM0138, FORM0139, FORM0138)
packs[PACK080_STINGER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0140, FORM0141, FORM0142)
packs[PACK081_STINGER_WITH_OCTOVADER_OR_FINKFLOWER] = FormationPack(FORM0143, FORM0142, FORM0141)
packs[PACK082_CHOW_PACK_1] = FormationPack(FORM0144, FORM0145, FORM0146)
packs[PACK083_CHOW_PACK_2] = FormationPack(FORM0147, FORM0146, FORM0145)
packs[PACK084_CHOMPCHOMP_PACK_1] = FormationPack(FORM0148, FORM0149, FORM0150)
packs[PACK085_CHOMPCHOMP_PACK_2] = FormationPack(FORM0151, FORM0150, FORM0149)
packs[PACK086_SHYAWAY_WITH_KRIFFID_OR_RIBBITE] = FormationPack(FORM0152, FORM0153, FORM0154)
packs[PACK087_SHYAWAY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0155, FORM0154, FORM0153)
packs[PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA] = FormationPack(FORM0156, FORM0157, FORM0158)
packs[PACK089_CHEWY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0159, FORM0158, FORM0157)
packs[PACK090_GECKIT_PACK_1] = FormationPack(FORM0160, FORM0161, FORM0162)
packs[PACK091_GECKIT_PACK_2] = FormationPack(FORM0163, FORM0162, FORM0161)
packs[PACK092_BIRDY_PACK_1] = FormationPack(FORM0164, FORM0165, FORM0166)
packs[PACK093_BIRDY_PACK_2] = FormationPack(FORM0167, FORM0166, FORM0165)
packs[PACK094_BLUEBIRD_PACK_1] = FormationPack(FORM0168, FORM0169, FORM0170)
packs[PACK095_BLUEBIRD_PACK_2] = FormationPack(FORM0171, FORM0170, FORM0169)
packs[PACK096_PINWHEEL_WITH_MUCKLE] = FormationPack(FORM0172, FORM0173, FORM0174)
packs[PACK097_PINWHEEL_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0175, FORM0174, FORM0173)
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(FORM0176, FORM0177, FORM0178)
packs[PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0179, FORM0178, FORM0177)
packs[PACK100_SLINGSHY_PACK_1] = FormationPack(FORM0180, FORM0181, FORM0182)
packs[PACK101_SLINGSHY_PACK_2] = FormationPack(FORM0183, FORM0182, FORM0181)
packs[PACK102_MAGMUS_WITH_ARMOREDANT_OERLIKON] = FormationPack(FORM0184, FORM0185, FORM0186)
packs[PACK103_MAGMUS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0187, FORM0186, FORM0185)
packs[PACK104_OERLIKON_PACK_1] = FormationPack(FORM0188, FORM0189, FORM0190)
packs[PACK105_OERLIKON_PACK_2] = FormationPack(FORM0191, FORM0190, FORM0189)
packs[PACK106_PYROSPHERE_WITH_CHAINEDKONG_CORKPEDITE] = FormationPack(FORM0192, FORM0193, FORM0194)
packs[PACK107_PYROSPHERE_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0195, FORM0194, FORM0193)
packs[PACK108_VOMER_PACK_1] = FormationPack(FORM0196, FORM0197, FORM0198)
packs[PACK109_VOMER_PACK_2] = FormationPack(FORM0199, FORM0198, FORM0197)
packs[PACK110_TERRACOTTA_PACK_1] = FormationPack(FORM0200, FORM0201, FORM0202)
packs[PACK111_TERRACOTTA_PACK_2] = FormationPack(FORM0203, FORM0202, FORM0201)
packs[PACK112_MALAKOOPA_PACK_1] = FormationPack(FORM0204, FORM0205, FORM0206)
packs[PACK113_MALAKOOPA_PACK_2] = FormationPack(FORM0207, FORM0206, FORM0205)
packs[PACK114_GUGOOMBA_PACK_1] = FormationPack(FORM0208, FORM0209, FORM0210)
packs[PACK115_GUGOOMBA_PACK_2] = FormationPack(FORM0211, FORM0210, FORM0209)
packs[PACK116_BIGBERTHA_PACK_1] = FormationPack(FORM0212, FORM0213, FORM0214)
packs[PACK117_BIGBERTHA_PACK_2] = FormationPack(FORM0215, FORM0214, FORM0213)
packs[PACK118_SHIP_POSTGAME] = FormationPack(FORM0216)
packs[PACK119_DOJO_POSTGAME] = FormationPack(FORM0217)
packs[PACK120_NINJA_PACK_1] = FormationPack(FORM0218, FORM0219, FORM0220)
packs[PACK121_NINJA_PACK_2] = FormationPack(FORM0221, FORM0220, FORM0219)
packs[PACK122_SPRINGER_PACK_1] = FormationPack(FORM0222, FORM0223, FORM0222)
packs[PACK123_SPRINGER_PACK_2] = FormationPack(FORM0224, FORM0223, FORM0222)
packs[PACK124_MADMALLET_PACK_1] = FormationPack(FORM0225, FORM0226, FORM0227)
packs[PACK125_MADMALLET_PACK_2] = FormationPack(FORM0227, FORM0226, FORM0225)
packs[PACK126_POUNDER_PACK_1] = FormationPack(FORM0228, FORM0229, FORM0230)
packs[PACK126_POUNDER_PACK_2] = FormationPack(FORM0230, FORM0229, FORM0228)
packs[PACK128_POUNDETTE_PACK_1] = FormationPack(FORM0231, FORM0232, FORM0233)
packs[PACK128_POUNDETTE_PACK_2] = FormationPack(FORM0233, FORM0232, FORM0231)
packs[PACK130_AMEBOIDS] = FormationPack(FORM0234)
packs[PACK131_AMEBOIDS_DUPE] = FormationPack(FORM0234)
packs[PACK132_GLUMREAPER_WITH_HIPPOPO_DOPPEL] = FormationPack(FORM0235, FORM0236, FORM0237)
packs[PACK133_GLUMREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0238, FORM0237, FORM0236)
packs[PACK134_LILBOO_PACK_1] = FormationPack(FORM0239, FORM0240, FORM0241)
packs[PACK135_LILBOO_PACK_2] = FormationPack(FORM0242, FORM0241, FORM0240)
packs[PACK136_JABITS_HAMMERS_PACK_1] = FormationPack(FORM0243, FORM0244, FORM0245)
packs[PACK137_JABITS_HAMMERS_PACK_2] = FormationPack(FORM0246, FORM0245, FORM0244)
packs[PACK138_RATFUNKS_ONLY] = FormationPack(FORM0247, FORM0248, FORM0247)
packs[PACK139_ARTICHOKERS_ONLY] = FormationPack(FORM0249, FORM0250, FORM0249)
packs[PACK140_MINES_BOSS_2] = FormationPack(FORM0251)
packs[PACK141_MINES_HENCHMAN_LEFT] = FormationPack(FORM0138, FORM0139, FORM0138)
packs[PACK142_MINES_HENCHMAN_MIDDLE] = FormationPack(FORM0138, FORM0139, FORM0138)
packs[PACK143_TOWER_FIREBALLS] = FormationPack(FORM0252, FORM0253, FORM0252)
packs[PACK144_STUMPET_ENCOUNTER] = FormationPack(FORM0254, FORM0255, FORM0254)
packs[PACK145_CORKPEDITE_ENCOUNTER] = FormationPack(FORM0256, FORM0257, FORM0256)
packs[PACK146_FACTORY_BOSS_RUSH_1] = FormationPack(FORM0258)
packs[PACK147_FACTORY_BOSS_RUSH_2] = FormationPack(FORM0259)
packs[PACK148_FACTORY_BOSS_RUSH_3] = FormationPack(FORM0260)
packs[PACK149_FACTORY_BOSS_RUSH_4] = FormationPack(FORM0261)
packs[PACK150_FACTORY_BOSS_RUSH_HENCHMAN] = FormationPack(FORM0262)
packs[PACK151_UNUSED] = FormationPack(FORM0263)
packs[PACK152_MINES_BOSS_ROOM_HENCHMAN] = FormationPack(FORM0060, FORM0061, FORM0062)
packs[PACK153_UNUSED] = FormationPack(FORM0264)
packs[PACK154_UNUSED] = FormationPack(FORM0265)
packs[PACK155_POSSIBLY_UNUSED] = FormationPack(FORM0226)
packs[PACK156_SEWER_CHEST_FIGHT] = FormationPack(FORM0266)
packs[PACK157_SHIP_CHEST_FIGHT] = FormationPack(FORM0267)
packs[PACK158_VALLEY_CHEST_FIGHT] = FormationPack(FORM0268)
packs[PACK159_SIX_DOOR_RUSH_FIGHT] = FormationPack(FORM0269)
packs[PACK160_UNUSED] = FormationPack(FORM0270)
packs[PACK161_TOWER_FIRST_FIGHT] = FormationPack(FORM0271)
packs[PACK162__UNUSED] = FormationPack(FORM0272)
packs[PACK163_BANDITS_WAY_BOSS] = FormationPack(FORM0273)
packs[PACK164_MINES_FIRST_BOSS] = FormationPack(FORM0274)
packs[PACK165_UNUSED] = FormationPack(FORM0275)
packs[PACK166_SHIP_SECOND_BOSS] = FormationPack(FORM0276)
packs[PACK167_SHIP_FIRST_BOSS] = FormationPack(FORM0277)
packs[PACK168_SEWER_BOSS] = FormationPack(FORM0278)
packs[PACK169_TEMPLE_BOSS] = FormationPack(FORM0279)
packs[PACK170_UNUSED] = FormationPack(FORM0280)
packs[PACK171_NIMBUS_CASTLE_THIRD_BOSS] = FormationPack(FORM0281)
packs[PACK172_VOLCANO_FIRST_BOSS] = FormationPack(FORM0282)
packs[PACK173_VALLEY_BOSS] = FormationPack(FORM0283)
packs[PACK174_FACTORY_FIRST_BOSS] = FormationPack(FORM0284)
packs[PACK175_NIMBUS_CASTLE_SECOND_BOSS] = FormationPack(FORM0285)
packs[PACK176_CHAPEL_BOSS] = FormationPack(FORM0286)
packs[PACK177_TOWER_SECOND_BOSS] = FormationPack(FORM0287)
packs[PACK178_DOJO_FIGHT_1] = FormationPack(FORM0288)
packs[PACK179_MUSHROOM_KINGDOM_BOSS] = FormationPack(FORM0289)
packs[PACK180_SEASIDE_BOSS] = FormationPack(FORM0290)
packs[PACK181_FOREST_BOSS] = FormationPack(FORM0291)
packs[PACK182_VOLCANO_BOSS] = FormationPack(FORM0292)
packs[PACK183_MUSHROOM_WAY_BOSS] = FormationPack(FORM0293)
packs[PACK184_FACTORY_SECOND_BOSS] = FormationPack(FORM0294)
packs[PACK185_FINAL_BOSS] = FormationPack(FORM0295)
packs[PACK186_KEEP_THIRD_BOSS] = FormationPack(FORM0296)
packs[PACK187_DOJO_SECOND_BOSS] = FormationPack(FORM0297)
packs[PACK188_DOJO_THIRD_BOSS] = FormationPack(FORM0298)
packs[PACK189_DOJO_PREFIGHT] = FormationPack(FORM0299)
packs[PACK190_UNUSED] = FormationPack(FORM0192)
packs[PACK191_HEAVY_TROOPAS] = FormationPack(FORM0300)
packs[PACK192_UNUSED] = FormationPack(FORM0301)
packs[PACK193_UNUSED] = FormationPack(FORM0302)
packs[PACK194_UNUSED] = FormationPack(FORM0303, FORM0304, FORM0303)
packs[PACK195_UNUSED] = FormationPack(FORM0303, FORM0304, FORM0304)
packs[PACK196_UNUSED] = FormationPack(FORM0305)
packs[PACK197_UNUSED] = FormationPack(FORM0306)
packs[PACK198_UNUSED] = FormationPack(FORM0307)
packs[PACK199_CROOKS_ONLY] = FormationPack(FORM0138, FORM0139, FORM0138)
packs[PACK200_UNUSED] = FormationPack(FORM0308)
packs[PACK201_UNUSED] = FormationPack(FORM0165, FORM0167, FORM0165)
packs[PACK202_UNUSED] = FormationPack(FORM0309)
packs[PACK203_UNUSED] = FormationPack(FORM0310, FORM0311, FORM0310)
packs[PACK204_UNUSED] = FormationPack(FORM0312)
packs[PACK205_UNUSED] = FormationPack(FORM0168, FORM0170, FORM0168)
packs[PACK206_DESERT_SHOGUNS] = FormationPack(FORM0313)
packs[PACK207_LANDS_END_CLOUD] = FormationPack(FORM0314)
packs[PACK208_NIMBUS_CASTLE_FIRST_BOSS] = FormationPack(FORM0315)
packs[PACK209_KEEP_FIRST_BOSS] = FormationPack(FORM0316)
packs[PACK210_KEEP_SECOND_BOSS] = FormationPack(FORM0317)
packs[PACK211_MACHINE_MACK_PACK] = FormationPack(FORM0318)
packs[PACK212_MACHINE_BOWYER_PACK] = FormationPack(FORM0319)
packs[PACK213_MACHINE_YARIDOVICH_PACK] = FormationPack(FORM0320)
packs[PACK214_FACTORY_MACHINE_AXEMS] = FormationPack(FORM0310, FORM0311, FORM0310)
packs[PACK215_SMITHY_2_PACK] = FormationPack(FORM0321)
packs[PACK216_MONSTRO_DOOR_BOSS] = FormationPack(FORM0322)
packs[PACK217_UNUSED] = FormationPack(FORM0323)
packs[PACK218_UNUSED] = FormationPack(FORM0324)
packs[PACK219_UNUSED] = FormationPack(FORM0325)
packs[PACK220_UNUSED] = FormationPack(FORM0326)
packs[PACK221_UNUSED] = FormationPack(FORM0327)
packs[PACK222_UNUSED] = FormationPack(FORM0056, FORM0058, FORM0059)
packs[PACK223_UNUSED] = FormationPack(FORM0328, FORM0329, FORM0330)
packs[PACK224_OBSTACLE_TERRA_COTTA] = FormationPack(FORM0331)
packs[PACK225_OBSTACLE_OERLIKON] = FormationPack(FORM0332)
packs[PACK226_OBSTACLE_SACKIT] = FormationPack(FORM0333)
packs[PACK227_OBSTACLE_CHOW] = FormationPack(FORM0334)
packs[PACK228_OBSTACLE_ALLEYRAT] = FormationPack(FORM0335)
packs[PACK229_OBSTACLE_BLOOBER] = FormationPack(FORM0336)
packs[PACK230_OBSTACLE_STINGER] = FormationPack(FORM0337)
packs[PACK231_OBSTACLE_GECKIT] = FormationPack(FORM0338)
packs[PACK232_OBSTACLE_ROBOMB] = FormationPack(FORM0339)
packs[PACK233_OBSTACLE_VOMER] = FormationPack(FORM0340)
packs[PACK234_OBSTACLE_MAGMUS] = FormationPack(FORM0341)
packs[PACK235_UNUSED] = FormationPack(FORM0342)
packs[PACK236_OBSTACLE_GUGOOMBA] = FormationPack(FORM0343)
packs[PACK237_OBSTACLE_MALAKOOPA] = FormationPack(FORM0344)
packs[PACK238_OBSTACLE_BIGBOO] = FormationPack(FORM0345)
packs[PACK239_OBSTACLE_SLINGSHY] = FormationPack(FORM0346)
packs[PACK240_OBSTACLE_CHEWY] = FormationPack(FORM0347)
packs[PACK241_OBSTACLE_KIPPER] = FormationPack(FORM0348)
packs[PACK242_OBSTACLE_AMANITA] = FormationPack(FORM0349)
packs[PACK243_OBSTACLE_GREAPER] = FormationPack(FORM0350)
packs[PACK244_OBSTACLE_PYROSPHERE] = FormationPack(FORM0351)
packs[PACK245_OBSTACLE_LAKITU] = FormationPack(FORM0352)
packs[PACK246_OBSTACLE_ZEOSTAR] = FormationPack(FORM0353)
packs[PACK247_OBSTACLE_SHAMANS] = FormationPack(FORM0354)
packs[PACK248_UNUSED] = FormationPack(FORM0355)
packs[PACK249_UNUSED] = FormationPack(FORM0356)
packs[PACK250_UNUSED] = FormationPack(FORM0357)
packs[PACK251_UNUSED] = FormationPack(FORM0358)
packs[PACK252_UNUSED] = FormationPack(FORM0359)
packs[PACK253_UNUSED] = FormationPack(FORM0360)
packs[PACK254_UNUSED] = FormationPack(FORM0361)
packs[PACK255_UNUSED] = FormationPack(FORM0301)

# Pack Collection
pack_collection = PackCollection(packs[:256])

