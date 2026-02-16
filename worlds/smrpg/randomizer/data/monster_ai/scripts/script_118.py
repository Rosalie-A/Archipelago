# 118 - FINKFLOWEREnemy
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
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 6),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack4, ScrowDustAttack, PollenNapAttack),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript(),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(RecoverSpell, RecoverSpell, DoNothing),
	SetTarget(RANDOM_OPPONENT),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack4, DoNothing, DoNothing),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript()
])