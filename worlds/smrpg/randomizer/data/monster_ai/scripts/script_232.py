# 232 - TORTE2Enemy
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
	IfVarBitsClear(BV7EE001, [0]),
	SetVarBits(BV7EE001, [0]),
	SetUntargetable(MONSTER_2_SET),
	SetUntargetable(MONSTER_5_SET),
	ClearVar(BV7EE007),
	RunBattleEvent(BE0029_TORTE_2),
	RunBattleDialog(154),
	RunObjectSequence(4),
	DecreaseVarBy1(BV7EE007),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE001, [1]),
	IncreaseVarBy1(BV7EE007),
	IncreaseVarBy1(BV7EE007),
	IncreaseVarBy1(BV7EE007),
	IncreaseVarBy1(BV7EE007),
	RunObjectSequence(4),
	SetTarget(MONSTER_1_SET),
	Attack(ATKMATK5Attack),
	DecreaseVarBy1(BV7EE007),
	SetVarBits(BV7EE001, [1]),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE007, 1),
	RunObjectSequence(4),
	SetTarget(MONSTER_1_SET),
	Attack(ATKMATK5Attack),
	DecreaseVarBy1(BV7EE007),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])