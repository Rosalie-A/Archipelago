# 128 - APPRENTICEEnemyHenchman
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
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StaticESpell, BoltSpell, BoltSpell),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(Attack3, Attack29, GunkBallAttack),
	StartCounterCommands(),
	IfTargetKOed(AT_LEAST_ONE_ALLY),
	IncreaseVarBy1(BV7EE000),
	IfVarEqualOrGreaterThan(BV7EE000, 3),
	SetTargetable(MONSTER_1_SET),
	RunBattleDialog(69),
	Wait1TurnandRestartScript()
])