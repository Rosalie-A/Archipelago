# 167 - MACHINEMADEAxemBlackEnemy
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
	Attack(Attack5, Attack5, Attack25),
	IfTargetAlive(AT_LEAST_ONE_OPPONENT),
	Attack(Attack5, Attack5, Attack25),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	Attack(SpritzBombAttack),
	Wait1TurnandRestartScript()
])