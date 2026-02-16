# 212 - KINGBOMBEnemy
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
	IfTurnCounterEquals(3),
	SetTargetable(MONSTER_1_SET),
	CastSpell(BigBangSpell),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	ClearVar(BV7EE000),
	SetTargetable(MONSTER_1_SET),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])