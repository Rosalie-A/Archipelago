# 76 - MANAGEREnemy
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
	CallTarget(MONSTER_2_CALL),
	CallTarget(MONSTER_3_CALL),
	CallTarget(MONSTER_4_CALL),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack25, SpritzBombAttack),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	Attack(Attack1, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])