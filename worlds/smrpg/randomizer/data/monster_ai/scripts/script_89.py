# 89 - ROBOMBEnemy
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
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	Wait1TurnandRestartScript(),
	Attack(BOBOMBBOMBAttack, BOBOMBBOMBAttack, Attack86),
	RemoveTarget(SELF),
	StartCounterCommands(),
	IfTargetedByElement([Element.FIRE]),
	Attack(BOBOMBBOMBAttack, BOBOMBBOMBAttack, Attack86),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])