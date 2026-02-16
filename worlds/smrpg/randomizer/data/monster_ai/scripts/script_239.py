# 239 - SMITHYChestEnemy
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
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(DummySpell40, DummySpell39, DummySpell41),
	SetVarBits(BV7EE003, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(DummySpell40, DummySpell38, DummySpell41),
	SetVarBits(BV7EE003, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0098_SMITHY_IS_DEFEATED),
	ExitBattle(),
	Wait1TurnandRestartScript(),
	IfHPBelow(2000),
	IfVarBitsClear(BV7EE002, [5]),
	SetVarBits(BV7EE002, [2]),
	SetVarBits(BV7EE002, [5]),
	ClearVarBits(BV7EE002, [1]),
	ClearVar(BV7EE009),
	Wait1TurnandRestartScript(),
	IfHPBelow(4000),
	IfVarBitsClear(BV7EE002, [6]),
	SetVarBits(BV7EE002, [1]),
	SetVarBits(BV7EE002, [6]),
	ClearVarBits(BV7EE002, [0]),
	ClearVar(BV7EE009),
	Wait1TurnandRestartScript(),
	IfHPBelow(6000),
	IfVarBitsClear(BV7EE002, [7]),
	SetVarBits(BV7EE002, [0]),
	SetVarBits(BV7EE002, [7]),
	ClearVar(BV7EE009),
	Wait1TurnandRestartScript()
])