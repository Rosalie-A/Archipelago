# 137 - DODOEnemySolo
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
	Attack(Attack1, MultistrikeAttack, MultistrikeAttack),
	Wait1Turn(),
	Attack(Attack1, FlutterHushAttack, FlutterHushAttack),
	Wait1Turn(),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0078_DODO_FLUTTERS_AND_EXITS_BATTLE),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(Attack1, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])