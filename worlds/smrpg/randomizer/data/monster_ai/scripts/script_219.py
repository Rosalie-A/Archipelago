# 219 - ZOMBONEEnemy
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
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	CastSpell(BoulderSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(BlastSpell, StormSpell, BoulderSpell),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, ScreamAttack),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0045_ZOMBONE_DIES),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWaterItem]),
	SetTarget(SELF),
	Attack(Attack0),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(Attack1, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])