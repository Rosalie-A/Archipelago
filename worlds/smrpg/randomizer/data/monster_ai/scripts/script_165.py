# 165 - MACHINEMADEYaridovichEnemy
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
	IfVarEqualOrGreaterThan(BV7EE003, 8),
	IfVarBitsSet(BV7EE000, [1]),
	ClearVarBits(BV7EE000, [1]),
	ClearVar(BV7EE003),
	ClearVar(BV7EE007),
	SetTargetable(SELF),
	RunBattleEvent(BE0025_DRILL_BIT),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE000, [0]),
	Attack(Attack1, PierceAttack, Attack31),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE000, [1]),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE001, 1),
	CastSpell(FlameStoneSpell, FlameStoneSpell, MeteorBlastSpell),
	IncreaseVarBy1(BV7EE001),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE001),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 3),
	SetVarBits(BV7EE000, [1]),
	SetUntargetable(SELF),
	RunBattleDialog(134),
	RunBattleEvent(BE0024_MACHINE_MADE_YARIDOVICH_MULTIPLIER),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
	RemoveTarget(MONSTER_2_SET),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])