# 37 - BLASTEREnemy
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
	Attack(BlazerAttack),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	Attack(Attack29, Attack29, DoNothing),
	StartCounterCommands()
])