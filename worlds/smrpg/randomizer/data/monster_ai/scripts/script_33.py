# 33 - KAMEKEnemy
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
	IfVarBitsSet(BV7EE000, [0]),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE000, [0]),
	IfVarEqualOrGreaterThan(BV7EE001, 1),
	ClearVar(BV7EE001),
	SetVarBits(BV7EE000, [0]),
	SetUntargetable(SELF),
	RunBattleEvent(BE0079_MAGIKOOPA_SUMMONS_MONSTER),
	RunBattleDialog(217),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(BoltSpell, BlastSpell, WillyWispSpell),
	IncreaseVarBy1(BV7EE001),
	Wait1TurnandRestartScript(),
	CastSpell(WaterBlastSpell, SolidifySpell, FlameWallSpell),
	IncreaseVarBy1(BV7EE001),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])