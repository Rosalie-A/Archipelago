# 146 - MACHINEMADEDrillbitEnemy
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
	Attack(Attack1, SkewerAttack, Attack1),
	StartCounterCommands(),
	IfCurrentlyInFormationID(320),
	IfTargetKOed(AT_LEAST_ONE_ALLY),
	IncreaseVarBy1(BV7EE007),
	IfVarEqualOrGreaterThan(BV7EE007, 4),
	ClearVar(BV7EE007),
	ClearVar(BV7EE003),
	SetTargetable(MONSTER_1_SET),
	ClearVarBits(BV7EE000, [1]),
	RunBattleEvent(BE0025_DRILL_BIT),
	Wait1TurnandRestartScript()
])