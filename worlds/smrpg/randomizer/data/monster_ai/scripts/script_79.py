# 79 - ALLEYRATEnemy
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
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack6, Attack6, PoisonAttack),
	ClearVarBits(BV7EE00F, [0]),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetTarget(SELF),
	CastSpell(EscapeSpell),
	StartCounterCommands()
])