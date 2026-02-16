# 56 - DODOEnemy
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
	IfVarBitsSet(BV7EE003, [3]),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE003, [1]),
	Attack(Attack1, MultistrikeAttack, FlutterHushAttack),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE003, [2]),
	Attack(Attack1, MultistrikeAttack, FlutterHushAttack),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(600, identifier="dodo_low_hp_check"),
	IfVarBitsSet(BV7EE003, [6]),
	IfVarBitsClear(BV7EE003, [3]),
	IfVarBitsClear(BV7EE003, [5]),
	SetVarBits(BV7EE003, [5]),
	SetVarBits(BV7EE003, [3]),
	SetVarBits(BV7EE003, [1]),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	RunBattleEvent(BE0049_DODO_FLUTTERS_AND_LEAVES_BATTLE),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	SetVarBits(BV7EE003, [3]),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(Attack1, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])