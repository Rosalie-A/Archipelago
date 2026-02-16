# 241 - CROCO2Enemy
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
	IfVarBitsSet(BV7EE004, [1]),
	Attack(Attack14, ChompAttack, ChompAttack),
	Wait1TurnandRestartScript(),
	Attack(Attack14, Attack25, Attack25),
	StartCounterCommands(),
	IfVarBitsClear(BV7EE004, [0]),
	IfHPBelow(400),
	SetVarBits(BV7EE004, [0, 1]),
	RunBattleEvent(BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK),
	RemoveAllInventory(),
	ClearVar(BV7EE00F),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunBattleEvent(BE0016_CROCO_RETURNS_ITEMS_ENOUGH_HERE_S_YOUR_JUNK),
	RemoveAllInventory(),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])