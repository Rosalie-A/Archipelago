# 24 - SHYRANGEREnemy
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
	SetTarget(SELF),
	CastSpell(EscapeSpell),
	Wait1TurnandRestartScript(),
	Attack(DUMMYAttack9, Attack20, Attack21),
	StartCounterCommands(),
	IfTargetAfflictedBy(SELF, [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]),
	SetVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(DUMMYAttack9, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])