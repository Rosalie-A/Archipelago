from .RandomizedUnits import *

generic_job_table: dict[Job, list[Job]] = {
    Job.SQUIRE: [Job.SQUIRE, Job.FEMALE_SQUIRE],
    Job.CHEMIST: [Job.CHEMIST, Job.FEMALE_CHEMIST],
    Job.KNIGHT: [Job.KNIGHT, Job.FEMALE_KNIGHT],
    Job.ARCHER: [Job.ARCHER, Job.FEMALE_ARCHER],
    Job.MONK: [Job.MONK, Job.FEMALE_MONK],
    Job.PRIEST: [Job.PRIEST, Job.FEMALE_PRIEST],
    Job.WIZARD: [Job.WIZARD, Job.FEMALE_WIZARD],
    Job.TIMEMAGE: [Job.TIMEMAGE, Job.FEMALE_TIMEMAGE],
    Job.SUMMONER: [Job.SUMMONER, Job.FEMALE_SUMMONER],
    Job.THIEF: [Job.THIEF, Job.FEMALE_THIEF],
    Job.MEDIATOR: [Job.MEDIATOR, Job.FEMALE_MEDIATOR],
    Job.ORACLE: [Job.ORACLE, Job.FEMALE_ORACLE],
    Job.GEOMANCER: [Job.GEOMANCER, Job.FEMALE_GEOMANCER],
    Job.LANCER: [Job.LANCER, Job.FEMALE_LANCER],
    Job.SAMURAI: [Job.SAMURAI, Job.FEMALE_SAMURAI],
    Job.NINJA: [Job.NINJA, Job.FEMALE_NINJA],
    Job.CALCULATOR: [Job.CALCULATOR, Job.FEMALE_CALCULATOR],
    Job.BARD: [Job.BARD],
    Job.DANCER: [Job.DANCER],
    Job.MIME: [Job.MIME, Job.FEMALE_MIME]
}

generic_monster_table: dict[Job, list[Job]] = {
    Job.YELLOW_CHOCOBO: [Job.YELLOW_CHOCOBO],
    Job.GOBLIN: [Job.GOBLIN],
    Job.BOMB: [Job.BOMB],
    Job.RED_PANTHER: [Job.RED_PANTHER],
    Job.PISCO_DEMON: [Job.PISCO_DEMON],
    Job.SKELETON: [Job.SKELETON],
    Job.GHOUL: [Job.GHOUL],
    Job.FLOTIBALL: [Job.FLOTIBALL],
    Job.JURAVIS: [Job.JURAVIS],
    Job.URIBO: [Job.URIBO],
    Job.WOODMAN: [Job.WOODMAN],
    Job.BULL_DEMON: [Job.BULL_DEMON],
    Job.MORBOL: [Job.MORBOL],
    Job.BEHEMOTH: [Job.BEHEMOTH],
    Job.DRAGON: [Job.DRAGON],
    Job.HYUDRA: [Job.HYUDRA]
}

special_job_table: dict[Job, list[Job]] = {
    #Job.RAMZA_SQUIRE_CHAPTER_1: [Job.RAMZA_SQUIRE_CHAPTER_1],
    #Job.RAMZA_SQUIRE_CHAPTER_23: [Job.RAMZA_SQUIRE_CHAPTER_23],
    #Job.RAMZA_SQUIRE_CHAPTER_4: [Job.RAMZA_SQUIRE_CHAPTER_4],
    Job.SQUIRE_DELITA: [Job.SQUIRE_DELITA],
    Job.SQUIRE_ALGUS: [Job.SQUIRE_ALGUS],
    Job.HOLY_KNIGHT_DELITA: [Job.HOLY_KNIGHT_DELITA],
    Job.ARC_KNIGHT_DELITA: [Job.ARC_KNIGHT_DELITA],
    Job.HOLY_KNIGHT_AGRIAS: [Job.HOLY_KNIGHT_AGRIAS],
    Job.ARC_KNIGHT_ZALBAG: [Job.ARC_KNIGHT_ZALBAG],
    Job.LUNE_KNIGHT: [Job.LUNE_KNIGHT],
    Job.PRINCESS: [Job.PRINCESS],
    Job.HOLY_SWORDSMAN: [Job.HOLY_SWORDSMAN],
    Job.DRAGONER: [Job.DRAGONER],
    Job.HOLY_PRIEST: [Job.HOLY_PRIEST],
    Job.DARK_KNIGHT_ENEMY: [Job.DARK_KNIGHT_ENEMY],
    Job.ASTROLOGIST: [Job.ASTROLOGIST],
    Job.ENGINEER_MUSTADIO: [Job.ENGINEER_MUSTADIO, Job.ENGINEER_BALK],
    Job.HELL_KNIGHT: [Job.HELL_KNIGHT],
    Job.ARC_KNIGHT_ELMDOR: [Job.ARC_KNIGHT_ELMDOR],
    Job.TEMPLE_KNIGHT: [Job.TEMPLE_KNIGHT],
    Job.WHITE_KNIGHT_C1: [Job.WHITE_KNIGHT_C1, Job.WHITE_KNIGHT_C3],
    Job.DIVINE_KNIGHT_VORMAV: [Job.DIVINE_KNIGHT_VORMAV, Job.DIVINE_KNIGHT_ROFEL, Job.DIVINE_KNIGHT_MELIADOUL],
    Job.KNIGHT_BLADE: [Job.KNIGHT_BLADE],
    Job.SORCERER: [Job.SORCERER],
    Job.HEAVEN_KNIGHT: [Job.HEAVEN_KNIGHT],
    Job.ASSASSIN_CELIA: [Job.ASSASSIN_CELIA, Job.ASSASSIN_LEDE],
    Job.CLERIC: [Job.CLERIC],
    Job.SOLDIER: [Job.SOLDIER],
    Job.KNIGHT_UNDEAD: [
        Job.KNIGHT_UNDEAD, Job.ARCHER_UNDEAD, Job.ORACLE_UNDEAD, Job.WIZARD_UNDEAD,
        Job.TIME_MAGE_UNDEAD, Job.SUMMONER_UNDEAD
    ]
}

special_monster_table: dict[Job, list[Job]] = {
    Job.HOLY_DRAGON: [Job.HOLY_DRAGON],
    Job.BYBLOS: [Job.BYBLOS],
    Job.STEEL_GIANT: [Job.STEEL_GIANT],
    Job.APANDA: [Job.APANDA],
    Job.ARCHAIC_DEMON: [Job.ARCHAIC_DEMON],
}

lucavi_table: dict[Job, list[Job]] = {
    Job.QUEKLAIN: [Job.QUEKLAIN],
    Job.VELIUS: [Job.VELIUS],
    Job.ZALERA: [Job.ZALERA],
    Job.ADRAMELK: [Job.ADRAMELK],
    Job.ELIDIBS: [Job.ELIDIBS],
    Job.HASHMALUM: [Job.HASHMALUM]
}

altima_table: dict[Job, list[Job]] = {
    Job.ALTIMA_1: [Job.ALTIMA_1],
    Job.ALTIMA_2: [Job.ALTIMA_2],
}

factory_mappings: dict[Job, dict[type[RandomizedUnit], int]] = {
    Job.RAMZA_SQUIRE_CHAPTER_1: {RamzaC1Squire: 1},
    Job.RAMZA_SQUIRE_CHAPTER_23: {RamzaC23Squire: 1},
    Job.RAMZA_SQUIRE_CHAPTER_4: {RamzaC4Squire: 9, RamzaC4SquireFullSkillset: 1},
    Job.SQUIRE_DELITA: {DelitaSquire: 1, DelitaSquireHard: 9},
    Job.HOLY_KNIGHT_DELITA: {DelitaHolyKnight: 1, DelitaHolyKnightHard: 9},
    Job.ARC_KNIGHT_DELITA: {DelitaArcKnight: 1, DelitaArcKnightHard: 9},
    Job.SQUIRE_ALGUS: {Algus: 9, AlgusWithCrossbow: 1, AlgusHard: 90, AlgusWithCrossbowHard: 10},
    Job.ARC_KNIGHT_ZALBAG: {ZalbagArcKnight: 1, ZalbagArcKnightHard: 9},
    Job.LUNE_KNIGHT: {LuneKnight: 1, LuneKnightHard: 9},
    Job.PRINCESS: {Princess: 1, PrincessHard: 9},
    Job.HOLY_SWORDSMAN: {HolySwordsman: 1, HolySwordsmanHard: 9, HolySwordsmanWithExcalibur: 1},
    Job.DRAGONER: {Dragoner: 1, DragonerHard: 9},
    Job.HOLY_PRIEST: {HolyPriest: 1, HolyPriestHard: 9},
    Job.DARK_KNIGHT_ENEMY: {DarkKnight: 1, DarkKnightHard: 9},
    Job.ASTROLOGIST: {Astrologist: 1, AstrologistHard: 9},
    Job.ENGINEER_MUSTADIO: {EngineerMustadio: 1, EngineerMustadioHard: 9},
    Job.DARK_KNIGHT_GUEST: {DarkKnight: 1, DarkKnightHard: 9},
    Job.HEAVEN_KNIGHT_GUEST: {HeavenKnight: 1, HeavenKnightHard: 9},
    Job.HELL_KNIGHT: {HellKnight: 1, HellKnightHard: 9},
    Job.ARC_KNIGHT_ELMDOR: {ArcKnightElmdor: 1, ArcKnightElmdorHard: 9, ArcKnightElmdorWithKit: 1},
    Job.HOLY_KNIGHT_AGRIAS: {HolyKnightAgrias: 1, HolyKnightAgriasHard: 9},
    Job.TEMPLE_KNIGHT: {TempleKnight: 1, TempleKnightHard: 9},
    Job.WHITE_KNIGHT_C1: {
        WhiteKnightChapter1: 9, WhiteKnightChapter1WithCounter: 1,
        WhiteKnightChapter1Hard: 90, WhiteKnightChapter1WithCounterHard: 10
    },
    Job.ENGINEER_GUEST: {EngineerMustadio: 1, EngineerMustadioHard: 9},
    Job.DIVINE_KNIGHT_VORMAV: {DivineKnightVormav: 1, DivineKnightVormavHard: 9},
    Job.DIVINE_KNIGHT_ROFEL: {DivineKnightRofel: 1, DivineKnightRofelHard: 9},
    Job.KNIGHT_BLADE: {
        KnightBlade: 1, KnightBladeWithKit: 1, KnightBladeHard: 9
    },
    Job.SORCERER: {Sorcerer: 1, SorcererHard: 9},
    Job.WHITE_KNIGHT_C3: {
        WhiteKnight: 9, WhiteKnightWithCounter: 1,
        WhiteKnightHard: 90, WhiteKnightWithCounterHard: 10
    },
    Job.HEAVEN_KNIGHT: {HeavenKnight: 1, HeavenKnightHard: 9},
    Job.DIVINE_KNIGHT_MELIADOUL: {DivineKnightMeliadoul: 1, DivineKnightMeliadoulHard: 9},
    Job.ENGINEER_BALK: {EngineerBalk: 1, EngineerBalkHard: 9},
    Job.ASSASSIN_CELIA: {AssassinCelia: 1},
    Job.ASSASSIN_LEDE: {AssassinLede: 1},
    Job.DIVINE_KNIGHT_MELIADOUL_ENEMY: {DivineKnightMeliadoul: 1, DivineKnightMeliadoulHard: 9},
    Job.CLERIC: {
        Cleric: 9, ClericWithUltima: 1,
        ClericHard: 90, ClericWithUltimaHard: 10
    },
    Job.SOLDIER: {Soldier: 1, SoldierHard: 9},
    Job.ARC_KNIGHT_ZOMBIE: {ArcKnightZombie: 9, ArcKnightZombieWithKit: 1},
    Job.HOLY_KNIGHT_AGRIAS_GUEST: {HolyKnightAgrias: 1},
    Job.KNIGHT_UNDEAD: {UndeadKnight: 1},
    Job.ARCHER_UNDEAD: {UndeadArcher: 1},
    Job.ALTIMA_1: {Altima1: 1},
    Job.WIZARD_UNDEAD: {UndeadWizard: 1},
    Job.TIME_MAGE_UNDEAD: {UndeadTimeMage: 1},
    Job.ORACLE_UNDEAD: {UndeadOracle: 1},
    Job.SUMMONER_UNDEAD: {UndeadSummoner: 1},
    Job.ALTIMA_2: {Altima2: 1},
    Job.SQUIRE: {
        MaleSquire: 1,
        MaleSquireEasy: 2,
        MaleSquireModerate1: 3, MaleSquireModerate2: 3,
        MaleSquireAdvanced1: 4, MaleSquireAdvanced2: 4,
        MaleSquireExpert1: 5, MaleSquireExpert2: 5, MaleSquireExpert3: 5,
        MaleSquireRare: 1
    },
    Job.FEMALE_SQUIRE: {
        FemaleSquire: 1,
        FemaleSquireEasy: 2,
        FemaleSquireModerate1: 3, FemaleSquireModerate2: 3,
        FemaleSquireAdvanced1: 4, FemaleSquireAdvanced2: 4,
        FemaleSquireExpert1: 5, FemaleSquireExpert2: 5, FemaleSquireExpert3: 5, FemaleSquireExpert4: 5,
        FemaleSquireRare: 1
    },
    Job.CHEMIST: {
        MaleChemist: 1,
        MaleChemistEasy: 2,
        MaleChemistModerate1: 3, MaleChemistModerate2: 3,
        MaleChemistAdvanced1: 4, MaleChemistAdvanced2: 4,
        MaleChemistExpert1: 5, MaleChemistExpert2: 5, MaleChemistExpert3: 5,
        MaleChemistRare: 1
    },
    Job.FEMALE_CHEMIST: {
        FemaleChemist: 1,
        FemaleChemistEasy: 2,
        FemaleChemistModerate1: 3, FemaleChemistModerate2: 3,
        FemaleChemistAdvanced1: 4, FemaleChemistAdvanced2: 4,
        FemaleChemistExpert1: 5, FemaleChemistExpert2: 5,
        FemaleChemistRare: 1
    },
    Job.KNIGHT: {
        MaleKnight: 1,
        MaleKnightEasy: 2,
        MaleKnightModerate: 3,
        MaleKnightAdvanced: 4,
        MaleKnightExpert1: 5, MaleKnightExpert2: 5, MaleKnightExpert3: 5,
        MaleKnightRare: 1
    },
    Job.FEMALE_KNIGHT: {
        FemaleKnight: 1,
        FemaleKnightEasy: 2,
        FemaleKnightModerate: 3,
        FemaleKnightAdvanced: 4,
        FemaleKnightExpert1: 5, FemaleKnightExpert2: 5, FemaleKnightExpert3: 5, FemaleKnightExpert4: 5,
        FemaleKnightRare: 1
    },
    Job.ARCHER: {
        MaleArcher: 1,
        MaleArcherEasy: 2,
        MaleArcherModerate: 3,
        MaleArcherAdvanced: 4,
        MaleArcherExpert1: 5, MaleArcherExpert2: 5, MaleArcherExpert3: 5,
        MaleArcherRare: 1
    },
    Job.FEMALE_ARCHER: {
        FemaleArcher: 1,
        FemaleArcherEasy: 2,
        FemaleArcherModerate: 3,
        FemaleArcherAdvanced: 4,
        FemaleArcherExpert1: 5, FemaleArcherExpert2: 5, FemaleArcherExpert3: 5, FemaleArcherExpert4: 5,
        FemaleArcherRare: 1
    },
    Job.MONK: {
        MaleMonk: 1,
        MaleMonkEasy: 2,
        MaleMonkModerate: 3,
        MaleMonkAdvanced: 4,
        MaleMonkExpert1: 5, MaleMonkExpert2: 5, MaleMonkExpert3: 5,
        MaleMonkRare: 1
    },
    Job.FEMALE_MONK: {
        FemaleMonk: 1,
        FemaleMonkEasy: 2,
        FemaleMonkModerate: 3,
        FemaleMonkAdvanced: 4,
        FemaleMonkExpert1: 5, FemaleMonkExpert2: 5, FemaleMonkExpert3: 5, FemaleMonkExpert4: 5,
        FemaleMonkRare: 1
    },
    Job.PRIEST: {
        MalePriest: 1,
        MalePriestEasy: 2,
        MalePriestModerate: 3,
        MalePriestAdvanced1: 4, MalePriestAdvanced2: 4,
        MalePriestExpert1: 5, MalePriestExpert2: 5,
        MalePriestRare: 1
    },
    Job.FEMALE_PRIEST: {
        FemalePriest: 1,
        FemalePriestEasy: 2,
        FemalePriestModerate: 3,
        FemalePriestAdvanced: 4,
        FemalePriestExpert1: 5, FemalePriestExpert2: 5,
        FemalePriestRare: 1
    },
    Job.WIZARD: {
        MaleWizard: 1,
        MaleWizardEasy: 2,
        MaleWizardModerate: 3,
        MaleWizardAdvanced1: 4, MaleWizardAdvanced2: 4,
        MaleWizardExpert1: 5, MaleWizardExpert2: 5,
        MaleWizardRare: 1
    },
    Job.FEMALE_WIZARD: {
        FemaleWizard: 1,
        FemaleWizardEasy: 2,
        FemaleWizardModerate: 3,
        FemaleWizardAdvanced: 4,
        FemaleWizardExpert1: 5, FemaleWizardExpert2: 5,
        FemaleWizardRare: 1
    },
    Job.TIMEMAGE: {
        MaleTimeMage: 1,
        MaleTimeMageEasy: 2,
        MaleTimeMageModerate: 3,
        MaleTimeMageAdvanced1: 4, MaleTimeMageAdvanced2: 4,
        MaleTimeMageExpert1: 5, MaleTimeMageExpert2: 5,
        MaleTimeMageRare: 1
    },
    Job.FEMALE_TIMEMAGE: {
        FemaleTimeMage: 1,
        FemaleTimeMageEasy: 2,
        FemaleTimeMageModerate: 3,
        FemaleTimeMageAdvanced: 4,
        FemaleTimeMageExpert1: 5, FemaleTimeMageExpert2: 5,
        FemaleTimeMageRare: 1
    },
    Job.SUMMONER: {
        MaleSummoner: 1,
        MaleSummonerEasy: 2,
        MaleSummonerModerate: 3,
        MaleSummonerAdvanced1: 4, MaleSummonerAdvanced2: 4,
        MaleSummonerExpert: 5,
        MaleSummonerRare: 1
    },
    Job.FEMALE_SUMMONER: {
        FemaleSummoner: 1,
        FemaleSummonerEasy: 2,
        FemaleSummonerModerate: 3,
        FemaleSummonerAdvanced: 4,
        FemaleSummonerExpert: 5,
        FemaleSummonerRare: 1
    },
    Job.THIEF: {
        MaleThief: 1,
        MaleThiefEasy: 2,
        MaleThiefModerate: 3,
        MaleThiefAdvanced: 4,
        MaleThiefExpert1: 5, MaleThiefExpert2: 5, MaleThiefExpert3: 5,
        MaleThiefRare: 1
    },
    Job.FEMALE_THIEF: {
        FemaleThief: 1,
        FemaleThiefEasy: 2,
        FemaleThiefModerate: 3,
        FemaleThiefAdvanced: 4,
        FemaleThiefExpert1: 5, FemaleThiefExpert2: 5, FemaleThiefExpert3: 5, FemaleThiefExpert4: 5,
        FemaleThiefRare: 1
    },
    Job.MEDIATOR: {
        MaleMediator: 1,
        MaleMediatorEasy: 2,
        MaleMediatorModerate: 3,
        MaleMediatorAdvanced1: 4, MaleMediatorAdvanced2: 4,
        MaleMediatorExpert: 5,
        MaleMediatorRare: 1
    },
    Job.FEMALE_MEDIATOR: {
        FemaleMediator: 1,
        FemaleMediatorEasy: 2,
        FemaleMediatorModerate: 3,
        FemaleMediatorAdvanced: 4,
        FemaleMediatorExpert: 5,
        FemaleMediatorRare: 1
    },
    Job.ORACLE: {
        MaleOracle: 1,
        MaleOracleEasy: 2,
        MaleOracleModerate: 3,
        MaleOracleAdvanced1: 4, MaleOracleAdvanced2: 4,
        MaleOracleExpert1: 5, MaleOracleExpert2: 5,
        MaleOracleRare: 1
    },
    Job.FEMALE_ORACLE: {
        FemaleOracle: 1,
        FemaleOracleEasy: 2,
        FemaleOracleModerate: 3,
        FemaleOracleAdvanced: 4,
        FemaleOracleExpert1: 5, FemaleOracleExpert2: 5,
        FemaleOracleRare: 1
    },
    Job.GEOMANCER: {
        MaleGeomancer: 1,
        MaleGeomancerModerate: 2,
        MaleGeomancerAdvanced: 3,
        MaleGeomancerExpert1: 4, MaleGeomancerExpert2: 4, MaleGeomancerExpert3: 4,
        MaleGeomancerRare: 1
    },
    Job.FEMALE_GEOMANCER: {
        FemaleGeomancer: 1,
        FemaleGeomancerModerate: 2,
        FemaleGeomancerAdvanced1: 3, FemaleGeomancerAdvanced2: 3,
        FemaleGeomancerExpert1: 4, FemaleGeomancerExpert2: 4, FemaleGeomancerExpert3: 4,
        FemaleGeomancerRare: 1
    },
    Job.LANCER: {
        MaleLancer: 1,
        MaleLancerModerate: 2,
        MaleLancerAdvanced: 3,
        MaleLancerExpert1: 4, MaleLancerExpert2: 4, MaleLancerExpert3: 4,
        MaleLancerRare: 1
    },
    Job.FEMALE_LANCER: {
        FemaleLancer: 1,
        FemaleLancerModerate: 2,
        FemaleLancerAdvanced1: 3, FemaleLancerAdvanced2: 3,
        FemaleLancerExpert1: 4, FemaleLancerExpert2: 4, FemaleLancerExpert3: 4,
        FemaleLancerRare: 1
    },
    Job.SAMURAI: {
        MaleSamurai: 2,
        MaleSamuraiAdvanced: 4,
        MaleSamuraiExpert: 6,
        MaleSamuraiRare: 1
    },
    Job.FEMALE_SAMURAI: {
        FemaleSamurai: 2,
        FemaleSamuraiAdvanced1: 4, FemaleSamuraiAdvanced2: 4,
        FemaleSamuraiExpert: 6,
        FemaleSamuraiRare: 1
    },
    Job.NINJA: {
        MaleNinja: 2,
        MaleNinjaAdvanced: 4,
        MaleNinjaExpert: 6,
        MaleNinjaRare: 1
    },
    Job.FEMALE_NINJA: {
        FemaleNinja: 2,
        FemaleNinjaAdvanced1: 4, FemaleNinjaAdvanced2: 4,
        FemaleNinjaExpert: 6,
        FemaleNinjaRare: 1
    },
    Job.CALCULATOR: {
        MaleCalculator: 1,
        MaleCalculatorExpert: 2
    },
    Job.FEMALE_CALCULATOR: {
        FemaleCalculator: 1,
        FemaleCalculatorExpert: 2
    },
    Job.BARD: {MaleBard: 1},
    Job.DANCER: {FemaleDancer: 1},
    Job.MIME: {MaleMime: 1},
    Job.FEMALE_MIME: {FemaleMime: 1},
    Job.YELLOW_CHOCOBO: {YellowChocobo: 1, BlackChocobo: 1, RedChocobo: 1},
    Job.BLACK_CHOCOBO: {YellowChocobo: 1, BlackChocobo: 1, RedChocobo: 1},
    Job.RED_CHOCOBO: {YellowChocobo: 1, BlackChocobo: 1, RedChocobo: 1},
    Job.GOBLIN: {Goblin: 1, BlackGoblin: 1, Gobbledeguck: 1},
    Job.BLACK_GOBLIN: {Goblin: 1, BlackGoblin: 1, Gobbledeguck: 1},
    Job.GOBBLEDEGUCK: {Goblin: 1, BlackGoblin: 1, Gobbledeguck: 1},
    Job.BOMB: {Bomb: 1, Grenade: 1, Explosive: 1},
    Job.GRENADE: {Bomb: 1, Grenade: 1, Explosive: 1},
    Job.EXPLOSIVE: {Bomb: 1, Grenade: 1, Explosive: 1},
    Job.RED_PANTHER: {RedPanther: 1, Cuar: 1, Vampire: 1},
    Job.CUAR: {RedPanther: 1, Cuar: 1, Vampire: 1},
    Job.VAMPIRE: {RedPanther: 1, Cuar: 1, Vampire: 1},
    Job.PISCO_DEMON: {PiscoDemon: 1, Squidlarkin: 1, Mindflare: 1},
    Job.SQUIDLARKIN: {PiscoDemon: 1, Squidlarkin: 1, Mindflare: 1},
    Job.MINDFLARE: {PiscoDemon: 1, Squidlarkin: 1, Mindflare: 1},
    Job.SKELETON: {Skeleton: 1, BoneSnatch: 1, LivingBone: 1},
    Job.BONE_SNATCH: {Skeleton: 1, BoneSnatch: 1, LivingBone: 1},
    Job.LIVING_BONE: {Skeleton: 1, BoneSnatch: 1, LivingBone: 1},
    Job.GHOUL: {Ghoul: 1, Gust: 1, Revnant: 1},
    Job.GUST: {Ghoul: 1, Gust: 1, Revnant: 1},
    Job.REVNANT: {Ghoul: 1, Gust: 1, Revnant: 1},
    Job.FLOTIBALL: {Flotiball: 1, Ahriman: 1, Plague: 1},
    Job.AHRIMAN: {Flotiball: 1, Ahriman: 1, Plague: 1},
    Job.PLAGUE: {Flotiball: 1, Ahriman: 1, Plague: 1},
    Job.JURAVIS: {Juravis: 1, SteelHawk: 1, Cocatoris: 1},
    Job.STEEL_HAWK: {Juravis: 1, SteelHawk: 1, Cocatoris: 1},
    Job.COCATORIS: {Juravis: 1, SteelHawk: 1, Cocatoris: 1},
    Job.URIBO: {Uribo: 1, Porky: 1, Wildbow: 1},
    Job.PORKY: {Uribo: 1, Porky: 1, Wildbow: 1},
    Job.WILDBOW: {Uribo: 1, Porky: 1, Wildbow: 1},
    Job.WOODMAN: {Woodman: 1, Trent: 1, Taiju: 1},
    Job.TRENT: {Woodman: 1, Trent: 1, Taiju: 1},
    Job.TAIJU: {Woodman: 1, Trent: 1, Taiju: 1},
    Job.BULL_DEMON: {BullDemon: 1, Minitaurus: 1, Sacred: 1},
    Job.MINITAURUS: {BullDemon: 1, Minitaurus: 1, Sacred: 1},
    Job.SACRED: {BullDemon: 1, Minitaurus: 1, Sacred: 1},
    Job.MORBOL: {Morbol: 1, Ochu: 1, GreatMorbol: 1},
    Job.OCHU: {Morbol: 1, Ochu: 1, GreatMorbol: 1},
    Job.GREAT_MORBOL: {Morbol: 1, Ochu: 1, GreatMorbol: 1},
    Job.BEHEMOTH: {Behemoth: 1, KingBehemoth: 1, DarkBehemoth: 1},
    Job.KING_BEHEMOTH: {Behemoth: 1, KingBehemoth: 1, DarkBehemoth: 1},
    Job.DARK_BEHEMOTH: {Behemoth: 1, KingBehemoth: 1, DarkBehemoth: 1},
    Job.DRAGON: {Dragon: 1, BlueDragon: 1, RedDragon: 1},
    Job.BLUE_DRAGON: {Dragon: 1, BlueDragon: 1, RedDragon: 1},
    Job.RED_DRAGON: {Dragon: 1, BlueDragon: 1, RedDragon: 1},
    Job.HYUDRA: {Hyudra: 1, Hydra: 1, Tiamat: 1},
    Job.HYDRA: {Hyudra: 1, Hydra: 1, Tiamat: 1},
    Job.TIAMAT: {Hyudra: 1, Hydra: 1, Tiamat: 1},
    Job.HOLY_DRAGON: {HolyDragon: 1},
    Job.BYBLOS: {Byblos: 1},
    Job.STEEL_GIANT: {SteelGiant: 1},
    Job.APANDA: {Apanda: 1},
    Job.ARCHAIC_DEMON: {ArchaicDemon: 1, UltimaDemon: 1},
    Job.ULTIMA_DEMON: {ArchaicDemon: 1, UltimaDemon: 1},
    Job.VELIUS: {VeliusWithKit: 1},
    Job.ZALERA: {ZaleraWithKit: 1},
    Job.HASHMALUM: {HashmalumWithKit: 1},
    Job.QUEKLAIN: {QueklainWithKit: 1},
    Job.ADRAMELK: {AdramelkWithKit: 1},
    Job.ELIDIBS: {Elidibs: 1}
}

base_shuffle_list: list[type[RandomizedUnit]] = [
    Wiegraf1Boss, AlgusBoss, Gafgarion1Boss, Gafgarion2Boss, Gafgarion3Boss, Zalmo1Boss, IzludeBoss, Wiegraf2Boss,
    Malak1Boss, Malak2Boss, Wiegraf3Boss, Elmdor1Boss, Celia1Boss, Lede1Boss, MeliadoulBoss, Zalmo2Boss, Balk1Boss,
    Celia2Boss, Lede2Boss, Celia3Boss, Lede3Boss, Elmdor2Boss, DycedargBoss, VormavBoss, Rofel1Boss, Kletian1Boss,
    ZalbagBoss, Rofel2Boss, Kletian2Boss, Balk2Boss
]

zodiac_story_shuffle_list: list[type[RandomizedUnit]] = [
    QueklainBoss, VeliusBoss, ZaleraBoss, AdramelkBoss, HashmalumBoss
]

altima_story_shuffle_list: list[type[RandomizedUnit]] = [
    Altima1Boss, Altima2Boss
]

sidequest_boss_shuffle_list: list[type[RandomizedUnit]] = [
    Worker7Boss
]

sidequest_zodiac_shuffle_list: list[type[RandomizedUnit]] = [
    ElidibsBoss
]
