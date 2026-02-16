# 99 - FORKIESEnemy
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
	RunBattleDialog(152),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarBitsSet(BV7EE004, [1]),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StormSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [1]),
	Attack(Attack3),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	IfVarBitsClear(BV7EE004, [2]),
	RunBattleDialog(153),
	SetVarBits(BV7EE004, [1]),
	SetVarBits(BV7EE004, [2]),
	Wait1TurnandRestartScript()
])