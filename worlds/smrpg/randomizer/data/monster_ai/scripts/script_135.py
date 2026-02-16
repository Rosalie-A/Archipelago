# 135 - SHELLYEnemy
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
	StartCounterCommands(),
	IfHPBelow(400, identifier="shelly_low_hp_check_80_percent"),
	IfVarBitsClear(BV7EE004, [3]),
	SetVarBits(BV7EE004, [3]),
	RunObjectSequence(4),
	Wait1TurnandRestartScript(),
	IfHPBelow(300, identifier="shelly_low_hp_check_60_percent"),
	IfVarBitsClear(BV7EE004, [2]),
	SetVarBits(BV7EE004, [2]),
	RunObjectSequence(5),
	Wait1TurnandRestartScript(),
	IfHPBelow(200, identifier="shelly_low_hp_check_40_percent"),
	IfVarBitsClear(BV7EE004, [1]),
	SetVarBits(BV7EE004, [1]),
	RunObjectSequence(6),
	Wait1TurnandRestartScript(),
	IfHPBelow(100, identifier="shelly_low_hp_check_20_percent"),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	RunObjectSequence(7),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(8),
	RunBattleEvent(BE0092_SHELLY_BREAKS),
	CallTarget(MONSTER_1_CALL),
	RunObjectSequence(2),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])