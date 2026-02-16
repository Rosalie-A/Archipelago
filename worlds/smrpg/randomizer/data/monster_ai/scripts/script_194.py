# 194 - BUNDTEnemy
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
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack31, LullaByeAttack),
	ClearVarBits(BV7EE00F, [0]),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	IfVarEqualOrGreaterThan(BV7EE007, 1),
	IfVarBitsClear(BV7EE000, [7]),
	DecreaseVarBy1(BV7EE007),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	IfVarEqualOrGreaterThan(BV7EE007, 1),
	ClearVarBits(BV7EE000, [7]),
	Wait1TurnandRestartScript(),
	CastSpell(DiamondSawSpell, BlizzardSpell, BlizzardSpell),
	IfVarEqualOrGreaterThan(BV7EE007, 1),
	IfVarBitsClear(BV7EE000, [7]),
	DecreaseVarBy1(BV7EE007),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE007, 1),
	ClearVarBits(BV7EE000, [7]),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(200),
	IfVarBitsClear(BV7EE000, [1]),
	SetVarBits(BV7EE000, [1]),
	RunBattleEvent(BE0031_UNUSED),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE000, [0]),
	IfVarBitsSet(BV7EE000, [1]),
	SetVarBits(BV7EE000, [0]),
	RunBattleEvent(BE0032_BUNDT_MOVES_AGAIN_BOTH_COOKS_RUN_AWAY),
	RemoveTarget(MONSTER_3_SET),
	RemoveTarget(MONSTER_4_SET),
	RunBattleEvent(BE0033_CANDLES_APPEAR_ON_BUNDT),
	SetUntargetable(MONSTER_3_SET),
	RunBattleEvent(BE0034_BLOW_THOSE_CANDLES_OUT),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE007, 5),
	SetTargetable(MONSTER_3_SET),
	RemoveTarget(MONSTER_3_SET),
	RunObjectSequence(6),
	SetTargetable(MONSTER_2_SET),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	IfVarBitsSet(BV7EE000, [0]),
	IncreaseVarBy1(BV7EE007),
	IfVarLessThan(BV7EE00A, 2),
	SetVarBits(BV7EE000, [7]),
	Wait1TurnandRestartScript()
])