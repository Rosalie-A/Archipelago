# 217 - TENTACLESEnemy2
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
	Attack(Attack0),
	IncreaseVarBy1(BV7EE009),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsSet(BV7EE003, [0]),
	IfVarBitsClear(BV7EE003, [1]),
	IncreaseVarBy1(BV7EE000),
	IfVarEqualOrGreaterThan(BV7EE000, 6),
	SetVarBits(BV7EE003, [1]),
	RunObjectSequence(3),
	SetVarBits(BV7EE00D, [0]),
	RunObjectSequence(2),
	ClearVar(BV7EE009),
	RunBattleEvent(BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE003, [0]),
	IncreaseVarBy1(BV7EE000),
	IfVarEqualOrGreaterThan(BV7EE000, 3),
	SetVarBits(BV7EE003, [0]),
	RunObjectSequence(3),
	SetVarBits(BV7EE00D, [0]),
	RunObjectSequence(2),
	ClearVar(BV7EE009),
	RunBattleEvent(BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])