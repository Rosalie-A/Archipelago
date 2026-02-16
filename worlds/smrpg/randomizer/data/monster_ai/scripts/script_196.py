# 196 - JINX2Enemy
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
	SetVarBits(BV7EE000, [0]),
	Attack(QuicksilverAttack),
	Wait1TurnandRestartScript(),
	IfHPBelow(400),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	SetTarget(SELF),
	Attack(ValorUpAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE004, [0]),
	Attack(JinxedAttack, TripleKickAttack, QuicksilverAttack),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	Attack(SilverBulletAttack),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(JinxedAttack, TripleKickAttack, QuicksilverAttack),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(TripleKickAttack, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])