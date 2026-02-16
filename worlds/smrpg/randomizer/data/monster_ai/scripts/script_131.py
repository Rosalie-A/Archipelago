# 131 - MARIOCLONESEnemy

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
	Attack(Attack90),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsSet(BV7EE004, [0]),
	ClearVarBits(BV7EE00E, [1]),
	DecreaseVarBy1(BV7EE000),
	DecreaseVarBy1(BV7EE009),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	RunBattleEvent(BE0083_BELOME_3_CLONES),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	ClearVarBits(BV7EE00E, [0]),
	DecreaseVarBy1(BV7EE000),
	DecreaseVarBy1(BV7EE009),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	RunBattleEvent(BE0083_BELOME_3_CLONES),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWaterItem]),
	IfTargetAlive(SELF),
	IfVarBitsSet(BV7EE004, [0]),
	ClearVarBits(BV7EE00E, [1]),
	DecreaseVarBy1(BV7EE000),
	DecreaseVarBy1(BV7EE009),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	RunBattleEvent(BE0083_BELOME_3_CLONES),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWaterItem]),
	IfTargetAlive(SELF),
	ClearVarBits(BV7EE00E, [0]),
	DecreaseVarBy1(BV7EE000),
	DecreaseVarBy1(BV7EE009),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	RunBattleEvent(BE0083_BELOME_3_CLONES),
	Wait1TurnandRestartScript()
])