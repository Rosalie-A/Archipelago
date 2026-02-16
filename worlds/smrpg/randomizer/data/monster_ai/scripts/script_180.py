# 180 - JINX 4

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
	IfVarBitsClear(BV7EE002, [0]),
	SetTarget(SELF),
	Attack(ATKDEF100Attack),
	SetTarget(RANDOM_OPPONENT),
	SetVarBits(BV7EE002, [0]),
	Attack(TripleKickAttack, QuicksilverAttack, BombsAwayAttack),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	Attack(SilverBulletAttack),
	Wait1TurnandRestartScript(),
	Attack(TripleKickAttack, QuicksilverAttack, BombsAwayAttack),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	RunObjectSequence(14),
	IfVarLessThan(BV7EE003, 1),
	RunBattleDialog(80),
	Attack(SilverBulletAttack),
	ClearVar(BV7EE003),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	RunObjectSequence(14),
	IfVarEqualOrGreaterThan(BV7EE003, 100),
	IncreaseVarBy1(BV7EE00A),
	RunBattleEvent(BE0062_JINX_4_BE),
	IfVarEqualOrGreaterThan(BV7EE00A, 15),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	RunObjectSequence(14),
	IfVarEqualOrGreaterThan(BV7EE003, 100),
	IncreaseVarBy1(BV7EE00A),
	RunBattleEvent(BE0062_JINX_4_BE),
	ClearVar(BV7EE003),
	Wait1TurnandRestartScript()
])