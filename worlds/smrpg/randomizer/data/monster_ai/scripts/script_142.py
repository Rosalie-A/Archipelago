# 142 - TORTEEnemy
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
    IfCurrentlyInFormationID(286),
	IfVarBitsClear(BV7EE001, [0]),
	SetVarBits(BV7EE001, [0]),
	IfTargetAlive(MONSTER_2_SET),
	SetUntargetable(MONSTER_2_SET),
	MakeInvulnerable(MONSTER_3_SET),
	MakeInvulnerable(MONSTER_4_SET),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	RunBattleDialog(135),
	Attack(Attack3),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	RunBattleDialog(136),
	Attack(Attack3),
	StartCounterCommands()
])