# 13 - BIRDYEnemyStatic
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
	IfVarBitsSet(BV7EE004, [0]),
	RunBattleDialog(209),
	SetTarget(RANDOM_ALLY_OR_SELF),
	Attack(Attack0),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(Attack10, Attack10, GrinderAttack),
	StartCounterCommands(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarBitsClear(BV7EE004, [0]),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	RunBattleDialog(208),
	SetVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript()
])