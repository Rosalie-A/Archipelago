# 144 - JINXCLONEEnemy
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
	Attack(JinxedAttack, JinxedAttack, TripleKickAttack),
	Wait1Turn(),
	Attack(JinxedAttack, TripleKickAttack, QuicksilverAttack),
	Wait1Turn(),
	Attack(QuicksilverAttack, BombsAwayAttack, SilverBulletAttack),
	Wait1Turn(),
	StartCounterCommands(),
	IfHPBelow(0),
	ClearVar(BV7EE000),
	SetTargetable(MONSTER_1_SET),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])