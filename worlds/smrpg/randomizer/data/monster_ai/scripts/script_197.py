# 197 - COUNTDOWNEnemy
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
	IfVarBitsSet(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 1),
	RunObjectSequence(18),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(53),
	CastSpell(CrystalSpell, CrystalSpell, IceRockSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 2),
	RunObjectSequence(19),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(54),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(RecoverSpell),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 3),
	RunObjectSequence(20),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(55),
	CastSpell(AuroraFlashSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 4),
	RunObjectSequence(21),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(56),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(MegaRecoverSpell),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 5),
	RunObjectSequence(22),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(57),
	CastSpell(WaterBlastSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 6),
	RunObjectSequence(23),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(58),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 7),
	RunObjectSequence(24),
	IncreaseVarBy1(BV7EE000),
	RunBattleDialog(59),
	CastSpell(PetalBlastSpell),
	Wait1TurnandRestartScript(),
	RunObjectSequence(25),
	ClearVar(BV7EE000),
	RunBattleDialog(60),
	CastSpell(CoronaSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	IfLastMonsterStanding(),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE004, [1]),
	SetVarBits(BV7EE004, [1]),
	SetVarBits(BV7EE004, [0]),
	SetUntargetable(SELF),
	RunBattleDialog(221),
	RunObjectSequence(26),
	Wait1TurnandRestartScript()
])