# 136 - PUNCHINELLOEnemy
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
	IfVarBitsClear(BV7EE000, [0]),
	SetTarget(SELF),
	Attack(ATKDEF100Attack),
	SetTarget(RANDOM_OPPONENT),
	SetVarBits(BV7EE000, [0]),
	RunBattleEvent(BE0068_PUNCHINELLO_2_SUMMONS_BOMBS),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	RunBattleEvent(BE0068_PUNCHINELLO_2_SUMMONS_BOMBS),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 1),
	Attack(ElegyAttack),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	CastSpell(SandStormSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 3),
	CastSpell(FlameStoneSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 5),
	Attack(Attack1),
	Wait1TurnandRestartScript(),
	Attack(GrinderAttack),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE001, [1]),
	RemoveTarget(MONSTER_2_SET),
	ClearVarBits(BV7EE001, [1]),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE002, [1]),
	RemoveTarget(MONSTER_3_SET),
	ClearVarBits(BV7EE002, [1]),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE003, [1]),
	RemoveTarget(MONSTER_4_SET),
	ClearVarBits(BV7EE003, [1]),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE004, [1]),
	RemoveTarget(MONSTER_5_SET),
	ClearVarBits(BV7EE004, [1]),
	Wait1TurnandRestartScript()
])