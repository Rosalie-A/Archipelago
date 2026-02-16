# 175 - JOHNNY3Enemy

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
	DisableCommand([COMMAND_ITEM]),
	SetTarget(SELF),
	Attack(ATKDEF100Attack),
	SetTarget(RANDOM_OPPONENT),
	SetVarBits(BV7EE001, [0]),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Attack(Attack1, SkewerAttack, SkewerAttack),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 6),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	CastSpell(DiamondSawSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	CastSpell(MegaDrainSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(1000),
	IfVarBitsClear(BV7EE001, [1]),
	SetVarBits(BV7EE001, [1]),
	SetTarget(SELF),
	Attack(GetToughAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfHPBelow(500),
	IfVarBitsClear(BV7EE001, [2]),
	SetVarBits(BV7EE001, [2]),
	SetTarget(SELF),
	Attack(VigorupAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript()
])