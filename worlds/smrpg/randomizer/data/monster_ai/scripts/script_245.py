# 245 - AXEMRANGERSEnemy
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
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	RunBattleEvent(BE0062_JINX_4_BE),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE004, [1]),
	IfVarBitsSet(BV7EE002, [0]),
	SetVarBits(BV7EE004, [1]),
	RunBattleDialog(180),
	RunBattleDialog(181),
	CastSpell(BreakerBeamSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE002, [0]),
	IfVarEqualOrGreaterThan(BV7EE00D, 1),
	ClearVar(BV7EE00D),
	CastSpell(BreakerBeamSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE002, [0]),
	RunBattleDialog(222),
	IncreaseVarBy1(BV7EE00D),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0069_AXEM_RANGERS_ARE_DEFEATED),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])