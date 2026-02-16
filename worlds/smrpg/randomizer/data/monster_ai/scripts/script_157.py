# 157 - MALLOWCLONEEnemy
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
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 6),
	CastSpell(StaticESpell, ElectroshockSpell, BoltSpell),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(Attack89),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsSet(BV7EE004, [0]),
	ClearVarBits(BV7EE00E, [1]),
	DecreaseVarBy1(BV7EE000),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	ClearVarBits(BV7EE00E, [0]),
	DecreaseVarBy1(BV7EE000),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWaterItem]),
	IfTargetAlive(SELF),
	IfVarBitsSet(BV7EE004, [0]),
	ClearVarBits(BV7EE00E, [1]),
	DecreaseVarBy1(BV7EE000),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWaterItem]),
	IfTargetAlive(SELF),
	ClearVarBits(BV7EE00E, [0]),
	DecreaseVarBy1(BV7EE000),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])