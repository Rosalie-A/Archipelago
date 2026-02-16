# 251 - VALENTINAEnemy
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing
from ...variables.battle_event_names import *
from ...variables.battle_variable_names import *
from ...items.items import *
from ...spells.spells import *
from ...enemies.enemies import *
from ...enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *

script = MonsterScript([
	IfVarBitsClear(BV7EE003, [0]),
	IfTargetAlive(SLOT_2),
	SetVarBits(BV7EE003, [0, 6]),
	SetUntargetable(SELF),
	RunBattleEvent(BE0048_VALENTINA_SUMMONS_DODO_DODO_CARRIES_OFF_MIDDLE_CHARACTER),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE003, [0]),
	SetVarBits(BV7EE003, [0, 1, 2, 5]),
	SetTargetable(MONSTER_2_SET),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE00D, 5),
	ClearVar(BV7EE00D),
	CastSpell(PetalBlastSpell, AuroraFlashSpell, LightBeamSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	IfVarBitsSet(BV7EE003, [2]),
	CastSpell(SolidifySpell, DrainBeamSpell, DiamondSawSpell),
	IncreaseVarBy1(BV7EE00D),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE003, [2]),
	Attack(Attack0),
	IncreaseVarBy1(BV7EE00D),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	IfVarBitsSet(BV7EE003, [1]),
	CastSpell(WaterBlastSpell, BlizzardSpell, CrystalSpell),
	IncreaseVarBy1(BV7EE00D),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE003, [1]),
	Attack(Attack0),
	IncreaseVarBy1(BV7EE00D),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(1200),
	IfVarBitsSet(BV7EE003, [6]),
	IfVarBitsClear(BV7EE003, [2]),
	IfVarBitsSet(BV7EE003, [1]),
	SetVarBits(BV7EE003, [2]),
	ClearVarBits(BV7EE003, [3]),
	SetTargetable(MONSTER_2_SET),
	RunBattleEvent(BE0050_DODO_RETURNS_TO_VALENTINA_S_FORMATION),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunBattleEvent(BE0051_VALENTINA_DODO_END),
	RemoveTarget(ALL_ALLIES_AND_SELF),
	Wait1TurnandRestartScript()
])