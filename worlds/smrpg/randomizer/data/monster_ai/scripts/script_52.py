# 52 - BOOMEREnemy
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
	IfVarEqualOrGreaterThan(BV7EE003, 2),
	IfVarBitsSet(BV7EE002, [1]),
	ClearVarBits(BV7EE002, [1]),
	SetVarBits(BV7EE002, [0]),
	ClearVar(BV7EE003),
	SetTarget(SELF),
	RunObjectSequence(8),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE003, 2),
	IfVarBitsSet(BV7EE002, [0]),
	ClearVarBits(BV7EE002, [0]),
	SetVarBits(BV7EE002, [1]),
	ClearVar(BV7EE003),
	SetTarget(SELF),
	RunObjectSequence(9),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	Attack(Attack1, Attack1, SkewerAttack),
	IncreaseVarBy1(BV7EE003),
	Wait1TurnandRestartScript(),
	CastSpell(BlizzardSpell, BlastSpell, StormSpell),
	IncreaseVarBy1(BV7EE003),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE002, [0]),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	Attack(ShakerAttack, DoNothing, DoNothing),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE002, [1]),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(ShakerAttack, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])