# 132 - BOOSTERDUMMY
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
	IfVarBitsClear(BV7EE002, [0]),
	SetUntargetable(SELF),
	SetVarBits(BV7EE002, [0]),
	RunBattleDialog(37),
	RunBattleEvent(BE0037_BOOSTER_WORKING),
	SetVarBits(BV7EE001, [0]),
	Wait1TurnandRestartScript(),
	RunBattleDialog(37),
	RunBattleEvent(BE0037_BOOSTER_WORKING),
	SetVarBits(BV7EE001, [0]),
	ClearVarBits(BV7EE001, [1]),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])