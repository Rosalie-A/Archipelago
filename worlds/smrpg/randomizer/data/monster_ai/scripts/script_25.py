# 25 - BOBOMBEnemy
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
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	Wait1TurnandRestartScript(),
	Attack(BOBOMBBOMBAttack),
	RemoveTarget(SELF),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByElement([Element.FIRE]),
	Attack(BOBOMBBOMBAttack),
	IncreaseVarBy1(BV7EE001),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])