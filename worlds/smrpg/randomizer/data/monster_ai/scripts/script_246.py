# 246 - BOOSTEREnemy
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
	IfLastMonsterStanding(),
	IfHPBelow(500),
	Attack(Attack1, SpritzBombAttack, LocoExpressAttack),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	Attack(Attack1, Attack25, Attack1),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])