# 49 - FROGOGEnemy
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
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	SetTarget(RANDOM_OPPONENT),
	Attack(Attack1),
	Wait1TurnandRestartScript(),
	Attack(Attack1, DUMMYAttack1, DUMMYAttack1),
	StartCounterCommands()
])