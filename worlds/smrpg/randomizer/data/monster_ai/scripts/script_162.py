# 162 - SMELTEREnemy
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
	IfVarBitsSet(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(2),
	IfVarLessThan(BV7EE000, 2),
	SetVarBits(BV7EE003, [0]),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	IncreaseVarBy1(BV7EE000),
	RunBattleEvent(BE0086_SMELTER_POURS_MOLTEN_LIQUID_SMITHY_WELDS),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetVarBits(BV7EE004, [0]),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript()
])